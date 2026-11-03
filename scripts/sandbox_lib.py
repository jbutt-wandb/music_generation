"""Shared library for the CoreWeave serverless-sandbox tooling.

Imported by the two partitioned entry points (each a PEP 723 uv script that
declares cwsandbox and runs via `uv run --no-project --python 3.12`):

  scripts/sandbox.py           the app pathway — seed/up/sync/down the marimo
                               studio sandbox and print its public URL
  scripts/sandbox_generate.py  the terminal/agent pathway — headless one-song
                               generation with a Slurm-cluster fallback

Both pathways create the SAME sandbox shape (create_studio): one 1-GPU
serverless sandbox whose /work mount is an instant fork of a seeded filesystem
snapshot (app venv + ~57 GB of MiniMax-Music3 weights). That symmetry is
deliberate — services/ports are fixed at creation, so a sandbox created by the
generate pathway must already carry the marimo service (and APP_TOKEN) for the
app pathway to later reuse it, and vice versa.

Not a runnable script: no PEP 723 header here; the entry points provide the
cwsandbox dependency. cwsandbox installs SIGINT/SIGTERM handlers at import
time, so this module must only ever be imported on the main thread.
"""

from __future__ import annotations

import io
import json
import os
import secrets as pysecrets
import shlex
import sys
import tarfile
import time
from pathlib import Path

from dotenv import dotenv_values

from cwsandbox import (
    AuthStrategy,
    CWSandboxAuthenticationError,
    Endpoint,
    EndpointAuth,
    EndpointKind,
    FileSystemSnapshotOptions,
    Sandbox,
    SandboxResourceExhaustedError,
    SandboxSnapshotError,
    SandboxStatus,
    SandboxTimeoutError,
    SandboxUnavailableError,
    Service,
    ServiceVisibility,
)

# --- constants -----------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / ".launch" / "sandbox-state.json"  # tokens/ids — chmod 600

AUTH = AuthStrategy.COREWEAVE_API_KEY  # <- CWSANDBOX_API_KEY from .env

# The serverless GPU pool is heterogeneous (H100 80GB sm_90 AND RTX PRO 6000
# 96GB sm_120) — this tag ships CUDA 12.8 + PyTorch 2.8 and works on both.
# It is a *-runtime* image with no git/gcc; ensure_build_tools papers over
# that per-sandbox (apt lands in the container layer, never the snapshot).
# SANDBOX_IMAGE in .env/environment overrides it (pin a custom image by digest).
DEFAULT_IMAGE = "pytorch/pytorch:2.8.0-cuda12.8-cudnn9-runtime"

APP_TAG = "musicgen"  # stable app tag; role tags ("-studio", "-seed") reap precisely

MOUNT = "/work"
MOUNT_SIZE = "200Gi"  # weights ~57GB + venv + managed python + snapshot staging
# headroom: the snapshot agent stages a full tar of the mount ON the mount, so
# the payload must stay under about half of this (see prune_mount).

# A GPU request reserves ONLY the GPU — cpu/memory must be explicit and
# serverless requires requests == limits. 16/64Gi mirrors the Slurm job's
# --cpus-per-task=16 (Music3 peaks well under 64G of host RAM).
GPU_RESOURCES = {"cpu": "16", "memory": "64Gi", "gpu": 1}
SEED_RESOURCES = {"cpu": "8", "memory": "32Gi"}  # downloads/installs need no GPU

MAX_LIFETIME = 24 * 3600  # server-enforced billing backstop if we forget `down`
SEED_LIFETIME = 4 * 3600  # seeding is ~30-60 min; slack for a slow HF mirror

APP_PORT = 2718  # marimo
MODEL_ID = "MiniMaxAI/MiniMax-Music3"

# uv uses ITS OWN managed interpreter stored under the snapshot mount —
# container pythons vary across the heterogeneous pool and a venv keyed to one
# would break on restore.
UV_ENV = (
    f"UV_CACHE_DIR={MOUNT}/cache/uv "
    f"UV_PYTHON_INSTALL_DIR={MOUNT}/uv-python "
    "UV_PYTHON_PREFERENCE=only-managed"
)
UV = f"{UV_ENV} {MOUNT}/bin/uv"

# Mirrors the old rsync exclude list (plus state/secrets). .sandbox_id and
# .gen.lock are sandbox-side runtime artifacts — a stray local copy must never
# ride the tarball (a shipped .sandbox_id would fake "inside a sandbox").
TAR_EXCLUDES = {
    ".venv", ".git", ".env", ".launch", "generated_audio", "demo_audio",
    "logs", "wandb", "__pycache__", ".marimo", "__marimo__",
    ".ipynb_checkpoints", ".DS_Store", ".sandbox_id", ".gen.lock",
}

# The two env vars every MiniMax-Music3 process must run under (CLAUDE.md).
TORCH_ENV = {
    "TORCH_DISABLE_NATIVE_JIT": "1",
    "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True",
}


# --- .env / state ----------------------------------------------------------------

def load_dotenv() -> dict[str, str]:
    """The repo's .env as a dict, parsed by python-dotenv — the same parser
    scripts/minimax_music3.py and app/compose.py use, so quoting/comment/export
    edge cases cannot diverge between the app and this tooling."""
    path = ROOT / ".env"
    if not path.exists():
        return {}
    return {k: v for k, v in dotenv_values(path).items() if v is not None}


def require_api_key(dotenv: dict[str, str]) -> None:
    """Hard-require the two spin-up keys — nothing is created without BOTH.
    Exposes CWSANDBOX_API_KEY to the SDK via os.environ (never print either)."""
    if not os.environ.get("CWSANDBOX_API_KEY"):
        if dotenv.get("CWSANDBOX_API_KEY"):
            os.environ["CWSANDBOX_API_KEY"] = dotenv["CWSANDBOX_API_KEY"]
        else:
            sys.exit("CWSANDBOX_API_KEY not found in .env or the environment — create a "
                     "console token (Sandbox User role) at console.coreweave.com/tokens")
    if not (os.environ.get("WANDB_API_KEY") or dotenv.get("WANDB_API_KEY")):
        sys.exit("WANDB_API_KEY (W&B Inference) is required — the in-app composer "
                 "authenticates with it; nothing will be spun up without it. "
                 "Get one at wandb.ai/authorize")


def resolve_image(dotenv: dict[str, str]) -> str:
    return os.environ.get("SANDBOX_IMAGE") or dotenv.get("SANDBOX_IMAGE") or DEFAULT_IMAGE


def resolve_gpu_resources(dotenv: dict[str, str]) -> dict:
    """GPU_RESOURCES with optional SANDBOX_CPU / SANDBOX_MEMORY overrides."""
    res = dict(GPU_RESOURCES)
    cpu = os.environ.get("SANDBOX_CPU") or dotenv.get("SANDBOX_CPU")
    mem = os.environ.get("SANDBOX_MEMORY") or dotenv.get("SANDBOX_MEMORY")
    if cpu:
        res["cpu"] = cpu
    if mem:
        res["memory"] = mem
    return res


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
    STATE_FILE.chmod(0o600)  # holds the app access token


# --- sandbox primitives ----------------------------------------------------------

def sh(sb: Sandbox, script: str, timeout: float | None = None):
    """Attached exec of a SHORT shell command. Anything that can outlive the
    SDK's ~300 s request timeout must go through run_long() instead."""
    return sb.exec(["bash", "-c", script], timeout_seconds=timeout).result()


def run_long(sb: Sandbox, name: str, script: str, timeout: float,
             poll: float = 15, on_line=None) -> None:
    """Run a long step DETACHED and poll a sentinel for completion.

    Attached exec dies at the SDK's ~300 s request timeout, so every slow step
    (uv sync, HF download, a whole song generation) runs under nohup with its
    exit code dropped into a .rc file we poll. Logs land in /work/logs/.
    `on_line(last_log_line)` fires on every poll — the generate pathway uses it
    to stream generation phases.

    Each poll is ONE exec RPC (rc + last log line, sentinel-separated), and the
    interval backs off exponentially from 2 s to `poll` so near-no-op steps
    (e.g. an unchanged uv sync) return in seconds instead of a flat 15.
    """
    log, rc = f"{MOUNT}/logs/{name}.log", f"{MOUNT}/logs/{name}.rc"
    sep = "__CW_RC_END__"
    wrapped = f"({script}) > {log} 2>&1; echo $? > {rc}"
    sh(sb, f"mkdir -p {MOUNT}/logs && rm -f {rc} && "
           f"(nohup bash -c {shlex.quote(wrapped)} >/dev/null 2>&1 &)")
    t0 = time.monotonic()
    next_beat = 60.0
    interval = 2.0
    while time.monotonic() - t0 < timeout:
        time.sleep(interval)
        interval = min(interval * 2, poll)
        out = sh(sb, f"cat {rc} 2>/dev/null; echo {sep}; "
                     f"tail -c 2000 {log} 2>/dev/null | tr '\\r' '\\n' "
                     f"| tail -n 1").stdout or ""
        rc_val, _, last = out.partition(sep)
        rc_val, last = rc_val.strip(), last.strip()
        if rc_val == "0":
            print(f"  {name}: done ({time.monotonic() - t0:.0f}s)")
            return
        if rc_val:
            tail = sh(sb, f"tail -n 25 {log}").stdout
            raise RuntimeError(f"{name} failed (rc={rc_val}) — tail of {log}:\n{tail}")
        if on_line and last:
            on_line(last)
        if time.monotonic() - t0 >= next_beat:  # 1-line heartbeat per minute
            print(f"  {name}: running {time.monotonic() - t0:.0f}s  {last[:110]}")
            next_beat += 60.0
    raise TimeoutError(f"{name} did not finish within {timeout}s — see {log} in the sandbox")


# Probe from INSIDE the sandbox with python (the pytorch image may lack curl).
# Any HTTP status counts as "listening" — marimo answers 401 under token auth.
_HTTP_PROBE = (
    "import sys, urllib.request, urllib.error\n"
    "try:\n"
    "    urllib.request.urlopen('http://localhost:{port}{path}', timeout=3)\n"
    "except urllib.error.HTTPError:\n"
    "    pass\n"
    "except Exception:\n"
    "    sys.exit(1)\n"
)


def wait_http(sb: Sandbox, port: int, label: str, path: str = "/",
              timeout: float = 600, interval: float = 10) -> bool:
    """Phase-2 readiness: sandbox RUNNING != app listening — poll the port."""
    print(f"Waiting for {label}", end="", flush=True)
    t0 = time.monotonic()
    while time.monotonic() - t0 < timeout:
        r = sb.exec(["python", "-c", _HTTP_PROBE.format(port=port, path=path)]).result()
        if r.returncode == 0:
            print(f" up ({time.monotonic() - t0:.0f}s)")
            return True
        print(".", end="", flush=True)
        time.sleep(interval)
    print(" TIMEOUT")
    return False


def create_with_retry(label: str, image: str, wait_timeout: float = 900,
                      deadline: float | None = None, **kwargs) -> Sandbox:
    """Sandbox.run (keep-alive form) + wait-until-RUNNING, retrying the two
    transient platform failures seen live:

    - CreateSandbox can fail RESOURCE_EXHAUSTED ("runner capacity exhausted" /
      gateway errors) when the serverless pool is momentarily full. Nothing is
      created or billed — back off and recreate.
    - A created sandbox can wedge in CREATING past the wait timeout (observed
      live >2 h on a fork that normally boots in ~4 min). Treat > wait_timeout
      as wedged: delete the stuck one and recreate.

    `deadline` (time.monotonic() value) caps total patience — the generate
    pathway passes its fallback budget here; expiry raises TimeoutError so the
    caller can fall back to the Slurm cluster.
    """
    fss = kwargs.get("file_system_snapshot")
    if fss is not None and getattr(fss, "file_system_snapshot_id", None):
        print(f"  {label}: creating from a snapshot fork — restoring ~70 GB "
              f"takes ~4 min to reach RUNNING; it is not hung")
    for attempt in range(6):
        if deadline is not None and time.monotonic() >= deadline:
            raise TimeoutError(f"{label}: budget exhausted before a sandbox was RUNNING")
        if deadline is not None:
            wait_timeout = min(wait_timeout, max(30.0, deadline - time.monotonic()))
        sb = None
        try:
            sb = Sandbox.run(
                "sleep", "infinity",  # keep-alive main process; work runs via exec
                auth=AUTH,
                container_image=image,
                placement_mode="serverless",
                **kwargs,
            )
            sb.wait(timeout=wait_timeout)
            return sb
        except SandboxResourceExhaustedError as e:
            if attempt == 5:
                raise
            reason = f"capacity exhausted ({e})"
        except SandboxTimeoutError:
            if sb is not None:  # don't leave the wedged sandbox billing
                Sandbox.delete(sb.sandbox_id, auth=AUTH, missing_ok=True).result()
            if deadline is not None and time.monotonic() >= deadline:
                raise TimeoutError(f"{label}: budget exhausted waiting for RUNNING")
            if attempt == 5:
                raise
            reason = (f"wedged in CREATING > {wait_timeout:.0f}s "
                      f"(deleted the stuck sandbox; recreating)")
        wait = 60 * (attempt + 1)
        if deadline is not None:
            wait = min(wait, max(1.0, deadline - time.monotonic()))
        print(f"  {label}: {reason}; retry {attempt + 1}/5 in {wait:.0f}s")
        time.sleep(wait)
    raise AssertionError("unreachable")


def make_tarball() -> bytes:
    """gzip tarball of the repo (the code the sandbox runs), minus junk/secrets."""
    buf = io.BytesIO()

    def keep(ti: tarfile.TarInfo) -> tarfile.TarInfo | None:
        parts = Path(ti.name).parts
        return None if any(p in TAR_EXCLUDES for p in parts) else ti

    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for child in sorted(ROOT.iterdir()):
            if child.name in TAR_EXCLUDES:
                continue
            tar.add(child, arcname=child.name, filter=keep)
    return buf.getvalue()


def upload_code(sb: Sandbox) -> None:
    """Push local code into the sandbox: authenticated file API + untar.
    The local repo is the source of truth; snapshot code may be stale."""
    data = make_tarball()
    print(f"Uploading code ({len(data) / 1e6:.1f} MB) -> {MOUNT}/app")
    sb.write_file("/tmp/app.tar.gz", data).result()
    sh(sb, f"mkdir -p {MOUNT}/app && tar -xzf /tmp/app.tar.gz -C {MOUNT}/app && rm /tmp/app.tar.gz")


def service_url(sb: Sandbox, port: int) -> str:
    urls = {int(p): u for p, _name, u in sb.service_urls}
    return urls[port]


def reconnect(sandbox_id: str | None) -> Sandbox | None:
    """Reattach to a previously created sandbox if it is still RUNNING."""
    if not sandbox_id:
        return None
    try:
        sb = Sandbox.from_id(sandbox_id, auth=AUTH)
        if not hasattr(sb, "get_status"):  # newer SDKs return an OperationRef
            sb = sb.result()
        return sb if sb.get_status() == SandboxStatus.RUNNING else None
    except CWSandboxAuthenticationError:
        # Misconfigured auth must not masquerade as "sandbox gone" — callers
        # would silently create duplicates (require_api_key() not called?).
        raise
    except Exception:
        return None


def find_studio(state: dict) -> Sandbox | None:
    """Reuse path shared by both pathways: stored id first, then a tag search
    (another session on this machine or a teammate may have created it).
    Listed handles are directly usable — no re-fetch needed."""
    sb = reconnect(state.get("studio_id"))
    if sb:
        return sb
    try:
        for cand in Sandbox.list(tags=[f"{APP_TAG}-studio"], auth=AUTH).result():
            if cand.get_status() == SandboxStatus.RUNNING:
                return cand
    except Exception:
        pass
    return None


def reap_by_tag(delete_snapshot: bool = False, role: str | None = None) -> None:
    """Delete sandboxes by tag. role=None reaps EVERY app sandbox (`down`);
    failure paths must pass role="studio" so a concurrent seed/reseed build
    (tagged [APP_TAG, APP_TAG-seed]) survives someone else's failed launch."""
    tag = f"{APP_TAG}-{role}" if role else APP_TAG
    state = load_state()
    found = Sandbox.list(tags=[tag], auth=AUTH).result()  # OperationRef -> list
    for sb in found:
        print(f"Deleting sandbox {sb.sandbox_id}")
        Sandbox.delete(sb.sandbox_id, auth=AUTH, missing_ok=True).result()
    if not found:
        print("No sandboxes to stop.")
    for key in ("studio_id", "launched_at"):
        state.pop(key, None)
    if delete_snapshot and state.get("snapshot_id"):
        print(f"Deleting snapshot {state['snapshot_id']} (next launch needs `seed` again)")
        Sandbox.delete_snapshot(state.pop("snapshot_id"), auth=AUTH, missing_ok=True).result()
    save_state(state)


# --- studio sandbox (shared by both pathways) ------------------------------------

def fss_new() -> FileSystemSnapshotOptions:
    """A fresh, empty snapshot mount (the seed sandbox builds into this)."""
    return FileSystemSnapshotOptions(mount_path=MOUNT, size=MOUNT_SIZE)


def fss_fork(snapshot_id: str) -> FileSystemSnapshotOptions:
    """Each sandbox gets an independent instant FORK of the seeded mount."""
    return FileSystemSnapshotOptions(
        mount_path=MOUNT, size=MOUNT_SIZE, file_system_snapshot_id=snapshot_id)


def https_service(port: int, name: str) -> Service:
    # Public HTTPS endpoint: the platform terminates TLS but does ZERO caller
    # auth (OPEN) — marimo's own token auth is the boundary.
    return Service(port=port, name=name, visibility=ServiceVisibility.PUBLIC,
                   endpoint=Endpoint(kind=EndpointKind.HTTPS, auth=EndpointAuth.OPEN))


def studio_env(dotenv: dict[str, str], app_token: str) -> dict[str, str]:
    """ONLY the keys the sandbox needs — never the whole .env (it carries
    unrelated secrets). Secrets travel via environment_variables, never argv."""
    env = {
        "HF_HOME": f"{MOUNT}/hf",
        "APP_TOKEN": app_token,  # marimo --token-password
        # Keep W&B artifacts/caches on the big mount, not the container disk.
        "WANDB_DIR": f"{MOUNT}/wandb",
        "WANDB_CACHE_DIR": f"{MOUNT}/wandb/cache",
        "WANDB_CONFIG_DIR": f"{MOUNT}/wandb/config",
        **TORCH_ENV,
    }
    for key in ("WANDB_API_KEY", "WANDB_ENTITY", "WANDB_PROJECT", "HF_TOKEN"):
        val = dotenv.get(key) or os.environ.get(key)
        if val:
            env[key] = val
    missing = [k for k in ("WANDB_ENTITY", "WANDB_PROJECT") if k not in env]
    if missing:
        print(f"note: {', '.join(missing)} not set — runs will NOT be logged to "
              f"W&B (recommended: set WANDB_ENTITY and WANDB_PROJECT in .env)",
              file=sys.stderr)
    return env


def create_studio(dotenv: dict[str, str], state: dict, snapshot_id: str,
                  deadline: float | None = None) -> Sandbox:
    """Create the one GPU sandbox both pathways share. Persists its id to state
    IMMEDIATELY so `down` can reap it even if bootstrap fails later."""
    state.setdefault("app_token", pysecrets.token_urlsafe(32))
    save_state(state)
    sb = create_with_retry(
        "studio",
        image=resolve_image(dotenv),
        deadline=deadline,
        resources=resolve_gpu_resources(dotenv),
        max_lifetime_seconds=MAX_LIFETIME,
        tags=[APP_TAG, f"{APP_TAG}-studio"],
        environment_variables=studio_env(dotenv, state["app_token"]),
        services=[https_service(APP_PORT, "app")],
        file_system_snapshot=fss_fork(snapshot_id),
    )
    state.update({
        "studio_id": sb.sandbox_id,
        "launched_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    })
    save_state(state)
    return sb


def ensure_build_tools(sb: Sandbox) -> None:
    """The pytorch *-runtime* image ships no git/gcc. git is REQUIRED: pyproject
    pins diffusers to a git commit and `uv sync` shells out to the git CLI on a
    uv-cache miss. gcc/libc6-dev guard against Triton JIT-compiling host C at
    the first kernel launch (torch imports fine, the model loads fine, the
    first generation dies with 'Failed to find C compiler').

    apt installs land in the CONTAINER layer — NOT the /work snapshot — so
    every fresh sandbox/fork needs this again. Idempotent: instant no-op when
    present. Detached via run_long: apt mirror speed varies wildly and an
    attached exec dies at ~300 s. Disappears once SANDBOX_IMAGE points at a
    custom image with the tools baked in.
    """
    probe = "command -v cc >/dev/null 2>&1 && command -v git >/dev/null 2>&1"
    if (sh(sb, f"{probe} && echo OK").stdout or "").strip().endswith("OK"):
        return
    apt = ("apt-get update -qq && "
           "apt-get install -y -qq --no-install-recommends gcc libc6-dev git")
    for attempt in (1, 2):
        try:
            run_long(sb, "ensure-tools", apt, timeout=900)
            return
        except (RuntimeError, TimeoutError):
            if attempt == 2:
                raise
            print("  ensure-tools: apt failed (flaky mirrors?); retrying once")


def bootstrap_code(sb: Sandbox) -> None:
    """Shared bootstrap for BOTH pathways and the seed builds: fresh code +
    tools + venv reconciliation. uv sync is a near-no-op unless
    pyproject/uv.lock changed since the seed. The W&B dirs must exist before
    any wandb.init — headless generations never run start_marimo, so they are
    created here, the one step every pathway passes through."""
    upload_code(sb)
    ensure_build_tools(sb)
    sh(sb, f"mkdir -p {MOUNT}/wandb/cache {MOUNT}/wandb/config {MOUNT}/logs")
    run_long(sb, "uv-sync", f"cd {MOUNT}/app && {UV} sync", timeout=2400)


def ensure_app_token(sb: Sandbox, state: dict) -> str:
    """The token that actually guards marimo is the APP_TOKEN baked into the
    sandbox's creation env — an adopted sandbox (tag search, fresh clone,
    teammate's launch) won't match local state, and printing the local token
    would 401. Recover it from the sandbox and persist it."""
    try:
        token = (sh(sb, 'printf %s "$APP_TOKEN"').stdout or "").strip()
    except Exception:
        token = ""
    if token:
        if state.get("app_token") != token:
            state["app_token"] = token
            save_state(state)
        return token
    if state.get("app_token"):
        return state["app_token"]
    raise RuntimeError(
        "cannot determine the app token: the sandbox env has no APP_TOKEN and "
        "local state has none — recreate with `sandbox.py down && sandbox.py up`")


def pull_wavs(sb: Sandbox) -> int:
    """Download WAVs from the sandbox that are missing locally. The app
    pathway's outputs live only on the ephemeral /work mount — without this,
    `down` (or the 24 h lifetime) destroys a session's songs."""
    local_dir = ROOT / "generated_audio" / "MiniMax-Music3"
    local_dir.mkdir(parents=True, exist_ok=True)
    remote_dir = f"{MOUNT}/app/generated_audio/MiniMax-Music3"
    out = (sh(sb, f"ls -1 {remote_dir}/*.wav 2>/dev/null || true").stdout or "").strip()
    pulled = 0
    for path in out.splitlines():
        dest = local_dir / path.rsplit("/", 1)[-1]
        if dest.exists():
            continue
        data = sb.read_file(path).result()
        dest.write_bytes(data)
        print(f"  pulled {dest.name} ({len(data) / 1e6:.1f} MB)")
        pulled += 1
    return pulled


def create_seed(dotenv: dict[str, str], label: str,
                fss: FileSystemSnapshotOptions) -> Sandbox:
    """The CPU-only build sandbox shared by seed and reseed — downloads and
    installs need no GPU (and work even when the GPU pool is full)."""
    return create_with_retry(
        label,
        image=resolve_image(dotenv),
        resources=SEED_RESOURCES,
        max_lifetime_seconds=SEED_LIFETIME,
        tags=[APP_TAG, f"{APP_TAG}-seed"],
        environment_variables={k: v for k, v in {
            "HF_TOKEN": dotenv.get("HF_TOKEN"), "HF_HOME": f"{MOUNT}/hf",
        }.items() if v},
        file_system_snapshot=fss,
    )


def start_marimo(sb: Sandbox) -> None:
    """(Re)start the marimo app detached.

    Launcher→app interface: APP_TOKEN/W&B/HF/torch env come from the sandbox's
    creation environment; MUSICGEN_SANDBOX_ID is only known post-create, so it
    is injected here on the marimo process (and mirrored to
    /work/app/.sandbox_id for any other in-sandbox process that wants it).
    The `( ... </dev/null &)` fd isolation is critical — a child inheriting the
    exec session's fds keeps the exec stream open and sh() hangs to the SDK's
    ~300 s cap (observed live).
    """
    sid = sb.sandbox_id
    sh(sb, "pkill -f 'bin/marimo' || true")  # pkill -f takes a regex — keep it metachar-free
    time.sleep(3)  # let the port free up
    sh(sb, f"mkdir -p {MOUNT}/wandb/cache {MOUNT}/wandb/config {MOUNT}/logs && "
           f"cd {MOUNT}/app && printf '%s' {shlex.quote(sid)} > .sandbox_id && "
           f"(MUSICGEN_SANDBOX_ID={shlex.quote(sid)} CUDA_VISIBLE_DEVICES=0 "
           f"nohup .venv/bin/marimo run app/app.py --host 0.0.0.0 --port {APP_PORT} "
           f'--headless --watch --token --token-password "$APP_TOKEN" '
           f"> {MOUNT}/logs/marimo.log 2>&1 </dev/null &)")


# --- seed/reseed building blocks ---------------------------------------------------

def ensure_model(sb: Sandbox) -> None:
    """Download the MiniMax-Music3 weights into HF_HOME under the mount unless
    already present (instant no-op per reseed). HF_TOKEN comes from the seed
    sandbox's creation env — huggingface_hub reads it; it never crosses argv."""
    marker = f"{MOUNT}/hf/hub/models--{MODEL_ID.replace('/', '--')}/snapshots"
    if "OK" in (sh(sb, f"test -e {shlex.quote(marker)} && echo OK").stdout or ""):
        print(f"  {MODEL_ID}: already present")
        return
    run_long(
        sb, "hf-minimax-music3",
        f"HF_HOME={MOUNT}/hf {MOUNT}/app/.venv/bin/python -c "
        f"\"from huggingface_hub import snapshot_download; "
        f"snapshot_download('{MODEL_ID}')\"",
        timeout=3 * 3600,  # ~57 GB; mirror speed varies
    )


def prune_mount(sb: Sandbox) -> None:
    """Shrink /work before snapshotting — the snapshot agent stages a FULL TAR
    OF THE MOUNT *ON* THE MOUNT, so a snapshot transiently needs ~2x the
    payload in mount space; keep the payload under about half of MOUNT_SIZE. A
    failed attempt can also leave its staging tar behind, poisoning later
    tries — swept here and before each snapshot attempt. `uv cache prune --ci`
    drops re-downloadable wheels but KEEPS the git-built diffusers wheel."""
    sh(sb, f"rm -f {MOUNT}/.cw-object-store-agent-*.tar; "
           f"rm -rf {MOUNT}/logs/*; "
           f"find {MOUNT}/app -name __pycache__ -type d -exec rm -rf {{}} + "
           f"2>/dev/null; {UV} cache prune --ci >/dev/null 2>&1 || true",
       timeout=280)
    size = (sh(sb, f"du -sh {MOUNT} 2>/dev/null | cut -f1", timeout=280).stdout or "?").strip()
    print(f"  mount payload after prune: {size} (must stay < ~half of {MOUNT_SIZE})")


def snapshot_with_retry(sb: Sandbox) -> str:
    """Snapshot the /work mount, waiting for READY. The RPC can fail
    transiently even after the SDK's own retries (gateway errors and
    FSS_CREATE_TIMED_OUT, both seen live) — and it strikes at the moment of
    maximum accumulated state, so never let one failure discard a fully built
    mount: the sandbox is still alive; retry against it."""
    print("Snapshotting /work (waits for READY — can take a few minutes)...")
    for attempt in range(5):
        sh(sb, f"rm -f {MOUNT}/.cw-object-store-agent-*.tar")  # stale staging tar
        try:
            return sb.snapshot().result()
        except (SandboxUnavailableError, SandboxResourceExhaustedError,
                SandboxSnapshotError) as e:
            if attempt == 4:
                raise
            print(f"  snapshot attempt failed ({e}); retry {attempt + 1}/4 in 60s")
            time.sleep(60)
    raise AssertionError("unreachable")


def verify_seed(sb: Sandbox) -> None:
    """Verify the payload BEFORE paying for the snapshot: forks assume these
    exact paths; rc-sentinels prove steps exited 0, not that artifacts exist."""
    required = [
        f"{MOUNT}/app/.venv/bin/python",
        f"{MOUNT}/app/.venv/bin/marimo",
        f"{MOUNT}/hf/hub/models--{MODEL_ID.replace('/', '--')}/snapshots",
    ]
    checks = " && ".join(f"test -e {shlex.quote(p)}" for p in required)
    if (sh(sb, f"{checks} && echo OK", timeout=120).stdout or "").strip() != "OK":
        missing = sh(sb, "; ".join(
            f"test -e {shlex.quote(p)} || echo MISSING {p}" for p in required),
            timeout=120).stdout
        raise RuntimeError(f"seed verification failed:\n{missing}")
    print("Seed verified: app venv, marimo, and model weights present.")
    print(sh(sb, f"du -sh {MOUNT}/hf {MOUNT}/app/.venv 2>/dev/null; "
                 f"df -h {MOUNT} | tail -1", timeout=300).stdout)


def resolve_snapshot_id(args_snapshot_id, state: dict, dotenv: dict[str, str]) -> str | None:
    """Explicit flag outranks local state; SNAPSHOT_ID in .env is the adoption
    path for a fresh clone (skip seeding by using a teammate's snapshot)."""
    return args_snapshot_id or state.get("snapshot_id") or dotenv.get("SNAPSHOT_ID")

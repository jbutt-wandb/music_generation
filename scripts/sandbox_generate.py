#!/usr/bin/env -S uv run --no-project --python 3.12 --script
# NB: --no-project + the explicit --python matter: without them uv resolves
# against the app's pyproject/.python-version and can rebuild the app venv for
# this script's environment (destructive, observed on a sibling project).
# /// script
# requires-python = ">=3.11"
# dependencies = ["cwsandbox>=1.19", "python-dotenv>=1.0"]
# ///
"""Headless one-song generation — the TERMINAL/AGENT pathway.

Partitioned from the app launcher (scripts/sandbox.py); both share
scripts/sandbox_lib.py and create the SAME sandbox shape, so a sandbox started
by either pathway is reused by the other (per-session reuse). Concurrent
generations in one sandbox are serialized by a flock on /work/app/.gen.lock
(the app side holds the same lock) — one GPU, one run.

Flow:
  1. Reuse a RUNNING musicgen sandbox if healthy, else create one from the
     seeded snapshot — all within --timeout-budget (default 600 s, env
     MUSICGEN_SANDBOX_BUDGET).
  2. Push local code (source of truth), write prompt/lyrics into the sandbox,
     run scripts/minimax_music3.py on its GPU, stream progress.
  3. Download the WAV to local generated_audio/MiniMax-Music3/<slug>_s<seed>.wav
     and print the W&B run URL.

FALLBACK: only when the budget expires (or sandbox acquisition fails outright:
capacity exhausted, not entitled, no snapshot, bootstrap failure) does
generation fall back to the CoreWeave Slurm training cluster over ssh —
reusing a running or pending `musicgen` allocation, else provisioning one,
launching via the standard nohup/srun template, and scp-ing the WAV back. An
allocation this script provisioned is released afterwards (even on failure); a
pre-existing one is left alone. A generation that TIMES OUT after it started
is terminal — it is never re-run on the cluster.

By default the sandbox is LEFT RUNNING afterwards for cheap iteration
(--down tears it down; the 24 h max lifetime is the billing backstop).

Examples:
  uv run --no-project --python 3.12 scripts/sandbox_generate.py \\
      --prompt_file prompt.txt --lyrics_file assets/neon_rain.txt \\
      --audio_duration 90 --seed 42 --title neon-rain
  ... --backend cluster     # force the Slurm fallback path (testing)
"""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

# cwsandbox (imported via sandbox_lib) installs SIGINT/SIGTERM handlers at
# import time — keep this import on the main thread.
import sandbox_lib as lib
from sandbox_lib import MOUNT

# The log grammar (failure signatures, done markers, W&B URL) and slugify are
# owned by app/backend.py — one parser for both the app and this fallback, so
# a new failure signature learned from a run lands in exactly one place.
# backend.py is stdlib-only, so this import is safe for a --no-project script.
sys.path.insert(0, str(lib.ROOT))
from app.backend import _parse_log, slugify  # noqa: E402

GEN_TIMEOUT = 45 * 60  # generation watchdog, mirrors the old app backend
LOCAL_WAV_DIR = lib.ROOT / "generated_audio" / "MiniMax-Music3"
# POSIX-class twin of backend.WANDB_URL_RE for sandbox-side grep -E.
_WANDB_URL_GREP = r"https://wandb\.ai/[^[:space:]]+/runs/[^[:space:]]+"

# --- Slurm fallback constants (self-contained: app/backend.py no longer has these)
SSH_HOST = "coreweave-login"
REMOTE_DIR = "~/music_gen_demo"
JOB_NAME = "musicgen"
SBATCH_CMD = ("sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G "
              f"--job-name={JOB_NAME} --wrap \"sleep infinity\"")


class FallbackNeeded(Exception):
    """Raised ONLY during sandbox acquisition (find/create/bootstrap) when the
    cluster should take over. Failures after generation starts are terminal."""


def _gen_cmd_tail(args, slug: str, lyrics_arg: str, output_rel: str) -> str:
    """The minimax_music3.py invocation shared VERBATIM by the sandbox and
    cluster pathways — one source so the fallback can never generate with
    different parameters than the primary."""
    return ("scripts/minimax_music3.py "
            f'--prompt "$(cat tmp/{slug}_prompt.txt)" {lyrics_arg} '
            f"--audio_duration {args.audio_duration} "
            f"--num_inference_steps {args.num_inference_steps} "
            f"--seed {args.seed} --output {output_rel}")


def _output_rel(slug: str, seed: int) -> str:
    return f"generated_audio/MiniMax-Music3/{slug}_s{seed}.wav"


# --- sandbox pathway ---------------------------------------------------------------

def ensure_sandbox(dotenv: dict, state: dict, deadline: float):
    """Reuse a healthy RUNNING musicgen sandbox or create one from the snapshot
    within the budget, then bootstrap local code onto it (the local repo is the
    source of truth — a stale snapshot script must never run silently).
    Raises FallbackNeeded when the cluster should take over."""
    sb = lib.find_studio(state)
    if sb:
        try:
            healthy = (lib.sh(sb, f"test -x {MOUNT}/app/.venv/bin/python && echo OK")
                       .stdout or "").strip().endswith("OK")
        except Exception as e:
            # The sandbox died between the status check and the exec (teammate
            # ran `down`, lifetime expired) — treat as unusable, not a crash.
            print(f"Sandbox {sb.sandbox_id} unreachable "
                  f"({type(e).__name__}) — recreating.")
            healthy = False
        if healthy:
            print(f"Reusing sandbox {sb.sandbox_id}")
            state["studio_id"] = sb.sandbox_id
            lib.save_state(state)
        else:
            print(f"Sandbox {sb.sandbox_id} is not usable — recreating.")
            lib.reap_by_tag(role="studio")  # never touch a concurrent seed build
            state = lib.load_state()
            sb = None

    if sb is None:
        snapshot_id = lib.resolve_snapshot_id(None, state, dotenv)
        if not snapshot_id:
            raise FallbackNeeded(
                "no snapshot (run `scripts/sandbox.py seed` once) — falling back")
        try:
            sb = lib.create_studio(dotenv, state, snapshot_id, deadline=deadline)
        except TimeoutError as e:
            raise FallbackNeeded(f"budget exhausted creating a sandbox: {e}")
        except Exception as e:
            # Terminal, non-transient failures (not entitled, quota, bad
            # snapshot) should not burn the rest of the budget retrying.
            raise FallbackNeeded(f"sandbox creation failed: {type(e).__name__}: {e}")

    try:
        lib.bootstrap_code(sb)
    except (RuntimeError, TimeoutError) as e:
        raise FallbackNeeded(
            f"sandbox bootstrap failed: {e}\n"
            f"  sandbox {sb.sandbox_id} is LEFT RUNNING (billing) — reap it "
            f"with `uv run --no-project --python 3.12 scripts/sandbox.py down`")
    return sb


def generate_in_sandbox(sb, args, slug: str, prompt: str, lyrics: str | None) -> dict:
    """Write inputs, run the generation detached, stream phases, fetch the WAV."""
    lib.sh(sb, f"mkdir -p {MOUNT}/app/tmp")
    sb.write_file(f"{MOUNT}/app/tmp/{slug}_prompt.txt", prompt.encode()).result()
    lyrics_arg = ""
    if lyrics is not None:
        sb.write_file(f"{MOUNT}/app/tmp/{slug}.txt", lyrics.encode()).result()
        lyrics_arg = f"--lyrics_file tmp/{slug}.txt"

    name = f"gen-{slug}-s{args.seed}"
    output_rel = _output_rel(slug, args.seed)
    # Env (W&B/HF/torch guards) comes from the sandbox's creation environment.
    # flock serializes the GPU against a concurrent app-side generation; -E 73
    # makes "lock busy" distinguishable from the command's own exit codes.
    gen = f".venv/bin/python {_gen_cmd_tail(args, slug, lyrics_arg, output_rel)}"
    cmd = f"cd {MOUNT}/app && flock -n -E 73 .gen.lock -c {shlex.quote(gen)}"

    last_phase = [""]

    def on_line(line: str) -> None:
        if line != last_phase[0]:
            last_phase[0] = line
            print(f"  … {line[:110]}")

    started = time.monotonic()
    try:
        lib.run_long(sb, name, cmd, timeout=GEN_TIMEOUT, on_line=on_line)
    except RuntimeError as e:
        if "rc=73" in str(e):
            sys.exit("another generation is already running in this sandbox "
                     "(.gen.lock held — likely the app) — wait for it and retry")
        raise
    except TimeoutError:
        # TERMINAL by design: never re-run a started generation on the cluster.
        sys.exit(
            f"generation exceeded {GEN_TIMEOUT // 60} min — giving up (no "
            f"cluster fallback for a started run). The detached job may still "
            f"finish in sandbox {sb.sandbox_id}: check {MOUNT}/logs/{name}.log "
            f"via `sandbox.py status`, then `sandbox.py pull`.")

    # One tiny grep RPC instead of catting a tqdm-bloated log over the wire.
    url = (lib.sh(sb, f"grep -aoE -m1 '{_WANDB_URL_GREP}' "
                      f"{MOUNT}/logs/{name}.log 2>/dev/null || true")
           .stdout or "").strip() or None

    LOCAL_WAV_DIR.mkdir(parents=True, exist_ok=True)
    local_wav = LOCAL_WAV_DIR / f"{slug}_s{args.seed}.wav"
    data = sb.read_file(f"{MOUNT}/app/{output_rel}").result()
    local_wav.write_bytes(data)
    return {
        "wav_path": str(local_wav),
        "run_url": url,
        "wall_seconds": round(time.monotonic() - started),
    }


# --- Slurm cluster fallback ---------------------------------------------------------

def _ssh(command: str, input_text: str | None = None, timeout: float = 60):
    # errors="replace": tail -c can cut the log mid-UTF-8-character (tqdm's bar
    # glyphs are multi-byte) and strict decoding would crash the poll loop.
    return subprocess.run(
        ["ssh", "-o", "BatchMode=yes", SSH_HOST, command],
        input=input_text, capture_output=True, text=True, errors="replace",
        timeout=timeout)


def _cluster_allocation() -> tuple[str, str] | None:
    """(jobid, state) of an existing musicgen allocation, preferring RUNNING —
    a PENDING one must be waited on, not duplicated with a second sbatch."""
    r = _ssh(f'squeue -u $USER -h -n {JOB_NAME} -o "%i %T"')
    if r.returncode != 0:
        return None
    rows = [ln.split() for ln in (r.stdout or "").strip().splitlines() if ln.split()]
    if not rows:
        return None
    running = [row for row in rows if row[1] == "RUNNING"]
    jobid, st = (running or rows)[0][:2]
    return jobid, st


def _wait_running(jobid: str, timeout: float = 300) -> None:
    t0 = time.monotonic()
    while True:
        st = (_ssh(f'squeue -h -j {jobid} -o "%T"').stdout or "").strip()
        if st == "RUNNING":
            return
        if time.monotonic() - t0 > timeout:
            raise RuntimeError(f"allocation {jobid} not RUNNING after "
                               f"{timeout:.0f}s (state: {st or 'gone'})")
        time.sleep(10)


def generate_on_cluster(args, slug: str, prompt: str, lyrics: str | None) -> dict:
    """The fallback: the pre-sandbox workflow, self-contained (docs/run_commands.md).
    Reuses a running (or pending) musicgen allocation or provisions one;
    releases it afterwards ONLY if this run provisioned it — including when
    provisioning itself fails or times out."""
    print("Falling back to the Slurm training cluster...")
    started = time.monotonic()
    jobid, we_provisioned = None, False
    try:
        found = _cluster_allocation()
        if found:
            jobid, st = found
            if st == "RUNNING":
                print(f"Reusing allocation {jobid}")
            else:
                print(f"Found allocation {jobid} in state {st}; waiting...")
                _wait_running(jobid)  # pre-existing: never ours to scancel
        else:
            idle = (_ssh("sinfo -p h100 -h -t idle -o '%D'").stdout or "").strip()
            if not idle or idle == "0":
                print("warning: sinfo reports no idle h100 nodes — the "
                      "allocation may queue", file=sys.stderr)
            r = _ssh(SBATCH_CMD)
            if r.returncode != 0:
                raise RuntimeError(f"sbatch failed: {r.stderr.strip()}")
            jobid, we_provisioned = r.stdout.strip().split()[-1], True
            print(f"Provisioned allocation {jobid}; waiting for it to run...")
            _wait_running(jobid)  # inside try: a never-RUNNING job still gets scancel'ed

        log = f"logs/{slug}_s{args.seed}.log"
        _ssh(f"mkdir -p {REMOTE_DIR}/tmp {REMOTE_DIR}/logs && "
             f"cat > {REMOTE_DIR}/tmp/{slug}_prompt.txt", input_text=prompt)
        lyrics_arg = ""
        if lyrics is not None:
            _ssh(f"cat > {REMOTE_DIR}/tmp/{slug}.txt", input_text=lyrics)
            lyrics_arg = f"--lyrics_file tmp/{slug}.txt"
        output_rel = _output_rel(slug, args.seed)
        torch_env = " ".join(f"{k}={v}" for k, v in lib.TORCH_ENV.items())
        launch = (
            f"cd {REMOTE_DIR} && mkdir -p {Path(output_rel).parent} && "
            f"nohup env {torch_env} "
            f"srun --jobid={jobid} --overlap --export=ALL "
            f".venv/bin/python {_gen_cmd_tail(args, slug, lyrics_arg, output_rel)} "
            f"> {log} 2>&1 &")
        subprocess.Popen(["ssh", "-o", "BatchMode=yes", SSH_HOST, launch],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        t0, url = time.monotonic(), None
        while time.monotonic() - t0 < GEN_TIMEOUT:
            time.sleep(15)
            tail = (_ssh(f'tail -c 4000 {REMOTE_DIR}/{log} 2>/dev/null '
                         f'| tr "\\r" "\\n"').stdout or "")
            state, phase, found_url = _parse_log(tail)
            url = found_url or url
            if state == "done":
                break
            if state == "failed":
                raise RuntimeError(
                    f"cluster generation failed — log tail:\n{tail[-1500:]}")
            if phase:
                print(f"  … {phase[:110]}")
        else:
            raise TimeoutError(f"cluster generation exceeded {GEN_TIMEOUT}s")

        LOCAL_WAV_DIR.mkdir(parents=True, exist_ok=True)
        local_wav = LOCAL_WAV_DIR / f"{slug}_s{args.seed}.wav"
        subprocess.run(
            ["scp", "-q", f"{SSH_HOST}:music_gen_demo/{output_rel}", str(local_wav)],
            check=True, timeout=180)
        return {"wav_path": str(local_wav), "run_url": url,
                "wall_seconds": round(time.monotonic() - started),
                "backend": "cluster"}
    finally:
        if we_provisioned and jobid:
            print(f"Releasing allocation {jobid} (this run provisioned it).")
            try:
                _ssh(f"scancel {jobid}")
            except Exception:
                print(f"warning: scancel {jobid} failed — release it manually "
                      f"(squeue -u $USER)", file=sys.stderr)


# --- main -----------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt", help="Structured Caption text")
    src.add_argument("--prompt_file", help="file containing the Structured Caption")
    lyr = parser.add_mutually_exclusive_group()
    lyr.add_argument("--lyrics", help="tagged lyrics text")
    lyr.add_argument("--lyrics_file", help="file containing tagged lyrics "
                                           "(omit both for an instrumental)")
    parser.add_argument("--audio_duration", type=int, default=60)
    parser.add_argument("--num_inference_steps", type=int, default=30)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--title", default=None,
                        help="names the local WAV (default: lyrics-file stem)")
    parser.add_argument("--timeout-budget", type=float, default=None,
                        help="seconds to get a sandbox RUNNING before the Slurm "
                             "fallback (default 600; env MUSICGEN_SANDBOX_BUDGET; "
                             "0 = skip straight to the cluster)")
    parser.add_argument("--backend", choices=("auto", "sandbox", "cluster"),
                        default="auto",
                        help="auto = sandbox with cluster fallback; force either")
    parser.add_argument("--down", action="store_true",
                        help="tear the sandbox down after generating "
                             "(default: leave it running for iteration)")
    args = parser.parse_args()

    dotenv = lib.load_dotenv()
    prompt = args.prompt or Path(args.prompt_file).read_text()
    lyrics = (args.lyrics if args.lyrics is not None
              else Path(args.lyrics_file).read_text() if args.lyrics_file else None)
    title = args.title or (Path(args.lyrics_file).stem if args.lyrics_file
                           else Path(args.prompt_file).stem if args.prompt_file
                           else "song")
    slug = slugify(title)
    budget = (args.timeout_budget if args.timeout_budget is not None  # 0 is a value
              else float(os.environ.get("MUSICGEN_SANDBOX_BUDGET")
                         or dotenv.get("MUSICGEN_SANDBOX_BUDGET") or 600))

    result = None
    if args.backend in ("auto", "sandbox"):
        lib.require_api_key(dotenv)
        state = lib.load_state()
        deadline = time.monotonic() + budget
        try:
            sb = ensure_sandbox(dotenv, state, deadline)
            result = generate_in_sandbox(sb, args, slug, prompt, lyrics)
            result["backend"] = "sandbox"
            if args.down:
                print("Tearing the sandbox down (--down).")
                lib.reap_by_tag(role="studio")
            else:
                print(f"Sandbox {sb.sandbox_id} left running for iteration — "
                      f"release it with `scripts/sandbox.py down`.")
        except FallbackNeeded as e:
            if args.backend == "sandbox":
                sys.exit(f"sandbox pathway failed and fallback is disabled: {e}")
            print(f"Sandbox pathway unavailable: {e}")

    if result is None:  # backend == "cluster", or sandbox acquisition bailed
        result = generate_on_cluster(args, slug, prompt, lyrics)

    print(f"\n✅ {result['wav_path']}  ({result['wall_seconds']}s, "
          f"backend={result['backend']})")
    print(f"   W&B run: {result.get('run_url') or 'URL not found in log'}")


if __name__ == "__main__":
    main()

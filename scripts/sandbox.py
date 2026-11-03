#!/usr/bin/env -S uv run --no-project --python 3.12 --script
# NB: --no-project + the explicit --python matter: without them uv resolves
# against the app's pyproject/.python-version and can rebuild the app venv for
# this script's environment (destructive, observed on a sibling project).
# /// script
# requires-python = ">=3.11"
# dependencies = ["cwsandbox>=1.19", "python-dotenv>=1.0"]
# ///
"""Music Generation Studio launcher — the APP pathway on CoreWeave serverless
GPU sandboxes.

Replaces the Slurm allocation + local-marimo workflow: the marimo app now runs
INSIDE a 1-GPU serverless sandbox (the same GPU generates the music) and is
served at a public tokenized HTTPS URL. The sandbox's /work is an instant fork
of a filesystem snapshot built once by `seed` (app venv + ~57 GB of
MiniMax-Music3 weights), so a launch is sandbox creation + snapshot restore
(~4-5 min), not a 57 GB download.

This is a standalone uv inline-metadata script (PEP 723) — cwsandbox must NOT
be added to the app's pyproject. Run it as:

    uv run --no-project --python 3.12 scripts/sandbox.py <cmd>

Subcommands:
  probe    ~1-minute GPU entitlement/capacity check (GPU sandboxes are preview)
  seed     one-time: build the /work snapshot on a cheap CPU-only sandbox
  reseed   incremental snapshot refresh (fork + delta + re-snapshot, minutes)
  up       create (or reuse) the studio sandbox, start marimo, print/open URL
  sync     push local code to the running sandbox and restart marimo
  pull     download WAVs from the sandbox that are missing locally
  down     stop all musicgen sandboxes (pulls WAVs first; --no-pull skips);
           --delete-snapshot also drops the FSS
  status   sandbox state, GPU model, marimo health, URL

The headless terminal/agent pathway (generate one song, Slurm fallback) is the
separate scripts/sandbox_generate.py — the two share scripts/sandbox_lib.py.

Auth + config come from the repo's .env (CWSANDBOX_API_KEY, WANDB_*, HF_TOKEN,
optional SNAPSHOT_ID / SANDBOX_IMAGE / SANDBOX_CPU / SANDBOX_MEMORY). Secret
VALUES are never printed and never passed on argv — they travel via sandbox
environment_variables only.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time

# cwsandbox (imported via sandbox_lib) installs SIGINT/SIGTERM handlers at
# import time — keep this import on the main thread.
import sandbox_lib as lib
from cwsandbox import Sandbox
from sandbox_lib import APP_PORT, APP_TAG, MOUNT, AUTH


# --- probe ---------------------------------------------------------------------

def cmd_probe(_args) -> None:
    """GPU entitlement + capacity probe. An unentitled org fails at create in
    <2 s ('not entitled to create GPU sandboxes', nothing billed); a full pool
    fails with RESOURCE_EXHAUSTED. Success also reveals which GPU model the
    heterogeneous pool hands us. Costs cents."""
    dotenv = lib.load_dotenv()
    sb, t0 = None, time.monotonic()
    try:
        sb = Sandbox.run(
            "sleep", "600",
            auth=AUTH,
            container_image=lib.resolve_image(dotenv),
            placement_mode="serverless",
            resources={"cpu": "2", "memory": "8Gi", "gpu": 1},
            max_lifetime_seconds=600,
            # APP_TAG too, so `down` reaps a probe orphaned by Ctrl-C.
            tags=[APP_TAG, f"{APP_TAG}-probe"],
        )
        sb.wait(timeout=600)
        print(f"RUNNING after {time.monotonic() - t0:.1f}s")  # expect ~30-65s
        print(sb.exec(["nvidia-smi", "-L"]).result().stdout)  # which card?
        print("GPU ACCESS CONFIRMED")
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")  # entitlement/capacity lands here
        sys.exit(1)
    finally:
        if sb is not None:
            Sandbox.delete(sb.sandbox_id, auth=AUTH, missing_ok=True).result()


# --- seed / reseed ----------------------------------------------------------------

def _build_snapshot(sb: Sandbox, state: dict,
                    old_id: str | None = None, keep_old: bool = False) -> None:
    """The one build sequence behind seed AND reseed: code + venv + weights →
    verify → prune → snapshot → persist; then (reseed) retire the old snapshot
    only once the replacement is READY and saved."""
    lib.bootstrap_code(sb)
    lib.ensure_model(sb)  # instant no-op when the weights are already present
    lib.verify_seed(sb)
    lib.prune_mount(sb)

    new_id = lib.snapshot_with_retry(sb)
    state["snapshot_id"] = new_id
    lib.save_state(state)
    print(f"✅ snapshot ready: {new_id}  (saved to {lib.STATE_FILE})")

    # Old snapshots bill per GiB-hr of storage — drop them once replaced.
    if old_id and old_id != new_id:
        if keep_old:
            print(f"Keeping old snapshot {old_id} (--keep-old)")
        else:
            print(f"Deleting old snapshot {old_id}")
            Sandbox.delete_snapshot(old_id, auth=AUTH, missing_ok=True).result()


def cmd_seed(_args) -> None:
    """One-time snapshot build on a CPU-ONLY sandbox (downloads + installs need
    no GPU — don't pay for one, and it works even when the GPU pool is full).
    Everything the app needs at runtime must live UNDER /work: snapshots
    capture only the mount. Expect ~30-60 min (~57 GB of weights)."""
    dotenv = lib.load_dotenv()
    state = lib.load_state()
    if state.get("snapshot_id"):
        sys.exit(f"snapshot {state['snapshot_id']} already exists.\n"
                 "For an incremental update (dep bump, runtime fix) run `reseed` "
                 "instead — minutes, not another full seed.\n"
                 "For a clean rebuild run `down --delete-snapshot` first.")

    print("Creating CPU seed sandbox...")
    sb = lib.create_seed(dotenv, "seed", lib.fss_new())
    try:
        print(f"Seed sandbox {sb.sandbox_id} running.")
        # uv itself must survive into forked sandboxes -> static binary under
        # the mount (pip exists in the pytorch image; curl may not).
        lib.sh(sb, f"python -m pip install -q uv && mkdir -p {MOUNT}/bin && "
                   f'cp "$(command -v uv)" {MOUNT}/bin/uv', timeout=240)
        _build_snapshot(sb, state)
    finally:
        print("Deleting seed sandbox.")
        Sandbox.delete(sb.sandbox_id, auth=AUTH, missing_ok=True).result()


def cmd_reseed(args) -> None:
    """Incremental snapshot refresh: fork the current snapshot on a CPU-only
    sandbox, apply only the delta (code, uv sync, missing weights),
    re-snapshot, then delete the old snapshot only after the new one is READY
    (--keep-old skips the delete). Running studio sandboxes are untouched —
    their mounts are independent forks; they pick the new snapshot up on the
    next `up`."""
    dotenv = lib.load_dotenv()
    state = lib.load_state()
    base_id = lib.resolve_snapshot_id(args.snapshot_id, state, dotenv)
    if not base_id:
        sys.exit("no snapshot to reseed from — run `seed` first, or adopt one "
                 "with --snapshot-id <id> (or SNAPSHOT_ID in .env)")

    print(f"Reseeding from snapshot {base_id} on a CPU-only sandbox...")
    sb = lib.create_seed(dotenv, "reseed", lib.fss_fork(base_id))
    try:
        print(f"Reseed sandbox {sb.sandbox_id} running.")
        _build_snapshot(sb, state,
                        old_id=state.get("snapshot_id"), keep_old=args.keep_old)
    finally:
        print("Deleting reseed sandbox.")
        Sandbox.delete(sb.sandbox_id, auth=AUTH, missing_ok=True).result()


# --- up / sync -------------------------------------------------------------------

def _finish(sb: Sandbox, state: dict) -> None:
    """Shared tail of `up` and `sync`: wait for marimo, print the URL, open."""
    if not lib.wait_http(sb, APP_PORT, "marimo", timeout=600):
        raise RuntimeError(
            f"marimo did not come up — check {MOUNT}/logs/marimo.log via "
            f"`sandbox.py status`")
    # The token must be the one baked into THIS sandbox's env — an adopted
    # sandbox won't match local state (ensure_app_token reconciles).
    token = lib.ensure_app_token(sb, state)
    url = f"{lib.service_url(sb, APP_PORT)}/?access_token={token}"
    print(f"\n✅ ready: {url}")
    print("   stop:  uv run --no-project --python 3.12 scripts/sandbox.py down")
    if sys.platform == "darwin":
        subprocess.run(["open", url], check=False)


def _sync(sb: Sandbox, state: dict) -> None:
    """Push local code (source of truth), restart marimo, print the URL."""
    lib.bootstrap_code(sb)
    lib.start_marimo(sb)
    _finish(sb, state)


def cmd_up(args) -> None:
    dotenv = lib.load_dotenv()
    state = lib.load_state()

    # Reuse path (the sandbox analogue of find-or-create on the Slurm queue) —
    # identical to `sync` once a sandbox is in hand.
    sb = lib.find_studio(state)
    if sb:
        print(f"Reusing sandbox {sb.sandbox_id}")
        state["studio_id"] = sb.sandbox_id
        lib.save_state(state)
        _sync(sb, state)
        return

    snapshot_id = lib.resolve_snapshot_id(args.snapshot_id, state, dotenv)
    if not snapshot_id:
        sys.exit("No snapshot yet — run the one-time `sandbox.py seed` first, "
                 "or adopt a teammate's snapshot with --snapshot-id <id> "
                 "(or SNAPSHOT_ID in .env).")
    if snapshot_id != state.get("snapshot_id"):
        print(f"Adopting snapshot {snapshot_id} into {lib.STATE_FILE}")
        state["snapshot_id"] = snapshot_id
        lib.save_state(state)

    print("Creating studio sandbox (~60s create + ~4 min snapshot restore)...")
    try:
        sb = lib.create_studio(dotenv, state, snapshot_id)
        print(f"Sandbox up: {sb.sandbox_id}")
        _sync(sb, state)
    except lib.SandboxResourceExhaustedError:
        sys.exit("The serverless GPU pool is full (all retries exhausted). "
                 "Nothing was created or billed. Try `up` again later, or "
                 "generate headlessly now — scripts/sandbox_generate.py falls "
                 "back to the Slurm cluster automatically.")
    except Exception:
        # Reap ONLY the studio role — a seed/reseed build running in another
        # terminal shares APP_TAG and must survive this failure.
        print("Launch failed — reaping the studio sandbox.", file=sys.stderr)
        lib.reap_by_tag(role="studio")
        raise


def cmd_sync(_args) -> None:
    """Push local code (source of truth) to the running sandbox and restart
    marimo — the fast edit loop; no sandbox recreation."""
    state = lib.load_state()
    sb = lib.find_studio(state)
    if not sb:
        sys.exit("studio sandbox is not running — use `sandbox.py up`")
    state["studio_id"] = sb.sandbox_id
    lib.save_state(state)
    _sync(sb, state)


# --- pull / down / status -----------------------------------------------------------

def cmd_pull(_args) -> None:
    """Download sandbox-side WAVs missing locally. The app's outputs live only
    on the ephemeral mount — pull before (or instead of) `down`."""
    sb = lib.find_studio(lib.load_state())
    if not sb:
        sys.exit("studio sandbox is not running — nothing to pull")
    pulled = lib.pull_wavs(sb)
    print(f"{pulled} new WAV(s) -> generated_audio/MiniMax-Music3/"
          if pulled else "nothing new to pull")


def cmd_down(args) -> None:
    if not args.no_pull:
        try:
            sb = lib.find_studio(lib.load_state())
            if sb:
                pulled = lib.pull_wavs(sb)
                if pulled:
                    print(f"Pulled {pulled} WAV(s) before teardown.")
        except Exception as e:  # never let a pull hiccup block the teardown
            print(f"warning: WAV pull failed ({type(e).__name__}: {e}) — "
                  f"tearing down anyway", file=sys.stderr)
    lib.reap_by_tag(delete_snapshot=args.delete_snapshot)


def cmd_status(_args) -> None:
    state = lib.load_state()
    any_found = False
    # One list per role: the SDK filters tags server-side and listed handles
    # carry no tags, so roles cannot be partitioned from a single broad list.
    for role in ("studio", "seed", "probe"):
        for sb in Sandbox.list(tags=[f"{APP_TAG}-{role}"], auth=AUTH).result():
            any_found = True
            status = sb.get_status().name
            urls = "  ".join(u for _p, _n, u in sb.service_urls) or "-"
            print(f"{role:7s} {sb.sandbox_id}  {status:8s} {urls}")
            if role == "studio" and status == "RUNNING":
                try:  # one exec for GPU + marimo health; listed handle execs fine
                    info = (lib.sh(
                        sb, "nvidia-smi -L 2>/dev/null | head -1; "
                            "pgrep -f 'bin/marimo' >/dev/null "
                            "&& echo marimo:UP || echo marimo:DOWN"
                    ).stdout or "").strip().replace("\n", "  ")
                    if info:
                        print(f"        {info}")
                    token = lib.ensure_app_token(sb, state)
                    print(f"        url: {lib.service_url(sb, APP_PORT)}"
                          f"/?access_token={token}")
                except Exception:
                    pass
    if not any_found:
        print("no sandboxes")
    if state.get("launched_at"):
        print(f"launched: {state['launched_at']}")
    print(f"snapshot: {state.get('snapshot_id') or 'none (run `sandbox.py seed`)'}")


# --- main ------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("probe", help="1-min GPU entitlement/capacity check").set_defaults(fn=cmd_probe)
    sub.add_parser("seed", help="one-time snapshot build (venv + weights)").set_defaults(fn=cmd_seed)
    reseed = sub.add_parser("reseed", help="incremental snapshot refresh")
    reseed.add_argument("--snapshot-id",
                        help="base snapshot to fork (default: state, then SNAPSHOT_ID in .env)")
    reseed.add_argument("--keep-old", action="store_true",
                        help="keep the replaced snapshot instead of deleting it")
    reseed.set_defaults(fn=cmd_reseed)
    up = sub.add_parser("up", help="launch (or reuse) the studio sandbox")
    up.add_argument("--snapshot-id",
                    help="adopt an existing org snapshot and launch from it "
                         "(also honored as SNAPSHOT_ID in .env)")
    up.set_defaults(fn=cmd_up)
    sub.add_parser("sync", help="push code + restart marimo").set_defaults(fn=cmd_sync)
    sub.add_parser("pull", help="download WAVs missing locally").set_defaults(fn=cmd_pull)
    down = sub.add_parser("down", help="stop all musicgen sandboxes (pulls WAVs first)")
    down.add_argument("--delete-snapshot", action="store_true",
                      help="also delete the FSS snapshot (next launch re-seeds)")
    down.add_argument("--no-pull", action="store_true",
                      help="skip downloading WAVs before teardown")
    down.set_defaults(fn=cmd_down)
    sub.add_parser("status", help="sandbox state, GPU, marimo health, URL").set_defaults(fn=cmd_status)
    args = parser.parse_args()

    dotenv = lib.load_dotenv()
    lib.require_api_key(dotenv)
    args.fn(args)


if __name__ == "__main__":
    main()

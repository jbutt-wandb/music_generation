"""Execution backend for the marimo app: the local GPU of the CoreWeave sandbox.

The app runs INSIDE a serverless GPU sandbox (launched by `scripts/sandbox.py up`),
so generation is a plain local subprocess of `scripts/minimax_music3.py` — the
app stays a pure client of the same script the CLI workflow uses, and W&B
logging, captions, and outputs stay identical.

This module NEVER provisions or releases sandboxes — `scripts/sandbox.py` owns
the lifecycle. `sandbox_status()` only detects whether we are inside one.

It is also the canonical, stdlib-only home of the generation-log grammar
(FAILURE_RE / DONE_MARKER / WANDB_URL_RE / _parse_log) and of slugify():
`scripts/sandbox_generate.py` imports them so both pathways parse the same
script's output identically.
"""

import fcntl
import logging
import os
import re
import subprocess
import sys
import tempfile
import threading
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_WAV_DIR = os.path.join("generated_audio", "MiniMax-Music3")

# `srun: error` cannot occur in the app's local subprocess log; it is kept for
# scripts/sandbox_generate.py, whose Slurm fallback imports this grammar.
FAILURE_RE = re.compile(r"Traceback|CUDA out of memory|srun: error|RuntimeError|Killed|ValueError")
DONE_MARKER = "Successfully finished run="
SAVED_MARKER = "Saved audio locally to"
# Matches both the startup line ("View run at <url>") and the completion line
# ("View run <name> at: <url>").
WANDB_URL_RE = re.compile(r"View run .*?at:? (https://wandb\.ai/\S+)")
PROGRESS_RE = re.compile(r"(\d+)%\|")

# One generation at a time. The threading lock stops duplicate launches within
# this marimo process (a re-fired cell, a second browser tab); the flock on
# .gen.lock extends that to the whole sandbox, where scripts/sandbox_generate.py
# may target the same GPU from outside this process.
_RUN_LOCK = threading.Lock()
GEN_LOCK_PATH = os.path.join(REPO_ROOT, ".gen.lock")


def get_logger():
    """App-wide logger -> logs/app_ui.log (created lazily, shared by app + backend)."""
    logger = logging.getLogger("musicgen_app")
    if not logger.handlers:
        os.makedirs("logs", exist_ok=True)
        handler = logging.FileHandler(os.path.join("logs", "app_ui.log"))
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


log = get_logger()


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled"


def _query_gpu_name():
    """Live GPU probe; returns the device name or None. Never raises."""
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().splitlines()[0].strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return None


# The GPU model is immutable for the sandbox's lifetime; cache it so the UI's
# status cell doesn't spawn nvidia-smi on every re-render (retry only while
# the probe has never succeeded).
_GPU_NAME_CACHE = None


def sandbox_status():
    """Return {"sandbox_id": str, "gpu_name": str|None} when inside a sandbox, else None.

    Detection: the launcher exports MUSICGEN_SANDBOX_ID into the sandbox env
    (fallback: a `.sandbox_id` file it drops at the repo root). Never raises.
    """
    global _GPU_NAME_CACHE
    try:
        sandbox_id = os.environ.get("MUSICGEN_SANDBOX_ID")
        if not sandbox_id:
            try:
                with open(os.path.join(REPO_ROOT, ".sandbox_id"), encoding="utf-8") as f:
                    sandbox_id = f.read().strip() or None
            except OSError:
                sandbox_id = None
        if not sandbox_id:
            return None
        if _GPU_NAME_CACHE is None:
            _GPU_NAME_CACHE = _query_gpu_name()
        return {"sandbox_id": sandbox_id, "gpu_name": _GPU_NAME_CACHE}
    except Exception:
        return None


def _parse_log(text):
    """-> (state in {running, done, failed}, human phase string, wandb_url|None)."""
    url = None
    m = WANDB_URL_RE.search(text)
    if m:
        url = m.group(1).rstrip(".")
    if DONE_MARKER in text and SAVED_MARKER in text:
        return "done", "finished", url
    if FAILURE_RE.search(text):
        return "failed", "failed — see log", url
    phase = "starting…"
    if "Loading MiniMax-Music3" in text:
        phase = "loading model… (~1–2 min)"
    if "Generating music for prompt" in text:
        phase = "composing with the language model… (the long part)"
    pcts = PROGRESS_RE.findall(text)
    if pcts:
        phase = f"decoding audio — {pcts[-1]}%"
    if "wandb: uploading" in text or "wandb: updating" in text:
        phase = "uploading to W&B…"
    return "running", phase, url


def _tail_log(log_path, n_bytes=4000):
    """Last n_bytes of the log without re-reading the whole growing file."""
    with open(log_path, encoding="utf-8", errors="replace") as f:
        size = os.path.getsize(log_path)
        f.seek(max(0, size - n_bytes))
        return f.read().replace("\r", "\n")


def run_sandbox(prompt, lyrics_text, title_slug, duration, seed, steps, on_status=print, poll_seconds=5, timeout_minutes=45):
    """Generate on this sandbox's GPU as a local subprocess. Blocking; reports via on_status."""
    busy = {"ok": False, "error": "Another generation is already in progress — wait for it to finish.", "log_tail": ""}
    if not _RUN_LOCK.acquire(blocking=False):
        log.warning("run_sandbox REFUSED (slug=%s seed=%s): another generation is already in progress", title_slug, seed)
        return busy
    gen_lock = open(GEN_LOCK_PATH, "w")
    try:
        try:
            fcntl.flock(gen_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            log.warning("run_sandbox REFUSED (slug=%s seed=%s): .gen.lock held by another process", title_slug, seed)
            return busy
        return _run_generation(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes)
    finally:
        gen_lock.close()  # closing the fd releases the flock
        _RUN_LOCK.release()


def _run_generation(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes):
    log.info("run_sandbox START slug=%s seed=%s duration=%s steps=%s", title_slug, seed, duration, steps)
    # Live GPU check before spending a launch: a wedged driver should be an
    # upfront refusal, not a CUDA traceback minutes in.
    if _query_gpu_name() is None:
        log.error("run_sandbox REFUSED slug=%s: nvidia-smi probe failed", title_slug)
        return {"ok": False, "error": "The sandbox GPU is unavailable (nvidia-smi failed). Recreate the sandbox with scripts/sandbox.py.", "log_tail": ""}

    workdir = tempfile.mkdtemp(prefix="musicgen_app_")
    lyrics_path = os.path.join(workdir, f"{title_slug}.txt")
    with open(lyrics_path, "w", encoding="utf-8") as f:
        f.write(lyrics_text)
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", f"app_{title_slug}_s{seed}.log")
    os.makedirs(LOCAL_WAV_DIR, exist_ok=True)
    wav_path = os.path.join(LOCAL_WAV_DIR, f"{title_slug}_s{seed}.wav")

    on_status("starting generation on the sandbox GPU…")
    # sys.executable is the sandbox venv's python (the one running marimo); the
    # process inherits the sandbox env (TORCH_DISABLE_NATIVE_JIT and
    # PYTORCH_CUDA_ALLOC_CONF are set at sandbox creation, and the script
    # self-defaults both as well).
    with open(log_path, "w") as log_file:
        proc = subprocess.Popen(
            [sys.executable, os.path.join("scripts", "minimax_music3.py"),
             "--prompt", prompt, "--lyrics_file", lyrics_path,
             "--audio_duration", str(duration), "--num_inference_steps", str(steps),
             "--seed", str(seed), "--output", wav_path],
            stdout=log_file, stderr=subprocess.STDOUT,
        )

    started = time.time()
    log_tail = ""
    last_phase = None
    while time.time() - started < timeout_minutes * 60:
        time.sleep(poll_seconds)
        log_tail = _tail_log(log_path)
        state, phase, wandb_url = _parse_log(log_tail)
        if phase != last_phase:
            log.info("run_sandbox phase slug=%s: %s", title_slug, phase)
            last_phase = phase
        on_status(phase)
        if state == "done":
            log.info("run_sandbox DONE slug=%s seed=%s wall=%ss url=%s", title_slug, seed, round(time.time() - started), wandb_url)
            return {
                "ok": True, "wav_path": wav_path, "run_url": wandb_url,
                "wall_seconds": round(time.time() - started), "log_tail": log_tail,
            }
        if state == "failed" or (proc.poll() is not None and proc.returncode != 0):
            log.error("run_sandbox FAILED slug=%s seed=%s; log tail:\n%s", title_slug, seed, log_tail[-1500:])
            return {"ok": False, "error": "Generation failed on the sandbox GPU.", "log_tail": log_tail}
    proc.terminate()
    log.error("run_sandbox TIMEOUT slug=%s after %s min", title_slug, timeout_minutes)
    return {"ok": False, "error": f"Timed out after {timeout_minutes} min.", "log_tail": log_tail}

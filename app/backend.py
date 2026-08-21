"""Execution backends for the marimo app: CoreWeave cluster (CUDA) or local Mac (MPS).

Both run `scripts/minimax_music3.py` — the app is purely a client of the same
script the CLI workflow uses, so W&B logging, captions, and outputs stay
identical. The cluster backend follows the CLAUDE.md launch pattern verbatim
(nohup + srun --overlap into an existing allocation, one log per run).

This module NEVER provisions or releases the Slurm allocation — the user must
start it themselves (see README). `cluster_status()` only detects it.
"""

import logging
import os
import re
import subprocess
import tempfile
import threading
import time

SSH_HOST = "coreweave-login"
REMOTE_DIR = "~/music_gen_demo"
JOB_NAME = "musicgen"
LOCAL_WAV_DIR = os.path.join("generated_audio", "MiniMax-Music3")

FAILURE_RE = re.compile(r"Traceback|CUDA out of memory|srun: error|RuntimeError|Killed|ValueError")
DONE_MARKER = "Successfully finished run="
# Matches both the startup line ("View run at <url>") and the completion line
# ("View run <name> at: <url>").
WANDB_URL_RE = re.compile(r"View run .*?at:? (https://wandb\.ai/\S+)")
PROGRESS_RE = re.compile(r"(\d+)%\|")

SBATCH_CMD = (
    'sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G '
    '--job-name=musicgen --wrap "sleep infinity"'
)

# One generation at a time, process-wide: there is one GPU, and marimo can
# re-fire a cell (e.g. a mid-run dependency change or a second browser tab)
# — the lock turns a would-be duplicate launch into a logged refusal.
_RUN_LOCK = threading.Lock()


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


def _ssh(command, input_text=None, timeout=30):
    # errors="replace": `tail -c` can cut the log mid-UTF-8-character (tqdm's
    # bar glyphs are multi-byte), which would crash strict decoding.
    return subprocess.run(
        ["ssh", "-o", "BatchMode=yes", SSH_HOST, command],
        input=input_text, capture_output=True, text=True, errors="replace", timeout=timeout,
    )


def cluster_status():
    """Return {"jobid": str, "state": str} for a running musicgen allocation, else None.

    Never provisions — detection only.
    """
    try:
        result = _ssh(f'squeue -u $USER -h -n {JOB_NAME} -t R -o "%i %T"')
    except (subprocess.TimeoutExpired, OSError):
        return None
    line = result.stdout.strip().splitlines()
    if result.returncode != 0 or not line:
        return None
    jobid, state = line[0].split()[:2]
    return {"jobid": jobid, "state": state}


def _parse_log(text):
    """-> (state in {running, done, failed}, human phase string, wandb_url|None)."""
    url = None
    m = WANDB_URL_RE.search(text)
    if m:
        url = m.group(1).rstrip(".")
    if DONE_MARKER in text and "Saved audio locally to" in text:
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


def _finalize(slug, seed, wandb_url, started, fetch_wav, log_tail):
    os.makedirs(LOCAL_WAV_DIR, exist_ok=True)
    local_wav = os.path.join(LOCAL_WAV_DIR, f"{slug}_s{seed}.wav")
    fetch_wav(local_wav)
    return {
        "ok": True, "wav_path": local_wav, "run_url": wandb_url,
        "wall_seconds": round(time.time() - started), "log_tail": log_tail,
    }


def run_cluster(prompt, lyrics_text, title_slug, duration, seed, steps, on_status=print, poll_seconds=5, timeout_minutes=45):
    """Generate on the H100 cluster inside the existing allocation. Blocking; reports via on_status."""
    if not _RUN_LOCK.acquire(blocking=False):
        log.warning("run_cluster REFUSED (slug=%s seed=%s): another generation is already in progress", title_slug, seed)
        return {"ok": False, "error": "Another generation is already in progress — wait for it to finish.", "log_tail": ""}
    try:
        return _run_cluster_locked(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes)
    finally:
        _RUN_LOCK.release()


def _run_cluster_locked(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes):
    status = cluster_status()
    if status is None:
        log.warning("run_cluster (slug=%s): no running allocation", title_slug)
        return {"ok": False, "error": "No running 'musicgen' allocation found. Start one first:\n" + SBATCH_CMD, "log_tail": ""}
    jobid = status["jobid"]
    log.info("run_cluster START slug=%s seed=%s duration=%s steps=%s jobid=%s", title_slug, seed, duration, steps, jobid)

    log_name = f"logs/app_{title_slug}_s{seed}.log"
    on_status("uploading inputs to the cluster…")
    _ssh(f"mkdir -p {REMOTE_DIR}/tmp {REMOTE_DIR}/logs && cat > {REMOTE_DIR}/tmp/{title_slug}_prompt.txt", input_text=prompt)
    _ssh(f"cat > {REMOTE_DIR}/tmp/{title_slug}.txt", input_text=lyrics_text)

    launch = (
        f"cd {REMOTE_DIR} && "
        f"nohup env TORCH_DISABLE_NATIVE_JIT=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True "
        f"srun --jobid={jobid} --overlap --export=ALL "
        f'.venv/bin/python scripts/minimax_music3.py --prompt "$(cat tmp/{title_slug}_prompt.txt)" '
        f"--lyrics_file tmp/{title_slug}.txt --audio_duration {duration} "
        f"--num_inference_steps {steps} --seed {seed} > {log_name} 2>&1 &"
    )
    # Popen: the ssh session stays open for the lifetime of the remote process;
    # we watch the log instead of the process and let this reaper exit on its own.
    launcher = subprocess.Popen(
        ["ssh", "-o", "BatchMode=yes", SSH_HOST, launch],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    on_status("launched on the H100 — waiting for the model…")
    log.info("run_cluster LAUNCHED slug=%s -> %s", title_slug, log_name)

    started = time.time()
    log_tail = ""
    last_phase = None
    try:
        while time.time() - started < timeout_minutes * 60:
            time.sleep(poll_seconds)
            try:
                result = _ssh(f'tail -c 4000 {REMOTE_DIR}/{log_name} 2>/dev/null | tr "\\r" "\\n"')
            except subprocess.TimeoutExpired:
                log.warning("run_cluster poll ssh timeout (slug=%s) — retrying", title_slug)
                continue
            log_tail = result.stdout
            state, phase, wandb_url = _parse_log(log_tail)
            if phase != last_phase:
                log.info("run_cluster phase slug=%s: %s", title_slug, phase)
                last_phase = phase
            on_status(phase)
            if state == "done":
                log.info("run_cluster DONE slug=%s seed=%s wall=%ss url=%s", title_slug, seed, round(time.time() - started), wandb_url)
                def fetch(local_wav):
                    subprocess.run(
                        ["scp", "-q", f"{SSH_HOST}:music_gen_demo/generated_audio/MiniMax-Music3/minimax_music3_output.wav", local_wav],
                        check=True, timeout=120,
                    )
                return _finalize(title_slug, seed, wandb_url, started, fetch, log_tail)
            if state == "failed":
                log.error("run_cluster FAILED slug=%s seed=%s; log tail:\n%s", title_slug, seed, log_tail[-1500:])
                return {"ok": False, "error": "Generation failed on the cluster.", "log_tail": log_tail}
        log.error("run_cluster TIMEOUT slug=%s after %s min", title_slug, timeout_minutes)
        return {"ok": False, "error": f"Timed out after {timeout_minutes} min.", "log_tail": log_tail}
    finally:
        if launcher.poll() is None and time.time() - started >= timeout_minutes * 60:
            launcher.terminate()


def run_mps(prompt, lyrics_text, title_slug, duration, seed, steps, on_status=print, poll_seconds=5, timeout_minutes=120):
    """Generate locally on Apple Silicon (--device mps). Experimental; blocking."""
    if not _RUN_LOCK.acquire(blocking=False):
        log.warning("run_mps REFUSED (slug=%s seed=%s): another generation is already in progress", title_slug, seed)
        return {"ok": False, "error": "Another generation is already in progress — wait for it to finish.", "log_tail": ""}
    try:
        return _run_mps_locked(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes)
    finally:
        _RUN_LOCK.release()


def _run_mps_locked(prompt, lyrics_text, title_slug, duration, seed, steps, on_status, poll_seconds, timeout_minutes):
    log.info("run_mps START slug=%s seed=%s duration=%s steps=%s", title_slug, seed, duration, steps)
    workdir = tempfile.mkdtemp(prefix="musicgen_app_")
    lyrics_path = os.path.join(workdir, f"{title_slug}.txt")
    with open(lyrics_path, "w", encoding="utf-8") as f:
        f.write(lyrics_text)
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", f"app_{title_slug}_s{seed}_mps.log")

    on_status("starting local MPS generation (first run downloads ~57 GB)…")
    with open(log_path, "w") as log_file:
        proc = subprocess.Popen(
            [os.path.join(".venv", "bin", "python"), os.path.join("scripts", "minimax_music3.py"),
             "--device", "mps", "--prompt", prompt, "--lyrics_file", lyrics_path,
             "--audio_duration", str(duration), "--num_inference_steps", str(steps), "--seed", str(seed)],
            stdout=log_file, stderr=subprocess.STDOUT,
        )

    started = time.time()
    log_tail = ""
    last_phase = None
    while time.time() - started < timeout_minutes * 60:
        time.sleep(poll_seconds)
        with open(log_path, encoding="utf-8", errors="replace") as f:
            log_tail = f.read()[-4000:].replace("\r", "\n")
        state, phase, wandb_url = _parse_log(log_tail)
        if phase != last_phase:
            log.info("run_mps phase slug=%s: %s", title_slug, phase)
            last_phase = phase
        on_status(phase)
        if state == "done":
            log.info("run_mps DONE slug=%s seed=%s wall=%ss", title_slug, seed, round(time.time() - started))
            def fetch(local_wav):
                os.replace(os.path.join("generated_audio", "MiniMax-Music3", "minimax_music3_output.wav"), local_wav)
            return _finalize(title_slug, seed, wandb_url, started, fetch, log_tail)
        if state == "failed" or (proc.poll() is not None and proc.returncode != 0):
            log.error("run_mps FAILED slug=%s; log tail:\n%s", title_slug, log_tail[-1500:])
            return {"ok": False, "error": "Local MPS generation failed (this path is experimental).", "log_tail": log_tail}
    proc.terminate()
    log.error("run_mps TIMEOUT slug=%s after %s min", title_slug, timeout_minutes)
    return {"ok": False, "error": f"Timed out after {timeout_minutes} min.", "log_tail": log_tail}

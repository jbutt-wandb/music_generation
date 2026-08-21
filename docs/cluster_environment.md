# Cluster Environment Setup — MiniMax-Music3 on CoreWeave H100s

How to configure the environment for `minimax_music3.py` (MiniMax-Music3 text-to-music
via diffusers Modular Pipelines) so it runs cleanly on the Slurm cluster. Most entries
are inherited from the sibling video repo (`video_generation_model`), where each one
was a real failure hit on 2026-08-10 on these same nodes — the node-level quirks apply
to any torch ≥ 2.13 workload. Re-verify on the first Music3 run and update this doc.

## TL;DR checklist

```bash
# On the cluster, in the project directory (~/music_gen_demo):
export PATH="$HOME/.local/bin:$PATH"     # uv is not on PATH in non-interactive shells
# do NOT `uv add kernels` (see below)

# Verify the audio writer imports BEFORE launching — a save failure throws only
# AFTER the full generation and wastes the whole run:
.venv/bin/python -c "import soundfile"

# In .env (or the job script):
TORCH_DISABLE_NATIVE_JIT=1               # required on these compute nodes for torch >= 2.13
HF_TOKEN=hf_...                          # newer huggingface_hub ignores HUGGINGFACEHUB_API_TOKEN
WANDB_API_KEY=...
WANDB_ENTITY=...
WANDB_PROJECT=...
```

Launch pattern that works (from a login node, into an existing allocation):

```bash
cd ~/music_gen_demo && mkdir -p logs
nohup env TORCH_DISABLE_NATIVE_JIT=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  srun --jobid=<JOBID> --overlap --export=ALL \
  .venv/bin/python scripts/minimax_music3.py --prompt "..." \
  --lyrics_file assets/neon_rain.txt --audio_duration 60 --seed 42 \
  > logs/music_run.log 2>&1 &
```

Hardware: one H100 80GB is plenty — the model is ~23 GB in bf16 (8B Qwen3 language
model + 0.6B RVQ depth decoder + 2.4B flow-matching transformer + vocoder). The first
run downloads ~57 GB into `~/.cache/huggingface`; check the quota before launching.

The marimo app (`app/app.py`) drives this same setup remotely: it writes its inputs
to `~/music_gen_demo/tmp/` and its logs to `logs/app_*.log`, and it **assumes a
running `musicgen` allocation — it never provisions or releases one.**

## The errors and their fixes

### 1. `execve(): uv: No such file or directory`

**Cause:** `uv` lives in `~/.local/bin`, which is only added to PATH by the interactive
shell profile. Non-interactive shells (`ssh host "cmd"`, `srun` payloads, sbatch scripts)
don't source it.

**Fix:** either `export PATH="$HOME/.local/bin:$PATH"` at the top of job scripts, or skip
`uv run` entirely and invoke the venv interpreter directly: `.venv/bin/python script.py`.
The direct interpreter path is the more robust choice inside `srun`.

### 2. `subprocess.CalledProcessError: ['/usr/bin/gcc', '.../cuda_utils.c', ...]` (triton)

**Cause:** torch 2.13's `torch._native` op system intercepts certain aten ops and routes
them to triton-JIT kernels. Triton's JIT gcc-compiles a small C stub against `Python.h` —
and the compute nodes have no Python dev headers (no root to install `python3-dev`).
The Qwen3 language model at the heart of Music3 exercises exactly the op family
(`aten::bmm` in RoPE paths) that hit this in the video repo.

**Fix:** set `TORCH_DISABLE_NATIVE_JIT=1` in the environment. This is torch's official
escape hatch: it skips registering the triton/cuteDSL native ops so torch uses its
standard precompiled CUDA kernels. Results are identical; the perf difference is
negligible for this workload. The script also sets it defensively before `import torch`,
but keep it in the launch template for any other entry point.

### 3. Same gcc/triton error via the `kernels` package

**Cause:** installing `kernels` (to enable hub attention backends) makes transformers
pull triton-JIT hub kernels, which fail to compile for the same missing-headers reason.

**Fix:** don't install `kernels` on this cluster.

### 4. Audio write fails *after* generation

**Cause class:** the WAV writer is the last thing to run — any import/codec problem in
it throws after all the GPU work is done. In the video repo the equivalent failure
(PyAV missing for the mp4 mux) cost a full 15-minute generation.

**Fix:** this repo writes with `soundfile` (its wheel bundles libsndfile, no system
ffmpeg needed). Verify `.venv/bin/python -c "import soundfile"` on the compute node
*before* the first launch. If the pipeline's `load_components()` ever fails on the
tokenizer/vocoder side with a missing-dependency warning, the contingency is
`uv add torchaudio` — not needed at the pinned revs as of 2026-08-19.

### 5. (Warning, not fatal) unauthenticated Hugging Face Hub requests

**Cause:** a `.env` that sets `HUGGINGFACEHUB_API_TOKEN`, a legacy variable name that
newer `huggingface_hub` releases no longer read.

**Fix:** add `HF_TOKEN=<same value>` to `.env`. MiniMax-Music3 is CC-BY-4.0 and not
license-gated, so this only matters for download rate limits — but the ~57 GB first
download is exactly when you'll want it.

### 6. Silent component failures in Modular Pipelines

**Lesson from the video repo:** if a modular-pipeline component is unexpectedly `None`
at generation time, the real cause is a *warning* logged much earlier — search the log
for "Failed to create component", not the final traceback.

## Failure-mode summary

| Symptom | Root cause | Fix |
|---|---|---|
| `uv: No such file or directory` | `~/.local/bin` not on non-interactive PATH | Use `.venv/bin/python` directly |
| gcc fails compiling `cuda_utils.c` | triton JIT needs `Python.h`; nodes lack dev headers | `TORCH_DISABLE_NATIVE_JIT=1`; don't install `kernels` |
| import/codec error at the WAV write | audio writer only runs *after* generation | verify `import soundfile` before launching |
| "unauthenticated requests to the HF Hub" | legacy `HUGGINGFACEHUB_API_TOKEN` var | add `HF_TOKEN` to `.env` |
| component is `None` mid-pipeline | earlier "Failed to create component" warning | fix the missing dep the warning names |

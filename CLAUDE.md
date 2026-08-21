# CLAUDE.md

Rules for coding agents working in this repo. The GPU workloads run remotely on a
CoreWeave Slurm cluster; the agent drives everything from the local machine over ssh.

## Cluster execution — compute nodes only, never the login node

- Connect with `ssh coreweave-login`. The login node is for orchestration only
  (sbatch/squeue/scancel, file transfer, tailing logs). **Never run Python
  workloads, model downloads, or anything GPU/CPU-heavy on the login node.**
- All generation runs on a compute node, always through an allocation:
  1. `sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G --job-name=musicgen --wrap "sleep infinity"`
  2. launch work into it with `srun --jobid=<JOBID> --overlap --export=ALL`
- `uv` is not on PATH in non-interactive/srun shells — invoke `.venv/bin/python`
  directly. Full environment quirks and error→fix table: `docs/cluster_environment.md`.
- The marimo app (`app/app.py`) never provisions or releases allocations — it only
  detects a running `musicgen` job. Agents still manage allocations per these rules.
- Release the allocation (`scancel <JOBID>`) when iteration is done; confirm with
  `squeue`. Don't leave idle GPUs held.

## Provisioning — check resources fit before launching

Before every provision/launch, verify the request is appropriate:

- `sinfo -p h100` — confirm idle nodes exist; `squeue -u $USER` — confirm no
  forgotten allocation is already running (reuse it if so).
- MiniMax-Music3 needs **one** H100 80GB (~23 GB of bf16 weights, fully resident
  with `--offload none`). **Do not request 2 GPUs** — the stages run sequentially
  and a second card sits idle.
- `--audio_duration` is capped at 360 s; generation is single-sample, so seed
  sweeps are separate launches, not bigger allocations. The first run downloads
  ~57 GB to `~/.cache/huggingface` — check quota. Always set
  `TORCH_DISABLE_NATIVE_JIT=1` and `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`.

## Prompting — read the guide first

**Always read `docs/minimax_music_prompt_guide.md` before composing or sending any
model command.** MiniMax-Music3 takes two inputs with strictly separate jobs: the
`--prompt` is a **Structured Caption** (three labeled sections: Global Metadata /
Vocal Details / Arrangement, ~250–450 words), and `--lyrics` carries the words to
sing with bracketed section tags each on their own line. Lyric text is sacred —
never rewrite it or quote it into the caption; only the tags are directives.
The two skills in `.claude/skills/` divide this work and chain via the section
tags: **`lyrics-writer`** drafts original tagged lyrics (theme → `assets/<title>.txt`,
structure sized to `--audio_duration`), then **`music-caption-rewriter`** turns a
style brief + those lyrics' tags into the Structured Caption (genre router →
style-family index → reference templates). Run them in that order — lyrics first,
caption second — so the caption's Arrangement timeline matches the actual sections;
if the lyrics change, regenerate the caption too. Iterate at the cheapest layer
that answers the request: new take → `--seed` only; new sound → new caption
(lyrics + seed fixed); new words → new lyrics, then new caption. Worked,
known-good commands live in `docs/run_commands.md`.

## Run, monitor, log

- Launch pattern (from the login node, into the allocation), one log file per run:

  ```bash
  cd ~/music_gen_demo && mkdir -p logs
  nohup env TORCH_DISABLE_NATIVE_JIT=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
    srun --jobid=<JOBID> --overlap --export=ALL \
    .venv/bin/python scripts/minimax_music3.py <args> > logs/<name>.log 2>&1 &
  ```

- Monitor the log until a terminal state, watching for **failure signatures as
  well as success**: `Traceback`, `CUDA out of memory`, `srun: error`,
  `RuntimeError`, `Killed`, or the launched PID disappearing. Completion markers
  are `wandb: Synced` and `Saved audio locally to ...wav` — note that
  `wandb: View run at <url>` prints at *startup* and is not a completion signal.
- Every run logs to W&B (entity/project from `.env`); the run URL is in the log
  and the finished WAV is on the run page (panel "Generated Audio").
  Cluster-side outputs land in `generated_audio/MiniMax-Music3/`; scp finals
  back to local `generated_audio/`.
- After a run teaches something new (a good caption pattern, timing numbers, the
  measured sample rate or peak VRAM), record it in `docs/run_commands.md` and
  keep `scripts/` and `docs/` in sync between the local repo and the cluster
  mirror (`~/music_gen_demo`).

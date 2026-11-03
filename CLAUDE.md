# CLAUDE.md

Rules for coding agents working in this repo. GPU workloads run in **CoreWeave
serverless GPU sandboxes** (primary) with the CoreWeave Slurm cluster as a
budgeted **fallback**; the agent drives everything from the local machine.

## Sandbox execution — the primary pathway

Two partitioned entry points (PEP 723 uv scripts — always invoke with
`uv run --no-project --python 3.12`, never plain `uv run`, which would rebuild
the app venv):

- **`scripts/sandbox.py`** — the app pathway: `probe | seed | reseed | up |
  sync | pull | down | status`. `up` serves the marimo app from inside a 1-GPU
  sandbox at a public tokenized URL.
- **`scripts/sandbox_generate.py`** — the headless pathway: one song end-to-end
  (`--prompt_file/--prompt`, `--lyrics_file/--lyrics`, `--audio_duration`,
  `--seed`, `--title`), reusing or creating the same sandbox shape. If no
  sandbox is RUNNING within `--timeout-budget` (default 600 s;
  `MUSICGEN_SANDBOX_BUDGET`; `0` = skip straight to the cluster), it falls back
  to the Slurm cluster. `--backend sandbox|cluster` forces either path.

Rules:

- **Sandboxes bill while RUNNING.** Default to leaving a sandbox up only while
  actively iterating; run `scripts/sandbox.py down` when iteration is done and
  confirm with `status`. The 24 h max lifetime is a backstop, not a plan.
- **`probe` before the first GPU use** in a new org/key context (~1 min, costs
  cents): GPU sandboxes are preview-gated and the pool is heterogeneous
  (H100 80 GB or RTX PRO 6000 96 GB — both fit Music3 fully resident).
- **The snapshot is the cold-start solution**: `seed` builds it once (CPU
  sandbox, venv + ~57 GB weights, ~30-60 min); `reseed` refreshes it
  incrementally after dependency/runtime changes. Keep it current — a stale
  snapshot means every launch pays a long `uv sync`.
- **Never commit `.launch/`** (tokens, ids — gitignored) and never print
  secret values; they travel only via sandbox `environment_variables`.
- One GPU per sandbox is a platform cap and is all Music3 needs. Generation is
  single-sample; seed sweeps are sequential runs (the per-sandbox `.gen.lock`
  serializes the GPU), not bigger requests.
- Environment quirks and the error→fix table: `docs/sandbox_environment.md`.

## Fallback: Slurm cluster (via scripts/sandbox_generate.py, or by hand)

Used only when the sandbox pathway is unavailable (capacity, entitlement). The
old rules stand whenever this path is taken:

- Connect with `ssh coreweave-login`. The login node is for orchestration only
  (sbatch/squeue/scancel, file transfer, tailing logs). **Never run Python
  workloads or anything GPU/CPU-heavy on the login node.**
- All generation runs through an allocation:
  1. `sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G --job-name=musicgen --wrap "sleep infinity"`
  2. launch into it with `srun --jobid=<JOBID> --overlap --export=ALL`
- Check before provisioning: `sinfo -p h100` (idle nodes exist) and
  `squeue -u $USER` (no forgotten allocation — reuse it, including PENDING ones;
  never double-sbatch). **Do not request 2 GPUs** — one H100 holds the model.
- `uv` is not on PATH in non-interactive/srun shells — invoke
  `.venv/bin/python` directly. Always set `TORCH_DISABLE_NATIVE_JIT=1` and
  `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` in the launch line.
  Details: `docs/cluster_environment.md`.
- The cluster mirror `~/music_gen_demo` must be rsync'ed before manual cluster
  runs (template in `docs/run_commands.md`); `sandbox_generate.py`'s fallback
  assumes it exists.
- Release the allocation (`scancel <JOBID>`) when iteration is done; confirm
  with `squeue`. Don't leave idle GPUs held.

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

- Canonical headless generation (sandbox-first, cluster fallback, WAV downloaded
  to local `generated_audio/MiniMax-Music3/<slug>_s<seed>.wav`):

  ```bash
  uv run --no-project --python 3.12 scripts/sandbox_generate.py \
    --prompt_file prompt.txt --lyrics_file assets/<title>.txt \
    --audio_duration 120 --seed 42 --title <title>
  ```

  It streams generation phases and prints the W&B URL; `--down` tears the
  sandbox down afterwards (default leaves it running for iteration — then
  release it with `scripts/sandbox.py down` when done).

- When monitoring any raw generation log, watch for **failure signatures as
  well as success**: `Traceback`, `CUDA out of memory`, `RuntimeError`,
  `ValueError`, `Killed` (plus `srun: error` on the cluster path). Completion
  markers are `wandb: Synced` and `Saved audio locally to ...wav` — note that
  `wandb: View run at <url>` prints at *startup* and is not a completion
  signal. The one shared parser for this grammar lives in `app/backend.py`
  (`_parse_log`) — add new signatures there, nowhere else.
- Every run logs to W&B (entity/project from `.env`); the run URL is in the log
  and the finished WAV is on the run page (panel "Generated Audio").
- After a run teaches something new (a good caption pattern, timing numbers,
  a new failure signature), record it in `docs/run_commands.md` — and for
  sandbox-environment lessons, `docs/sandbox_environment.md`.

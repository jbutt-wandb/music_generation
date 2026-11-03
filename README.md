# Music Generation

Generate full songs — vocals, arrangement, up to 6 minutes of stereo audio — from two text
inputs: a **Structured Caption** describing the sound, and **tagged lyrics** (`[Verse]`,
`[Chorus]`, …; omit for an instrumental). Runs [MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)
on a CoreWeave serverless GPU sandbox and logs every run to Weights & Biases. Drive it by
hand or let a coding agent run the whole loop. Hear what the model can do in the
[official demo gallery](https://minimax-ai.github.io/music3-demo/).

| | |
|---|---|
| Model | MiniMax-Music3 (~11B, CC-BY-4.0, ~57 GB — downloaded once into a reusable snapshot) |
| Hardware | 1 GPU: serverless sandbox (H100 80 GB or RTX PRO 6000 96 GB) — fits fully resident; `--offload` modes run on 8–24 GB cards |
| Output | 44.1 kHz stereo WAV, ≤ 360 s, ~2 min of compute per 60 s of audio |
| Compute | CoreWeave serverless GPU sandboxes (preview — `sandbox.py probe` checks entitlement); Slurm `h100` cluster as fallback (no access? contact **Tara Madhyastha** at CoreWeave) |

For a WB project with example outputs, see this:
https://wandb.ai/wandb-smle/jb_music_gen/

## Setup

1. **Credentials** — `cp .env_example .env` and fill it in: `CWSANDBOX_API_KEY`
   (console.coreweave.com/tokens, "Sandbox User" role), `WANDB_API_KEY`,
   `WANDB_ENTITY`, `WANDB_PROJECT` (songs are logged to *your* project), and `HF_TOKEN`
   (authenticates the model download).
2. **Local environment** — `uv sync`. diffusers is pinned to a git commit; do **not**
   install `kernels`.
3. **One-time snapshot** — build the sandbox filesystem snapshot (app venv + weights,
   ~30–60 min on a cheap CPU sandbox; teammates can skip it via `SNAPSHOT_ID` in `.env`):
   ```bash
   uv run --no-project --python 3.12 scripts/sandbox.py probe   # ~1 min entitlement check
   uv run --no-project --python 3.12 scripts/sandbox.py seed
   ```
4. *(Fallback only)* a `coreweave-login` ssh alias + cluster mirror — needed just for the
   Slurm fallback path: see [`docs/cluster_environment.md`](docs/cluster_environment.md).

## Make a song

Always **lyrics first, caption second** — the caption's arrangement is built around the
lyrics' section tags.

**Option A — the web app (marimo).** The studio UI runs *inside* a GPU sandbox and is
served at a tokenized URL — describe a song and let it compose, or edit lyrics and
caption panes yourself:

```bash
uv run --no-project --python 3.12 scripts/sandbox.py up     # prints the app URL
# ... make music in the browser ...
uv run --no-project --python 3.12 scripts/sandbox.py down   # pulls WAVs, stops billing
```

Full setup, screenshots, usage, troubleshooting: [`app/README.md`](app/README.md).

**Option B — headless scripts:**

```bash
# 1. Lyrics (runs locally — W&B Inference / Kimi K2.6, uses your WANDB_API_KEY):
uv run scripts/generate_lyrics.py --theme "dawn drive after a night shift" --duration 120
#    -> assets/<title>.txt

# 2. Caption: write prompt.txt as a Structured Caption — see the prompt guide,
#    or crib from the 61 official examples in docs/demo_prompt_examples.md

# 3. Music — sandbox-first, automatic Slurm fallback, WAV lands locally:
uv run --no-project --python 3.12 scripts/sandbox_generate.py \
  --prompt_file prompt.txt --lyrics_file assets/<title>.txt \
  --audio_duration 120 --seed 42
```

The sandbox is left running for iteration — release it with `scripts/sandbox.py down`
(or pass `--down`). More variants (instrumental, inline lyrics, forcing a backend, the
manual cluster workflow): [`docs/run_commands.md`](docs/run_commands.md).

**With a coding agent** (Claude Code opened in this repo) — the bundled skills draft both
inputs, and [`CLAUDE.md`](CLAUDE.md) teaches the agent the sandbox-first workflow:

```
/lyrics-writer Theme: <story or mood>. Duration: 120s.
/music-caption-rewriter Caption: <style brief>. Lyrics: assets/<title>.txt
"generate this"
```

**Option C — the Slurm cluster by hand** (fallback path): provision an allocation and
run `scripts/minimax_music3.py` under srun — templates and worked examples in
[`docs/run_commands.md`](docs/run_commands.md), environment quirks in
[`docs/cluster_environment.md`](docs/cluster_environment.md).

**Iterating:** new take → change `--seed` only; new sound → new caption (lyrics + seed
fixed); new words → new lyrics, then a new caption.

## Results

Every run is a W&B run: the song plays in the browser under **Media → "Generated Audio"**,
with the full config (caption, lyrics, seed, duration) attached, so any output can be
traced and reproduced. WAVs land locally in `generated_audio/MiniMax-Music3/` —
`sandbox_generate.py` downloads them automatically; app-session WAVs arrive via
`sandbox.py pull` (or `down`, which pulls first).

## Learn more

- [`docs/music_generation_guide.md`](docs/music_generation_guide.md) — every parameter: duration cap, offload modes, seeds, W&B logging
- [`docs/minimax_music_prompt_guide.md`](docs/minimax_music_prompt_guide.md) — the caption and lyrics formats (read before writing any prompt)
- [Official demo gallery](https://minimax-ai.github.io/music3-demo/) — 61 example tracks with their prompts, playable in the browser
- [`docs/demo_prompt_examples.md`](docs/demo_prompt_examples.md) — those 61 demo prompts + lyrics extracted into markdown, grouped by genre
- [`docs/run_commands.md`](docs/run_commands.md) — copy-paste commands, worked runs, discovered constraints
- [`docs/sandbox_environment.md`](docs/sandbox_environment.md) — sandbox architecture and error→fix table
- [`docs/cluster_environment.md`](docs/cluster_environment.md) — the Slurm fallback: setup and error→fix table
- [`docs/gpu_memory_tutorial.md`](docs/gpu_memory_tutorial.md) — running the model on smaller GPUs and Apple Silicon (MPS)
- [`CLAUDE.md`](CLAUDE.md) — rules for coding agents driving the workflow

## Layout

```
app/                marimo web app (runs inside the GPU sandbox) — see app/README.md
scripts/            minimax_music3.py (music) · sandbox.py (app-sandbox lifecycle) ·
                    sandbox_generate.py (headless generation, Slurm fallback) ·
                    sandbox_lib.py · generate_lyrics.py (lyrics, local) ·
                    extract_demo_prompts.py · check_device.py
docs/               guides, prompt formats, run commands
assets/             lyrics files
.claude/skills/     lyrics-writer (ours) + music-caption-rewriter (official, from MiniMax)
generated_audio/    outputs, one subdirectory per model
demo_audio/         official demo mp3s by genre (regenerate: extract_demo_prompts.py --download-audio)
```

# Reference
1. https://minimax-ai.github.io/music3-demo/

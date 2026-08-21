# Music Generation

Generate full songs — vocals, arrangement, up to 6 minutes of stereo audio — from two text
inputs: a **Structured Caption** describing the sound, and **tagged lyrics** (`[Verse]`,
`[Chorus]`, …; omit for an instrumental). Runs [MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)
on a CoreWeave H100 and logs every run to Weights & Biases. Drive it by hand or let a
coding agent run the whole loop. Hear what the model can do in the
[official demo gallery](https://minimax-ai.github.io/music3-demo/).

| | |
|---|---|
| Model | MiniMax-Music3 (~11B, CC-BY-4.0, ~57 GB first download) |
| Hardware | 1× H100 80 GB — fits fully resident; `--offload` modes run on 8–24 GB cards |
| Output | 44.1 kHz stereo WAV, ≤ 360 s, ~2 min of compute per 60 s of audio |
| Cluster | CoreWeave Slurm, `h100` partition (no access? contact **Tara Madhyastha** at CoreWeave) |

For a WB project with example outputs, see this:
https://wandb.ai/wandb-smle/jb_music_gen/

## Setup

1. **Credentials** — `cp .env_example .env` and fill it in: `WANDB_API_KEY`,
   `WANDB_ENTITY`, `WANDB_PROJECT` (songs are logged to *your* project), and `HF_TOKEN`
   (authenticates the model download).
2. **Local environment** — `uv sync`. diffusers is pinned to a git commit; do **not**
   install `kernels`.
3. **Cluster mirror** — set up a `coreweave-login` ssh alias (key auth), then:
   ```bash
   rsync -av --exclude .git --exclude .venv --exclude generated_audio --exclude demo_audio \
     ./ coreweave-login:music_gen_demo/
   ssh coreweave-login "cd ~/music_gen_demo && export PATH=\$HOME/.local/bin:\$PATH && uv sync"
   ```
   Re-run the rsync whenever files change.

## Make a song

Always **lyrics first, caption second** — the caption's arrangement is built around the
lyrics' section tags.

**With scripts:**

```bash
# 1. Lyrics (runs locally — W&B Inference / Kimi K2.6, uses your WANDB_API_KEY):
uv run scripts/generate_lyrics.py --theme "dawn drive after a night shift" --duration 120
#    -> assets/<title>.txt

# 2. Caption: write prompt.txt as a Structured Caption — see the prompt guide,
#    or crib from the 61 official examples in docs/demo_prompt_examples.md

# 3. Music (on the cluster, inside an allocation — never on the login node):
sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G --job-name=musicgen --wrap "sleep infinity"
srun --jobid=<JOBID> --overlap --pty bash
cd ~/music_gen_demo
uv run scripts/minimax_music3.py --prompt "$(cat prompt.txt)" --lyrics_file assets/<title>.txt --audio_duration 120 --seed 42
```

Release the GPU with `scancel <JOBID>` when done. More variants (instrumental, inline
lyrics, background launches, a paste-proof helper): [`docs/run_commands.md`](docs/run_commands.md).

**With a coding agent** (Claude Code opened in this repo) — the bundled skills draft both
inputs, and [`CLAUDE.md`](CLAUDE.md) teaches the agent the provision → launch → monitor →
review loop:

```
/lyrics-writer Theme: <story or mood>. Duration: 120s.
/music-caption-rewriter Caption: <style brief>. Lyrics: assets/<title>.txt
"generate this on the cluster"
```

**Iterating:** new take → change `--seed` only; new sound → new caption (lyrics + seed
fixed); new words → new lyrics, then a new caption.

### Option C — the web app (marimo)

A local studio UI modeled on the official demo Space — describe a song and let it
compose, or edit lyrics and caption panes yourself, then generate on the cluster:

```bash
uv run marimo run app/app.py
```

> ⚠️ Requires a **running cluster allocation** (the app never provisions or
> releases GPUs) and one-time cluster setup. **Full setup, screenshots, usage,
> and troubleshooting: [`app/README.md`](app/README.md).**

## Results

Every run is a W&B run: the song plays in the browser under **Media → "Generated Audio"**,
with the full config (caption, lyrics, seed, duration) attached, so any output can be
traced and reproduced. The WAV also lands on the cluster in `generated_audio/MiniMax-Music3/`.

## Learn more

- [`docs/music_generation_guide.md`](docs/music_generation_guide.md) — every parameter: duration cap, offload modes, seeds, W&B logging
- [`docs/minimax_music_prompt_guide.md`](docs/minimax_music_prompt_guide.md) — the caption and lyrics formats (read before writing any prompt)
- [Official demo gallery](https://minimax-ai.github.io/music3-demo/) — 61 example tracks with their prompts, playable in the browser
- [`docs/demo_prompt_examples.md`](docs/demo_prompt_examples.md) — those 61 demo prompts + lyrics extracted into markdown, grouped by genre
- [`docs/run_commands.md`](docs/run_commands.md) — copy-paste commands, worked cluster runs, discovered constraints
- [`docs/cluster_environment.md`](docs/cluster_environment.md) — cluster setup and error→fix table
- [`docs/gpu_memory_tutorial.md`](docs/gpu_memory_tutorial.md) — running the model on smaller GPUs and Apple Silicon (MPS)
- [`CLAUDE.md`](CLAUDE.md) — rules for coding agents driving the cluster workflow

## Layout

```
app/                marimo web app — see app/README.md for setup, screenshots, usage
scripts/            minimax_music3.py (music, cluster GPU or MPS) · generate_lyrics.py
                    (lyrics, local) · extract_demo_prompts.py · check_device.py
docs/               guides, prompt formats, run commands
assets/             lyrics files
.claude/skills/     lyrics-writer (ours) + music-caption-rewriter (official, from MiniMax)
generated_audio/    outputs, one subdirectory per model
demo_audio/         official demo mp3s by genre (regenerate: extract_demo_prompts.py --download-audio)
```

# Reference
1. https://minimax-ai.github.io/music3-demo/

# Music Generation Guide — MiniMax-Music3

How to query the text-to-music model in this repo and what every parameter means. The
script follows the same skeleton as its video sibling: parse args → load the diffusers
pipeline → generate → write WAV → log the audio to Weights & Biases.

| | MiniMax-Music3 |
|---|---|
| Script (local repo) | `scripts/minimax_music3.py` |
| Script (in the sandbox) | `/work/app/scripts/minimax_music3.py` — both pathways run it there |
| Script (cluster fallback) | `~/music_gen_demo/scripts/minimax_music3.py` |
| Output | full song: stereo WAV, vocals + arrangement (44.1 kHz on the released checkpoint — the script reads `pipe.sampling_rate`, never assumes) |
| Size / hardware | ~11B total (8B Qwen3 LLM + 0.6B RVQ depth decoder + 2.4B flow-matching transformer + vocoder) ≈ 23 GB bf16 — fits one H100 80GB outright |
| diffusers API | Modular Pipelines (`ModularPipeline`, experimental, pinned git commit) |
| Guidance | no CFG knobs exposed — no `negative_prompt` / `guidance_scale` |
| Architecture | autoregressive LLM emits per-frame semantic codes (25 frames/s) → flow-matching transformer denoises Flow-VAE latents chunk by chunk → vocoder decodes to waveform |
| Max duration | 9,000 acoustic frames = **360 s**; the model may end the song earlier |
| Batching | single-sample generation only |

## Querying MiniMax-Music3

```bash
# Canonical: the sandbox pathway wraps this script end-to-end (creates/reuses
# the GPU sandbox, runs it there, downloads the WAV; Slurm fallback built in):
uv run --no-project --python 3.12 scripts/sandbox_generate.py \
  --prompt_file prompt.txt --lyrics_file assets/neon_rain.txt \
  --audio_duration 60 --seed 42

# Direct invocation (inside the sandbox, on a compute node, or any CUDA box):
uv run scripts/minimax_music3.py \
  --prompt "<Structured Caption — see docs/minimax_music_prompt_guide.md>" \
  --lyrics_file assets/neon_rain.txt \
  --audio_duration 60 --seed 42

# Cluster fallback launch template (see docs/cluster_environment.md):
cd ~/music_gen_demo && mkdir -p logs
nohup env TORCH_DISABLE_NATIVE_JIT=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  srun --jobid=<JOBID> --overlap --export=ALL \
  .venv/bin/python scripts/minimax_music3.py \
  --prompt "<caption>" --lyrics_file assets/neon_rain.txt \
  --audio_duration 60 --seed 42 \
  > logs/music_run.log 2>&1 &
```

The model needs one GPU; the script reports extra visible GPUs but does not use them
(the stages run sequentially, so a second card buys nothing).

## Parameter reference

**`--prompt`** — the music description, written as a **Structured Caption** (three
labeled sections: Global Metadata / Vocal Details / Arrangement), not free text. This
is the single highest-leverage input: read
[`minimax_music_prompt_guide.md`](minimax_music_prompt_guide.md) and use the vendored
`music-caption-rewriter` skill to draft it. Everything the caption doesn't pin down
(BPM, key, instrumentation), the model chooses itself — and section tags/descriptions
are generative guidance, not symbolic guarantees.

**`--lyrics` / `--lyrics_file`** — the words to sing (mutually exclusive; `--lyrics`
inline, `--lyrics_file` a UTF-8 file, see `assets/neon_rain.txt`). Structure with
bracketed tags — `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Instrumental]`,
`[Solo]`, `[Outro]` — **each tag on its own line**; text on the same line as a leading
tag is silently dropped by the checkpoint's input contract. Budget is ~5,000 tokenized
tokens. Omit both flags for an instrumental (the script passes `[Instrumental]`; also
say "instrumental" in the caption's Vocal Details).

**`--audio_duration`** — upper bound on the track length in seconds (default 60,
max 360 = 9,000 acoustic frames at 25 frames/s). It is a *cap*, not a target: the
language model decides where the song ends and may stop earlier — write an `[Outro]`
into the lyrics and an ending into the caption's Arrangement if you want a clean close.
Runtime scales roughly linearly with the generated length.

**`--num_inference_steps`** — flow-matching Euler steps per decode chunk (default 30,
matching the pipeline's own default). Only affects the latent-denoising stage, not the
autoregressive LLM that writes the song, so it changes audio fidelity rather than
composition. Leave at 30 unless experimenting.

**`--seed`** — initializes the generator the song is sampled from. Same seed + same
parameters = same track. Change the seed for a different take on the same caption; fix
it to compare caption/lyric tweaks apples-to-apples.

**`--offload`** — memory strategy (`none` | `auto` | `group`):
| Mode | Peak VRAM | What it does |
|---|---|---|
| `none` (default) | ~23 GB | everything resident on the GPU — fastest, right for H100 |
| `auto` | ~21–22 GB | components shuttle between host RAM and GPU per stage |
| `group` | ~6–8 GB | the 8B LLM streams block-by-block with CUDA-stream prefetch — slowest, for small cards |

**`--model_id`** — the Hugging Face repo to load (`MiniMaxAI/MiniMax-Music3`,
~57 GB download on first use, CC-BY-4.0). Only change it for a checkpoint variant of
the same architecture.

**`--device`** — `cuda` (default; sandbox and cluster paths, all offload modes) or
`mps` (Apple Silicon, **experimental**, script-only — the app no longer exposes it):
requires ≥32 GB unified memory (~23 GB of bf16 weights), supports only
`--offload none` (the offload machinery is CUDA-only), runs 5–20× slower than an
H100 (autoregressive decode is memory-bandwidth-bound), and the pipeline's operator
coverage on MPS is unverified — expect possible failures. The first local run
downloads ~57 GB to `~/.cache/huggingface`.

**`--output`** — optional explicit WAV path (parent dirs created). Default is
`generated_audio/<model>/minimax_music3_output.wav`; the app and
`sandbox_generate.py` pass per-run `<slug>_s<seed>.wav` paths so concurrent or
successive runs never overwrite each other.

**The marimo app** (launched with `scripts/sandbox.py up`, served from inside a GPU
sandbox) is a front-end over this exact script — same arguments, same W&B logging.
It never provisions or releases sandboxes itself; `scripts/sandbox.py` owns the
lifecycle (see `app/README.md`).

**Why no `negative_prompt` / `guidance_scale`?** The composition is written by an
autoregressive language model, not a CFG-guided denoiser; the flow-matching stage runs
with the pipeline's internal guidance configuration and exposes no CFG knobs at the
top level.

### W&B logging

Runs log to the entity/project from `WANDB_ENTITY` / `WANDB_PROJECT` env vars. The run's
config is a complete recipe: every CLI arg plus `lyrics_text` — the *resolved* lyrics —
so a run stays reproducible even if the lyrics file later changes. The finished WAV is
logged as a `wandb.Audio` panel named **"Generated Audio"**, captioned with the song
title and seed (title = the lyrics filename stem, the first sung line for inline lyrics,
or "Instrumental"), and plays right in the browser. The script also contains a
commented-out "Method B" block showing how to log generations into a `wandb.Table`
(prompt / lyrics / seed / duration / audio per row) for side-by-side comparison.

## Practical recipes

- **Iterating on a caption:** `--audio_duration 30` with a fixed seed → fast drafts
  that still reveal genre, vocal timbre, and groove; restore the full length for the
  final render.
- **Different takes of one song:** keep caption + lyrics fixed, vary `--seed`.
- **A/B testing captions:** fix the seed, change only the caption, compare the two
  W&B runs side by side.
- **Instrumental:** omit the lyrics flags and describe the lead instrument in the
  caption's Vocal Details ("This piece is instrumental; a muted trumpet carries the
  lead melodic role").
- **Full-length songs:** raise `--audio_duration` toward 300–360 s and give the model
  a complete lyric structure (two verses, choruses, bridge, outro) to fill it with.
- **New words:** rewrite the lyrics with the `lyrics-writer` skill *first*, then
  regenerate the caption with `music-caption-rewriter` — the caption's Arrangement
  is built around the lyrics' section tags and goes stale when they change (full
  chain: `docs/minimax_music_prompt_guide.md`, "The end-to-end chain").

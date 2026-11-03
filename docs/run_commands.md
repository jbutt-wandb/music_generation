# MiniMax Music3

## Text + lyrics -> song
### Full
uv run ./scripts/minimax_music3.py --model_id "MiniMaxAI/MiniMax-Music3" \
    --prompt "Global Metadata
Basic Attributes: bpm is around 108. key is A, and scale is minor. Indie Synth-Pop / Electropop.
Global Emotional Progression: Opens wistful and intimate over sparse pads; each chorus lifts into cathartic, neon-lit euphoria; the outro exhales back into late-night stillness.
Sonics & Production Profile: Glossy late-night radio production; warm rounded low end, airy top; verses breathe, choruses tighten into a sidechained pulse.
Vocal Details
Vocal Gender & Timbre: Singer A (Female), airy and close-miked with a soft break in the upper register.
Vocal Style: Conversational and intimate in the verses, opening into sustained belts in the choruses.
Harmony/Backing Vocals: Light stacked harmonies double the chorus hook; a low octave layer thickens the final chorus.
Vocal FX: Subtle plate reverb throughout; a quarter-note delay throw on the last word of each chorus.
Arrangement
Instrument Lifecycle: Warm analog synth pads and a round electric bassline carry the verses; a pulsing arpeggio and driving electronic drums enter at each chorus; everything but pads and voice falls away for the outro.
Groove & Foundation Progression: Verses ride a soft four-on-the-floor kick with muted hats; choruses add a sidechained pump, open hats, and claps on 2 and 4; the outro dissolves the pulse entirely.
Embellishments, Textures & Spatial FX: White-noise risers into each chorus, a reverse-reverb swell into the bridge, faint vinyl crackle under the verses." \
    --lyrics_file assets/neon_rain.txt \
    --audio_duration 60 \
    --seed 42

### Partial
uv run ./scripts/minimax_music3.py \
    --prompt "Global Metadata: Indie synth-pop, around 108 BPM, wistful-to-euphoric arc, glossy late-night production. Vocal Details: Female lead, airy timbre, intimate verses opening into belted choruses. Arrangement: Warm pads and round bass under the verses; sidechained pulse, arpeggios and driving drums lift the choruses; stripped-back outro." \
    --lyrics_file assets/neon_rain.txt \
    --audio_duration 60 \
    --seed 42

## Inline lyrics
uv run ./scripts/minimax_music3.py \
    --prompt "<caption>" \
    --lyrics "[Verse]
Streetlights hum on the avenue
Every window glows a different blue
[Chorus]
We were made of neon and rain
Dancing down the fire escape" \
    --audio_duration 45 \
    --seed 42

## Instrumental
Omit both lyrics flags; the script passes an `[Instrumental]`-only lyrics string.
State "instrumental" in the caption's Vocal Details and name the lead instrument.

uv run ./scripts/minimax_music3.py \
    --prompt "Global Metadata: Lo-fi jazz-hop, 72 BPM, warm and nocturnal, dusty tape saturation. Vocal Details: This piece is instrumental; a muted trumpet carries the lead melodic role over Rhodes chords. Arrangement: Brushed drums and upright bass hold a laid-back groove; the trumpet trades phrases with the Rhodes; vinyl crackle and rain ambience sit under the whole track; a solo piano figure closes it out." \
    --audio_duration 90 \
    --seed 42

# Full song workflow

Two interchangeable routes for the same pipeline — always lyrics first, caption
second (the caption's timeline is built around the lyrics' tags; see
minimax_music_prompt_guide.md).

## Route A — scripts, run sequentially (no coding agent needed)

```bash
# 1. Lyrics (local; W&B Inference / Kimi K2.6, authenticated by WANDB_API_KEY from .env):
uv run scripts/generate_lyrics.py \
    --theme "driving home at dawn after a night shift, tired but at peace" \
    --duration 120 \
    --constraints "female POV, no forced rhymes"
#    -> prints the title and writes assets/<title>.txt
#    (--language, --model, --out, --force for variants)

# 2. Caption: write prompt.txt as a Structured Caption (crib from
#    docs/demo_prompt_examples.md or the prompt guide's example skeleton)

# 3. Music — the canonical headless command: reuses or creates a GPU sandbox
#    (10-min budget, then automatic Slurm fallback), streams phases, downloads
#    the WAV to generated_audio/MiniMax-Music3/<slug>_s<seed>.wav:
uv run --no-project --python 3.12 scripts/sandbox_generate.py \
  --prompt_file prompt.txt --lyrics_file assets/<title>.txt \
  --audio_duration 120 --seed 42
#    (--backend sandbox|cluster forces a path; --timeout-budget 0 skips straight
#     to the cluster; --down tears the sandbox down after; default leaves it
#     running — release later with `scripts/sandbox.py down`)
```

## Route B — skills, via a coding agent (Claude Code in this repo)

```
# 1. In Claude Code (local repo):
/lyrics-writer Theme: <story/mood>. Duration: 120s.
#    → assets/<title>.txt — review and iterate before spending GPU time

# 2. Style brief + the finished lyrics:
/music-caption-rewriter Caption: <rough style brief>. Lyrics: assets/<title>.txt
#    → save the returned Structured Caption to prompt.txt

# 3. Same sandbox_generate.py command as Route A.
```

Iterate at the right layer (both routes): new take → `--seed` only; new sound →
new caption (lyrics + seed fixed); new words → new lyrics, then a new caption.

# Marimo web app

A studio UI over the same script (`app/app.py`), served from INSIDE a GPU
sandbox: Simple mode (Kimi K2.6 composes lyrics + caption from a description)
and Studio mode (edit lyrics, three caption panes, presets, tag chips).

```bash
uv run --no-project --python 3.12 scripts/sandbox.py up     # prints the app URL
# ...
uv run --no-project --python 3.12 scripts/sandbox.py down   # pulls WAVs, stops billing
```

One-time first: `sandbox.py probe` (entitlement check) and `sandbox.py seed`
(builds the venv+weights snapshot). Full setup guide, screenshots, usage, and
troubleshooting: **`../app/README.md`**; sandbox error→fix table:
`sandbox_environment.md`. App runs log to W&B exactly like script runs; WAVs
land sandbox-side in `generated_audio/MiniMax-Music3/` — `sandbox.py pull`
brings new ones local.

---

# Slurm cluster — the FALLBACK path

Everything below is the pre-sandbox workflow. It remains valid and is what
`sandbox_generate.py` falls back to (it expects the `~/music_gen_demo` mirror):

```bash
# Sync the repo to the cluster mirror (re-run whenever scripts/docs change):
rsync -av --exclude .git --exclude .venv --exclude generated_audio \
  --exclude demo_audio --exclude logs ./ coreweave-login:music_gen_demo/
```

## Manual runs (interactive compute shell)

For hands-on iteration, step into the running allocation from the login node
(`squeue -u $USER` for the JOBID) and work interactively — `uv` is on PATH in
this shell, and long captions live in a file:

```bash
srun --jobid=<JOBID> --overlap --pty bash

cd ~/music_gen_demo
# put your Structured Caption in prompt.txt, then:
uv run scripts/minimax_music3.py --prompt "$(cat prompt.txt)" --lyrics_file assets/neon_rain.txt --audio_duration 90 --seed 42
```

Keep the command on ONE line when pasting — a stray newline splits it into two
shell commands (`--lyrics_file: expected one argument` followed by
`assets/neon_rain.txt: Permission denied` is the signature of that paste
failure). Paste-proof helper, seed as the only argument:

```bash
cat > run_gen.sh <<'EOF'
#!/bin/bash
uv run scripts/minimax_music3.py \
  --prompt "$(cat prompt.txt)" \
  --lyrics_file assets/neon_rain.txt \
  --audio_duration 90 \
  --seed "${1:-42}"
EOF
chmod +x run_gen.sh

./run_gen.sh        # seed 42
./run_gen.sh 7      # different take
```

(The `TORCH_DISABLE_NATIVE_JIT` / `PYTORCH_CUDA_ALLOC_CONF` env vars aren't
needed here: the script sets the JIT guard itself, and Music3 has ~55 GB of
VRAM headroom. They remain mandatory in the non-interactive nohup/srun
template below, which protects any entry point.)

## Cluster launch template

```bash
# Allocation (if none): sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G \
#   --job-name=musicgen --wrap "sleep infinity"
cd ~/music_gen_demo && mkdir -p logs
nohup env TORCH_DISABLE_NATIVE_JIT=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  srun --jobid=<JOBID> --overlap --export=ALL \
  .venv/bin/python scripts/minimax_music3.py <args> > logs/<name>.log 2>&1 &
```

## Worked examples (cluster)

Real runs on 1× H100 (all logged to W&B `wandb-smle/jb_music_gen`; each run's
full caption and lyrics are stored in its config).

### Initial generation — indie synth-pop, 60 s (run ywz7q3x4, 2026-08-20)

The "Partial" command above, launched from the login node into allocation 1150
(`sbatch -p h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G --job-name=musicgen
--wrap "sleep infinity"`) with the standard nohup/srun pattern. Ran clean on the
first attempt with `--offload none`.

- **Timing:** ~2 min of generation for a 60 s song (plus ~2 min startup/model
  load). The flow-matching decode is trivial (420 steps @ ~41 it/s ≈ 10 s);
  the autoregressive LLM stage dominates.
- **Output:** exactly 60.07 s, 44.1 kHz 16-bit stereo WAV, 10.6 MB — confirms
  the vocoder's 44.1 kHz (the model card's "32 kHz" is wrong for this
  checkpoint).
- The audio panel ("Generated Audio") uploads to the W&B run automatically;
  `wandb: Synced` + `Saved audio locally to ...wav` appeared as expected.

### Three-movement ambient/psychedelic R&B suite, 180 s cap (run q1ggvxzv, 2026-10-27)

One continuous piece with movement-level tempo/texture shifts described in a
single caption (psychedelic R&B ~65–70 BPM → muffled low-passed piano ~60 BPM →
drumless free-tempo choral outro). Caption in the run's W&B config; lyrics
`assets/let-the-morning-find-us.txt`.

- **Duration is a cap, confirmed:** very sparse lyrics (ad-libs, a whispered
  couplet, one repeated outro line) with `--audio_duration 180` produced a
  129.7 s song — the model ends when the lyrics run out. To fill a long
  duration with sparse vocals, add more `[Instrumental]`/section tags or
  repeat the outro line more times.

### Memory / duration constraints (pre-run knowledge — verify against real runs)

- ~23 GB of bf16 weights: fits one H100 80GB with no offloading (`--offload none`).
  `--offload auto` ≈ 21–22 GB peak; `--offload group` ≈ 6–8 GB peak (slowest).
- Duration cap: **360 s** (9,000 acoustic frames at 25 frames/s); the language
  model may end the song earlier than `--audio_duration`.
- Single-sample generation only — one song per process; sweep seeds with
  separate launches.
- First run downloads ~57 GB to `~/.cache/huggingface` — check quota first.
- Record after the first real runs: actual `pipe.sampling_rate`, peak VRAM
  (`torch.cuda.max_memory_allocated`), wall-clock per 60 s of audio.

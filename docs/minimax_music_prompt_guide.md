# MiniMax-Music3 Prompt Writing Guide (key context)

Condensed from the official guidance shipped with the model
(`MiniMaxAI/MiniMax-Music3` model card and the `music-caption-rewriter` agent
skill at https://github.com/MiniMax-AI/MiniMax-Music3/tree/main/skills). The
full skill — genre router, 18 style-family indexes, and 1,000 reference caption
templates — is vendored in this repo at `.claude/skills/music-caption-rewriter/`
and should be used to draft captions. All 61 official demo tracks' exact inputs
(caption + lyrics), grouped by genre, are in
[`demo_prompt_examples.md`](demo_prompt_examples.md).

## The two inputs

Every generation takes **two separate strings** — do not mix their jobs:

- **`--lyrics`** — the words to sing, structured with bracketed section tags.
  Lyric text is *sacred*: never rewrite, paraphrase, or summarize it into the
  caption. Only the bracketed tags act as musical directives.
- **`--prompt`** — the **Structured Caption**: a prose description of the music
  itself (genre, tempo, emotion, vocals, arrangement). It describes *how* the
  song sounds, never *what* the lyrics say.

## Lyrics format

- Section tags each on **their own line**: `[Verse]`, `[Pre-Chorus]`,
  `[Chorus]`, `[Bridge]`, `[Instrumental]`, `[Solo]`, `[Outro]`. Text on the
  same line as a leading tag is **dropped** by the checkpoint's input contract.
- Lyric lines follow their tag, one line per sung line.
- Budget: ~**5,000 tokens** of tokenized lyrics.
- **Instrumental tracks:** omit `--lyrics`/`--lyrics_file`; the script passes an
  `[Instrumental]`-only string. Also state "instrumental" in the caption's
  Vocal Details and name the instrument carrying the lead melodic role.
- Tags provide *generative guidance*, not symbolic guarantees — section
  boundaries, tempo, and key may drift from what you asked for.

## Structured Caption format

The caption has **three top-level sections, in this order**. The bundled
templates use labeled sub-fields; follow the same anatomy:

```
Global Metadata
  Basic Attributes: BPM, key + scale, genre / subgenre.
  Global Emotional Progression: the mood arc across the song
    (how it opens, lifts, tenses, resolves).
  Application Scenarios & Imagery: what the track is for, what it evokes.
  Sonics & Production Profile: soundstage, frequency balance, dynamics,
    compression character.

Vocal Details
  Vocal Gender & Timbre: e.g. "Singer A (Male), clear resonant tenor..."
  Vocal Style: delivery per section (conversational verses, belted choruses...).
  Harmony/Backing Vocals: when they enter, what texture they add.
  Vocal FX: reverb/delay/saturation treatment, kept restrained.

Arrangement
  Instrument Lifecycle (Primary/Secondary Layering): which instruments drive
    which sections; what enters, exits, changes, or intensifies.
  Groove & Foundation Progression: the drum/bass story from section to section.
  Embellishments, Textures & Spatial FX: risers, swells, ambience, transitions.
```

### Caption writing rules (from the official skill)

- Write the arrangement as a **section-by-section timeline** with a readable
  energy arc — not a static equipment list or a stack of production jargon.
- Target **~250–450 English words** total.
- Use an exact BPM/key **only when you actually want it**; otherwise give a
  range or qualitative tempo. Never fabricate technical detail for its own sake.
- Build the timeline around the lyric section tags when lyrics are present —
  every actionable tag should have a matching moment in the Arrangement.
- Never reverse an explicit constraint: vocal gender, instrumental requirement,
  tempo limit, required instrument, or prohibited element.
- No song title, no lyric quotes, no reasoning traces in the caption.

## Using the skills

Two skills in `.claude/skills/` cover the two inputs, and they chain — lyrics
first, caption second, with the bracketed section tags as the interface:

**`lyrics-writer`** (this repo's own) drafts original tagged lyrics from a theme:
enforces the tag contract (tags on their own lines, standard vocabulary,
~5,000-token budget), sizes the section structure to the target
`--audio_duration`, and saves to `assets/<title>.txt`. The same rules are also
available as a standalone script — `scripts/generate_lyrics.py` (W&B Inference /
Kimi K2.6) — for the no-agent workflow in `run_commands.md`.

The marimo app's Simple mode and lyric assists use the same composer rules
(`app/compose.py`, Kimi K2.6 via W&B Inference) — one implementation shared
with `scripts/generate_lyrics.py`.

**`music-caption-rewriter`** (official, vendored from MiniMax): for anything
beyond a quick draft, invoke it instead of writing the caption by hand. Its
workflow:

1. It builds a private "Music Brief" from your rough description + lyric tags.
2. Routes it through `references/genre-router.md` to 1–2 of 18 style families.
3. Picks up to three reference templates with distinct roles — **Foundation**
   (overall identity), **Modifier** (a requested secondary color), and
   **Arrangement** (timeline logic).
4. Synthesizes an original caption — it never copies template sentences and
   never reproduces lyric text.

The output drops straight into `--prompt`. In tandem: pass the finished lyrics
to the caption rewriter as its optional `Lyrics` input — it reads only the
bracketed tags (never the words) to build an Arrangement timeline that matches
your actual sections, so every `[Bridge]` or `[Pre-Chorus]` you wrote gets a
corresponding musical moment.

### The end-to-end chain

**Always lyrics first, caption second** — the caption is built around the
lyrics' tags and goes stale if the section structure changes afterwards.

```
/lyrics-writer Theme: <story/mood>. Duration: <seconds>. Constraints: <optional>
        → assets/<title>.txt            (review & iterate here — it's free)

/music-caption-rewriter Caption: <rough style brief>. Lyrics: assets/<title>.txt
        → Structured Caption            (save to prompt.txt)

uv run scripts/minimax_music3.py --prompt "$(cat prompt.txt)" \
  --lyrics_file assets/<title>.txt --audio_duration <seconds> --seed 42
```

Iterate at the right layer: new *take* → change only `--seed`; new *sound* →
rerun the caption rewriter with a new brief (lyrics + seed fixed); new *words* →
back to the lyrics writer, then regenerate the caption.

## Example skeleton

Caption (`--prompt`), paired with `assets/neon_rain.txt`:

```
Global Metadata
Basic Attributes: bpm is around 108. key is A, and scale is minor. Indie
Synth-Pop / Electropop.
Global Emotional Progression: Opens wistful and intimate over sparse pads;
each chorus lifts into cathartic, neon-lit euphoria; the outro exhales back
into late-night stillness.
Application Scenarios & Imagery: Night drives through a rain-slicked city,
fire-escape rooftops, neon reflections.
Sonics & Production Profile: Glossy late-night radio production; warm rounded
low end, airy top; verses breathe, choruses tighten into a sidechained pulse.

Vocal Details
Vocal Gender & Timbre: Singer A (Female), airy and close-miked with a soft
break in the upper register.
Vocal Style: Conversational and intimate in the verses, opening into sustained
belts in the choruses.
Harmony/Backing Vocals: Light stacked harmonies double the chorus hook; a
low octave layer thickens the final chorus.
Vocal FX: Subtle plate reverb throughout; a quarter-note delay throw on the
last word of each chorus.

Arrangement
Instrument Lifecycle: Warm analog synth pads and a round electric bassline
carry the verses; a pulsing arpeggio and driving electronic drums enter at
each chorus; everything but pads and voice falls away for the outro.
Groove & Foundation Progression: Verses ride a soft four-on-the-floor kick
with muted hats; choruses add a sidechained pump, open hats, and claps on 2
and 4; the outro dissolves the pulse entirely.
Embellishments, Textures & Spatial FX: White-noise risers into each chorus,
a reverse-reverb swell into the bridge, faint vinyl crackle under the verses.
```

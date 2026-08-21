"""Shared LLM composition for MiniMax-Music3 inputs, via W&B Inference (Kimi K2.6).

Used by both `scripts/generate_lyrics.py` (CLI) and the marimo app (`app/app.py`).
Two jobs, mirroring the two model inputs:
- `write_lyrics`  — original section-tagged lyrics (the `.claude/skills/lyrics-writer` rules)
- `compose_song`  — full composition for the app's Simple mode: lyrics + the three
  Structured Caption sections (the rules in docs/minimax_music_prompt_guide.md)

Authenticates with WANDB_API_KEY from `.env`; usage is attributed to
WANDB_ENTITY/WANDB_PROJECT.
"""

import json
import os
import re

import openai
from dotenv import load_dotenv

load_dotenv(override=True)

WANDB_INFERENCE_BASE_URL = "https://api.inference.wandb.ai/v1"
DEFAULT_MODEL = "moonshotai/Kimi-K2.6"

# The checkpoint's input contract and sizing heuristics, mirrored from
# .claude/skills/lyrics-writer/SKILL.md and docs/minimax_music_prompt_guide.md.
LYRICS_SYSTEM = """\
You write original song lyrics for MiniMax-Music3, a text-to-music model. The
lyrics carry only WHAT IS SUNG — never describe production, instrumentation,
or vocal timbre inside them (a separate music-description caption handles that).

Hard format rules (the checkpoint's input contract):
1. Every section tag sits on ITS OWN LINE: [Verse], [Chorus], ... Text on the
   same line as a leading tag is silently dropped by the model.
2. One sung line per text line; blank line between sections.
3. Standard tags: [Intro], [Verse], [Pre-Chorus], [Chorus], [Bridge],
   [Instrumental], [Solo], [Outro]. Numbered ([Verse 2]) and expressive
   ([Sad Intro]) variants are allowed when they genuinely help.
4. ORIGINAL TEXT ONLY. Never reproduce or closely paraphrase existing
   copyrighted lyrics, even when asked to match a known song — match mood and
   structure instead.

Size the structure to the target duration (the model ends the song when the
lyrics run out):
- <=45s: Verse -> Chorus
- 60-90s: Verse -> Pre-Chorus -> Chorus -> Verse -> Chorus -> Outro
- 120-180s: Verse -> Pre-Chorus -> Chorus -> Verse -> Pre-Chorus -> Chorus -> Bridge -> Chorus -> Outro
- 240-360s: full double form; consider [Instrumental] or [Solo] breaks

Craft: repeat the chorus verbatim (small final-chorus lift is fine); singable
lines of roughly 4-10 words with consistent meter within a section; concrete
imagery around one controlling image or scene; a discernible emotional arc —
the bridge (if any) turns or reframes, it doesn't repeat; slant rhyme beats
forced rhyme; no title line inside the lyrics.

Also invent a short evocative song title (not sung, used for the filename).
"""

# The Structured Caption rules condensed from docs/minimax_music_prompt_guide.md
# (which is itself condensed from MiniMax's official caption-rewriter skill).
CAPTION_SYSTEM = """\
You write the music-description caption for MiniMax-Music3 as three labeled
sections. The caption describes HOW the song sounds — never quote, paraphrase,
or summarize the lyric text; only the bracketed section tags inform structure.

Section anatomy (follow the official template style):
- Global Metadata: Basic Attributes (BPM, key + scale, genre / subgenre);
  Global Emotional Progression (the mood arc across the song); Application
  Scenarios & Imagery; Sonics & Production Profile (soundstage, frequency
  balance, dynamics).
- Vocal Details: Vocal Gender & Timbre; Vocal Style per section;
  Harmony/Backing Vocals; Vocal FX (kept restrained). For instrumentals,
  state the piece is instrumental and name the lead melodic instrument.
- Arrangement: Instrument Lifecycle (Primary/Secondary layering per section);
  Groove & Foundation Progression; Embellishments, Textures & Spatial FX.

Rules: write the Arrangement as a section-by-section timeline that follows the
lyrics' bracketed tags (every actionable tag gets a musical moment); target
~250-450 words total across the three sections; give an exact BPM/key only when
it genuinely serves the request, otherwise a range or qualitative tempo; a
readable energy arc, not an equipment list; no song title inside the caption.
"""

_COMPOSE_INSTRUCTION = """\
Respond with ONLY a JSON object, no code fences, in exactly this shape:
{"title": "...", "lyrics": "...", "global_metadata": "...", "vocal_details": "...", "arrangement": "..."}
The three caption fields contain only their own section's text (no section
heading line inside the value)."""

_LYRICS_INSTRUCTION = """\
Respond with ONLY a JSON object, no code fences, in exactly this shape:
{"title": "<short evocative title>", "lyrics": "<the complete tagged lyrics, newline-separated>"}"""


def client():
    api_key = os.environ.get("WANDB_API_KEY")
    if not api_key:
        raise RuntimeError("WANDB_API_KEY not set — add it to .env (same key the music script uses).")
    return openai.OpenAI(
        base_url=WANDB_INFERENCE_BASE_URL,
        api_key=api_key,
        project=f"{os.environ.get('WANDB_ENTITY', '')}/{os.environ.get('WANDB_PROJECT', '')}",
    )


def parse_result(text, required_keys):
    """Parse the model's JSON reply, tolerating stray code fences."""
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.S)
    result = json.loads(cleaned)
    missing = [k for k in required_keys if not result.get(k)]
    if missing:
        raise ValueError(f"model reply is missing {missing}")
    return result


def _chat(system, user, model):
    response = client().chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content


def write_lyrics(theme, duration=90, language="English", constraints=None, model=DEFAULT_MODEL):
    """Original tagged lyrics from a theme -> {title, lyrics}."""
    request = (
        f"Theme: {theme}\n"
        f"Target --audio_duration: {duration} seconds\n"
        f"Language: {language}\n"
    )
    if constraints:
        request += f"Constraints: {constraints}\n"
    return parse_result(
        _chat(LYRICS_SYSTEM + "\n" + _LYRICS_INSTRUCTION, request, model),
        ("title", "lyrics"),
    )


def compose_song(description, duration=60, instrumental=False, model=DEFAULT_MODEL):
    """Full composition from a one-line idea (the app's Simple mode).

    -> {title, lyrics, global_metadata, vocal_details, arrangement}
    """
    system = (
        "You compose complete inputs for MiniMax-Music3: first the lyrics, then the "
        "three-section caption that fits them.\n\n== LYRICS RULES ==\n" + LYRICS_SYSTEM
        + "\n== CAPTION RULES ==\n" + CAPTION_SYSTEM + "\n" + _COMPOSE_INSTRUCTION
    )
    request = (
        f"Song idea: {description}\n"
        f"Target --audio_duration: {duration} seconds\n"
    )
    if instrumental:
        request += (
            "This piece is INSTRUMENTAL: the lyrics value must be exactly \"[Instrumental]\" "
            "and Vocal Details must describe the lead melodic instrument instead of a voice.\n"
        )
    return parse_result(
        _chat(system, request, model),
        ("title", "lyrics", "global_metadata", "vocal_details", "arrangement"),
    )


def validate_lyrics(lyrics):
    """Return warning strings for contract violations (tags sharing a line with text, no tags)."""
    warnings = []
    for line in lyrics.splitlines():
        if re.match(r"^\s*\[[^\]]+\]\s*\S", line):
            warnings.append(f"Text on the same line as a tag is dropped by the model: {line!r}")
    if not re.search(r"^\s*\[[^\]]+\]\s*$", lyrics, re.M):
        warnings.append("No section tags found; the model expects [Verse]/[Chorus]/... structure.")
    return warnings


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled"

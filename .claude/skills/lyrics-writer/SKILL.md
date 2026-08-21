---
name: lyrics-writer
description: Write original, section-tagged song lyrics for MiniMax-Music3 from a theme, story, or mood — sized to a target duration and formatted to the checkpoint's input contract ([Verse]/[Chorus] tags each on their own line). Use when users ask to write, draft, revise, translate, or adapt lyrics for music generation, or need a lyrics file for --lyrics_file. Companion to music-caption-rewriter, which handles the music-description side.
---

# Lyrics Writer

Write original lyrics ready to pass to MiniMax-Music3's `--lyrics_file`. The lyrics
carry *what is sung*; the Structured Caption (written separately by the
`music-caption-rewriter` skill) carries *how it sounds*. Keep those jobs separate:
never describe production, instrumentation, or vocal timbre inside the lyrics.

## Inputs

Accept:

- **Theme** (required): subject, story, mood, or imagery in any level of detail.
- **Duration** (optional): the intended `--audio_duration` in seconds — sizes the structure.
- **Language** (optional): default English; write natively in the requested language, not translated-sounding.
- **Constraints** (optional): genre feel, rhyme scheme, point of view, words/phrases to include or avoid, an existing draft to revise, a demo track to match in tone.

## Hard format rules (the checkpoint's input contract)

1. Every section tag sits on **its own line**: `[Verse]`, `[Chorus]`, … Text on the
   same line as a leading tag is **silently dropped** by the model — never write
   `[Chorus] We were made of…`.
2. One sung line per text line. Blank line between sections for readability.
3. Standard tags: `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`,
   `[Instrumental]`, `[Solo]`, `[Outro]`. Numbered (`[Verse 2]`) and expressive
   (`[Sad Intro]`, `[Whispered Bridge]`) variants are accepted and act as local
   directives — use them when they genuinely help.
4. Budget: ~5,000 tokens. Real songs use far less; never pad.
5. **Original text only.** Never reproduce, closely paraphrase, or interpolate
   existing copyrighted lyrics — including when asked to "sound like" a known song
   (match its mood and structure instead).

## Sizing structure to duration

The model treats duration as a cap and ends the song when the lyrics run out, so
match the structure to the target length:

| `--audio_duration` | Suggested skeleton |
|---|---|
| ≤ 45 s | Verse → Chorus |
| ~60–90 s | Verse → Pre-Chorus → Chorus → Verse → Chorus → Outro |
| ~120–180 s | Verse → Pre-Chorus → Chorus → Verse → Pre-Chorus → Chorus → Bridge → Chorus → Outro |
| ~240–360 s | Full double form; consider `[Instrumental]` or `[Solo]` breaks between the second chorus and bridge |

Repeat the chorus **verbatim** each time (small final-chorus lift is fine).
Keep lines singable: roughly 4–10 words, consistent meter within a section,
verses that advance the story, a chorus that distills it into a hook.

## Craft checklist (validate before returning)

- Concrete imagery over abstraction; one controlling image or scene per song.
- A discernible emotional arc across sections — the bridge (if any) turns or
  reframes, it doesn't repeat.
- Rhyme serves the line, not the reverse; slant rhyme beats forced rhyme.
- No production talk ("the drums kick in"), no stage directions, no title line.
- Tags each on their own line; structure matches the requested duration.

## Workflow in this repo

1. Write the lyrics following the rules above.
2. Save to `assets/<kebab-case-title>.txt` (don't overwrite `neon_rain.txt`).
3. Hand off in tandem: invoke `music-caption-rewriter` with the user's style brief
   as `Caption` and these finished lyrics as `Lyrics` — it reads only the bracketed
   tags to build its Arrangement timeline and will never quote the lyric text.
4. The pair drops into the generation command:
   `--lyrics_file assets/<title>.txt --prompt "<rewritten caption>"`.

For structural reference, 35 professionally written tagged lyric sheets (all vocal
and regional demo tracks) live in `docs/demo_prompt_examples.md` — study structure
and tag usage there, never copy lines.

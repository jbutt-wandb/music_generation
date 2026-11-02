# Song Similarity + Generation: Approaches

> Companion literature review of recent papers per approach family:
> [song_similarity_literature_review.md](song_similarity_literature_review.md)

The problem: given a target — a reference track or a text style brief — make
MiniMax-Music3 produce a song that sounds like it, and quantify how close each
attempt actually got so iteration is measurable rather than vibes-based.

That splits into two coupled sub-problems:

1. **Steering** — constructing inputs (caption, lyrics, seed) that push the
   model toward the target sound.
2. **Measuring** — a repeatable similarity score between the target and a
   generated WAV, so different seeds/captions can be compared objectively.

Approaches A–C below are steering strategies, D is the measuring stick, and E
combines them into a loop.

## The control surface

MiniMax-Music3 has **no reference-audio conditioning**. Every steering signal
must pass through its text inputs:

| Lever | What it changes | Cost per iteration |
|---|---|---|
| `--seed` | A new take of the same song | One GPU run |
| `--prompt` (Structured Caption) | The sound: genre, tempo, key, mood, vocals, arrangement | Caption rewrite + one GPU run |
| `--lyrics` | The words and section structure | New lyrics, then new caption, then one GPU run |
| `--audio_duration` | Length (≤ 360 s) | One GPU run |

This is why "similarity" here is largely a **caption problem**: if we can
describe the target well in the caption vocabulary, the model does the rest.
Audio-side tools (B, C, D) exist to translate a reference track into that
vocabulary and to verify the result.

## A. Caption-template retrieval (text → text)

Map a style brief to the nearest of the 1,000 bundled caption templates in
`.claude/skills/music-caption-rewriter/templates/`, then synthesize from them.

Three variants, in increasing infrastructure order:

- **LLM routing (status quo).** The `music-caption-rewriter` skill's
  progressive-disclosure flow: `references/genre-router.md` → one or two of the
  18 `index-*.md` family files → up to three template cards. Zero infra, and
  the router encodes human disambiguation knowledge (e.g. "R&B singing over
  trap drums routes to modern R&B primary"). Weakness: recall is bounded by
  the router tables — a brief that straddles families or uses vocabulary the
  cues don't cover can miss the best template.
- **Lexical retrieval (BM25 / TF-IDF).** Index the raw template text; rank by
  term overlap with the brief. No model download, instant, pure
  numpy/scikit-learn. Weak on paraphrase: "moody late-night synths" won't
  match "nocturnal electronic atmosphere".
- **Local text embeddings + cosine.** Embed all 1,000 templates once with a
  sentence-transformers model (runs on the Mac, MPS or CPU; vectors cached to
  disk as a `.npy` + ID list), embed the brief at query time, take top-k.
  Handles paraphrase, trivially fast at query time, and template IDs map
  straight back to files (card ID == filename stem). One new dependency.

These compose rather than compete: embedding retrieval can produce a candidate
set that the LLM router flow then reranks and synthesizes from. Note the skill
itself forbids embeddings *inside its workflow* — retrieval code belongs in
`scripts/` or `app/` as a separate tool (see Infrastructure notes).

**Needs:** nothing (variant 1) up to `sentence-transformers` (variant 3).
**Captures:** style vocabulary; only as good as the brief.
**Limit:** text-only — can't consume a reference track.

## B. MIR feature extraction (audio → caption metadata)

Use classic music-information-retrieval features to read hard facts off a
reference track and fill the caption's Basic Attributes deterministically:

- `librosa` (or `essentia`): tempo (BPM), key and mode estimate, RMS
  energy/dynamics curve, spectral centroid/rolloff (brightness), onset density.
- Those map one-to-one onto caption fields: "bpm is 150. key is E, and scale
  is minor." Energy curves can even inform the Global Emotional Progression
  wording ("launches immediately at high energy, dips at 1:30…").

**Needs:** `librosa` (pure local, CPU is fine).
**Captures:** tempo, key, energy shape — the objective skeleton.
**Limit:** says nothing about timbre, production style, vocal character, or
arrangement prose — the parts of the caption that carry most of the style. Best
used as a constraint layer under approach C, not alone.

## C. Music captioning (audio → text → Structured Caption)

Run a music-understanding model over the reference track to get a prose
description, then have Kimi-K2.6 (via the existing `app/compose.py` W&B
Inference client) rewrite that prose into the three-section Structured Caption
format — effectively **style transfer by caption inversion**.

Candidate captioners: LP-MusicCaps, Qwen-Audio-class audio LLMs, or MuQ/CLAP
zero-shot tagging (embed the audio, score it against a bank of tag phrases,
keep the top tags as pseudo-caption input).

**Needs:** one audio-understanding checkpoint (a few GB; Mac-runnable for the
smaller ones), plus the existing LLM client for the rewrite step.
**Captures:** genre, instrumentation, mood, vocal character — the prose the
MIR features miss.
**Limit:** captioners hallucinate and speak their own vocabulary, not
MiniMax's; quality gates on the rewrite step. Pairs well with B (facts from
MIR override the captioner's guesses) and A (retrieved templates provide the
target phrasing).

## D. Joint audio–text embeddings (the measuring stick)

Contrastive audio–text models embed music and language into one space, giving
two scores:

- **Audio–audio cosine** between the reference track and a generated WAV — the
  core similarity metric for evaluating takes.
- **Text–audio cosine** between a candidate caption and the reference audio —
  rank caption drafts *before* spending a GPU run.

Main options:

| Model | Type | Notes |
|---|---|---|
| **MuQ-MuLan** | music–text contrastive | Strongest music-domain option: ~72.4% agreement with human listeners on instrument-similarity XAB; beats LAION-CLAP and MuLan on MagnaTagATune tagging. HF checkpoint via `transformers`. |
| **LAION-CLAP** | general audio–text contrastive | Close behind (~71.9% on the same XAB benchmark), mature tooling (`laion-clap` package), lots of prior art. |
| **MuQ / MERT** | audio-only self-supervised | No text tower, so audio–audio only; MuQ outperforms MERT across MARBLE benchmark tasks. Useful as a second opinion on the audio–audio score. |

Practical shape: a `score_similarity(reference_wav, generated_wav)` helper that
chunks long audio (these models embed ~10 s windows), mean-pools, and returns
cosine — logged to W&B alongside each run so every take gets a number.

**Needs:** one checkpoint (~1–2 GB), runs on the Mac; `soundfile` already in
the repo for I/O.
**Captures:** overall timbre/style proximity. **Limit:** a single scalar —
blind to *why* two tracks differ (tempo? vocals? mix?); B's features help
attribute the gap.

## E. Closed-loop generation (best-of-N and iterative refinement)

Combine steering and measuring into an optimization loop:

1. **Best-of-N (cheapest loop):** fix the caption, sweep N seeds (separate
   single-GPU launches per CLAUDE.md), score every WAV against the reference
   with D, keep the argmax. No new ideas needed — just metric + sweep.
2. **Caption iteration:** feed Kimi the current caption, the similarity score,
   and the attributed gap from B ("generated is 12 BPM fast, brighter spectral
   centroid, reference has female vocal") and ask for a targeted caption edit;
   regenerate; repeat until the score plateaus.
3. **Candidate pre-ranking:** before any GPU run, use D's text–audio score to
   pick the most promising of several caption drafts, cutting wasted runs.

**Needs:** everything above plus orchestration (a driver script managing
launches, scoring, and W&B logging).
**Cost:** N GPU runs per round — the expensive approach; the pre-ranking in
(3) exists to keep N small.
**Value:** turns similarity from a report card into a controller.

## Comparison

| Approach | Input | New deps | Runs on | Relative cost | Standalone value |
|---|---|---|---|---|---|
| A. Template retrieval | text brief | none → `sentence-transformers` | Mac | trivial | High — improves every caption today |
| B. MIR features | reference audio | `librosa` | Mac (CPU) | trivial | Medium — exact BPM/key for captions |
| C. Music captioning | reference audio | captioner checkpoint | Mac (small) | low | High — only path from audio to a full caption |
| D. Audio–text embeddings | both WAVs (or caption + WAV) | `laion-clap` or MuQ via `transformers` | Mac | low | High — objective score for every run |
| E. Closed loop | reference + A–D | orchestration only | Mac + H100 | high (N GPU runs) | Highest, but needs the others first |

## Recommended phasing

Each phase is independently useful; later phases build on earlier ones.

1. **Phase 1 — embedding retrieval over templates (A).** Prototype in
   `scratchpad.ipynb`: embed the 1,000 templates, cache vectors, top-k for a
   brief; eyeball retrieval quality against the LLM router's picks. Then
   productionize as a small script.
2. **Phase 2 — similarity scoring (D).** MuQ-MuLan or LAION-CLAP
   `score_similarity` helper; log the score to W&B for every generated WAV so
   seed sweeps become rankable immediately.
3. **Phase 3 — reference-to-caption (B + C).** MIR features for the hard
   attributes, a captioner + Kimi rewrite for the prose; output is a draft
   Structured Caption from any reference MP3/WAV.
4. **Phase 4 — close the loop (E).** Best-of-N seed sweeps ranked by Phase 2's
   score, then score-guided caption iteration.

## Infrastructure notes

- **W&B Inference has no embeddings endpoint** (chat/completion models only,
  verified against the model catalog) — all embedding and scoring models run
  locally. They are small; none of this needs a cluster allocation. The H100
  is only ever spent on generation itself.
- Keep the `music-caption-rewriter` skill's no-embeddings rule intact: retrieval
  and scoring live in `scripts/` / `app/` (mirroring the `app/compose.py`
  client/env pattern — `load_dotenv`, `WANDB_API_KEY`), and the skill may *call*
  them as a tool rather than absorb them.
- Template IDs are stable join keys: card ID == `templates/<id>.txt` stem ==
  embedding-index row, so no extra mapping layer is needed.
- New dependencies arrive per phase, not up front: `sentence-transformers`
  (Phase 1), MuQ/CLAP checkpoint (Phase 2), `librosa` + captioner (Phase 3).

## Sources

- [MuQ: Self-Supervised Music Representation Learning with Mel-RVQ](https://arxiv.org/abs/2501.01108) — MuQ and MuQ-MuLan; MARBLE benchmark results vs MERT.
- [Pretrained Text-Audio Embeddings: CLAP & MuQ-MuLan](https://www.emergentmind.com/topics/pretrained-text-audio-embeddings-clap-and-muq-mulan) — XAB human-agreement and tagging comparisons.
- [LP-MusicCaps: LLM-based pseudo music captioning](https://arxiv.org/abs/2307.16372) — music captioning for approach C.
- [W&B Inference model catalog](https://docs.wandb.ai/guides/inference/models/) — confirms chat-only, no embeddings endpoint.

# Song Similarity + Generation: Literature Review

Companion to [song_similarity_approaches.md](song_similarity_approaches.md).
Sources found via the Hugging Face Papers API (`/api/papers/search`), August
2026; sections mirror the approach families A–E from the approaches doc. Each
paper links to its `hf.co/papers` page.

## Key takeaways

1. **"Audionese" is real and validates the caption-template strategy.** Meta's
   prompt-challenge study showed text-to-audio models have a preferred prompt
   distribution far from natural user briefs, and that LLM-rewriting user
   prompts toward it measurably improves output quality. Our
   brief → template → Structured Caption pipeline is exactly this, specialized
   to MiniMax-Music3.
2. **Frontier systems solve reference-similarity with architecture we don't
   have.** Qwen-Music, SongEcho, and MPEcho condition directly on reference
   audio/melody. MiniMax-Music3 can't — which confirms that for this repo, the
   reference must be *translated into text* (approaches B/C), not injected.
3. **The measuring stick is settled science.** Frozen MuQ features + a small
   head (MuQ-Eval) hit 0.84 per-sample correlation with human quality ratings;
   MAD shows self-supervised embeddings beat FAD for human-preference
   alignment. Use MuQ/MuQ-MuLan embeddings; skip FAD entirely.
4. **Temporal/structural captioning exists off the shelf.** FUTGA produces
   per-segment, time-boundary captions for full songs — nearly the same shape
   as the caption's Arrangement section. SonicVerse fuses MIR feature probes
   into captions, validating the B+C hybrid.
5. **Best-of-N with a verifier is an established inference-time scaling
   paradigm** (diffusion noise search, multi-verifier audio-video, symbolic
   music inference alignment) — our Phase 4 closed loop is the same recipe
   with seeds as the search space and embedding similarity as the verifier.

## 1. Reference-conditioned song generation (what frontier systems do)

These papers attack "make a song like this one" head-on, with model access we
don't have — useful as the ceiling and for design vocabulary.

- **[Qwen-Music Technical Report](https://huggingface.co/papers/2607.11699)**
  (2026-07). Two tasks: text-to-music and **cover song generation**
  (reinterpret an existing song with a different style/vocals). Tokenizes
  audio to 25 Hz semantic tokens, plans melody with a "Melody-CoT" before
  generating, supports reference-audio melody cloning. The closest published
  statement of our problem — solved via native audio conditioning.
- **[SongEcho](https://huggingface.co/papers/2602.19976)** (2026-02) and
  **[MPEcho](https://huggingface.co/papers/2607.26698)** (2026-07). Cover-song
  generation conditioned on the original vocal melody plus a text prompt;
  MPEcho adds phoneme-level alignment. SongEcho also contributes **Suno70k**,
  an AI-song dataset, as a data workaround.
- **[JEN-1 DreamStyler](https://huggingface.co/papers/2406.12292)** (2024-06).
  Textual-inversion-style "musical concept learning": fine-tunes pivotal
  parameters on ~2 min of reference audio so a pseudo-word denotes that style.
  The fine-tuning analogue of our caption-inversion approach C.
- Open full-song systems for context on the caption interface itself:
  **[ACE-Step 1.5](https://huggingface.co/papers/2602.00744)** (2026-01,
  LM + DiT hybrid with editing features),
  **[Muse](https://huggingface.co/papers/2601.03973)** (2026-01, fully
  open-source long-form song generation with fine-grained style conditioning),
  **[SegTune](https://huggingface.co/papers/2510.18416)** (2025-10,
  segment-level prompts with LLM-assisted duration prediction — same
  section-timeline philosophy as the Structured Caption's Arrangement), and
  **[LeVo](https://huggingface.co/papers/2506.07520)** (2025-06, DPO
  multi-preference alignment for lyrics-to-song).

**Implication:** none of these help steer MiniMax-Music3 directly, but they
fix the target vocabulary (melody vs. style vs. vocal identity as separable
axes) and confirm that without audio conditioning, text is the only channel.

## 2. Measuring similarity and quality (approach D)

- **[MuQ](https://huggingface.co/papers/2501.01108)** (2025-01,
  [code](https://github.com/tencent-ailab/muq)). Self-supervised music
  representation via Mel-RVQ; SOTA on MARBLE, beats MERT; MuQ-MuLan variant
  adds the text tower for zero-shot tagging and text–audio scoring. Our
  default embedding backbone.
- **[MuQ-Eval](https://huggingface.co/papers/2603.22677)** (2026-03).
  Per-sample quality metric: frozen MuQ-310M features + attention pooling +
  2-layer MLP reaches utterance-level SRCC 0.838 / system-level 0.957 against
  expert ratings. Two findings matter for us: (a) *encoder choice dominates
  everything else* — more evidence for MuQ; (b) LoRA on ~150 clips yields a
  usable **personalized** quality head — a plausible later step trained on our
  own take ratings. Caveat: sensitive to signal artifacts, insensitive to
  musical-structural distortions.
- **[Aligning Text-to-Music Evaluation with Human Preferences](https://huggingface.co/papers/2503.16669)**
  (2025-03). Shows FAD and most reference-based metrics correlate weakly with
  human preference (0.14); proposes **MAD** (MAUVE Audio Divergence) on
  self-supervised embeddings (0.62, and 0.84 average rank correlation on
  synthetic desiderata). Justifies skipping FAD for run evaluation.
- **[SLAP](https://huggingface.co/papers/2506.17815)** (2025-06,
  [code](https://github.com/pliploop/slap)). BYOL-style language-audio
  pretraining without negatives — a CLAP alternative addressing the modality
  gap.
- **[CoLLAP](https://huggingface.co/papers/2410.02271)** (2024-10). Extends
  contrastive language-audio pretraining to **long-form** audio with temporal
  structure augmentation — relevant because our outputs run up to 360 s and
  most contrastive models embed ~10 s windows.
- **[CrossMuSim](https://huggingface.co/papers/2503.23128)** (2025-03).
  Music-similarity retrieval guided by LLM-generated text descriptions of
  tracks, A/B-tested on a production streaming platform — production evidence
  that text descriptions are a strong similarity signal, which is the premise
  of our whole caption-side strategy.
- **[Music Plagiarism Detection](https://huggingface.co/papers/2601.21260)**
  (2026-01). Segment-based similarity formulation — the adversarial cousin of
  our problem; a reminder to score similarity per-segment, not only globally.

## 3. Audio → caption (approaches B + C)

- **[LP-MusicCaps](https://huggingface.co/papers/2307.16372)** (2023-07,
  [code](https://github.com/seungheondoh/lp-music-caps)). The standard
  LLM-pseudo-captioning baseline; solid but clip-level and genre-vocabulary
  coarse.
- **[FUTGA](https://huggingface.co/papers/2407.20445)** (2024-07,
  [model](https://huggingface.co/JoshuaW1997/FUTGA)). Fine-grained,
  **temporally-enhanced** captioning of full-length songs: detects transition
  points, describes each segment and its musical function. This is nearly the
  Arrangement section of a Structured Caption generated from audio — the
  single most promising Phase-3 captioner.
- **[SonicVerse](https://huggingface.co/papers/2506.15154)** (2025-06,
  [code](https://github.com/AMAAI-Lab/sonicverse),
  [demo Space](https://huggingface.co/spaces/amaai-lab/SonicVerse)).
  Multi-task captioning where MIR feature-detection heads (key, vocals,
  instrumentation) feed the caption LLM — published validation of our "B
  constrains C" hybrid.
- **[Rethinking Music Captioning with Music Metadata LLMs](https://huggingface.co/papers/2602.03023)**
  (2026-02). Predicts structured metadata from audio, then lets a text LLM
  style the caption at inference — same two-stage split as our
  captioner → Kimi-K2.6 rewrite plan.
- **[Music Flamingo](https://huggingface.co/papers/2511.10289)** (2025-11,
  NVIDIA) and **[Audio Flamingo Next](https://huggingface.co/papers/2604.10905)**
  (2026-04). Large open audio-language models with strong music understanding
  and long audio input; heavier-weight alternatives if FUTGA-class models
  prove too coarse. **[CMI-Bench](https://huggingface.co/papers/2506.12285)**
  (2025-06) benchmarks music instruction-following for choosing among them.

## 4. Steering via text: prompt optimization and retrieval (approaches A + E)

- **[On The Open Prompt Challenge In Conditional Audio Generation](https://huggingface.co/papers/2311.00897)**
  (2023-11, Meta). Treats the generator as a black box (exactly our
  situation), identifies the user-prompt vs. training-prompt alignment gap and
  the "audionese" distribution models prefer, then improves quality by
  LLM-rewriting prompts with text–audio alignment as a ranking feedback
  signal. The closest methodological ancestor of the caption-rewriter skill
  *and* of Phase 4's score-guided caption iteration.
- **[Multimodal Music Generation with Explicit Bridges and Retrieval Augmentation (VMB)](https://huggingface.co/papers/2412.09428)**
  (2024-12, [code](https://github.com/wbs2788/vmb)). Uses text and music as
  explicit bridges plus **retrieval augmentation** for generation — published
  support for retrieving reference material (our templates) to condition
  generation rather than free-writing prompts.
- **[Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps](https://huggingface.co/papers/2501.09732)**
  (2025-01, DeepMind). Frames generation-time compute as *search over noises
  with verifiers* — the theoretical backbone of best-of-N: our seeds are the
  noise candidates and embedding similarity is the verifier.
- **[Inference-Time Scaling for Joint Audio-Video Generation](https://huggingface.co/papers/2606.03183)**
  (2026-06). Multi-verifier test-time optimization with adaptive reward
  weighting — the pattern to copy if we score takes on several axes at once
  (similarity + MuQ-Eval quality + BPM match).
- **[Text2midi-InferAlign](https://huggingface.co/papers/2505.12669)**
  (2025-05). Inference-time text–audio alignment for symbolic music — same
  loop in the MIDI domain.
- **[MusicMagus](https://huggingface.co/papers/2402.06178)** (2024-02,
  [code](https://github.com/ldzhangyx/MusicMagus)). Zero-shot text-to-music
  *editing* via diffusion latent manipulation — requires model internals, so
  not applicable to MiniMax-Music3 today, but defines what "change only the
  timbre, keep the song" looks like when you do have access.

## What this changes about the plan

| Repo phase | Literature verdict |
|---|---|
| Phase 1 — template retrieval | Strengthened: "audionese" (2311.00897) and retrieval-augmented generation (VMB) both argue for retrieving in-distribution prompt material rather than free-writing. CrossMuSim shows text descriptions carry similarity signal in production. |
| Phase 2 — similarity scoring | Sharpened: default to **MuQ/MuQ-MuLan** embeddings (encoder choice dominates, per MuQ-Eval); add a MuQ-Eval-style quality head so takes are ranked on similarity *and* quality; avoid FAD (2503.16669). Chunk-and-pool for 360 s outputs, or consider CoLLAP for long-form. |
| Phase 3 — reference → caption | **FUTGA first** (temporal, per-segment captions map to the Arrangement section), MIR features constraining it SonicVerse-style; Music Flamingo–class models as the heavyweight fallback. |
| Phase 4 — closed loop | Framed as verifier-guided search (2501.09732): seeds = candidates, MuQ similarity + quality = verifiers, LLM caption rewriting with score feedback (2311.00897) = the outer loop. Multi-verifier weighting per 2606.03183 if axes conflict. |
| Not viable here | Direct reference-audio conditioning (Qwen-Music, SongEcho, MPEcho) and latent editing (MusicMagus) need model access MiniMax-Music3 doesn't expose — they mark the ceiling text-only steering is competing against. |

## Method note

Queries run against `https://huggingface.co/api/papers/search` (hybrid
semantic + full-text): *music similarity retrieval; music captioning;
text-to-music generation controllable; music generation evaluation metric;
song generation lyrics; music style transfer reference audio; contrastive
music text embedding; inference-time scaling audio generation; reference music
imitation generation cover; prompt optimization audio generation LLM feedback;
music understanding LLM benchmark; zero-shot music editing prompt inversion.*
27 papers shortlisted from ~90 hits; abstracts and metadata via
`/api/papers/{id}`.

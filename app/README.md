# Music Generation Studio — the marimo web app

A web UI for generating full songs with **MiniMax-Music3**, modeled on the
official demo Space. You describe a song (or write lyrics + a Structured Caption
yourself) and the finished track plays in your browser — with every run logged
to Weights & Biases when `WANDB_ENTITY`/`WANDB_PROJECT` are configured
(recommended; without them runs are not logged).

The app runs **inside a CoreWeave serverless GPU sandbox**: `scripts/sandbox.py up`
creates a 1-GPU sandbox from a pre-built filesystem snapshot (app venv + ~57 GB
of model weights), starts marimo in it, and prints a tokenized HTTPS URL. The
same GPU that serves the app generates the music — no ssh, no Slurm allocation.

```bash
uv run --no-project --python 3.12 scripts/sandbox.py up   # → prints the app URL
```

> ## ⚠️ The sandbox bills while it runs
> A studio sandbox costs GPU-time from the moment it is ready until you tear it
> down. **Run `sandbox.py down` when you're done** — it pulls your WAVs first,
> then deletes the sandbox. A 24 h max lifetime is the backstop if you forget,
> not the plan.

---

## Prerequisites

1. **`CWSANDBOX_API_KEY`** in `.env` — create a token with the **"Sandbox User"**
   IAM role at [console.coreweave.com/tokens](https://console.coreweave.com/tokens).
   GPU sandboxes are in preview; if `probe` reports *"not entitled to create GPU
   sandboxes"*, ask your CoreWeave account team to allowlist the org.
2. **`WANDB_API_KEY`** in `.env` — also **required**: it authenticates the app's
   lyric/caption composer (Kimi K2.6 via W&B Inference). The launchers exit
   upfront unless BOTH required keys are present — nothing is spun up otherwise.
3. **Recommended: `WANDB_ENTITY` + `WANDB_PROJECT`** in `.env` — with both set,
   every song and its config is logged to that W&B project (recommended); if
   either is unset, generation still works but **runs are not logged at all**.
   Plus `HF_TOKEN` for the one-time model download during `seed`. Optional:
   `SNAPSHOT_ID` (adopt a teammate's snapshot), `SANDBOX_IMAGE`,
   `SANDBOX_CPU`/`SANDBOX_MEMORY` overrides.
4. **`uv`** on the local machine. (No local `uv sync` is needed just to launch
   the app — the launcher is a self-contained uv script, and the app's venv
   lives in the snapshot.)
5. An ssh alias `coreweave-login` is **only** needed for the Slurm *fallback*
   path of `scripts/sandbox_generate.py` — the app itself never uses ssh.

## One-time setup — probe, then seed the snapshot

```bash
# 1. ~1-minute GPU entitlement/capacity check (creates + deletes a tiny GPU
#    sandbox; costs cents; also reveals which GPU model the pool hands you):
uv run --no-project --python 3.12 scripts/sandbox.py probe

# 2. Build the filesystem snapshot: app venv + ~57 GB of MiniMax-Music3 weights,
#    assembled on a cheap CPU-only sandbox (no GPU needed; works even when the
#    GPU pool is full). Expect ~30-60 min. The snapshot id lands in
#    .launch/sandbox-state.json.
uv run --no-project --python 3.12 scripts/sandbox.py seed
```

Every later launch *forks* this snapshot instead of re-downloading. When
`pyproject.toml`/`uv.lock` or the runtime change, refresh it incrementally with
`sandbox.py reseed` (minutes, not another full seed). Teammates can skip seeding
entirely: share the snapshot id and they set `SNAPSHOT_ID` in their `.env` (or
pass `up --snapshot-id <id>`).

## Every session

```bash
# 1. Launch (or reuse) the studio sandbox — ~60 s create + ~4 min snapshot
#    restore, then marimo starts and the URL prints (and opens, on macOS):
uv run --no-project --python 3.12 scripts/sandbox.py up
#    ✅ ready: https://2718-<sandbox-id>....cwsandbox.com/?access_token=<token>

# 2. Make music in the browser.

# 3. Done for the day — pulls new WAVs to generated_audio/MiniMax-Music3/,
#    then deletes the sandbox (billing stops):
uv run --no-project --python 3.12 scripts/sandbox.py down
```

> **The URL is public internet.** The platform does no caller auth on sandbox
> endpoints — marimo's `access_token` in the URL is the only lock. Don't share
> the link; `down`/`up` rotates the sandbox (and `status` re-prints the URL).

Other lifecycle commands:

| Command | What it does |
|---|---|
| `sandbox.py sync` | push local code changes to the running sandbox and restart marimo (fast edit loop) |
| `sandbox.py pull` | download WAVs that exist in the sandbox but not locally |
| `sandbox.py status` | sandbox state, GPU model, marimo health, the URL, snapshot id |
| `sandbox.py down --delete-snapshot` | teardown **and** drop the snapshot (next launch needs `seed` again) |
| `sandbox.py down --no-pull` | teardown without downloading WAVs first |

## Using the app

**Simple mode** — type what you want ("a smoky late-night soul ballad about old
flames, warm female voice"), or click an idea chip. Then either:

- **✎ Write lyrics & review** — Kimi K2.6 composes original lyrics and a full
  three-section caption and places them in the Studio tab for you to edit, or
- **♪ Generate** — composes and sends it straight to the GPU in one go.

Tick **Instrumental** for a song without vocals.

**Studio mode** — full control over both model inputs:

- **Lyrics** pane with quick-insert section tags (`[intro]`, `[verse]`,
  `[chorus]`, …). Tags must sit alone on their own line — words on a tag line
  are silently dropped by the model. A small assist box writes lyrics for you
  from a one-line description.
- **Three caption panes** (Global metadata / Vocal details / Arrangement) —
  the Structured Caption that controls how the song *sounds*. Format guide:
  [`../docs/minimax_music_prompt_guide.md`](../docs/minimax_music_prompt_guide.md);
  61 official worked examples:
  [`../docs/demo_prompt_examples.md`](../docs/demo_prompt_examples.md).
- **Preset chips** load known-good lyrics + caption pairs to start from.
- **Title** names the output file and the W&B caption.

**Settings** (collapsed panel) — max duration 5–360 s (it's a cap; the model
ends the song when the lyrics resolve), seed + randomize, flow-matching steps
(leave at 30).

The execution panel shows **"✅ Running in sandbox `<id>` · GPU: `<model>`"**
when all is well. A red **"Not running inside a GPU sandbox"** callout means the
app was started outside the launcher (e.g. `marimo run app/app.py` on a laptop) —
generation is disabled; launch with `sandbox.py up` instead.

## What to expect during generation

Generation takes **~2 minutes per 60 s of song, plus ~1.5 minutes of model
loading** per run (the model loads per generation; the sandbox's GPU pool is
heterogeneous — H100 80 GB or RTX PRO 6000 96 GB — both fit the model fully
resident). A spinner streams the real phases. **One generation at a time**: the
app refuses duplicate clicks, and a sandbox-wide lock also serializes against a
concurrent `sandbox_generate.py` run targeting the same GPU. When it finishes
you get an audio player, a stats line (title, seed, duration, wall time), a
**link to the W&B run**, and a download button. The WAV lands in the sandbox at
`generated_audio/MiniMax-Music3/<title>_s<seed>.wav` — run `sandbox.py pull`
(or just `down`) to bring new WAVs to the same local path.

## Logs & troubleshooting

| Where | What |
|---|---|
| `.launch/sandbox-state.json` (local, chmod 600) | snapshot id, sandbox id, app token |
| `logs/app_ui.log` (inside the sandbox) | every UI event — read via `sandbox.py status` + `cwsandbox exec`, or marimo's log |
| `/work/logs/marimo.log` (inside the sandbox) | the marimo server's own output |
| `logs/app_<slug>_s<seed>.log` (inside the sandbox) | raw generation logs, one per run |

| Symptom | Cause / fix |
|---|---|
| `probe` fails `not entitled to create GPU sandboxes` | org not allowlisted for GPU sandboxes (preview) — contact the CoreWeave account team |
| `capacity exhausted` retries during `up` | the serverless GPU pool is momentarily full; the launcher retries 6× with backoff — or use `scripts/sandbox_generate.py` whose budget falls back to the Slurm cluster |
| Sandbox stuck in CREATING | snapshot restore legitimately takes ~4 min; the launcher treats longer hangs as wedged, deletes and recreates automatically |
| Browser shows 401 / login page | token mismatch — run `sandbox.py status` to print the correct URL (it recovers the token from the sandbox) |
| Red "Not running inside a GPU sandbox" callout | app launched outside the sandbox — use `sandbox.py up` |
| "Another generation is already in progress" | one song at a time (app lock, or `.gen.lock` held by a CLI run) — wait for the current run |
| Generation failed + log tail shown | read the tail; sandbox environment issues are catalogued in [`../docs/sandbox_environment.md`](../docs/sandbox_environment.md) |
| Composer errors about `WANDB_API_KEY` | fill in `.env` (Prerequisites §2) and relaunch (`down` + `up`) — the keys travel at sandbox creation |

## Files in this directory

```
app.py           the marimo app (UI + reactive wiring)
backend.py       execution: local-subprocess generation on the sandbox GPU,
                 sandbox detection, the one-run-at-a-time locks, and the
                 canonical generation-log grammar + slugify
compose.py       Kimi K2.6 composer (lyrics + captions), shared with scripts/generate_lyrics.py
screenshots/     images used by this README
```

The sandbox lifecycle lives in `../scripts/sandbox.py` (+ `sandbox_lib.py`);
the headless/agent pathway with Slurm fallback is `../scripts/sandbox_generate.py`.

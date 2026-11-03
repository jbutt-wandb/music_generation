# Sandbox Environment — MiniMax-Music3 on CoreWeave Serverless GPU Sandboxes

How the sandbox pathway is put together and how to fix it when it misbehaves.
Facts verified against cwsandbox SDK 1.19.x (Nov 2026); the product moves fast —
when live behavior disagrees with this doc, trust live behavior and update here.
The Slurm-cluster counterpart (now the fallback path) is
[`cluster_environment.md`](cluster_environment.md).

## Platform facts that shape the design

| Fact | Consequence here |
|---|---|
| Serverless sandboxes: **1 GPU max**, type not selectable; the pool is heterogeneous — H100 80 GB (`sm_90`) *and* RTX PRO 6000 96 GB (`sm_120`) | Fine: Music3 is ~23 GB bf16, fully resident on either. The image (CUDA 12.8 / PyTorch 2.8) covers both archs. `probe` tells you which card you drew. |
| GPU sandboxes are **preview-gated per org** | An unentitled org fails at create in <2 s (nothing billed). `sandbox.py probe` answers entitlement + capacity in ~1 min for cents. |
| **Billing runs from "ready" to termination**, metered per ms | `down` when done; `max_lifetime_seconds` (24 h studio, 4 h seed, 600 s probe) is the server-enforced backstop. |
| A GPU request reserves **only** the GPU; serverless needs requests = limits | Studio: 16 CPU / 64 Gi (mirrors the old Slurm job; `SANDBOX_CPU`/`SANDBOX_MEMORY` override). Seed: 8 CPU / 32 Gi, **no GPU** — downloads need none. |
| Services/ports are **fixed at creation**; endpoints do **zero caller auth** | Both pathways create the identical sandbox shape (marimo service on 2718 + `APP_TOKEN`) so either can reuse the other's sandbox. marimo's token is the only lock on a public URL. |
| Attached `exec` dies at the SDK's ~300 s request timeout | Anything slow (uv sync, 57 GB download, a whole song) runs **detached** via `run_long`: nohup + exit code to a `.rc` sentinel, polled with one compound RPC and 2→15 s backoff. |
| FSS snapshots capture **only the mount** — not the container layer, not processes | Everything runtime-critical lives under `/work`; apt installs do NOT survive into forks (see build-tools guard). There is no "snapshot a loaded model" — the model loads per generation. |
| Snapshot staging tars the mount **onto the mount** | Payload must stay under ~half of the 200 Gi mount; `prune_mount` enforces this and sweeps stale staging tars before every snapshot attempt. |

## The /work mount layout (what the snapshot contains)

```
/work/app          the repo + its .venv (uv-managed python under /work/uv-python)
/work/hf           HF_HOME — ~57 GB of MiniMax-Music3 weights
/work/bin/uv       static uv binary (survives forks; container pythons vary)
/work/cache/uv     uv cache (pruned before snapshot; keeps the git-built diffusers wheel)
/work/logs         run_long step logs + .rc sentinels, marimo.log, generation logs
/work/wandb        WANDB_DIR/-CACHE/-CONFIG — W&B artifacts stay off the container disk
```

## Snapshot lifecycle

- **`seed`** (one-time): CPU sandbox, fresh mount → uv binary → code tarball →
  build tools → `uv sync` → `snapshot_download` the weights → verify paths →
  prune → snapshot (retried ×5 — the RPC can fail transiently at the moment of
  maximum accumulated state; the sandbox stays alive, so retry, never rebuild).
  Snapshot id → `.launch/sandbox-state.json`.
- **`reseed`** (updates): fork the current snapshot on a CPU sandbox, apply only
  the delta (code, `uv sync`, missing weights — `ensure_model` is a no-op when
  present), re-snapshot, delete the old snapshot only after the new one is
  saved (`--keep-old` opts out). Minutes, not another full seed.
- **Adoption**: a teammate's snapshot id via `SNAPSHOT_ID` in `.env` or
  `up/reseed --snapshot-id <id>` — a fresh clone never needs its own seed.
- Old snapshots bill per GiB-hr of storage — the tooling deletes replaced ones.

## Launcher → app contract

- Creation env (never argv): `WANDB_API_KEY/ENTITY/PROJECT`, `HF_TOKEN`,
  `HF_HOME=/work/hf`, `APP_TOKEN` (marimo `--token-password`), `WANDB_DIR`
  family, `TORCH_DISABLE_NATIVE_JIT=1`,
  `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`. Only these keys are read
  from `.env` — never the whole file.
- `MUSICGEN_SANDBOX_ID` is injected on the marimo process at `start_marimo`
  (the id exists only post-create) and mirrored to `/work/app/.sandbox_id`;
  `app/backend.py:sandbox_status()` reads either. Both `.sandbox_id` and
  `.gen.lock` are gitignored and tar-excluded — a stray local copy would fake
  "inside a sandbox".
- `/work/app/.gen.lock` serializes the GPU sandbox-wide: the app holds an
  fcntl lock, the headless pathway wraps its run in `flock -n` — one
  generation at a time, by construction.
- State (`.launch/sandbox-state.json`, chmod 600): snapshot id, studio id,
  app token, launch time. The token that counts is the one baked into the
  *sandbox's* env — adopting someone else's sandbox reconciles it from there.

## The errors and their fixes

| Symptom | Root cause | Fix |
|---|---|---|
| `not entitled to create GPU sandboxes` (<2 s at create) | org not allowlisted for the GPU preview | CoreWeave account team / forge-support@coreweave.com; CPU sandboxes still work |
| `Create sandbox resource exhausted: runner capacity exhausted` | serverless GPU pool momentarily full; nothing created or billed | the tooling retries ×6 with backoff; `sandbox_generate.py` falls back to Slurm when its budget expires |
| Sandbox sits in CREATING "forever" | restoring the ~70 GB snapshot legitimately takes ~4 min; beyond the wait timeout it's wedged (observed live: 2 h+) | `create_with_retry` deletes the stuck sandbox and recreates — wedged CREATING bills nothing |
| A long step dies at exactly ~300 s | attached `exec` hit the SDK request timeout | run it via `run_long` (detached + `.rc` sentinel) — never run servers or long installs attached |
| `Failed to find C compiler` at the FIRST generation (model loaded fine) | Triton JIT-compiles host C at first kernel launch; the `*-runtime` image has no gcc — and apt lives in the container layer, which snapshots never carry | `ensure_build_tools` reinstalls gcc/libc6-dev/git on every fresh sandbox (idempotent). Permanent fix: a custom `SANDBOX_IMAGE` with tools baked in, pinned by digest |
| `uv sync` fails fetching diffusers | pyproject pins diffusers to a **git** commit and the runtime image ships no `git` | same build-tools guard (git is installed with gcc) |
| SDK call returns an `OperationRef` instead of the result | cwsandbox async surface | call `.result()` — `Sandbox.list`, `delete`, `write_file`, `snapshot`, exec all return futures; `Sandbox.from_id` may too |
| `CWSandboxAuthenticationError` mentioning the key | `CWSANDBOX_API_KEY` missing/typoed in `.env` | console.coreweave.com/tokens, "Sandbox User" role |
| Snapshot create fails after a full build | transient gateway/`FSS_CREATE_TIMED_OUT` — strikes at max accumulated state | the tooling retries ×5 against the still-alive sandbox; never tear down and rebuild over one failed RPC |
| W&B warns `Path /work/wandb wasn't writable` | WANDB_DIR not created before `wandb.init` | `bootstrap_code` mkdirs it on every pathway; if seen, the sandbox predates that fix — `sync` once |
| 401 opening the app URL | local token stale vs the sandbox's `APP_TOKEN` | `sandbox.py status` prints the URL with the recovered token |

## Costs at a glance

- Studio sandbox: GPU + 16 CPU + 64 Gi, billed while RUNNING → `down` promptly.
- Seed/reseed sandbox: CPU-only, self-deleting, bounded by a 4 h lifetime.
- Probe: ~1 min of 1 GPU + 2 CPU, self-deleting, 600 s lifetime cap.
- Snapshot storage: per GiB-hr (payload ~70 GB) — one snapshot at a time;
  replaced ones are deleted automatically.

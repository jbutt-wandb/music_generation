# Running an 11B Music Stack on Anything from 8 GB to 80 GB — a Tutorial

How to place, offload, and shrink MiniMax-Music3 with diffusers, using this repo's
real model as the running example. The stack is ~23 GB of bf16 weights across four
components — an 8B Qwen3 language model (~16 GB), a 0.6B RVQ depth decoder, a 2.4B
flow-matching transformer, and a Flow-VAE vocoder — so unlike its 124 GB video
sibling it fits an 80 GB H100 outright. The story here is therefore *inverted*:
on the cluster you need none of these techniques; they exist to run the same model
on progressively smaller cards.

Code marked **[in this repo]** runs here today (behind the `--offload` flag). Code
marked **[pattern]** is a worked sketch against diffusers main (our pinned rev) that
you'd adapt — modular pipelines are a moving API, so verify signatures against the
pinned commit.

## 0. First, know which wall you're hitting

GPU memory during inference is spent on two very different things:

- **Weights** — fixed at load time (~23 GB bf16 total, the 8B LLM being the
  dominant chunk). Solved by *offloading* (weights hop on/off the GPU) or
  *quantization* (weights get smaller).
- **Activations & latents** — scale with your request. For Music3 that means
  `--audio_duration`: the LLM's KV cache grows with the number of acoustic frames
  (25/s, up to 9,000), and the flow-matching stage denoises latents chunk by chunk
  (chunking keeps *its* footprint roughly constant). Solved by *freeing weights to
  make room*, or by *shrinking the request* (shorter duration).

Diagnose before choosing a technique — measure the peak after a run:

```python
# After a run (or in an except block around the pipe call):
for d in range(torch.cuda.device_count()):
    print(f"cuda:{d} peak allocated: {torch.cuda.max_memory_allocated(d)/2**30:.1f} GiB")
```

## 1. Everything resident — the H100 default **[in this repo]**

`--offload none` (the default): load all components in bf16 and put them on the GPU.
Fastest, simplest, and on an 80 GB card there is no reason to do anything else —
~23 GB of weights leaves ~55 GB of headroom for the KV cache and latents at any
legal duration.

```python
# scripts/minimax_music3.py (offload == "none"):
pipe = ModularPipeline.from_pretrained(model_id)
pipe.load_components(dtype=torch.bfloat16)
pipe.to("cuda")
```

## 2. Auto CPU offload — component-level **[in this repo]**

`--offload auto`: a `ComponentsManager` watches usage and shuttles whole components
between host RAM and the GPU as each stage runs (text encode → semantic generation →
chunk denoise → vocode). Peak VRAM ≈ 21–22 GB — barely below resident, because the
8B LLM must be fully on-GPU during its (long) autoregressive stage. Each stage
boundary pays a PCIe transfer.

```python
# scripts/minimax_music3.py (offload == "auto"):
manager = ComponentsManager()
pipe = ModularPipeline.from_pretrained(model_id, components_manager=manager)
pipe.load_components(dtype=torch.bfloat16)
manager.enable_auto_cpu_offload(device="cuda")
```

This mode earns its keep on ~24 GB cards (4090-class), not on the H100.

## 3. Group offloading — stream the LLM block-by-block **[in this repo]**

`--offload group`: the big win for small cards. The 8B language model's transformer
blocks stream through the GPU in groups, prefetched on a CUDA stream so the transfer
hides behind compute; the three small components stay resident. Peak VRAM ≈ 6–8 GB —
a generation fits an 8 GB card — at a real speed cost (the LLM stage is
autoregressive, so it revisits every block once per generated frame).

```python
# scripts/minimax_music3.py (offload == "group"):
from diffusers.hooks import apply_group_offloading

pipe = ModularPipeline.from_pretrained(model_id)
pipe.load_components(dtype=torch.bfloat16)
apply_group_offloading(
    pipe.language_model,
    onload_device=torch.device("cuda"),
    offload_device=torch.device("cpu"),
    offload_type="block_level",
    num_blocks_per_group=2,
    use_stream=True,
)
for name in ("rvq_depth_decoder", "condition_encoder", "transformer", "vocoder"):
    getattr(pipe, name).to("cuda")
```

Dial `num_blocks_per_group` up for speed (more resident at once) or down for memory;
`offload_type="leaf_level"` is the extreme end (max savings, max slowdown).

## 4. Quantization — make the weights smaller **[pattern]**

The only technique that reduces weight memory outright, and here it composes
naturally: the 8B LLM is a stock `Qwen3ForCausalLM`, exactly the model class
bitsandbytes is battle-tested on. 8-bit halves it (~16 GB → ~8 GB); 4-bit quarters it.

```python
from transformers import Qwen3ForCausalLM, BitsAndBytesConfig

language_model = Qwen3ForCausalLM.from_pretrained(
    "MiniMaxAI/MiniMax-Music3", subfolder="language_model",
    quantization_config=BitsAndBytesConfig(load_in_8bit=True),
    torch_dtype=torch.bfloat16,
)
pipe.update_components(language_model=language_model)
```

The LLM writes the *composition* — melody, phrasing, song structure — so quantization
error lands on the most audible part of the stack. A/B against bf16 on a fixed seed
before trusting it.

## 5. Apple Silicon (MPS) — `--device mps` **[in this repo, experimental]**

The script can target a Mac's unified memory instead of CUDA. The math that governs it:

- **Capacity:** ~23 GB of bf16 weights + KV cache share unified memory with macOS —
  16 GB Macs are out, 32 GB is tight, 36 GB+ is comfortable.
- **Bandwidth = speed:** autoregressive decode streams the 8B LLM's ~16 GB of weights
  once per acoustic frame (25/s of audio), so tokens/s ≈ bandwidth ÷ 16 GB. Base
  M-series (~120 GB/s) ≈ 3–4 min of LLM time per 60 s of audio; M-Max-class
  (~400–550 GB/s) ≈ 1 min; plus a slower flow-matching decode. Expect 5–20× the
  H100's wall clock overall.
- **Constraints:** only `--offload none` (the offload machinery is CUDA-only), and
  the modular pipeline's operator coverage on MPS is unverified — treat failures as
  expected, not surprising.

## 6. What diffusers does NOT give you

- **Batched generation** — the pipeline is single-sample (strings in, one song out).
  Seed sweeps are separate launches, not a batch dimension.
- **Multi-GPU speedups** — the three stages run sequentially and the whole stack fits
  one card; a second GPU sits idle. (This is why the sbatch template asks for
  `--gres=gpu:1` — the opposite of the video repo.)
- **Streaming audio** — generation is offline; the WAV exists only when the vocoder
  finishes.

## 7. Choosing: symptom → technique

| Symptom | Reach for | Cost |
|---|---|---|
| On the H100 cluster | 1. `--offload none` | none — this is the default |
| ~24 GB card (4090-class) OOMs at load | 2. `--offload auto` | stage-boundary transfers |
| 8–16 GB card | 3. `--offload group` | much slower LLM stage |
| Still short after offloading | 4. quantize the LLM | composition quality risk |
| OOM grows with `--audio_duration` | shorter duration (KV cache is the activation wall) | shorter song |

**This repo today:** all of 1–3 behind `--offload`; 4 is the documented upgrade path
for cards where even group offloading is not enough.

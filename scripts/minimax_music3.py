import argparse
import os

# Must be set before `import torch`: torch 2.13's _native ops otherwise register
# triton-JIT kernels that fail to compile on nodes without Python dev headers
# (see docs/cluster_environment.md).
os.environ.setdefault("TORCH_DISABLE_NATIVE_JIT", "1")

import torch
import wandb
import uuid
import numpy as np
import soundfile as sf
from diffusers import ComponentsManager, ModularPipeline
from dotenv import load_dotenv

load_dotenv(override=True)

# The pipeline caps generation at 9000 acoustic frames (25 frames/second = six
# minutes); the language model may stop earlier on its own.
MAX_AUDIO_SECONDS = 360

# The tokenized lyrics budget is ~5000 tokens; warn well before it.
LYRICS_CHAR_WARN_THRESHOLD = 12000


def load_lyrics(config):
    """Resolve the lyrics input and fail fast on a bad request before loading weights."""
    if config["lyrics"] is not None:
        lyrics = config["lyrics"]
    elif config["lyrics_file"] is not None:
        with open(config["lyrics_file"], encoding="utf-8") as f:
            lyrics = f.read()
    else:
        # `lyrics` is a required pipeline input; an [Instrumental]-only string
        # asks the checkpoint for a track without vocals.
        print("No lyrics given; generating an instrumental track.")
        lyrics = "[Instrumental]"

    if len(lyrics) > LYRICS_CHAR_WARN_THRESHOLD:
        print(
            f"Warning: lyrics are {len(lyrics)} characters; the checkpoint's tokenized "
            "lyrics budget is ~5000 tokens and overlong lyrics may be truncated."
        )
    return lyrics


def song_title(config, lyrics):
    """A short human-readable name for the W&B audio panel caption."""
    if config["lyrics_file"]:
        stem = os.path.splitext(os.path.basename(config["lyrics_file"]))[0]
        return stem.replace("_", " ").replace("-", " ").strip().title()
    # Inline lyrics: use the first sung (non-tag) line as the hook
    lines = [l.strip() for l in lyrics.splitlines() if l.strip() and not l.strip().startswith("[")]
    if lines:
        return lines[0] if len(lines[0]) <= 60 else lines[0][:57] + "..."
    return "Instrumental"


def load_model(model_id, num_gpus, offload, device):
    # MiniMax-Music3 is ~23 GB of bf16 weights (8B Qwen3 language model + 0.6B
    # RVQ depth decoder + 2.4B flow-matching transformer + Flow-VAE vocoder), so
    # unlike its 124 GB video sibling it fits a single 80GB H100 outright.
    # Generation is single-sample and the stages run sequentially, so extra GPUs
    # buy nothing; --offload exists for smaller cards, not for the cluster.
    if device == "mps":
        # Experimental: the offload modes are CUDA-only (ComponentsManager
        # targets cuda devices; group offloading needs CUDA streams).
        print("Loading MiniMax-Music3 Modular Pipeline on MPS (experimental)...")
        pipe = ModularPipeline.from_pretrained(model_id)
        pipe.load_components(dtype=torch.bfloat16)
        pipe.to("mps")
        return pipe

    print(f"Loading MiniMax-Music3 Modular Pipeline on 1 of {num_gpus} GPU(s) (offload={offload})...")
    if offload == "auto":
        # ~21-22 GB peak: components shuttle between host RAM and the GPU as
        # each stage runs (text encode -> semantic generation -> denoise -> vocode)
        manager = ComponentsManager()
        pipe = ModularPipeline.from_pretrained(model_id, components_manager=manager)
        pipe.load_components(dtype=torch.bfloat16)
        manager.enable_auto_cpu_offload(device="cuda")
    elif offload == "group":
        # ~6-8 GB peak: the 8B language model streams through the GPU in block
        # groups prefetched on a CUDA stream; everything else stays resident.
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
    else:
        # Everything resident on one GPU: fastest, and the right choice on an H100.
        pipe = ModularPipeline.from_pretrained(model_id)
        pipe.load_components(dtype=torch.bfloat16)
        pipe.to("cuda")
    return pipe


def main(config):
    print("Starting music generation process...")
    # Resolve the lyrics first: fail fast on a bad path before spending minutes
    # loading ~23GB of weights. The resolved text goes into the W&B config so a
    # run stays reproducible even if the lyrics file later changes.
    lyrics = load_lyrics(config)
    config["lyrics_text"] = lyrics
    title = song_title(config, lyrics)

    if config["audio_duration"] > MAX_AUDIO_SECONDS:
        raise ValueError(
            f"--audio_duration {config['audio_duration']} exceeds the pipeline cap of "
            f"{MAX_AUDIO_SECONDS}s (9000 acoustic frames at 25 fps)."
        )

    if config["device"] == "mps":
        if not torch.backends.mps.is_available():
            raise RuntimeError("--device mps requested but MPS is not available on this machine.")
        if config["offload"] != "none":
            raise ValueError("--device mps supports only --offload none (the offload modes are CUDA-only).")
        num_gpus = 0
        print(
            "WARNING: MPS support is experimental and unverified for this pipeline. "
            "Expect ~23GB of unified memory used (>=32GB machine recommended), "
            "5-20x slower generation than an H100, and possible unsupported-operator "
            "failures. See docs/gpu_memory_tutorial.md."
        )
    else:
        num_gpus = torch.cuda.device_count()
        if num_gpus == 0:
            raise RuntimeError("MiniMax-Music3 needs a CUDA GPU (~23GB of bf16 weights; less with --offload).")
        print(f"Using {num_gpus} CUDA GPU(s)")

    # Set seed for reproducibility (CPU generator works across all offload modes)
    generator = torch.Generator().manual_seed(config["seed"])

    # Load Model
    pipe = load_model(config["model_id"], num_gpus, config["offload"], config["device"])

    # Log audio to WB
    with wandb.init(
        entity=os.environ.get("WANDB_ENTITY"),
        project=os.environ.get("WANDB_PROJECT"),
        config=config,
        name=f"minimax-music3-generation-{str(uuid.uuid1())[0:5]}",
    ) as run:

        print(f"Generating music for prompt: '{config['prompt']}' (duration={config['audio_duration']}s)")

        audios = pipe(
            prompt=config["prompt"],
            lyrics=lyrics,
            audio_duration=config["audio_duration"],
            num_inference_steps=config["num_inference_steps"],
            generator=generator,
            output="audios",
        )

        # Resolved from the vocoder config (44.1 kHz for the released checkpoint)
        sampling_rate = pipe.sampling_rate

        model_name = config["model_id"].split("/")[-1]
        output_dir = os.path.join("generated_audio", model_name)
        os.makedirs(output_dir, exist_ok=True)
        output_filename = os.path.join(output_dir, "minimax_music3_output.wav")
        # audios comes back as (batch, channels, samples) in [-1, 1];
        # soundfile wants (samples, channels)
        sf.write(output_filename, np.asarray(audios[0]).T, sampling_rate)

        print(f"Saved audio locally to {output_filename}")

        audio = wandb.Audio(
                output_filename,
                caption=f"{title} (seed {config['seed']})",
            )

        # Method A: Direct Audio Logging
        panel_name = "Generated Audio"
        run.log({panel_name: audio})

        # Method B: Log to a W&B Table
        # table = wandb.Table(columns=["Prompt", "Lyrics", "Seed", "Duration", "Audio"])
        # table.add_data(
        #     config["prompt"],
        #     lyrics,
        #     config["seed"],
        #     config["audio_duration"],
        #     wandb.Audio(output_filename)
        # )

        # run.log({"generation_results_table": table})

    # Run automatically finishes when exiting the 'with' block (even if an error occurs)
    print(f"Successfully finished run={run.id} and logged generation results to Weights & Biases!")

if __name__ == "__main__":

    # Example usage (Slurm, 1x H100):
    """
    srun --partition=h100 --gres=gpu:1 --cpus-per-task=16 --mem=100G \
    uv run scripts/minimax_music3.py --model_id "MiniMaxAI/MiniMax-Music3" \
    --prompt "Global Metadata: Indie synth-pop, 108 BPM, A minor, wistful-to-euphoric arc, glossy late-night radio production. Vocal Details: Female lead, airy timbre, intimate verses opening into belted choruses, light stacked harmonies, subtle plate reverb. Arrangement: Warm analog synth pads and a round bassline under the verses; sidechained pulse, arpeggios and driving drums lift the choruses; stripped-back outro on pads and voice." \
    --lyrics_file assets/neon_rain.txt \
    --audio_duration 60 \
    --seed 42

    # Instrumental: omit --lyrics/--lyrics_file entirely
    # Inline lyrics: --lyrics "[Verse]\nStreetlights hum...\n[Chorus]\n..."
    """

    parser = argparse.ArgumentParser(description="Generate a song (stereo WAV) from a music-description prompt and optional tagged lyrics using MiniMax-Music3.")
    parser.add_argument("--model_id", type=str, default="MiniMaxAI/MiniMax-Music3", help="The model ID to use for music generation (~57GB download on first use).")
    parser.add_argument("--prompt", type=str, default="Global Metadata: Indie synth-pop, 108 BPM, A minor, wistful-to-euphoric arc, glossy late-night radio production. Vocal Details: Female lead, airy timbre, intimate verses opening into belted choruses, light stacked harmonies, subtle plate reverb. Arrangement: Warm analog synth pads and a round bassline under the verses; sidechained pulse, arpeggios and driving drums lift the choruses; stripped-back outro on pads and voice.", help="The music description (Structured Caption: Global Metadata / Vocal Details / Arrangement — see docs/minimax_music_prompt_guide.md).")
    parser.add_argument("--lyrics", type=str, default=None, help="Inline lyrics with [Verse]/[Chorus]/[Bridge]/... section tags, each tag on its own line (~5000-token budget). Omit both lyrics flags for an instrumental.")
    parser.add_argument("--lyrics_file", type=str, default=None, help="Path to a UTF-8 lyrics file in the same format (see assets/neon_rain.txt).")
    parser.add_argument("--audio_duration", type=float, default=60, help="Upper bound on the track length in seconds (max 360; the model may end the song earlier).")
    parser.add_argument("--num_inference_steps", type=int, default=30, help="Flow-matching Euler steps per decode chunk (30 is the pipeline default; only change when experimenting).")
    parser.add_argument("--seed", type=int, default=42, help="The random seed for reproducibility.")
    parser.add_argument("--offload", type=str, default="none", choices=["none", "auto", "group"], help="Memory strategy: none = all on GPU (~23GB, right for H100); auto = component-level CPU offload (~21-22GB peak); group = stream the 8B LLM block-by-block (~6-8GB peak, slowest). CUDA only.")
    parser.add_argument("--device", type=str, default="cuda", choices=["cuda", "mps"], help="Compute device: cuda (default, the cluster path) or mps (Apple Silicon, EXPERIMENTAL: >=32GB unified memory, much slower, only --offload none).")

    args = parser.parse_args()

    if args.lyrics is not None and args.lyrics_file is not None:
        parser.error("--lyrics and --lyrics_file are mutually exclusive.")

    # Set configuration parameters
    CONFIG = {
        "model_id": args.model_id,
        "prompt": args.prompt,
        "lyrics": args.lyrics,
        "lyrics_file": args.lyrics_file,
        "audio_duration": args.audio_duration,
        "num_inference_steps": args.num_inference_steps,
        "seed": args.seed,
        "offload": args.offload,
        "device": args.device,
        }

    main(config=CONFIG)

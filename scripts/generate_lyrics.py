"""Generate original, section-tagged song lyrics for MiniMax-Music3 via W&B Inference.

The script counterpart of the `.claude/skills/lyrics-writer` agent skill; the
rules and the Kimi K2.6 client live in `app/compose.py`, shared with the marimo
app. Authenticates with the WANDB_API_KEY already in `.env` — no extra
credentials. Runs on the local machine (one small API call, no GPU).

Usage:
  uv run scripts/generate_lyrics.py --theme "driving home at dawn after a night shift" \
      --duration 120 --constraints "female POV, no forced rhymes"
  # -> assets/<title>.txt, ready for minimax_music3.py --lyrics_file
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.compose import DEFAULT_MODEL, slugify, validate_lyrics, write_lyrics  # noqa: E402


def main(config):
    print(f"Writing lyrics with {config['model']} via W&B Inference...")
    try:
        result = write_lyrics(
            theme=config["theme"],
            duration=config["duration"],
            language=config["language"],
            constraints=config["constraints"],
            model=config["model"],
        )
    except RuntimeError as e:
        sys.exit(str(e))

    lyrics = result["lyrics"].strip() + "\n"
    for warning in validate_lyrics(lyrics):
        print(f"Warning: {warning}")

    out_path = config["out"] or os.path.join("assets", f"{slugify(result['title'])}.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    if os.path.exists(out_path) and not config["force"]:
        sys.exit(f"{out_path} already exists; pass --out for a different path or --force to overwrite.")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(lyrics)

    print(f"Title: {result['title']}")
    print(f"Saved lyrics to {out_path}")
    print(f"\nNext: pass it to the music model, e.g.\n"
          f"  uv run scripts/minimax_music3.py --prompt \"$(cat prompt.txt)\" "
          f"--lyrics_file {out_path} --audio_duration {config['duration']} --seed 42")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate original section-tagged lyrics for MiniMax-Music3 via W&B Inference (writes assets/<title>.txt).")
    parser.add_argument("--theme", type=str, required=True, help="The story, mood, or subject of the song.")
    parser.add_argument("--duration", type=float, default=90, help="Intended --audio_duration in seconds (sizes the section structure; max 360).")
    parser.add_argument("--language", type=str, default="English", help="Language to write the lyrics in.")
    parser.add_argument("--constraints", type=str, default=None, help="Optional extras: POV, rhyme scheme, words to include/avoid, genre feel.")
    parser.add_argument("--out", type=str, default=None, help="Output path (default: assets/<title-slug>.txt).")
    parser.add_argument("--force", action="store_true", help="Overwrite the output file if it exists.")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="W&B Inference model ID (see https://api.inference.wandb.ai/v1/models).")

    args = parser.parse_args()

    CONFIG = {
        "theme": args.theme,
        "duration": args.duration,
        "language": args.language,
        "constraints": args.constraints,
        "out": args.out,
        "force": args.force,
        "model": args.model,
        }

    main(config=CONFIG)

"""Extract the MiniMax-Music3 demo tracks' prompts into docs/demo_prompt_examples.md.

The official demo page (https://minimax-ai.github.io/music3-demo/) embeds every
track's inputs in static HTML: a `<script id="track-data">` JSON blob carries the
Structured Caption (`final_caption`), `lyrics`, `category` and duration, while the
card markup carries each track's title and genre label. This script joins the two
and writes a genre-grouped markdown reference. Re-run it whenever MiniMax updates
the demo page.

Usage: uv run scripts/extract_demo_prompts.py [--url ...] [--out ...]
"""

import argparse
import datetime
import html
import json
import re
import urllib.request
from collections import Counter

DEMO_PAGE_URL = "https://minimax-ai.github.io/music3-demo/"
RAW_HTML_URL = "https://raw.githubusercontent.com/MiniMax-AI/music3-demo/main/index.html"

# The demo page groups tracks into three showcase sections (what each track is
# meant to demonstrate), not track types — "instrumental" tracks still have
# vocals and lyrics. Display names come from the page's own `categories` object.
CATEGORY_LABELS = {
    "vocal": "showcases: vocals",
    "instrumental": "showcases: arrangement / instrumentation",
    "local": "showcases: regional genres (Chinese)",
}


def fetch(url):
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def parse_track_data(page):
    m = re.search(r'<script type="application/json" id="track-data">(.*?)</script>', page, re.S)
    if not m:
        raise RuntimeError("track-data JSON blob not found — the demo page layout changed.")
    return json.loads(m.group(1))["tracks"]


def parse_cards(page):
    """Map track_id -> {title, genre} from the demo-card markup."""
    cards = {}
    for block in re.findall(r'<article class="demo-card".*?</article>', page, re.S):
        style = re.search(r'data-style="([^"]*)"', block)
        track = re.search(r'data-track="([^"]*)"', block)
        title = re.search(r'<span class="album-title">([^<]*)</span>', block)
        title_zh = re.search(r'<span class="album-title-zh"[^>]*>([^<]*)</span>', block)
        if not track:
            continue
        name = (title and title.group(1).strip()) or (title_zh and title_zh.group(1).strip()) or "(untitled)"
        genre = html.unescape(style.group(1)) if style else "*"
        cards[track.group(1)] = {"title": html.unescape(name), "genre": "Other" if genre == "*" else genre}
    return cards


def fence(text):
    """Fenced code block whose fence is longer than any backtick run in the text."""
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    marker = "`" * max(3, longest + 1)
    return f"{marker}\n{text.strip()}\n{marker}"


def mmss(ms):
    s = round(ms / 1000)
    return f"{s // 60}:{s % 60:02d}"


def anchor(heading):
    return re.sub(r"[^a-z0-9一-鿿-]", "", heading.lower().replace(" ", "-"))


def build_doc(tracks, cards, date):
    joined = []
    for t in tracks:
        card = cards.get(t["track_id"])
        if card is None:
            print(f"warning: track {t['track_id'][:12]}… has no card (no title/genre); grouping as Other")
            card = {"title": "(untitled)", "genre": "Other"}
        joined.append({**t, **card})
    for tid in set(cards) - {t["track_id"] for t in tracks}:
        print(f"warning: card {cards[tid]['title']!r} has no track data; skipped")

    by_genre = {}
    for t in joined:
        by_genre.setdefault(t["genre"], []).append(t)
    # Descending track count, "Other" last, name as tiebreaker
    genres = sorted(by_genre, key=lambda g: (g == "Other", -len(by_genre[g]), g))
    counts = Counter(t["category"] for t in joined)

    lines = [
        "# MiniMax-Music3 Demo Prompt Library",
        "",
        f"All {len(joined)} tracks from the official demo page "
        f"([{DEMO_PAGE_URL}]({DEMO_PAGE_URL})), with their exact inputs, grouped by genre. "
        f"Extracted {date} by `scripts/extract_demo_prompts.py` — re-run it to refresh.",
        "",
        f"The demo page presents each track as showcasing one strength of the model: "
        f"{counts.get('vocal', 0)} for vocals, {counts.get('instrumental', 0)} for "
        f"arrangement/instrumentation, {counts.get('local', 0)} for Chinese regional genres "
        f"(Zhongguofeng, Gufeng Pop, Folk). Each entry notes its showcase section.",
        "",
        "These are MiniMax-authored, known-good worked examples of the Structured Caption "
        "format (see [`minimax_music_prompt_guide.md`](minimax_music_prompt_guide.md)). "
        "Each caption drops straight into `--prompt`, and each lyrics block into "
        "`--lyrics_file`, of `scripts/minimax_music3.py`.",
        "",
        "## Contents",
        "",
    ]
    lines += [f"- [{g}](#{anchor(g)}) ({len(by_genre[g])})" for g in genres]

    for g in genres:
        lines += ["", f"## {g}"]
        for t in sorted(by_genre[g], key=lambda t: t["title"].lower()):
            lines += [
                "",
                f"### {t['title']}",
                "",
                f"*{CATEGORY_LABELS.get(t['category'], t['category'])} · {mmss(t['duration_ms'])}*",
                "",
                "**Prompt (Structured Caption):**",
                "",
                fence(t["final_caption"]),
            ]
            if t.get("lyrics", "").strip():
                lines += ["", "**Input lyrics:**", "", fence(t["lyrics"])]
    lines.append("")
    return "\n".join(lines), joined, by_genre


def safe_filename(name):
    """Strip characters that are unsafe in filenames, keeping unicode letters."""
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" .")
    return cleaned or "untitled"


def download_audio(joined, dest_root):
    import os
    import urllib.parse

    taken = set()
    downloaded = skipped = 0
    for t in sorted(joined, key=lambda t: (t["genre"], t["title"].lower())):
        genre_dir = os.path.join(dest_root, safe_filename(t["genre"]))
        os.makedirs(genre_dir, exist_ok=True)
        name = safe_filename(t["title"])
        # Titles can collide across the gallery; disambiguate with the track id
        if (t["genre"], name) in taken:
            name = f"{name}_{t['track_id'][:8]}"
        taken.add((t["genre"], name))
        path = os.path.join(genre_dir, f"{name}.mp3")
        if os.path.exists(path) and os.path.getsize(path) > 0:
            skipped += 1
            continue
        url = urllib.parse.urljoin(DEMO_PAGE_URL, t["audio_url"])
        print(f"  {t['genre']}/{name}.mp3")
        with urllib.request.urlopen(url) as resp, open(path, "wb") as f:
            f.write(resp.read())
        downloaded += 1
    print(f"Audio: {downloaded} downloaded, {skipped} already present, under {dest_root}/")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--url", default=RAW_HTML_URL, help="Demo page HTML to extract from.")
    parser.add_argument("--out", default="docs/demo_prompt_examples.md", help="Output markdown path.")
    parser.add_argument("--download-audio", nargs="?", const="demo_audio", default=None, metavar="DIR",
                        help="Also download every track's mp3 into DIR/<genre>/<title>.mp3 (default DIR: demo_audio). Skips files already present.")
    args = parser.parse_args()

    page = fetch(args.url)
    tracks = parse_track_data(page)
    cards = parse_cards(page)
    doc, joined, by_genre = build_doc(tracks, cards, datetime.date.today().isoformat())

    missing_captions = [t["title"] for t in joined if not t.get("final_caption", "").strip()]
    if missing_captions:
        raise RuntimeError(f"tracks with empty captions: {missing_captions}")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(doc)

    print(f"Wrote {args.out}: {len(joined)} tracks, {len(doc)} chars")
    for g in sorted(by_genre, key=lambda g: -len(by_genre[g])):
        print(f"  {g}: {len(by_genre[g])}")

    if args.download_audio:
        download_audio(joined, args.download_audio)


if __name__ == "__main__":
    main()

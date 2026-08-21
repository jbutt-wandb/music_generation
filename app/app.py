"""Music Generation Studio — a marimo front-end for MiniMax-Music3.

A local equivalent of the official Gradio Space (Simple + Studio modes, same
composition flow) whose generations run on the CoreWeave H100 cluster (or,
experimentally, locally on Apple Silicon). Run with:

    uv run marimo run app/app.py

REQUIREMENT: in CUDA mode the Slurm allocation must ALREADY be running — this
app never provisions or releases GPUs. Start it yourself first (see README).
"""

import marimo

app = marimo.App(width="medium")


@app.cell
def setup():
    import os
    import random
    import re
    import sys
    from pathlib import Path

    import marimo as mo

    # Make `app.compose`/`app.backend` importable and relative paths (assets/,
    # generated_audio/, docs/) correct no matter where marimo was launched from.
    _root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(_root))
    os.chdir(_root)

    from app.backend import SBATCH_CMD, cluster_status, get_logger, run_cluster, run_mps
    from app.compose import compose_song, slugify, validate_lyrics, write_lyrics

    # Per-browser-session id: every UI event is logged to logs/app_ui.log with
    # it, so overlapping sessions/tabs are distinguishable when debugging.
    import uuid as _uuid
    session_id = _uuid.uuid4().hex[:6]
    applog = get_logger()
    applog.info("[%s] UI session started", session_id)
    return (
        SBATCH_CMD, applog, cluster_status, compose_song, mo, os, random, re,
        run_cluster, run_mps, session_id, slugify, validate_lyrics, write_lyrics,
    )


@app.cell
def state(mo):
    # mo.ui values can't be set imperatively — composed/preset content flows
    # through this state, which seeds the elements' `value=` on re-run.
    get_fields, set_fields = mo.state(
        {"title": "", "lyrics": "", "global_meta": "", "vocal_details": "", "arrangement": ""}
    )
    get_desc, set_desc = mo.state("")
    get_result, set_result = mo.state(None)
    get_notice, set_notice = mo.state("")
    # Click-counter dedup (runaway-loop fix): each action cell records the
    # highest button count it has handled and dispatches only on a NEW click.
    # Two separate states so the two cells never re-trigger each other; each
    # state is read/written ONLY by its own cell.
    get_gen_handled, set_gen_handled = mo.state({"simple": 0, "studio": 0})
    get_compose_handled, set_compose_handled = mo.state({"write_review": 0, "assist": 0})
    return (
        get_compose_handled, get_desc, get_fields, get_gen_handled, get_notice,
        get_result, set_compose_handled, set_desc, set_fields, set_gen_handled,
        set_notice, set_result,
    )


@app.cell
def presets_data(re):
    def _split_caption(blob):
        """Split a full three-section caption blob into (global_meta, vocal_details, arrangement)."""
        parts = re.split(r"^\s*(?:Vocal Details|Arrangement)\s*$", blob, flags=re.M)
        if len(parts) == 3:
            gm = re.sub(r"^\s*Global Metadata\s*$", "", parts[0], flags=re.M).strip()
            return gm, parts[1].strip(), parts[2].strip()
        return blob.strip(), "", ""

    def _official_preset(title):
        """Load an official demo track's caption+lyrics from docs/demo_prompt_examples.md."""
        try:
            doc = open("docs/demo_prompt_examples.md", encoding="utf-8").read()
            m = re.search(rf"### {re.escape(title)}\n(.*?)(?=\n### |\Z)", doc, re.S)
            blocks = re.findall(r"```+\n(.*?)\n```+", m.group(1), re.S)
            gm, vd, arr = _split_caption(blocks[0])
            return {
                "title": title, "lyrics": blocks[1].strip() if len(blocks) > 1 else "[Instrumental]",
                "global_meta": gm, "vocal_details": vd, "arrangement": arr,
            }
        except Exception:
            return None

    def _neon_rain_preset():
        try:
            lyrics = open("assets/neon_rain.txt", encoding="utf-8").read().strip()
        except OSError:
            lyrics = ""
        return {
            "title": "Neon Rain",
            "lyrics": lyrics,
            "global_meta": (
                "Basic Attributes: bpm is around 108. key is A, and scale is minor. "
                "Indie Synth-Pop / Electropop.\n"
                "Global Emotional Progression: Opens wistful and intimate over sparse pads; "
                "each chorus lifts into cathartic, neon-lit euphoria; the outro exhales back "
                "into late-night stillness.\n"
                "Sonics & Production Profile: Glossy late-night radio production; warm rounded "
                "low end, airy top; verses breathe, choruses tighten into a sidechained pulse."
            ),
            "vocal_details": (
                "Vocal Gender & Timbre: Singer A (Female), airy and close-miked with a soft "
                "break in the upper register.\n"
                "Vocal Style: Conversational and intimate in the verses, opening into sustained "
                "belts in the choruses.\n"
                "Harmony/Backing Vocals: Light stacked harmonies double the chorus hook; a low "
                "octave layer thickens the final chorus.\n"
                "Vocal FX: Subtle plate reverb throughout; a quarter-note delay throw on the "
                "last word of each chorus."
            ),
            "arrangement": (
                "Instrument Lifecycle: Warm analog synth pads and a round electric bassline "
                "carry the verses; a pulsing arpeggio and driving electronic drums enter at "
                "each chorus; everything but pads and voice falls away for the outro.\n"
                "Groove & Foundation Progression: Verses ride a soft four-on-the-floor kick "
                "with muted hats; choruses add a sidechained pump, open hats, and claps on 2 "
                "and 4; the outro dissolves the pulse entirely.\n"
                "Embellishments, Textures & Spatial FX: White-noise risers into each chorus, a "
                "reverse-reverb swell into the bridge, faint vinyl crackle under the verses."
            ),
        }

    PRESETS = {"Neon Rain — Synth-Pop": _neon_rain_preset()}
    for _name in ("Feel Alive", "The Hit"):
        _p = _official_preset(_name)
        if _p:
            PRESETS[f"{_name} (official)"] = _p
    return (PRESETS,)


@app.cell
def header(mo):
    mo.md(
        """
        # ♪ Music Generation Studio
        Full songs from a description or your own lyrics + Structured Caption —
        **MiniMax-Music3**, generated on the CoreWeave CUDA and logged to W&B.
        """
    )
    return


@app.cell
def device_controls(mo):
    device = mo.ui.radio(
        options=["CUDA (recommended)", "MPS (experimental)"],
        value="CUDA (recommended)",
        label="**Where should the model run?**",
    )
    refresh = mo.ui.run_button(label="↻ Re-check cluster")
    return device, refresh


@app.cell
def cluster_panel(SBATCH_CMD, applog, cluster_status, device, mo, refresh, session_id):
    use_cluster = device.value.startswith("CUDA")
    alloc = cluster_status() if use_cluster else None
    applog.info(
        "[%s] cluster_panel run: refresh_clicked=%s device=%s alloc=%s",
        session_id, refresh.value, "cuda" if use_cluster else "mps", alloc,
    )
    if use_cluster:
        if alloc:
            cluster_note = mo.callout(
                mo.md(f"✅ Cluster allocation **{alloc['jobid']}** is running — ready to generate."),
                kind="success",
            )
        else:
            cluster_note = mo.callout(
                mo.md(
                    "⚠️ **The cluster allocation is NOT running — and this app never starts it.**\n\n"
                    "Provision it yourself, then click *Re-check cluster*:\n\n"
                    f"```bash\nssh coreweave-login\n{SBATCH_CMD}\n```\n\n"
                    "When you're done for the day, release it with `scancel <JOBID>`."
                ),
                kind="danger",
            )
    else:
        cluster_note = mo.callout(
            mo.md(
                "🧪 **MPS mode is experimental.** Needs ≥32 GB unified memory (~23 GB of "
                "weights), runs 5–20× slower than the H100, may hit unsupported operators, "
                "and downloads ~57 GB on first use."
            ),
            kind="warn",
        )
    ready = (not use_cluster) or (alloc is not None)
    return cluster_note, ready, use_cluster


@app.cell
def settings(mo):
    duration = mo.ui.slider(5, 360, value=60, step=5, label="Maximum song duration (seconds)")
    steps = mo.ui.slider(4, 60, value=30, step=1, label="Flow-matching steps per chunk")
    seed_input = mo.ui.number(value=42, start=0, stop=2**31 - 1, label="Seed")
    randomize_seed = mo.ui.checkbox(value=True, label="Randomize seed")
    settings_panel = mo.accordion(
        {
            "⚙️ Settings": mo.vstack(
                [
                    duration, steps, mo.hstack([seed_input, randomize_seed], justify="start"),
                    mo.md(
                        "*Guidance and streaming playback from the official Space don't apply "
                        "to this backend — the pipeline is guidance-internal and audio arrives "
                        "when generation completes.*"
                    ),
                ]
            )
        }
    )
    return duration, randomize_seed, seed_input, settings_panel, steps


@app.cell
def simple_elements(get_desc, mo, set_desc):
    description = mo.ui.text_area(
        value=get_desc(),
        placeholder="Describe your song…  e.g. a smoky late-night soul ballad about old flames, warm female voice",
        rows=4,
        full_width=True,
    )
    _ideas = [
        "a smoky late-night soul ballad about old flames, warm female voice",
        "a sun-drenched surf-rock song about skipping work to drive to the coast",
        "an upbeat funk track about the first coffee of the morning",
    ]
    idea_chip_1 = mo.ui.button(label=f"💡 {_ideas[0][:44]}…", on_click=lambda _, i=_ideas[0]: set_desc(i))
    idea_chip_2 = mo.ui.button(label=f"💡 {_ideas[1][:44]}…", on_click=lambda _, i=_ideas[1]: set_desc(i))
    idea_chip_3 = mo.ui.button(label=f"💡 {_ideas[2][:44]}…", on_click=lambda _, i=_ideas[2]: set_desc(i))
    instrumental = mo.ui.checkbox(value=False, label="Instrumental")
    # Counter buttons (not run_buttons): each click increments; the handling
    # cells dedup on the count, so reactive re-runs can never re-dispatch.
    write_review_btn = mo.ui.button(label="✎ Write lyrics & review", value=0, on_click=lambda v: v + 1)
    simple_generate_btn = mo.ui.button(label="♪  Generate", value=0, on_click=lambda v: v + 1, kind="success")
    return (
        description, idea_chip_1, idea_chip_2, idea_chip_3, instrumental,
        simple_generate_btn, write_review_btn,
    )


@app.cell
def studio_elements(PRESETS, get_fields, mo, set_fields):
    _f = get_fields()

    def _insert_tag(tag):
        set_fields(lambda f: {**f, "lyrics": (f["lyrics"].rstrip() + f"\n\n[{tag}]\n").lstrip()})

    def _load_preset(name):
        set_fields(dict(PRESETS[name]))

    title_input = mo.ui.text(value=_f["title"], placeholder="Untitled — used for the file name and W&B caption", label="Title", full_width=True)
    lyrics_area = mo.ui.text_area(value=_f["lyrics"], rows=11, full_width=True,
                                  placeholder="[Verse]\nYour words here, one sung line per row…",
                                  label="Lyrics")
    tag_buttons = mo.ui.array(
        [mo.ui.button(label=f"[{t}]", on_click=lambda _, t=t: _insert_tag(t))
         for t in ("intro", "verse", "pre-chorus", "chorus", "post-chorus", "bridge", "instrumental", "solo", "outro")]
    )
    global_meta_area = mo.ui.text_area(value=_f["global_meta"], rows=4, full_width=True,
                                       label="Global metadata — genre · BPM · key & scale · mood arc · scenario · production")
    vocal_details_area = mo.ui.text_area(value=_f["vocal_details"], rows=3, full_width=True,
                                         label="Vocal details — gender · timbre · style per section · harmonies · effects")
    arrangement_area = mo.ui.text_area(value=_f["arrangement"], rows=4, full_width=True,
                                       label="Arrangement — instruments per section · groove · bass · textures · spatial fx")
    assist_input = mo.ui.text(placeholder="Describe lyrics to write for you…  e.g. nostalgic road-trip song, punchy one-line chorus", full_width=True)
    assist_btn = mo.ui.button(label="✎ Write for me", value=0, on_click=lambda v: v + 1)
    preset_buttons = mo.ui.array(
        [mo.ui.button(label=f"🎵 {name}", on_click=lambda _, n=name: _load_preset(n)) for name in PRESETS]
    )
    studio_generate_btn = mo.ui.button(label="♪  Generate", value=0, on_click=lambda v: v + 1, kind="success")
    return (
        arrangement_area, assist_btn, assist_input, global_meta_area,
        lyrics_area, preset_buttons, studio_generate_btn, tag_buttons,
        title_input, vocal_details_area,
    )


@app.cell
def layout(
    arrangement_area, assist_btn, assist_input, cluster_note, description,
    device, global_meta_area, idea_chip_1, idea_chip_2, idea_chip_3,
    instrumental, lyrics_area, mo, preset_buttons, refresh, settings_panel,
    simple_generate_btn, studio_generate_btn, tag_buttons, title_input,
    vocal_details_area, write_review_btn,
):
    _simple = mo.vstack(
        [
            description,
            mo.hstack([idea_chip_1, idea_chip_2, idea_chip_3], justify="start", wrap=True),
            mo.hstack([instrumental, write_review_btn, simple_generate_btn], justify="start"),
            mo.md("*Write lyrics & review composes the song and opens it in Studio for editing; "
                  "Generate composes and renders in one go.*"),
        ]
    )
    _studio = mo.vstack(
        [
            mo.hstack(list(preset_buttons), justify="start", wrap=True),
            title_input,
            lyrics_area,
            mo.hstack(list(tag_buttons), justify="start", wrap=True),
            mo.md("*Section tags sit alone on their own line — words on a tag line are dropped. "
                  "Musical directions (tempo, instruments, dynamics) belong in Arrangement, never in the lyrics.*"),
            mo.hstack([assist_input, assist_btn], justify="start", widths=[5, 1]),
            global_meta_area,
            vocal_details_area,
            arrangement_area,
            studio_generate_btn,
        ]
    )
    mode_tabs = mo.ui.tabs({"✨ Simple": _simple, "🎛 Studio": _studio})
    _page = mo.vstack([device, refresh, cluster_note, mode_tabs, settings_panel])
    _page
    return (mode_tabs,)


@app.cell
def compose_actions(
    applog, assist_btn, assist_input, compose_song, description, duration,
    get_compose_handled, instrumental, mo, session_id, set_compose_handled,
    set_fields, set_notice, write_lyrics, write_review_btn,
):
    # Dedup guard: only a click count HIGHER than the last handled one is a new
    # click. Recreated widgets reset their counters to 0; recording the current
    # counts unconditionally re-bases without dispatching. Record BEFORE work
    # so any reactive re-run of this cell sees the click as already handled.
    _h = get_compose_handled()
    _new_review = write_review_btn.value > _h["write_review"]
    _new_assist = assist_btn.value > _h["assist"]
    applog.info(
        "[%s] compose_actions run: write_review=%s/%s assist=%s/%s",
        session_id, write_review_btn.value, _h["write_review"], assist_btn.value, _h["assist"],
    )
    if (_h["write_review"], _h["assist"]) != (write_review_btn.value, assist_btn.value):
        set_compose_handled({"write_review": write_review_btn.value, "assist": assist_btn.value})

    if _new_review:
        if not description.value.strip():
            set_notice("Describe your song first.")
        else:
            with mo.status.spinner(title="Composing with Kimi K2.6…", subtitle="writing lyrics and caption"):
                _c = compose_song(description.value, duration=duration.value, instrumental=instrumental.value)
            set_fields({"title": _c["title"], "lyrics": _c["lyrics"], "global_meta": _c["global_metadata"],
                        "vocal_details": _c["vocal_details"], "arrangement": _c["arrangement"]})
            set_notice(f"Composed **{_c['title']}** — review it in the Studio tab, then Generate.")
    if _new_assist and assist_input.value.strip():
        with mo.status.spinner(title="Writing lyrics with Kimi K2.6…"):
            _l = write_lyrics(assist_input.value, duration=duration.value)
        set_fields(lambda f: {**f, "title": _l["title"], "lyrics": _l["lyrics"]})
        set_notice(f"Lyrics written: **{_l['title']}** — edit freely, then Generate.")
    return


@app.cell
def generation(
    applog, arrangement_area, compose_song, description, duration,
    get_gen_handled, global_meta_area, instrumental, lyrics_area, mo, random,
    randomize_seed, ready, run_cluster, run_mps, seed_input, session_id,
    set_gen_handled, set_notice, set_result, simple_generate_btn, slugify,
    steps, studio_generate_btn, title_input, use_cluster, validate_lyrics,
    vocal_details_area,
):
    # Dedup guard (runaway-loop fix): a click count HIGHER than the recorded
    # one is a new click; anything else — including reactive re-runs and
    # counter resets from widget recreation — is a no-op. Counts are recorded
    # BEFORE any work so re-runs of this cell can never re-dispatch.
    _h = get_gen_handled()
    _new_simple = simple_generate_btn.value > _h["simple"]
    _new_studio = studio_generate_btn.value > _h["studio"]
    applog.info(
        "[%s] generation cell run: simple=%s/%s studio=%s/%s ready=%s backend=%s",
        session_id, simple_generate_btn.value, _h["simple"],
        studio_generate_btn.value, _h["studio"], ready,
        "cuda" if use_cluster else "mps",
    )
    if (_h["simple"], _h["studio"]) != (simple_generate_btn.value, studio_generate_btn.value):
        set_gen_handled({"simple": simple_generate_btn.value, "studio": studio_generate_btn.value})
    mo.stop(not (_new_simple or _new_studio))
    mo.stop(not ready, mo.md("**Cannot generate:** fix the execution panel above first."))

    if _new_simple:
        with mo.status.spinner(title="Composing with Kimi K2.6…", subtitle="writing lyrics and caption"):
            _c = compose_song(description.value or "an uplifting pop song", duration=duration.value,
                              instrumental=instrumental.value)
        _title, _lyrics = _c["title"], _c["lyrics"]
        _caption = (f"Global Metadata\n{_c['global_metadata']}\n\n"
                    f"Vocal Details\n{_c['vocal_details']}\n\nArrangement\n{_c['arrangement']}")
        # NOTE deliberately no set_fields() here: writing state from this cell
        # recreates the Studio widgets this cell depends on, which re-runs this
        # cell — the self-loop behind the runaway bug. Studio population is
        # "Write lyrics & review"'s job.
    else:
        _title = title_input.value.strip() or "Untitled"
        _lyrics = lyrics_area.value.strip() or "[Instrumental]"
        _caption = (f"Global Metadata\n{global_meta_area.value.strip()}\n\n"
                    f"Vocal Details\n{vocal_details_area.value.strip()}\n\n"
                    f"Arrangement\n{arrangement_area.value.strip()}")

    _seed = random.randint(0, 2**31 - 1) if randomize_seed.value else int(seed_input.value)
    _warnings = validate_lyrics(_lyrics)
    _runner = run_cluster if use_cluster else run_mps
    applog.info(
        "[%s] DISPATCH title=%r slug=%s seed=%s duration=%s steps=%s mode=%s",
        session_id, _title, slugify(_title), _seed, duration.value, steps.value,
        "simple" if _new_simple else "studio",
    )

    with mo.status.spinner(
        title=f"Generating “{_title}” — this takes a while, please wait…",
        subtitle="≈2 min per 60 s of song on the cluster (much longer on MPS). Leave this tab open.",
    ) as _sp:
        _res = _runner(
            prompt=_caption, lyrics_text=_lyrics, title_slug=slugify(_title),
            duration=duration.value, seed=_seed, steps=steps.value,
            on_status=lambda s: _sp.update(subtitle=f"{s}  ·  ≈2 min per 60 s of song — leave this tab open"),
        )
    _res.update({"title": _title, "seed": _seed, "warnings": _warnings})
    set_result(_res)
    set_notice("")
    return


@app.cell
def output(get_notice, get_result, mo, os):
    _res = get_result()
    _notice = mo.md(get_notice()) if get_notice() else None
    if _res is None:
        _out = _notice or mo.md("")
    elif not _res.get("ok"):
        _out = mo.vstack([
            mo.callout(mo.md(f"❌ **Generation failed.** {_res.get('error','')}"), kind="danger"),
            mo.accordion({"Log tail": mo.md(f"```\n{_res.get('log_tail','')[-2000:]}\n```")}),
        ])
    else:
        import soundfile as _sf
        _info = _sf.info(_res["wav_path"])
        _stats = (f"**{_res['title']}** · seed {_res['seed']} · {_info.duration:.0f} s of audio · "
                  f"generated in {_res['wall_seconds']} s")
        if _res.get("run_url"):
            _stats += f" · [view on W&B]({_res['run_url']})"
        _rows = [mo.md(f"### ♫ Your song\n{_stats}"), mo.audio(src=_res["wav_path"])]
        for _w in _res.get("warnings", []):
            _rows.append(mo.callout(mo.md(f"⚠ {_w}"), kind="warn"))
        with open(_res["wav_path"], "rb") as _fh:
            _rows.append(mo.download(data=_fh.read(), filename=os.path.basename(_res["wav_path"]), label="Download WAV"))
        _out = mo.vstack(_rows)
    _out
    return


if __name__ == "__main__":
    app.run()

# MiniMax-Music3 Demo Prompt Library

All 61 tracks from the official demo page ([https://minimax-ai.github.io/music3-demo/](https://minimax-ai.github.io/music3-demo/)), with their exact inputs, grouped by genre. Extracted 2026-08-19 by `scripts/extract_demo_prompts.py` — re-run it to refresh.

The demo page presents each track as showcasing one strength of the model: 26 for vocals, 26 for arrangement/instrumentation, 9 for Chinese regional genres (Zhongguofeng, Gufeng Pop, Folk). Each entry notes its showcase section.

These are MiniMax-authored, known-good worked examples of the Structured Caption format (see [`minimax_music_prompt_guide.md`](minimax_music_prompt_guide.md)). Each caption drops straight into `--prompt`, and each lyrics block into `--lyrics_file`, of `scripts/minimax_music3.py`.

## Contents

- [Pop](#pop) (8)
- [Rock](#rock) (8)
- [Blues](#blues) (7)
- [Funk](#funk) (7)
- [Country](#country) (5)
- [R&B](#rb) (5)
- [Bossa Nova](#bossa-nova) (4)
- [Jazz](#jazz) (3)
- [Metal](#metal) (3)
- [Dance Pop](#dance-pop) (2)
- [GuFeng](#gufeng) (2)
- [Soul](#soul) (2)
- [Urban](#urban) (2)
- [EDM](#edm) (1)
- [Folk](#folk) (1)
- [Hiphop](#hiphop) (1)

## Pop

### Features

*showcases: vocals · 3:11*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is Bb, and scale is major. Pop Rock / Soul.
Global Emotional Progression: The track initiates with a reflective, maternal intimacy, feeling small and close. As the narrative shifts from personal observation to shared experience, the arrangement swells with a supportive, mid-tempo rock energy. The bridge brings a poignant, nostalgic dip in energy that explores past insecurities before surging into a final, empowering anthem of self-worth, concluding with a warm, lingering reassurance.
Application Scenarios & Imagery: A heartfelt coming-of-age film montage, a late-afternoon kitchen conversation bathed in golden light, or a supportive playlist focused on body positivity and self-love.
Sonics & Production Profile: The soundstage is intimate but expands into a wide, cinematic stereo field during the choruses. It features a rich, analog-inspired frequency response with prominent low-mid warmth to ground the "mum" persona, and a high-end clarity that makes the vocal articulations feel breathe-on-the-neck close.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist delivers a seasoned, warm alto timbre that balances maternal authority with a soft, empathetic rasp. The texture is velvety and organic, reminiscent of classic soul icons but with a modern pop-rock precision.
Vocal Style: The delivery is conversational and back-phrased during the verses, leaning into the grid with a sense of gentle persuasion. The melodic contour features a signature hook motif centered around a descending minor third that feels like a comforting sigh. Key performance articulations include soft vocal fry on the lower register openings and graceful falsetto flips on the more emotional, high-reaching phrases. The phrasing is syncopated, mimicking natural speech patterns before locking into a steady, rhythmic cadence in the choruses.
Harmony/Backing Vocals: Lush, three-part soul-inspired harmonies enter during the second chorus and bridge. These are stacked with a wide stereo spread to create a "choir of support" effect, using creamy, ooh-and-aah textures to cushion the lead vocal.
Vocal FX: The verses utilize a tight "room" reverb for intimacy, which transitions into a lush, shimmering hall reverb during the larger sections. A subtle, warm saturation is applied to the mid-range to enhance the soul influence.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, fingerpicked electric guitar provides the primary harmonic foundation, utilizing a "glassy" tone with subtle chorus modulation. This is supported by a deep, melodic fretless bass that provides a rounded, fluid movement beneath the verses.
Secondary: A vintage Rhodes piano enters during the first pre-chorus, adding a soft, percussive harmonic layer. A distorted, overdriven rhythm guitar enters during the high-energy choruses to provide a wall of sound and rock grit. During the bridge, a delicate glockenspiel offers a high-register shimmering drone, representing the "inner sparkle" mentioned in the lyrics, while a soft cello provides a contrapuntal melody that mirrors the vocal’s lower register.
Groove & Foundation Progression: The track begins with a simple, ghost-note-heavy snare and kick pattern, emphasizing a "laid-back" soul pocket. As the track progresses, the drums expand into a full rock kit with a heavy, driving backbeat on the snare and eighth-note hi-hat pulses that propel the chorus. The bass guitar transitions from melodic slides to a more locked-in, rhythmic "walking" feel during the final anthem sections.
Embellishments, Textures & Spatial FX: Subtle shaker and tambourine layers are added in the second half to increase rhythmic density. Transitional elements include organic drum fills and a soft, rising synth swell that bridges the gap between the quiet verses and the powerful, soulful choruses. Natural room ambiance is preserved to give the listener the sense of being in the same space as the performers.
```

**Input lyrics:**

```
Your face is in the mail
You left it here
Forgot all about it
As you packed your gear
I know you don’t
Want to hear this
But
I really don’t think
You need it

You look in the mirror
You don’t like what you see

You can’t leave home
Without it
You’re beautiful
I’m telling you
But
You just don’t believe
Me anyway

You look in the mirror
You don’t like what you see

You just think I’m saying it
Because I’m your mum
But really
It’s a fact
You don’t need that
Make up
Love

You look in the mirror
don’t like what you see

In that way
You’re just like me
When I was so much younger
I didn’t like me either
So I just looked away
Couldn’t face a mirror
without a frown
Hated my own features
Couldn’t see a redeeming
Thing in there

I looked in the mirror
I didn’t like what I saw

So you’re just like your mother
Just like any other
Teenager out there
It’s all the same nowadays
Everybody wants to be
Perfect
Nobody feels they’re worth it
Everybody needs to see that
We can’t all be beauty models

We all look in that mirror
Nobody likes what they see

But

We are all beautiful
On the inside
Our hearts and souls
Are what we need to show
That essence within
Needs to be seen
True beauty shines within…
```

### In the Way

*showcases: vocals · 2:51*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 112. key is Eb, and scale is major. Pop Rock / Power Pop.
Global Emotional Progression: The track initiates with a reflective, nostalgic atmosphere that feels intimate and grounded. As it moves through the verses, there is a steady build of rhythmic anticipation, leading into a high-energy, cathartic chorus that feels both celebratory and bittersweet. The bridge pivots toward a more philosophical and airy sentiment, momentarily suspending the drive before the final chorus erupts in a definitive, high-velocity resolution that leaves the listener with a sense of closure.
Application Scenarios & Imagery: A cinematic transition showing characters moving through different life stages, a late-afternoon festival performance under a setting sun, or a high-definition montage of urban cityscapes and polaroid photographs.
Sonics & Production Profile: The production features a modern, wide-screen aesthetic with a heavy emphasis on the 200Hz punch and a shimmering 10kHz top-end. The soundstage is organized with a tight, centered rhythm section, while layers of guitars and synths are pushed to the extreme left and right to create a lush, immersive environment. The transients are sharp and defined, providing a crisp, commercial finish.

Vocal Details
Vocal Gender & Timbre: The lead vocalist is a female with a versatile mezzo-soprano range. Her timbre is naturally silky and clear in the lower register, developing a vibrant, resonant "chest-voice" belt in the higher reaches, characterized by a slight breathiness that adds a sense of vulnerability.
Vocal Style: The delivery is marked by a sophisticated rhythmic elasticity, frequently using back-phrasing behind the beat to mimic a conversational tone during the verses. The choruses feature a distinct hook motif involving a soaring octave leap on the key thematic phrases, followed by rapid, descending pentatonic flourishes. The performance utilizes subtle vocal fry at the start of phrases for emotional weight and transitions into a pure, vibrato-less head voice during the bridge to signify a shift in perspective.
Harmony/Backing Vocals: Lush three-part harmonies are introduced in the pre-chorus to build tension, expanding into a wall-of-sound arrangement in the chorus where the vocals are layered eight times to create a massive, choir-like texture. Subtle unison tracking is used in the second verse to thicken the lead melody.
Vocal FX: The lead vocal is treated with a short, bright room reverb to maintain intimacy, while a long, modulated shimmer reverb is automated specifically for the bridge. A synchronized quarter-note delay is used sparingly on phrase endings to trail off into the stereo field.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A crisp, fingerpicked acoustic guitar provides the initial harmonic structure, soon joined by a primary layer of clean, jangly electric guitars playing syncopated 16th-note rhythms. In the chorus, these evolve into thick, saturated rhythm guitars with a mid-forward grit that occupies the center-stage energy.
Secondary Layering: An ambient synthesizer pad provides a sustained harmonic wash in the background, entering during the intro to establish the tonal floor. A secondary electric guitar enters during the second verse, playing a high-register, delay-drenched counter-melody that interlocks with the vocal lines. During the chorus, a bright grand piano adds percussive staccato chords on the quarter notes to emphasize the pop-rock drive, while a subtle glockenspiel layer adds a crystalline shimmer to the top end of the frequency spectrum.
Groove & Foundation Progression: The foundation is built upon a distorted, melodic electric bass guitar that provides a driving, eighth-note pulse throughout the track. The percussion begins with a simplified kick and rimshot pattern, transitioning into a full, punchy snare-heavy groove with open hi-hats in the chorus. The kick drum is side-chained slightly to the bass to ensure a clean, modern low-end relationship that pushes the tempo forward without feeling cluttered.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by reverse cymbal swells that lead into the choruses and sub-bass drops that mark the downbeat of the bridge. Brief melodic guitar slides act as bridges between vocal phrases. The production uses localized white-noise sweeps and subtle filtered synth risers to heighten the transitions, ensuring the energy flow remains constant and engaging until the final sustained chord.
```

**Input lyrics:**

```
(Verse 1)
We were the kind who never stayed in one place,
Running through the city with the wind in our face.
Trading every secret like a currency of trust,
Didn’t know the moment when it started turning dust.

(Pre-Chorus)
I still scroll back just to see your name,
But the messages feel like another game.

(Chorus)
Forever friends – we promised it one day,
And we haven’t seen each other since the following day.
Guess forever’s quicker than we thought it’d be,
Faded like a sticker on a teenage diary.
Yeah, we said we’d never change… but life got in the way.

(Verse 2)
Now you’re a highlight in a story I outgrew,
A blurry little moment in a world that was new.
Funny how the rhythm doesn’t hit the same beat,
When the people that you dance with walk off down another street.

(Pre-Chorus)
I could call you up, but what would I say?
“Hey, remember us?”—it feels too far away.

(Chorus)
Forever friends – we promised it one day,
And we haven’t seen each other since the following day.
Guess forever’s quicker than we thought it’d be,
Faded like a sticker on a teenage diary.
Yeah, we said we’d never change… but life got in the way.

(Bridge)
Maybe we just ran out of the same headline,
And maybe that’s okay — stories shift over time.
Still I hope you’re smiling somewhere out there tonight,
Living loud, living free, living your own life.

(Final Chorus)
Forever friends – we promised it one day,
And we haven’t seen each other since the following day.
But the beat keeps moving and I’ll be okay,
Even if our forever only lasted one day.
```

### Regret

*showcases: vocals · 3:47*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 84. key is F#, and scale is minor. R&B / Pop Rock.
Global Emotional Progression: The track initiates with a somber, reflective atmosphere characterized by regret and domestic intimacy. As the transition moves into the first chorus, the emotion pivots into a powerful, anthemic surge of self-realization and frustration. The second verse maintains this increased tension, leading into a final emotional climax where the bitterness of the lyrics is met with a high-energy, defiant resolution before settling into a lingering, hollow outro.
Application Scenarios & Imagery: A rain-streaked window in a modern apartment, a slow-motion walk through a crowded city street at dusk, or the cathartic moment of finally leaving a toxic environment behind.
Sonics & Production Profile: The production balances the warmth of R&B with the grit of pop-rock. It features a dense, layered mid-range and a tight, punchy low-end. The soundstage is wide, using stereo-spread guitars to contrast a centered, intimate vocal presence, creating a professional polished sheen with significant headroom for the climactic choruses.
Vocal Details
Vocal Gender & Timbre: A male vocalist provides a soulful and emotive performance. His timbre is characterized by a gritty, chest-heavy resonance in the lower register, which seamlessly transitions into a polished, slightly strained head voice to convey emotional peak. The texture is smooth but possesses a raw, vulnerable edge during the more accusatory passages.
Vocal Style: The performance follows a conversational back-phrasing approach in the verses, sitting slightly behind the beat to emphasize the storytelling aspect. A key hook motif involves an iconic rising 5th leap on the primary resolution of the chorus, followed by soulful pentatonic runs. The delivery utilizes vocal fry on the downward phrases of the verses and shifts to urgent staccato bursts during the more rhythmic sections of the second verse.
Harmony/Backing Vocals: Dense, gospel-influenced stack harmonies emerge in the choruses, providing a lush wall of sound. These consist of four-part harmonies that emphasize the root and fifth, while the bridge features ethereal, falsetto-laden oohs and aahs that float in the upper stereo field.
Vocal FX: The verses utilize a dry, close-mic proximity effect with a short room reverb to simulate intimacy. The choruses are treated with synchronized stereo delays and a shimmering hall reverb to expand the scale, alongside subtle saturation to help the vocal cut through the distorted bass and guitars.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering)
Primary: A clean, chorus-drenched electric guitar provides the primary harmonic framework, utilizing fingerpicked arpeggios that sustain throughout the verses. A distorted, overdriven bass guitar enters as the secondary primary element, providing a thick, fuzzy foundation that adds a rock edge to the R&B groove, specifically emphasizing the downbeats.
Secondary: An ambient synthesizer pad sits low in the mix during the intro to establish the mood. Upon entering the chorus, a second rhythm guitar with high-gain distortion is introduced, panned hard right to add width and harmonic density. A subtle Wurlitzer electric piano provides mid-range warmth during the second verse, playing syncopated chords that respond to the vocal melody.
Groove & Foundation Progression: The groove begins with a minimal, dampened kick drum and a crisp rimshot on the two and four. As the chorus hits, the foundation expands into a heavy, live-recorded drum kit sound with a deep, thudding kick and a cracking snare. The hi-hats move from closed eighth notes to open, splashing sixteenth-note patterns to drive the energy. The bass guitar transitions from simple root notes in the verses to a more melodic, sliding performance in the final chorus.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by reverse guitar swells that act as transitions between sections. A subtle sub-drop emphasizes the start of each chorus for physical impact. During the bridge, brief localized foley sounds of a distant ticking clock are heard, enhancing the theme of wasted time, while high-frequency synth bells add a shimmering, crystalline texture to the final outro fade.
```

**Input lyrics:**

```
[Verse]
I let you take me to a movie
I should've known it from the start
It's my mistake I gave you too much
It's my mistake I gave you too much
you always made a fuss
for me not listening to you
our late night phone calls were fake to you
your happiness with me was fake for you
you just used me as a tool

[Chorus]
If only I had walked away
If only I had walked away
half my life wouldn't have been wasted away
half of my life wouldn't have been wasted away
If only I had walked away
If only I had walked away
from the start
[Verse 2]
I should've never let you hold me
I should've never let you in
I should've never let you hold me
I should've never let you in
 you use to say you love me only
but it was a complete phony
all you wanted was my money

[Chorus]
If only I had walked away
If only I had walked away
half of my life wouldn't have been wasted away
half of my life wouldn't have been wasted away
If only I had walked away
If only I had walked away
from the start

you said you didn't love me for those two years
but I wish I didn't know you for all those regretful years
you no longer make me tearful
but now I feel bashful towards you
you should pray to your Lord
 for all those years of thief
of my love

If only I had walked away
If only I had walked away
half of my life wouldn't have been wasted away
half of my life wouldn't have been wasted away
If only I had walked away
If only I had walked away
from the start
```

### The Farmer

*showcases: arrangement / instrumentation · 4:05*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 162. key is Eb, and scale is minor. Baroque Pop / Emo Rock.
Global Emotional Progression: The track initiates with a stately yet mournful chamber-inspired opening, establishing a sense of disciplined gravity. This evolves into a rhythmic, driving verse that balances stoic resolve with the genre's signature melodic angst. The pre-chorus acts as a calculated ascent, tightening the harmonic tension before releasing into a grand, anthemic chorus that feels both regal and desperate. The bridge serves as the emotional breaking point, transitioning from claustrophobic intensity to a defiant, high-energy peak during the shouting breakdown, finally resolving into a massive, wall-of-sound orchestral rock finale.
Application Scenarios & Imagery: This composition evokes images of a rain-slicked cathedral at twilight, an intense training montage in a gothic architectural setting, or the climactic internal monologue of a protagonist facing an inevitable sacrifice. It suits high-stakes cinematic dramas or alt-rock playlists focused on theatricality and conviction.
Sonics & Production Profile: The soundstage is vast and vertically stacked, blending the organic, mid-forward resonance of orchestral strings with the aggressive, saturated transients of modern emo-rock. The frequency response is characterized by a "V-shape" with a piercingly clear high-end for the violins and cymbals, balanced by a thick, distorted low-mid presence. High-fidelity clarity ensures that even in the densest "wall of sound" moments, the harpsichord and vocal textures remain distinct.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a dramatic baritenor range with a "theatrical-emo" edge. The timbre is versatile, shifting from a dark, chesty resonance in the lower registers to a strained, emotive "cry" in the higher belt, characterized by a sharp, slightly nasal grit that cuts through the orchestral arrangement.
Vocal Style: The delivery is meticulously phrased with a mix of staccato, urgent rhythmic clusters and long, sweeping legato lines. The performance utilizes iconic rising minor 6th leaps during the transition to the chorus to evoke a sense of yearning. The phrasing is often conversational and slightly behind the beat in the verses, but snaps to a rigid, militant precision during the choruses. Performance articulations include sharp glottal stops, breathy phrase endings, and a wide, operatic vibrato that activates at the tail end of sustained notes.
Harmony/Backing Vocals: Dense, choir-like vocal stacks appear in the choruses, utilizing three-part harmony (root, minor third, and fifth) to create a liturgical, hallowed atmosphere. In the bridge, a secondary "shout" vocal layer is introduced to provide a raw, counter-rhythmic texture against the lead’s melodic lines.
Vocal FX: A sophisticated plate reverb provides a vintage hall aesthetic, while a synchronized slapback delay is used in the verses to enhance the rhythmic "emo" character. Parallel saturation is applied during the bridge and final chorus to add harmonic distortion, giving the voice a "breaking" quality under emotional duress.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: The primary harmonic foundation is a dark, staccato-heavy string quartet (two violins, viola, cello) paired with a rapid-fire harpsichord that provides a constant sixteenth-note ostinato. Distorted, mid-gain electric guitars enter as primary drivers during the choruses, utilizing thick power chords and palm-muted chugging to bridge the gap between baroque and pop-rock. 
Secondary Layering: A secondary layer of clean electric guitar with a bright, "twinkly" tone provides melodic counterpoint in the verses, dancing around the vocal melody with pentatonic flourishes. A pipe organ enters during the pre-chorus to thicken the low-mid frequencies and add a sense of impending doom. In the final "All in Chorus," a brass section (French horns and trumpets) provides a triumphant fanfare, acting as a melodic call-and-response to the vocal hooks.
Groove & Foundation Progression: The rhythmic foundation is anchored by a driving, high-tempo drum kit featuring a tight, "cracked" snare sound and prominent hi-hat work. The verse maintains a "four-on-the-floor" kick pattern that creates a sense of forward march. The bass guitar is highly distorted and clanky, mimicking the cello's rhythmic patterns to provide a unified, aggressive low end. During the breakdown, the melodic instruments drop out, leaving only a thunderous, tribal-influenced drum solo that builds into a massive half-time groove for the final chorus.
Embellishments, Textures & Spatial FX: Orchestral timpani hits mark the transitions between sections, providing cinematic weight. Subtle woodwind trills (flute and oboe) add a delicate, "classical" texture during the quieter pre-chorus moments. Reverse reverb swells on the harpsichord and occasional sub-frequency drops create modern impact points, while the spatial environment is defined by a large-room hall convolution that ties the rock and baroque elements into a single, cohesive space.
```

**Input lyrics:**

```
[Verse]
Accept your share of suffering
as a soldier of Jesus our King
Soldiers don’t aimlessly wander
They work to please their officer

Athletes in the competition
Don’t make up rules as their goin'
The farmer who works hard sowing
Should have first share of the reaping

[Pre-Chorus]
Think about what I am sayin'
God will give you understandin'

[Chorus]
Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves

Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves

[Verse]
Accept your share of suffering
as a soldier of Jesus our King
Soldiers don’t aimlessly wander
They work to please their officer

Athletes in the competition
Don’t make up rules as their goin'
The farmer who works hard sowing
Should have first share of the reaping

[Pre-Chorus]
Think about what I am sayin'
God will give you understandin'

[Chorus]
Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves

Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves

[Bridge]
The gospel truth of Jesus
The descendant of David
Who's died and resurrected
For which I am in chains

The gospel truth of Jesus
The descendant of David
Who's died and resurrected
It cannot be contained

They can put me in prison
BUT THE GOSPEL CAN'T BE CHAINED!

[Breakdown to drums-Chorus]
Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves

[All in Chorus]
Be strong in the grace of Jesus.
The sound teachings you have witnessed
Entrust to ones who will teach well
Not just look out for themselves
```

### 凌晨通话

*showcases: regional genres (Chinese) · 2:34*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 78. key is Db, and scale is major. Mandopop / Emotional Cinematic Ballad.
Global Emotional Progression: The track initiates with a fragile, solitary atmosphere, mirroring a late-night internal monologue. As the arrangement moves into the pre-chorus, a sense of tension builds through atmospheric layers, peaking in the chorus with a cinematic, sweeping release of pent-up emotion. The second verse introduces a steady rhythmic heartbeat, maintaining a higher energy state that culminates in a poignant, stripped-back bridge before the final chorus delivers a resolute, bittersweet conclusion.
Application Scenarios & Imagery: Perfectly suited for viral Douyin or TikTok sentimental montages, urban night drives under glowing streetlights, or cinematic breakup scenes. It evokes imagery of a smartphone screen illuminating a dark room, raindrops streaking across a windowpane, and the blue hues of a city just before dawn.
Sonics & Production Profile: The production features a modern, high-fidelity soundstage with a deep, focused low-end and a crystalline high-frequency shimmer. The mid-range is carved out to allow the vocals to sit front-and-center. Spatial processing is expansive, utilizing long-tail reverbs to create a sense of vast, lonely architectural space, while the transients are softened to maintain a lush, polished pop aesthetic.
Vocal Details
Vocal Gender & Timbre: A male vocalist with a light, contemporary tenor timbre. The voice is characterized by a "silk-and-air" texture, possessing a youthful yet weary quality that feels both intimate and relatable.
Vocal Style: The delivery is conversational and breathy in the opening, utilizing significant back-phrasing to create a natural, storytelling rhythm. The melodic contour features iconic rising minor-third leaps in the chorus to emphasize yearning. The performance includes delicate vocal fry on descending phrases and graceful falsetto flips at the end of the pre-chorus lines. The phrasing is agile, moving from rubato-like freedom in the verses to a more locked-in, rhythmic syncopation during the bridge to drive the emotional urgency.
Harmony/Backing Vocals: Lush, multi-tracked vocal stacks appear in the choruses, creating a "wall of sound" effect. These are processed with a wider stereo spread than the lead. During the bridge, a single tracked unison harmony provides a subtle reinforcement, while high-register oohs and aahs provide a bed of texture in the second verse.
Vocal FX: A combination of a short room reverb for intimacy and a large hall reverb for the cinematic sections. A rhythmic quarter-note ping-pong delay is used selectively on the final words of phrases to emphasize the "echo" of a memory.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Attributes: A high-fidelity felt piano acts as the primary harmonic foundation, characterized by muted hammers and a warm, woody resonance. It plays delicate, upper-register ostinatos in the verses, transitioning into powerful, wide-voiced chords in the lower octaves during the choruses.
Secondary Layering: A clean, ethereal electric guitar with a chorus-heavy modulation provides ambient swells and rhythmic accents. In the chorus, a secondary distorted rhythm guitar enters to provide grit and harmonic thickness, creating a pop-rock crossover feel. A cinematic string section, primarily cellos and violins, enters in the first chorus to provide soaring counter-melodies and legato textures that bridge the gaps between vocal lines.
Groove & Foundation Progression: The track begins with no percussion, relying on the piano's internal pulse. A sub-heavy, distorted bass enters in the first verse to provide a modern, moody grit beneath the clean instruments. The groove fully ignites in the first chorus with a hybrid kit featuring a deep, dampened kick drum and a crisp, electronic snare with a heavy reverb tail. The second verse maintains a steady eighth-note hi-hat pattern to keep the momentum forward-moving, while the bridge features a rhythmic breakdown where the drums drop out, leaving only a pulsing synth heartbeat.
Embellishments, Textures & Spatial FX: Ambient pads create a constant, low-pass filtered hum in the background, simulating the stillness of the night. White noise risers and reverse cymbal crashes act as transitions between sections. Sub-drops are utilized at the start of each chorus to ground the arrangement, and a subtle "telephone filter" effect is briefly applied to a piano motif in the intro to mirror the lyrical theme of a distant call.
```

**Input lyrics:**

```
Verse 1
凌晨两点的电话
突然亮起
你的名字
停在萤幕里

我看著来电
却没有接起
很多话
突然变得多余

Pre-Chorus
有些沉默
其实就是距离

Chorus
那是最后一通电话
你说晚安
声音轻得像雨
落在夜晚

那是最后一通电话
故事走散
很多还没说完的爱
停在那一晚

Verse 2
街灯慢慢熄灭
天快亮
很多回忆
突然很烫

我才明白
原来很多遗憾
不是不爱
只是走不到一样

Pre-Chorus
很多沉默
其实就是答案

Chorus
那是最后一通电话
你说晚安
声音轻得像雨
落在夜晚

那是最后一通电话
故事走散
很多还没说完的爱
停在那一晚

Bridge
如果那天
我再勇敢
故事会不会
换一个答案

Final Chorus
那是最后一通电话
世界很安
那些没有说出口的爱
留在那一晚
```

### 去吧，去闯

*showcases: regional genres (Chinese) · 4:03*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Db, and scale is major. Mandopop / Contemporary Ballad.
Global Emotional Progression: The track initiates with a solemn, grounded sense of nostalgia, establishing a safe domestic space. The narrative arc moves from quiet observation in the first verse to a swelling sense of parental pride and encouragement during the choruses. The bridge introduces a brief moment of poignant vulnerability and longing, representing the distance between home and the world, before culminating in an uplifting, empowering final chorus. The emotional journey concludes in a deeply intimate, whispered state of unconditional acceptance.
Application Scenarios & Imagery: This composition evokes the image of a dimly lit living room at dusk, a steaming bowl of soup on a wooden table, and the tactile sensation of a weathered hand resting on a shoulder. It is perfectly suited for high-end family dramas, documentary segments on migration and homecoming, or commemorative tributes to parental devotion.
Sonics & Production Profile: The production features a high-fidelity, organic soundstage with a pronounced mid-range warmth to accommodate the mature vocal registers. The frequency response is characterized by a rich, non-muddy low-mid section and a soft roll-off in the extreme high frequencies to avoid any digital harshness. The dynamic range is wide, capturing the subtle breath of the singers during the verses while allowing the light rock elements in the chorus to bloom with a controlled, cinematic density.

Vocal Details
Vocal Gender & Timbre: The arrangement features a female lead and a male harmony partner, both possessing mature timbres indicative of a 50-70 age range. The female vocalist has a wise, tender, and slightly breathy mezzo-soprano texture with a distinct Taiwanese accent, offering a "motherly" warmth. The male vocalist provides a stabilizing foundation with a weathered, gravelly baritone timbre that feels steady, supportive, and grounded, echoing the "fatherly" perspective.
Vocal Style: The delivery is conversational and narrative, utilizing back-phrasing to create a natural, non-mechanical flow. The female lead employs graceful falsetto flips on emotive peaks and a gentle vibrato that widens at the end of phrases. The male vocal stays largely in the lower register, utilizing vocal fry for texture and providing a steady rhythmic anchor. A notable hook motif involves a descending major third interval that mimics a sigh of relief, paired with pentatonic ornaments that reflect traditional Mandopop phrasing.
Harmony/Backing Vocals: The male voice provides supportive low-octave reinforcement and parallel thirds during the choruses, creating a sense of two voices becoming one unified front. In the bridge, the harmonies become more contrapuntal, acting as a call-and-response to the female lead before returning to a tight, homophonic blend for the final refrain.
Vocal FX: A vintage plate reverb is used to provide a sense of a shared physical room, while a short slap-back delay is applied to the male voice to enhance its textural grit. The female vocal is treated with a warm tube-preamp saturation to highlight the silkiness of her delivery, with gentle de-essing to maintain a soft, non-intrusive sibilance.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A grand piano serves as the primary harmonic engine, beginning with a simple, resonant chordal introduction and evolving into fluid, rolling arpeggios as the track gains momentum. A clean-toned electric guitar, reminiscent of 90s soft rock, enters in the first verse with liquid-like chorus effects, providing a shimmering melodic counterpoint to the piano.
Secondary: A lush string ensemble—consisting of sweeping cellos and soaring violins—enters during the transition to the chorus to provide a cinematic swell. In the second chorus, a second rhythm guitar with a light overdrive and a mid-heavy "crunch" is introduced to satisfy the light rock requirements, thickening the frequency spectrum without obscuring the vocals. A subtle accordion layer appears momentarily in the second verse to enhance the nostalgic, folk-adjacent quality of the Taiwanese-style arrangement.
Groove & Foundation Progression: The foundation begins as purely rubato with the piano. In the first chorus, a steady electric bass with a round, muted tone enters to provide a rhythmic heartbeat. By the second chorus, a drum kit with a warm, dampened snare and soft mallets on the cymbals establishes a slow, driving "heartbeat" groove. The intensity peaks in the final chorus with more traditional stick-on-snare patterns before the drums and bass completely drop out for the final acoustic section.
Embellishments, Textures & Spatial FX: Subtle atmospheric pads provide a continuous low-level bed of warmth. Gentle chimes and a soft glockenspiel accent the "uplifting" turns in the chorus melody. The track features a localized foley element of a distant, soft wind chime to signify the "home" environment. The arrangement concludes with a significant reduction in spatial processing, moving from a large hall reverb back to a dry, intimate room sound for the whispered outro.
```

**Input lyrics:**

```
[Verse 1]
孩子啊 当年送你上车的那天
妈妈的手抖得像秋天的叶
爸爸站在巷口 假装看远方
其实眼睛早已跟著你走远
老榕树下我们说过的话
你带著走 我们留在心里暖
别怕夜黑 别怕路长
家永远在这里 等你回头望
[Chorus]
故乡的风吹过又吹过
我们的心跟著你漂流
当年你挥手奔向远方
我们含泪微笑 说去吧去闯
亲情是暖流 流在你血里
但前途更宽广 世界等你去证明
开眼界 拓生命 才是我们最大的期许
孩子 我看你是最好的
[Verse 2]
电话里你说「还好」我们就知道
你在硬撑 我们心疼却不说破
城市再亮 也照不到你心里的孤
但记得妈煮的那碗汤的温度
朋友圈的恭喜我们都看见
却更想听你说一句「我想你」
删掉的讯息我们懂
下次别藏了 直接打来说
[Chorus]
故乡的风吹过又吹过
我们的心跟著你漂流
当年你挥手奔向远方
我们含泪微笑 说去吧去闯
亲情是暖流 流在你血里
但前途更宽广 世界等你去证明
开眼界 拓生命 才是我们最大的期许
孩子 我看你是最好的
[Bridge]
护照上的章是你的勋章
不是负担 是你长大的证明
跨过山河 海峡 我们不怕等
只怕你忘了 回家的路怎么走
有一天你累了 倦了
记得老街门牌还亮著灯
那条小河还在唱
唱给那个向远方跑的孩子听
[Chorus]（最后一次稍加强度）
故乡的风吹过又吹过
我们永远在你身后
你投降过生活 也赢过自己
我们骄傲 看你变得更坚强
亲情是暖流 永不冷却
但飞得更高 才是我们放手的理由
孩子 去吧 尽情去绽放
因为在我们眼里
你一直是最好的
[Outro]
（轻声、重复）
你一直是最好的…
爸妈等你回家…
```

### 大叫大晃

*showcases: regional genres (Chinese) · 3:35*

**Prompt (Structured Caption):**

```
[Global Metadata
Basic Attributes: bpm is 74. key is Db, and scale is minor. Contemporary Art Pop / Melancholic Ballad.
Global Emotional Progression: The track initiates with a fragile, fragmented atmosphere reflecting internal isolation and a sense of being overwhelmed. Moving into the first chorus, the emotional state shifts into a chaotic, destabilized outburst characterized by rising sonic pressure and a frantic search for escape. The second verse and bridge sustain a state of heavy, suffocating anxiety before the final transition into the outro, where the tension finally dissolves into a spiritual, meditative calm, signifying a release of burdens and the attainment of transcendent peace.
Application Scenarios & Imagery: Ideal for a cinematic sequence depicting a mental breakdown followed by spiritual recovery; a visual of a cluttered, dim room where the walls slowly recede to reveal a vast, starlit sky; high-end dramatic storytelling focused on psychological resilience.
Sonics & Production Profile: The soundstage begins narrow and intimate, expanding into a wide, overwhelming wall of sound during the peaks. High-frequency clarity is prioritized for the vocal breathiness, while the low-end is sculpted to feel heavy and immersive without masking the mid-range. The production aesthetic is polished yet raw, utilizing high-fidelity textures to contrast sharp, "stabbing" instrumental hits with soft, pillowy reverbs.

Vocal Details
Vocal Gender & Timbre: A solo female vocalist leads the performance, possessing a high-tenor-adjacent soprano range. Her timbre is exceptionally versatile, moving from a thin, brittle, and breathy texture in the verses to a powerful, resonant, and slightly strained chest voice during the high-intensity chorus sections.
Vocal Style: The delivery is marked by conversational back-phrasing and hesitant, staccato bursts that mimic the uncertainty of the lyrics. Significant melodic interest is generated through erratic, wide-interval leaps—specifically a recurring octave jump that signifies emotional instability. During the bridge, she employs a delicate falsetto with graceful, trembling vibrato. The rhythmic interaction is fluid, often pulling against the grid to create a sense of disorientation.
Harmony/Backing Vocals: Minimalist in the verses, the harmonies swell into dense, shimmering clusters in the chorus to simulate "voices in a room." The outro features angelic, layered "ooh" and "aah" textures that act as a celestial choir, providing a stark contrast to the earlier solo vulnerability.
Vocal FX: The primary vocal uses a "dry and close" EQ curve initially to create intimacy, transitioning into a lush cathedral reverb with a 4-second tail during the spiritual finale. Subtle pitch-shifting artifacts are applied in the chorus to underscore the theme of disorder.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, DI-processed electric guitar serves as the foundation, utilizing intricate fingerpicked arpeggios that feel cyclical and hypnotic. In the chorus, a secondary high-gain rhythm guitar enters with aggressive, sustained power chords to add harmonic weight. A distorted, saturated synth bass provides a low-frequency growl, acting as a primary melodic counterpoint that pulses with a dark, gritty texture.
Secondary: An ambient pad provides a constant, low-velocity wash of sound, appearing in the intro to establish a hollow spatial depth. During the second verse, a glockenspiel introduces high-register, "icy" melodic fragments that mirror the imagery of rising mist. In the bridge, a solo cello enters with a mournful, sweeping legato line, providing a mid-range warmth that bridges the gap between the low bass and high vocals.
Groove & Foundation Progression: The track begins without a traditional drum kit, relying on the rhythmic swaying of the guitar. A muffled, sub-heavy kick drum enters in the chorus, providing a steady but distant heartbeat. By the bridge, the percussion evolves into a complex, syncopated pattern using metallic "found sound" hits and wooden rimshots. The groove completely dissipates in the outro, leaving only the vocal and a soft, static-free synth drone to carry the final resolution.
Embellishments, Textures & Spatial FX: Subtle granular synthesis "glitches" occur during transitions to represent the "disorder" of language. Deep sub-drops emphasize the start of the chorus sections, while soft, localized foley of a heavy door closing marks the transition into the meditative outro. The track concludes with a series of shimmering, high-frequency harmonic swells that fade slowly into silence.
```

**Input lyrics:**

```
[主歌一]
身边好多话
好多不同的词语
有些轻轻飘过 有些却扎进来
像旧伤口被重新翻开

那些字眼 那些音节
承载著我不开心的记忆
突然间 情绪就涌上来
我不知道怎么办

[副歌]
我大哭 我大叫
整个世界摇摇晃晃
像失序的房间
东西一直掉 一直掉
我站在中间 不知所措
好想逃 却不知道往哪里逃

[主歌二]
同样的词语
在不同人口中 是不同的温度
我没有办法改变他们
也没有办法改变自己
听到就痛的这种反应

焦虑像雾 从地板升起
渗进每一次呼吸
我想抓住什么
但手伸出去 只抓到空气

[桥段]
能不能有一个地方
没有那些刺痛的词语
能不能有一刻安静
让我重新学会 只听见自己的心跳

[尾声]
我轻轻闭上眼
把那些话 放在房间外面
它们还在 我知道
但我可以在这里
和自己在一起
慢慢 慢慢
找回平静的空间
慢慢 慢慢
找回平静的空间
[Outro]
教我祷告 求天父怜悯
给予超越世界的平安
给予超越世界的平安
给予超越世界的平安
```

### 花开

*showcases: regional genres (Chinese) · 1:26*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 68. key is Eb, and scale is major. C-Pop / Melodic Ballad.
Global Emotional Progression: The track initiates with a poignant, minimalist atmosphere that evokes a sense of nostalgic longing. As the arrangement transitions into the secondary sections, the emotional weight shifts from internal reflection to an expansive, soaring yearning. The climax reaches a peak of bittersweet resolution before the instrumentation thins out, leaving the listener in a state of quiet, lingering melancholy that mirrors the opening’s solitude.
Application Scenarios & Imagery: This composition is perfectly suited for a high-budget romantic drama soundtrack, specifically during scenes of departure or moonlit reflection. Visual imagery involves ink-wash landscapes transitioning into modern city lights at rain-slicked windows, emphasizing the bridge between traditional sentiment and contemporary C-Pop production.
Sonics & Production Profile: The soundstage is wide and immersive, characterized by a pristine high-fidelity sheen. There is a deep, warm low-end provided by the bass to ground the emotionality, while the mid-range is carved out to allow the vocal to sit forward. High frequencies are crisp, capturing the delicate transients of piano hammers and the shimmer of orchestral accents.

Vocal Details
Vocal Gender & Timbre: Male Soloist. The vocalist features a smooth, velvet-toned tenor voice with a significant amount of "chest-voice" resonance in the lower register. There is an authentic, slightly raspy edge during moments of high emotional exertion, providing a realistic, non-mechanical human quality.
Vocal Style: The delivery is characterized by a conversational, back-phrased rhythmic approach in the opening, moving into a more urgent, syncopated phrasing during the build-ups. The hook motifs utilize iconic rising minor 3rd intervals that resolve into long, sustained vibrato notes. Distinct performance articulations include graceful falsetto flips at the end of poetic lines and a soft vocal fry in the lower-register verses to signify intimacy.
Harmony/Backing Vocals: Lush, multi-tracked vocal stacks appear in the later choruses to create a "wall of sound" effect. These are processed with a wide stereo spread, acting as a soft harmonic cushion that reinforces the lead melody's emotional peaks without introducing competing lyrical lines.
Vocal FX: A sophisticated chain of shimmer reverb and a synchronized quarter-note ping-pong delay is used to create a sense of vast space. During the most intimate moments, the reverb tail is shortened and the high-end air is boosted to enhance the "whisper" quality of the performance.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: The primary harmonic foundation is a concert grand piano, performing delicate, rubato-inflected arpeggios that establish the melodic theme from the very start. It evolves from a soft, felt-dampened timbre in the beginning to a bright, forceful staccato attack during the crescendo.
Secondary Layering: A warm, analog-style synth pad enters during the first transition to provide a subtle floor of frequency. By the midpoint, a soaring cello melody is introduced as a contrapuntal layer, engaging in a call-and-response with the vocal. Shimmering acoustic guitar strums are layered in the periphery to add high-frequency rhythmic pulse, while a traditional Erhu makes a brief, haunting appearance in the bridge to anchor the cultural aesthetic.
Groove & Foundation Progression: The foundation begins with a purely harmonic focus, devoid of percussion. A deep, cinematic sub-bass enters mid-way to provide gravitas. The rhythm eventually solidifies with a slow-burn groove featuring a dampened kick drum and a layered snare with heavy hall reverb. The bass guitar follows a melodic, walking pattern rather than staying purely rhythmic, adding a layer of sophisticated fusion to the ballad structure.
Embellishments, Textures & Spatial FX: Subtle crystalline bell hits are scattered throughout the high-register to simulate the falling of leaves or light. Reverse piano swells act as transitions between structural shifts, while a soft sub-drop marks the entrance of the final high-energy section. The arrangement concludes with the fading tail of a sustained string chord and the mechanical sound of a piano pedal releasing.
```

**Input lyrics:**

```
花开南去后，
东海几年别，

一路白云里，
长安春几回。

去去行人远，
此去莫蹉跎。

相思深夜后，
秋色共谁寻。

谁能平此恨，
黄叶几回看。

何事居人世，
对酒落花前。

溪云几万重。
万里独何之。

如今是别离。
对酒落花前。
```

## Rock

### Born In New

*showcases: arrangement / instrumentation · 1:58*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 132. key is E, and scale is major. Anthemic Pop Rock / Modern Stadium Rock.
Global Emotional Progression: The track begins with a sense of panoramic wonder and light-footed curiosity, establishing a buoyant atmosphere in the initial verses. As the narrative progresses toward the chorus, there is a distinct surge in adrenaline and sonic scale, mirroring the physical sensation of a freefall. The bridge provides a celestial, suspended-in-air quality that briefly thins the arrangement before a high-energy final chorus delivers a triumphant emotional payoff. The outro gradually grounds the listener with a warm, stabilizing resolution.
Application Scenarios & Imagery: This track is perfectly suited for high-definition aerial cinematography, extreme sports montages, or a climactic cinematic sequence involving flight or liberation. The imagery is dominated by vivid blues and golden hour sunlight reflecting off silk fabric, evoking a sense of limitless vertical space and the rush of cool air.
Sonics & Production Profile: The production is characterized by a "stadium-sized" soundstage with significant width and height. High frequencies are shimmering and polished to emphasize the airiness, while the low-mids are thick and driving. The dynamic range is expansive, utilizing side-chain compression on ambient layers to allow the kick drum and vocal transients to pierce through a dense, lush wall of sound during the high-energy peaks.

Vocal Details
Vocal Gender & Timbre: A female lead vocalist with a powerful, soaring mezzo-soprano range takes center stage. Her timbre is crystalline and pure in the upper register but possesses a resonant, chesty warmth in the lower verses, providing an authentic sense of confidence and awe.
Vocal Style: The delivery is marked by a conversational, breathy phrasing in the verses, often sitting slightly behind the beat to convey a sense of calm during the "dive." Transitioning into the chorus, the vocalist employs an iconic rising octave leap on the primary hook, followed by powerful, sustained belting. She utilizes graceful falsetto flips at the end of phrases in the bridge to simulate a weightless sensation. The melodic contour is primarily diatonic with occasional expressive pentatonic runs that emphasize the anthemic nature of the songwriting.
Harmony/Backing Vocals: Dense, "gang-vocal" style harmonies enter during the chorus to create a communal, celebratory feel. These are panned extremely wide. In the bridge, ethereal, three-part vocal pads are layered with a high-cut filter to create a ghostly, atmospheric texture that supports the lead's more intimate delivery.
Vocal FX: The lead vocal features a pristine hall reverb with a long decay time that is automated to increase during the chorus sections. A subtle 1/4 note ping-pong delay is used to fill the stereo gaps, while a touch of parallel saturation adds "harmonic heat" to the vocal during the most intense melodic peaks.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The harmonic foundation is led by a bright, rhythmic acoustic guitar playing driving eighth-note patterns. This is complemented by a duo of high-gain electric guitars that enter in the chorus, utilizing palm-muted chugging in the transitions and wide, sustained power chords during the main hook to provide a massive wall of sound.
Secondary: A shimmering polyphonic synthesizer provides a constant "shimmer" layer in the high-frequency domain, acting as a textural drone. During the second verse, a clean electric guitar with a chorus effect adds a counter-melody that interlocks with the vocal line. In the bridge, a piano enters with a soft, felted timbre, playing high-register arpeggios that mimic the twinkling of light against the clouds before the final rock instrumentation returns.
Groove & Foundation Progression: The groove is anchored by a punchy, modern rock drum kit. The verses utilize a driving "four-on-the-floor" kick pattern with a tight, snappy snare to maintain forward momentum. In the chorus, the percussion expands into a full-energy backbeat with heavy use of washier crash cymbals and thundering floor tom fills. The bass guitar is a distorted, high-output precision bass that provides a gritty, low-end growl, locking perfectly with the kick drum to drive the anthemic pulse.
Embellishments, Textures & Spatial FX: The track is punctuated by white noise sweeps and sub-drops that signal the transition into the chorus sections. Subtle foley of rushing air is layered extremely low in the mix during the verses to enhance the "sky" theme. High-pitched glockenspiel hits accentuate the downbeats of the chorus, adding a "magical" sparkle to the primary rock arrangement. In the outro, a gentle acoustic guitar strum fades out against a wash of ambient synth pads.
```

**Input lyrics:**

```
[Verse]
Up in the sky I feel alive
Wind in my hair feel the dive
Hold my breath I see the ground
Heart is racing no turning around

[Verse 2]
Jump into the blue without a fear
Clouds are whispering you’re near
Open wide let the colors show
Parachute flyin' high in the glow

[Chorus]
Falling free just you and me
Parachute spread like wings we see
Touch the earth we're born anew
In the sky I found the truth

[Bridge]
Weightless moments pure delight
Riding currents day and night
Just a canvas in the air
Painting dreams without a care

[Chorus]
Falling free just you and me
Parachute spread like wings we see
Touch the earth we're born anew
In the sky I found the truth

[Outro]
Safe landing coming in
Start again where dreams begin
Parachute my safety net
Sky’s the limit no regrets
```

### Brushes

*showcases: vocals · 1:53*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 154. key is E, and scale is major. Pop Funk / Pop Punk.
Global Emotional Progression: The track begins with a bright, inviting momentum that establishes a playful curiosity. During the verses, the mood is grounded and narrative, maintaining a rhythmic bounce that feels optimistic. As the song transitions into the choruses, the emotional intensity surges into a high-energy, anthemic celebration of creativity, characterized by a wall-of-sound production style. The bridge introduces a brief spiritual and reflective shift, grounding the track before the final climactic choruses and a high-spirited, definitive punk-style ending.
Application Scenarios & Imagery: This track is perfectly suited for high-energy montage sequences, daytime summer festivals, or coming-of-age film soundtracks. The music evokes imagery of sun-drenched art studios, vibrant splashes of paint across a canvas, and the feeling of unrestrained artistic freedom.
Sonics & Production Profile: The soundstage is wide and highly saturated, blending the punchy, midrange-forward grit of pop-punk with the clean, transient-heavy polish of modern funk. The low end is tight and aggressive, while the high frequencies shimmer with crisp percussion and bright guitar overtones. A modern, heavy compression is applied to the master bus to create a dense, radio-ready energy that feels physically impactful.

Vocal Details
Vocal Gender & Timbre: Singer A (Female). The vocalist features a powerful, clear mezzo-soprano timbre with a natural rasp that emerges during high-energy passages. Her tone is versatile, capable of shifting from a bright, pop-focused clarity to a gritty, punk-inspired edge.
Vocal Style: The performance utilizes a conversational, rhythmic delivery in the verses, featuring syncopated phrasing that sits slightly ahead of the beat to drive urgency. The choruses are defined by an iconic rising 5th leap on the opening motif, followed by fast, pentatonic runs that showcase technical agility. Performance articulations include expressive vocal fry on phrase beginnings and a rapid, tight vibrato on sustained notes during the anthemic peaks.
Harmony/Backing Vocals: Dense, three-part stack harmonies are introduced in the choruses to create a "gang vocal" effect characteristic of pop-punk, providing a massive melodic foundation. During the bridge, softer, ethereal unison layers provide a choral texture that contrasts with the main vocal's grit.
Vocal FX: The lead vocal is processed with a crisp slapback delay and a bright plate reverb to enhance its presence. Parallel distortion is subtly blended into the choruses to help the vocal cut through the dense guitar layers, while a high-pass filter is briefly applied during the bridge for a telephonic, intimate effect.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation is built upon a dual-guitar attack; a clean, percussive funk guitar provides rhythmic "scratch" chords and syncopated muted notes, while a heavily overdriven punk guitar enters during the choruses to provide thick, sustaining power chords. A distorted, growling electric bass follows the root notes with aggressive pick-attack, ensuring a heavy harmonic weight in the low-mid frequencies.
Secondary: A bright, polyphonic synthesizer pad provides an ambient wash during the intro, creating an atmospheric entry point before the groove kicks in. During the second verse, a secondary clean guitar adds melodic counter-lines using a chorus effect, while a third rhythmic electric guitar is panned hard right in the choruses to widen the stereo field and increase the harmonic density.
Groove & Foundation Progression: The track is driven by a classic punk-inflected drum kit, featuring a high-tuned, cracking snare and a punchy kick drum. The groove starts with a steady eighth-note hi-hat pattern in the intro, evolving into a driving "four-on-the-floor" feel with syncopated snare ghosts during the verses. The choruses shift into a double-time energy with smashing crash cymbals and busy kick drum patterns, while the instrumental section features a breakdown with heavy tom-tom rolls and rhythmic syncopation between the bass and snare.
Embellishments, Textures & Spatial FX: Transition points are marked by white noise sweeps and rapid snare rolls. Brief sub-drops accentuate the downbeats of each chorus, providing a sense of physical impact. The outro features a final, sustained guitar feedback trail and a sudden, dry percussive stop, leaving a sense of high-octane resolution.
```

**Input lyrics:**

```
[intro]

she paints in moving lines here and there,
she makes the brush dance like fred Astaire.
oh mixing colors in a fantasy world of her own,
she's a princess with a canvas for a throne.

since she was little she lit up in art class,
she didn't how long that love would last!
her stress got lost in a puddle of colors,
with sunshine gold mixed in raw umber.

[chorus]
She found her sun in glittered gold,
and found her heart in crimson rose,
she found her peace in green hues,
and found her calm in all the blues.

her paintings take her to places far away,
to the cabins, woods, waterfalls, and lakes.
she sees the vision in her mind and eyes,
she's a creator like her Father on High.

[chorus]
She found her sun in glittered gold,
and found her heart in crimson rose,
she found her peace in different hues,
and found her calm in all the blues.

Oh, Lord make sure that her brushes flow,
and make sure that Your Spirit shows
that she can believe on the Master Artisan,
to equip the gift that You put in her hands.

[instrumental]

[chorus]
She found her sun in glittered gold,
and found her heart in crimson rose,
she found her peace in different hues,
and found her calm in all the blues.

[chorus]
She found her sun in glittered gold,
and found her heart in crimson rose,
she found her peace in different hues,
and found her calm in all the blues.

[outro]
```

### It's In My Head

*showcases: vocals · 3:05*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 165. key is E, and scale is major. 2000s Pop Punk / Skate Punk.
Global Emotional Progression: The track opens with a surge of nostalgic adrenaline, establishing a high-energy foundation that carries through the melodic hooks. The verses shift into a narrative, slightly more subdued rhythmic pocket to allow for storytelling before exploding back into the anthemic choruses. This cycle builds a sense of youthful defiance and emotional clarity, culminating in a virtuosic instrumental peak during the solo, followed by a vulnerable, stripped-back resolution that emphasizes the core sentiment of the track.
Application Scenarios & Imagery: A late-summer backyard party under string lights, a montage of high school memories captured on grainy film, or the high-intensity climax of a coming-of-age movie soundtrack.
Sonics & Production Profile: The production features a classic TLA-style mix with a prominent, scooped mid-range and a crystalline high-end. The soundstage is wide, utilizing heavily double-tracked guitars panned wide to create a thick wall of sound. The low-end is tight and controlled, ensuring the kick drum and bass guitar punch through clearly without muddying the fast-paced transitions.
Vocal Details
Vocal Gender & Timbre: Male. The lead vocalist features a classic tenor range with a slight "bratty" nasal quality characteristic of the early 2000s era. The timbre is bright and resonant, possessing a natural rasp that emerges during higher-register belts and emotional peaks.
Vocal Style: The delivery is highly syncopated and conversational during the verses, utilizing a rapid-fire rhythmic flow that sits slightly ahead of the beat to create urgency. The choruses feature iconic rising 5th leaps and pentatonic melodic runs that serve as the primary earworm hooks. Articulations include subtle vocal fry at the start of phrases and expressive, shaky vibrato on sustained notes to convey a sense of earnestness.
Harmony/Backing Vocals: The choruses are reinforced by soaring two-part stack harmonies in the third and fifth intervals. During the later sections, "whoa-oh" style gang vocals provide a communal, anthemic texture, while the final section utilizes a raw, single-track dry vocal to maximize intimacy.
Vocal FX: The lead vocal is treated with parallel compression for consistent presence and a subtle slapback delay that adds depth without obscuring the lyrics. A plate reverb with a short decay is applied to the harmony stacks to blend them into the instrumental backing.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The core harmonic structure is driven by two high-gain electric guitars. One guitar maintains a steady rhythm of palm-muted downstrokes during the verses, while the other provides melodic counter-fills using bright, octaved lead lines. In the choruses, both guitars open up into ringing power chords with a slight chorused shimmer.
Secondary: A secondary clean electric guitar enters during the transitional periods, utilizing light overdrive and rhythmic chugging to bridge the dynamic gap. A bright, percussive piano layer is subtly tucked into the chorus mix to reinforce the melodic transients of the guitar work. During the instrumental solo section, a lead guitar takes center stage with fast legato runs, pinch harmonics, and expressive wide bends.
Groove & Foundation Progression: The rhythm is anchored by a high-tempo "punk beat" featuring a relentless eighth-note snare pulse on the backbeat. The kick drum follows a complex, syncopated pattern that locks with the driving, overdriven bass guitar. The bass provides a thick, growling foundation using a pick-style attack to ensure every note transition is sharp and audible. In the final section, all percussion drops out, leaving only the vocal presence to carry the rhythm.
Embellishments, Textures & Spatial FX: The track utilizes frequent pick slides and drum rolls to signal section changes. Short bursts of white noise sweeps and reverse cymbal swells are used to transition from the verses into the explosive choruses. The bridge features a brief spatial expansion where the instruments are treated with a wider stereo delay, creating a momentary sense of suspension before the final solo.
```

**Input lyrics:**

```
(Hook)
Don’t waste your time on me youre already
The only one who keeps me rock steady
And the voices in my head
All assure me that that’s what you said
You miss me.
And if fate fell short this time,
Then your fading smile keeps me whole for a while
The feeling of your hand in mine,
Is something that I never wanna,
Forget about that summer

[verse 1]
I was in the 9th grade when I fell in love for the first time
And her name? Well it never ended up as hers-mine
I loved her for 4 years of her time and when she spurned mine
I felt like Hamilton shot in the side after burrs lie
And I’m not saying I regret it, in fact I’m indebted without you how would I know what a true friend is, but
After a couple of beer flasks and years past a new true love did appear so a sincere task
Would be infatuation of the strongest and the strangest and i know it might sound lame but her name was my whole playlist and,
I wouldn’t change it for the world
The feeling of bliss when ya kiss curled up with your girl,
And then she went and broke my heart,
And I’m not saying that it’s hard but it’s hard to see each other apart,
Now I guess I finally understand,
What they meant when they said I should’ve ran

(Hook)
Don’t waste your time on me youre already
The only one who keeps me rock steady
And the voices in my head
All assure me that that’s what you said
You miss me.
And if fate fell short this time,
Then your fading smile keeps me whole for a while
The feeling of your hand in mine,
Is something that I never wanna,
Forget about that summer

[verse 2]
Now I’m not saying that there’s any affection that’s headed in your direction this is just a reflection
On the fact that I hated you, but lately I’ve been thinking maybe I was afraid of you,
But the fickle predicament of imprisonment was at the interlude we introduced a listing of differences,
Ya maybe we both could have changed,
Or it was just my fault for insinuating you were deranged
A few months apart and everyday is a present,
Hesitant of heartfelt cause the harpy harkened unpleasant,
But the truth is in the face of the fact that I’m laughing
I’m actually happy now I never thought that could happen
But lovin is free, and a few words could change a person,
And every single human on earth feels a range of hurtin,
The world is a clock and no one can stop it
Don’t waste time on a Love that’s proven toxic

(Hook)
Don’t waste your time on me youre already
The only one who keeps me rock steady
And the voices in my head
All assure me that that’s what you said
You miss me.
And if fate fell short this time,
Then your fading smile keeps me whole for a while
The feeling of your hand in mine,
Is something that I never wanna,
Forget about that summer

[guitar solo]

[hook, Accapella]
```

### Lipstick

*showcases: arrangement / instrumentation · 2:36*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 168. key is D, and scale is minor. Punk / Riot Grrrl.
Global Emotional Progression: The track opens with a gritty, confrontational energy that establishes a raw and rebellious atmosphere. The verses maintain a predatory, underground tension characterized by a driving rhythmic pulse. This builds into an explosive, celebratory release during the choruses, which project a sense of hard-won belonging and raw power. The bridge accelerates the physical intensity, peaking in a chaotic, high-heat frenzy before returning to a triumphant final anthem and a sudden, high-impact finish.
Application Scenarios & Imagery: A sweat-drenched underground basement club with flickering neon lights, high-speed night driving through urban industrial zones, or a cinematic montage depicting a subculture initiation.
Sonics & Production Profile: The production is deliberately raw and abrasive, featuring a mid-forward frequency response that highlights the jagged edges of the guitars. The soundstage is narrow and claustrophobic in the verses, widening significantly in the choruses through heavy double-tracking. High-frequency transients from the cymbals are sharp and unpolished, while the low-end is punchy but lean, ensuring a fast-reacting dynamic aesthetic.

Vocal Details
Vocal Gender & Timbre: Female lead vocalist. The timbre is characterized by a sneering, husky alto with significant natural grit and a defiant, street-wise edge. The texture shifts from a conspiratorial, breathy rasp to a powerful, full-chested belt.
Vocal Style: The delivery is conversational and urgent, utilizing syncopated back-phrasing that occasionally pushes ahead of the beat for a sense of recklessness. A distinctive hook motif is established in the chorus with a descending minor third interval that sounds like a playground taunt. Performance articulations include sharp glottal stops, occasional vocal fry on low notes, and aggressive staccato bursts during the bridge to emphasize the rhythmic drive.
Harmony/Backing Vocals: The choruses feature a secondary layer of female gang vocals, providing a raw, unrefined unison shout that adds to the "clan" aesthetic. These backing vocals utilize a call-and-response structure in the bridge, creating a chaotic, multi-voiced texture that mimics a crowded room.
Vocal FX: The lead vocal is processed with a subtle slapback delay and a vintage preamp saturation to emulate a megaphone or overdriven stage mic. The gang vocals are treated with a short, plate reverb to give them a sense of spatial depth within the mix.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: Two main electric guitars drive the harmonic structure. The first guitar utilizes a high-gain, "buzzsaw" distortion, playing rapid-fire down-stroked power chords. The second guitar provides textural contrast with jagged, discordant double-stops and occasional feedback squeals that punctuate the end of phrases.
Secondary: A third electric guitar enters during the choruses to provide a wall-of-sound effect, playing sustained open chords that fill the stereo field. A secondary melodic layer appears in the bridge, consisting of a sliding, single-note guitar line that mimics a siren, adding to the mounting tension.
Groove & Foundation Progression: The groove is anchored by a distorted, overdriven bass guitar that plays relentless eighth-note root lines, providing a thick melodic floor. The percussion is a classic punk D-beat, featuring a crashing open hi-hat and a snare that hits with high velocity. During the bridge, the drums shift to a floor-tom heavy tribal pattern, increasing the tempo and intensity before the final chorus explosion.
Embellishments, Textures & Spatial FX: The track incorporates localized mechanical textures, such as the sound of a heavy sliding door slamming shut as a transition into the bridge. Short bursts of pick slides and the metallic clatter of drumsticks hitting the rims are scattered throughout to maintain a live, visceral feel. The spatial arrangement uses sudden volume swells on the guitars to create a "pumping" effect, enhancing the song's aggressive kinetic energy.
```

**Input lyrics:**

```
[Verse 1]
Met them at a show
Lips against my ear
Said
"You wanna play with us?
Meet us in the rear"
Backseat audition
Fogging up the glass
Cherry gloss and leather
Boots and bare ass

[Chorus]
Now I'm in the band (in the band)
Dirty little secret with an all-girl clan
Got stamped
Got slammed
Got lipstick branded
Clemen on the ceilin'
Baby
Guess I made the standard
Yeah
I'm in the band
(oh, I'm in the band)

[Verse 2]
Late night hotel
Room service
Scratch marks on my thighs
She said
"Every fresh recruit
Gets tested in the lights"
Backstage on a flightcase
Crowd still screaming through the wall
Tongues like loaded weapons
Tunin' me up for curtain call

[Chorus]
Now I'm in the band (in the band)
Dirty little secret with an all-girl clan
Got stamped
Got slammed
Got lipstick branded
Clemen on the ceilin'
Baby
Guess I made the standard
Yeah
I'm in the band
(oh, I'm in the band)

[Bridge]
Van door slams
Shirts come off
Windows fog
As it gets hot
Set list stuck to someone's back
Straps and chains and fingernails black
They said
"You can quit if you can't stand"
I just laughed and grabbed a hand

[Chorus]
‘Cause I'm in the band (in the band)
Sticky stains in the back of our van
Got scraped
Got claimed
Got bite marks handed
Hot
Half-dressed in a gear-case canyon
Yeah
I'm in the band
Yeah
I'm in the band
(oh yeah, I'm in the band)
```

### Passion

*showcases: arrangement / instrumentation · 1:56*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 132. key is G, and scale is major. Pop Rock / Power Pop.
Global Emotional Progression: The track opens with an urgent, high-voltage energy that reflects a sense of immediate attraction and momentum. Through the verses, the arrangement maintains a driving, persistent pulse that mirrors the lyrical theme of an unstoppable force. The choruses act as emotional peaks, shifting from the tense build-up of the verses into a broad, anthemic declaration of desire. A dynamic shift occurs in the later sections where the instrumentation breathes slightly, allowing for a more intimate but still powerful resolution that finishes with a high-impact rhythmic stop.
Application Scenarios & Imagery: High-energy live concert openers, fast-paced romantic comedy montage sequences, or late-night drives through a city neon-scape. The sound evokes imagery of spinning lights and the rushing velocity of a summer storm.
Sonics & Production Profile: The production features a wide, modern soundstage with a heavy emphasis on the 200Hz to 500Hz range for warmth and punch. The high-end is crisp and polished, allowing for clear separation between the multiple guitar layers. The overall aesthetic is commercially slick, utilizing parallel compression on the drums to ensure a consistent, driving wall of sound that feels both large and intimate.

Vocal Details
Vocal Gender & Timbre: A male lead vocalist provides a versatile performance, characterized by a gritty yet melodic tenor timbre. The voice possesses a natural saturation that allows it to cut through the dense guitar arrangements while maintaining a warm, approachable core.
Vocal Style: The delivery is marked by urgent, syncopated phrasing that stays slightly ahead of the beat to convey excitement. The performance utilizes a signature hook motif featuring a rising major 6th interval on the key emotional phrases. Distinct articulations include expressive vocal fry on the lower-register verse beginnings and clean, powerful belt tones during the choruses. The rhythmic delivery shifts from rapid-fire staccato bursts in the verse to long, sustained legato notes in the hook sections.
Harmony/Backing Vocals: Dense three-part harmonies are deployed during the chorus sections to create a massive, wide vocal wall. These backing tracks use a slightly more breathy timbre to provide a textured contrast to the lead, often utilizing "oohs" and "aahs" in the background of the second verse to add harmonic depth.
Vocal FX: The lead vocal is processed with a synchronized 1/8th note delay that is most prominent in the verse transitions. A medium-sized hall reverb provides a sense of physical space, while a subtle exciter is used to enhance the "air" frequencies above 10kHz for a modern radio-ready finish.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A duo of electric guitars forms the core identity; one executes tight, palm-muted rhythmic chugging in the verses while the other provides melodic counter-fills. In the choruses, these evolve into wide-panned, heavily distorted power chords that occupy the full stereo width. A bright, percussive acoustic guitar is layered underneath to provide high-frequency transient detail and rhythmic definition.
Secondary Layering: A polished grand piano enters during the second verse, playing staccato chords that double the guitar rhythm to add weight. A subtle polyphonic synthesizer provides a shimmering pad texture in the background, surfacing most clearly during the transitions. During the chorus, an additional high-gain lead guitar adds melodic reinforcement to the vocal melody, acting as a call-and-response element.
Groove & Foundation Progression: The foundation is built on a heavy-hitting drum kit with a prominent, clicky kick drum and a fat, gated-reverb snare. The bass guitar is highly distorted, providing a growling low-end foundation that follows the kick drum pattern precisely. The groove evolves from a straightforward eighth-note drive in the first verse to a more complex, syncopated pattern with heavy crash cymbal accents in the chorus to maximize the perceived energy increase.
Embellishments, Textures & Spatial FX: Transition points are marked by white noise risers and reverse cymbal crashes to signal structural shifts. Occasional sub-bass drops are used at the start of each chorus to provide a physical impact. Short, blues-inspired guitar slides and palm-muted scratches serve as organic "ear candy" between vocal phrases, ensuring the arrangement remains dynamic and engaging.
```

**Input lyrics:**

```
I'm gunna hit you like
Like tornado's do
Fast and furious
I'll be all over you

You'll be spinning round and round
Like a ferris wheel
Wonderin' if it's real
This passion that you feel

(chorus)
Caus girl i'm wanting you i'm needing you
Want you for my own
Girl hang up that phone....aint nobody home
Yeah girl i'm wanting you i'm needing you
That's why i'm standin' here
Aint it clear...
I wanna make love to you.

I wanna make love
Wanna make love
Make love to you
Girl the whole night through
I wanna make love to you.

I wanna flood through you like a tidal wave
A tsunami of love
A sea of endless pleasures
From The Good Lord up above

(chorus)
Caus girl i'm wanting you i'm needing you
Want you for my own
Girl hang up that phone....aint nobody home
Yeah girl i'm wanting you i'm needing you
That's why i'm standin' here
Aint it clear...
I wanna make love to you.

I'm sure now
Have I made it clear
I wanna make love to you.
```

### Playground

*showcases: vocals · 2:55*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 164. key is E, and scale is major. Pop Punk / Skate Punk.
Global Emotional Progression: The track begins with an explosive, high-energy surge that establishes a sense of restless urban urgency. Throughout the verses, the mood is gritty yet optimistic, mirroring a fast-paced walk through a crowded city. The choruses act as anthemic emotional peaks, providing a sense of liberation and communal belonging. The bridge introduces a brief moment of introspective tension through shifting rhythmic patterns before cascading back into a final, triumphant outpouring of energy that concludes with a sharp, punchy finish.
Application Scenarios & Imagery: Fast-paced urban exploration, high-intensity sports highlights, or a montage of a chaotic but exhilarating day in a sprawling metropolis. The music evokes images of flickering subway lights, crowded sidewalks, and the neon glow of a city that refuses to sleep.
Sonics & Production Profile: The soundstage is wide and aggressive, featuring a "wall of sound" approach where distorted guitars dominate the mid-range. The production is polished yet retains a raw edge, with a prominent high-frequency sizzle on the cymbals and a punchy, mid-forward snare drum. The low-end is tightly controlled, ensuring the fast-moving bass lines remain articulate amidst the dense arrangement.
Vocal Details
Vocal Gender & Timbre: Male lead vocalist. The voice is a high-tenor with a bright, energetic rasp and a youthful, rebellious edge. The timbre is characterized by a "sneering" clarity that cuts through the distortion, becoming more resonant and chest-heavy during the melodic peaks.
Vocal Style: The delivery is urgent and conversational, utilizing syncopated back-phrasing that mimics the rhythm of city speech. The melodic contour features iconic rising 5th leaps at the start of the chorus to create a sense of aspiration. Rapid-fire staccato bursts dominate the verses, while the choruses utilize sustained anthemic notes with a slight vocal fry on the onset of phrases. Precise pentatonic runs are used as brief flourishes during the transition from the bridge back to the final chorus.
Harmony/Backing Vocals: Gang-style backing vocals are heavily utilized in the choruses to create a "neighborhood" feel, providing thick unison support on the key hooks. During the second verse and bridge, two-part harmonies provide a melodic counterpoint, adding a pop-sensibility to the punk foundation.
Vocal FX: The lead vocal is treated with parallel compression for consistent presence and a subtle slapback delay to enhance the rhythmic drive. A short, bright room reverb is applied to prevent the vocals from sounding too dry, while the backing vocals are processed with a wider stereo spread and a high-pass filter to sit above the lead.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: Twin electric guitars with high-gain distortion serve as the primary engine. They execute rapid down-stroked power chords and palm-muted rhythmic chugging during the verses. In the chorus, they transition to wide, ringing open chords to maximize the frequency spectrum.
Secondary Textural Layer: A lead electric guitar provides a bright, single-note counter-melody during the second verse and bridge, using a slightly cleaner "crunch" tone to contrast with the rhythm tracks. A secondary layer of "octave-chord" melodies enters during the second half of the choruses, creating a shimmering high-end lift. During the bridge, a brief, filtered synth pulse provides a subtle rhythmic bed beneath the guitars before being overtaken by a feedback swell leading into the final section.
Groove & Foundation Progression: The groove is anchored by an aggressive four-on-the-floor kick drum pattern during the high-energy transitions, moving into a classic punk "D-beat" during the verses. The bass guitar provides a relentless eighth-note foundation, featuring a grit-heavy tone with significant growl in the 800Hz range. The chorus expands the groove with heavy crash cymbal riding and syncopated snare rolls, while the bridge momentarily breaks into a half-time feel to build tension.
Embellishments, Textures & Spatial FX: The track is punctuated by rapid pick scrapes and occasional natural guitar feedback at the end of phrases. Short, white-noise risers and reverse cymbal crashes are used to signal the transition from verse to chorus. Spatial depth is enhanced by localized room-reverb splashes on the snare hits during the bridge, creating a momentary sense of a larger physical space before the mix tightens back up for the finale.
```

**Input lyrics:**

```
[Verse 1]
Got a cracked MetroCard
Sleeves full of wristbands
Fourth coffee
Noon sun
Eyes on the quick plans
Stoop kids arguing
Taxi doors slamming
If my brain starts to wander
This town starts planning

[Chorus]
New York is a playground for the restless
If you’re bored
It throws you in the deep end
Every corner
Something pulling at your head
Your hands
If you’ve got nothing to do
Come get lost in the avenues
New York is a playground for the restless
(and it never says when)

[Verse 2]
Half-price rush line
Sidewalk stage on Broadway
Busker with a busted amp
Still turns it to a runway
Rooftop on a Tuesday
Strangers trading stories
Miss my stop on purpose
Just to chase the noise

[Chorus]
New York is a playground for the restless
If you’re bored
It throws you in the deep end
Every corner
Something pulling at your head
Your hands
If you’ve got nothing to do
Come get lost in the avenues
New York is a playground for the restless
(and it never says when)

[Bridge]
Bowery to Bed–Stuy
I’m chasing the “next” sign
Every empty hour gets filled
By the skyline
Tell me who I’d be
In a quiet town somewhere else
I’ll answer later
There’s a train I gotta catch

[Chorus]
New York is a playground for the restless
If you’re bored
It throws you in the deep end
Every corner
Something pulling at your head
Your hands
If you’ve got nothing to do
Just let the city choose for you
New York is a playground for the restless
(and it never, never ends)
```

### Smile

*showcases: vocals · 2:52*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 164. key is D, and scale is major. Pop Punk / Skate Punk.
Global Emotional Progression: The track opens with a sense of adolescent anticipation that quickly erupts into a high-energy, chaotic surge. The verses maintain a playful, mischievous tension through staccato instrumentation, which then explodes into a wide, anthemic, and celebratory release during the choruses. A sudden, dramatic drop in tempo and intensity during the bridge creates a dreamy, suspended-in-time sensation before the final chorus delivers a high-octane, triumphant resolution that ends on a ringing, feedback-drenched guitar chord.
Application Scenarios & Imagery: This track is ideal for high-energy coming-of-age movie sequences, extreme sports highlights, or a frantic school cafeteria setting. It evokes visuals of bright fluorescent lights, flying debris, and the vibrant, messy rebellion of youth.
Sonics & Production Profile: The soundstage is wide and aggressive, featuring a "wall of sound" approach with multi-tracked guitars panned wide. The frequency response is characterized by a prominent mid-range bite and a crisp high-end that emphasizes pick attack and snare snap. The production is modern and polished, utilizing heavy compression to ensure a constant level of high-intensity energy and clarity despite the dense arrangement.
Vocal Details
Vocal Gender & Timbre: Male lead vocalist. The voice is a youthful, energetic tenor with a grit-laden, slightly raspy edge that suggests a "bratty" pop-punk aesthetic. The timbre is bright and forward-projecting, maintaining clarity even during high-velocity lyrical passages.
Vocal Style: The performance alternates between rapid-fire, rhythmic delivery in the verses and soaring, melodic belts in the choruses. The vocalist employs iconic rising 5th leaps at the start of the hook to create an earworm effect. Phrasing is often pushed slightly ahead of the beat to create a sense of frantic urgency, punctuated by vocal fry on stressed syllables and expressive, breathy tail-offs during the bridge.
Harmony/Backing Vocals: Dense, three-part vocal harmonies appear in the choruses, creating a lush, group-chant feel. "Hey!" shouts and gang-style backing vocals provide rhythmic punctuation at the end of specific verse lines, while the bridge features a soft, double-tracked unison vocal for a more intimate, vulnerable texture.
Vocal FX: The primary vocal is treated with a short slap-back delay and a bright plate reverb to enhance its presence. During the bridge, a low-pass filter and increased hall reverb are applied to create a "distant" and "spatial" effect, which is abruptly removed as the final chorus hits.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation consists of two high-gain electric guitars performing synchronized, palm-muted downstrokes in the verses, which transition into wide, ringing power chords during the choruses. A saturated, distorted bass guitar follows the root notes closely, providing a thick, percussive low-frequency anchor.
Secondary: A third electric guitar enters during the second verse, playing bright, syncopated octaves in the higher register to add melodic movement. In the bridge, the distorted layers drop away entirely, replaced by a clean, chorused electric guitar playing gentle, arpeggiated figures and a subtle, shimmering glockenspiel that provides a "bell-like" texture.
Groove & Foundation Progression: The groove is a classic, high-speed punk beat. The kick drum is relentless, performing a mix of steady eighth notes and rapid double-time bursts. The snare drum has a high-tuned, "cracking" timbre, consistently hitting on the 2 and 4 beats. During the choruses, the drummer shifts from a closed hi-hat to wide-open, shimmering crash cymbals to maximize the wall of sound. The bridge features a half-time feel with a deep, resonant floor tom pattern before building back to full speed via a rapid snare roll.
Embellishments, Textures & Spatial FX: The track is punctuated by rapid guitar slides and occasional pick scrapes that emphasize the transition between sections. Short, white-noise risers and reverse cymbal crashes are used to signal the arrival of each chorus. An ambient, synth-based "sparkle" texture is layered into the bridge to enhance the slow-motion aesthetic, while a sub-bass drop emphasizes the final downbeat of the song for a heavy, impactful finish.
```

**Input lyrics:**

```
[Verse 1]
Bell rings
Tray shakes
Mystery meat on a plastic plate
Somebody yells
“Food break!”
Spaghetti slips like a red wave

Ketchup packets
Locked and loaded (hey!)
Tater tots in a paper boat
One flick
Whole room explodes
Mashed clouds hanging in your coat

[Chorus]
It’s a food fight in the hallway
Lasagna on the ceiling tiles
You got gravy on your hoodie
I’m dodging pudding
Trying not to smile
We’re screaming like it’s Friday
Bananas sliding down the floor
Yeah
It’s chaos in the cafeteria
This is what detention’s for

[Verse 2]
Green peas
Shot like BBs
Ricochet off a letterman sleeve
Milk cartons
Pop like fireworks
White streaks running down the bleachers’ beams

Principal ducks
Behind the trophies (oh yeah)
Loudspeaker begging us to “freeze”
But french fries fly
Like paper planes
Writing our names in the steam

[Chorus]
It’s a food fight in the hallway
Cornbread stuck to the exit sign
You got salsa in your sneakers
Cherry jelly dripping down the blinds
We’re laughing like it’s summer
Nacho chips crashing to the floor
Yeah
It’s chaos in the cafeteria
This is what detention’s for

[Bridge]
Slow motion
Macaroni orbiting your hair
Your eyes catch mine
Through a curtain of eclairs

We’re covered in chocolate
We’re covered in shame
But I kinda hope
We do it again

[Chorus]
It’s a food fight in the hallway
Apple pie sliding down the door
You got yogurt on your backpack
Whipped cream footprints on the floor
We’re breathing like we ran laps
Hearts racing as they mop the war
Yeah
It’s chaos in the cafeteria
This is what detention’s for
This is what detention’s for
```

### The Real Man

*showcases: vocals · 2:48*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 164. key is Gb, and scale is major. Y2K Punk Rock / Pop-Punk.
Global Emotional Progression: The track begins with an immersive, atmospheric opening that quickly shifts into a punchy, angst-ridden momentum during the first verse. There is a sense of desperate yearning that builds through the pre-chorus, culminating in a cathartic, high-energy explosion of sound in the chorus. This cycle of intimate vulnerability and outward sonic aggression repeats, eventually tapering into a resonant, lingering finish that emphasizes the emotional weight of the final plea.
Application Scenarios & Imagery: Cinematic coming-of-age montages, high-energy skate park sessions, or a rainy drive through a suburban neon landscape. The music evokes the aesthetic of grainy 35mm film, messy bedrooms with posters on the walls, and the intense, unfiltered emotions of early adulthood.
Sonics & Production Profile: The soundstage is wide and bright, featuring a polished yet aggressive high-end crispness characteristic of the early 2000s. The frequency response emphasizes a thick, saturated low-mid range to provide warmth to the guitars, while the drums are processed with a punchy, modern transient snap. The dynamic range shifts significantly between the sparse, airy verses and the densely layered, wall-of-sound choruses.
Vocal Details
Vocal Gender & Timbre: Male. The vocalist features a youthful, agile tenor voice with a signature "bratty" punk inflection and a slight rasp when pushing into the upper register.
Vocal Style: The delivery is conversational and breathy during the initial verses, utilizing back-phrasing to create a sense of personal storytelling. As the song progresses, the melody shifts into an iconic rising 5th leap at the start of the chorus to grab the listener’s attention. The phrasing becomes more urgent and staccato, incorporating expressive vocal fry on emphasized syllables and graceful falsetto flips at the end of emotional lines. The melodic contour is heavily rooted in major pentatonic scales with occasional chromatic passing notes to convey tension.
Harmony/Backing Vocals: Dense, three-part vocal harmonies appear in the choruses to create a lush, anthemic feel. During the second pre-chorus, a series of call-and-response backing tracks are layered behind the lead to build tension, using a slightly more nasal and filtered timbre.
Vocal FX: The vocals are treated with a short, plate reverb for space and a crisp "radio" EQ filter during the intro and first few bars of the verse. High-ratio compression is applied throughout to ensure the vocals sit prominently above the distorted instrumentation, complemented by a subtle doubling effect in the hooks.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation is built on high-gain electric guitars. In the opening sections, a single guitar plays clean, shimmering arpeggios with a light chorus effect. Upon entering the chorus, this evolves into a multi-tracked wall of heavily distorted rhythm guitars playing sustained power chords with aggressive down-strokes. The primary melodic interest is maintained by a lead guitar that interjects with octaves and bright, melodic counter-lines during the transitions.
Secondary: An ambient synthesizer pad provides a wash of texture during the intro, creating a wide stereo image. A second rhythm guitar is introduced specifically in the chorus sections to provide additional grit and stereo width. During the verses, a secondary clean guitar uses palm-muted staccato notes to provide a rhythmic counterpoint to the vocal melody.
Groove & Foundation Progression: The track is driven by a high-tempo punk drum kit featuring a sharp, ringing snare and a relentless eighth-note hi-hat pattern. The bass guitar is notably prominent, utilizing a distorted, overdriven tone that provides a clanky, metallic "pick-noise" texture, locking in with the kick drum for a driving foundation. The groove simplifies into a half-time feel during the pre-choruses to maximize the impact of the return to the fast-paced chorus beat.
Embellishments, Textures & Spatial FX: The intro features a subtle, low-pass filtered synth sweep that fades as the drums kick in. Short bursts of guitar feedback and pick slides act as transitional signals between the verse and chorus. A sub-drop is utilized on the first beat of the final chorus to provide a massive physical impact, while the outro utilizes a long, decaying reverb tail on a final guitar chord to fade into silence.
```

**Input lyrics:**

```
(intro)

(verse 1)
I was writing all my dreams down
Like this is me now
I don’t get how some people just leave
I want her to be real
But the only ones I see is on the reels
I speak in hyperboles
29 and single
Do you know how that feels?
This isn’t woe is me
It’s woah, just me...
Watch out...
This pen loves to bleed

(pre chorus)
When I pray it's for you
got the blues but got no clue
but I have to keep my cool

(chorus)
Fall on my knees
I need to see you
Don't say goodbye
before you say I love you
I was young and i was high
Don't judge on my past please
when I'm with you
I am the real me
Fall on my knees
I need to see you
Don't say goodbye
before you say I love you
I was young and i was high
Don't judge on my past please
when I'm with you
I am the real me

(pre chours)
When I pray it's for you
When I pray it's for you
When I pray it's for you
When I pray it's for you

(chorus, outro)
Fall on my knees
I need to see you
Don't say goodbye
before you say I love you
I was young and i was high
Don't judge on my past please
when I'm with you
I am the real me
```

## Blues

### California

*showcases: vocals · 4:48*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is G, and scale is minor. Country / Alt-Country Ballad.
Global Emotional Progression: The track initiates with a heavy, melancholic solitude, characterized by a stark and intimate atmosphere. As it transitions from the first verse into the chorus, the emotion shifts from internal sorrow to a weary, resolute frustration. The long instrumental break and subsequent guitar solo serve as a cathartic emotional peak, translating the longing for home into soaring melodic lines. The final verse returns to a resigned stillness before the last chorus provides a powerful, swelling conclusion that eventually dissipates into a lonely, fading finish.
Application Scenarios & Imagery: A late-night drive through a neon-lit city that feels foreign and cold, a solitary figure looking out a high-rise window at a sprawling metropolis, or a cinematic montage of someone packing a bag to leave a life that never quite fit.
Sonics & Production Profile: The soundstage is deep and atmospheric, utilizing a high degree of stereo width for the ambient elements while keeping the rhythmic core centered and grounded. The frequency response is characterized by a rich, woody low-mid range from the acoustic instruments and a polished, airy top end. The production emphasizes a "lived-in" feel with organic textures and a wide dynamic range that breathes between the sparse verses and the wall-of-sound choruses.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a rugged, weathered baritone with a palpable "ache" in the delivery. The timbre is gravelly yet vulnerable, exhibiting a natural breathiness that suggests exhaustion and sincerity. 
Vocal Style: The delivery is marked by a conversational, behind-the-beat phrasing in the verses, utilizing subtle vocal fry and breathy tail-offs to convey the weight of the narrative. A recurring hook motif is established through a soulful, descending minor third at the end of key phrases. In the choruses, the vocalist employs a powerful chest-voice projection with an expressive, wide vibrato on sustained notes. The bridge features a stylistic shift toward a more rhythmic, staccato delivery, creating a sense of urgency before returning to the melodic sweeps of the final sections.
Harmony/Backing Vocals: Background vocals are absent in the initial verse to emphasize isolation, but enter in the first chorus as low-register unison doubles. By the second chorus and bridge, stack-harmonized "oohs" and "aahs" provide a haunting, ethereal pad in the background. The final chorus features high, lonesome tenor harmonies that sit wide in the stereo field to create a sense of vast, open space.
Vocal FX: The verses utilize a close-proximity effect with minimal reverb to create an "in-the-ear" intimacy. The choruses transition into a lush hall reverb with a long decay and a subtle slapback delay, adding a sense of grandeur and distance that mirrors the lyrical themes of longing and far-off places.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation is built upon a somber, fingerpicked acoustic guitar that emphasizes the root and fifth of the minor chords, providing a rhythmic and harmonic pulse throughout the track. In the verses, a clean electric guitar with a slow tremolo effect enters to provide dark, sustaining chords that hang in the air. 
Secondary: A distorted electric bass enters during the verses, providing a gritty, low-frequency growl that contrasts with the clean guitars and symbolizes the "cage" mentioned in the description. An ambient synth pad provides a shimmering, high-frequency drone during the intro and transitions, creating a sense of cold, artificial light. During the chorus, a second rhythm guitar—a thick, overdriven Telecaster—is added to the mix, doubling the chord progression to provide a sudden increase in harmonic density and power.
Groove & Foundation Progression: The track begins without percussion, relying on the rubato feel of the acoustic guitar. A minimal drum kit enters in the first verse with a light, dampened snare hit on the four-count and a soft, pulsing kick drum. The groove expands significantly in the chorus, where the drummer moves to the wash of the ride cymbal and adds heavy, tom-heavy fills. The long instrumental break features a driving, steady rhythm that supports the melodic exploration of the guitar solo, while the final verse drops back to just the kick drum and acoustic guitar for a moment of stark contrast.
Embellishments, Textures & Spatial FX: A lap steel guitar provides weeping, glissando accents that weave through the stereo field, particularly during the instrumental break and the guitar solo. Sub-bass drops are used to punctuate the transition into the choruses, adding a modern cinematic weight to the arrangement. Brief, localized foley of a distant screen door creaking and the soft sound of rain on a tin roof are layered into the transition between the bridge and the solo to ground the track in its "hometown" imagery.
```

**Input lyrics:**

```
[Sad Intro]

[Verse 1]
They said the sunshine would set me free,
But it’s feeling more like a cage to me.
Crowded streets and skies so bright,
Still can’t chase away the night.

The mountains rise, but my heart sinks low,
This isn’t the place I thought I’d grow.
Dreams out here are hard to hold,
Too much glitter, not enough gold.

[Chorus]
I can’t stay here in California,
This life just don’t feel right.
The glitz and the glamor weigh me down,
I need the quiet of my hometown.
The West Coast breeze ain’t what I need,
I miss the stars and the open trees.
I can’t stay here in California,
It’ll never be home.

[Verse 2]
I’ve tried to love these coastal skies,
But they can’t compare to a Southern sunrise.
The air don’t smell like rain on pine,
And I can’t find peace in these endless lines.

Golden hills, they shine and glow,
But they don’t call me when the lights get low.
Too much noise, too little soul,
California just ain’t my goal.

[Chorus]
I can’t stay here in California,
This life just don’t feel right.
The glitz and the glamor weigh me down,
I need the quiet of my hometown.
The West Coast breeze ain’t what I need,
I miss the stars and the open trees.
I can’t stay here in California,
It’ll never be home.

[Long Instrumental Break]

[Bridge]
Give me a dirt road, a little creek,
The kind of quiet that lets me speak.
Trade this rush for a slower pace,
Somewhere I can find my place.

[Guitar Solo]

[Verse 3]
The ocean whispers, “Stay a while,”
But I can’t fake another smile.
These city lights don’t warm my heart,
It’s time for me to make a new start.

[Chorus]
I can’t stay here in California,
This life just don’t feel right.
The glitz and the glamor weigh me down,
I need the quiet of my hometown.
The West Coast breeze ain’t what I need,
I miss the stars and the open trees.
I can’t stay here in California,
It’ll never be home.
```

### Crossroad

*showcases: arrangement / instrumentation · 3:39*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 168. key is E, and scale is minor. Blues / Punk.
Global Emotional Progression: The track initiates with a raw, weary sentiment of rural isolation, quickly escalating into a high-velocity, nihilistic frenzy. The middle sections maintain a frantic, motoric energy that mirrors the desperation of the narrative, eventually peaking in a chaotic, distorted crescendo during the final confrontation at the crossroads, concluding with a sudden, unresolved silence that underscores the finality of the deal.
Application Scenarios & Imagery: A high-octane chase through a rain-slicked southern backroad, a dimly lit underground punk club with beer-soaked floors, or a modern noir film sequence depicting a character’s descent into a supernatural bargain.
Sonics & Production Profile: The soundstage is narrow and aggressive, characterized by a mid-forward saturation and high-gain grit. The frequency response is dominated by a biting upper-midrange from distorted guitars and a thumping, overdriven low-end, creating a claustrophobic yet powerful aesthetic that favors raw energy over polished clarity.
Vocal Details
Vocal Gender & Timbre: Male. The vocalist features a gravelly, weather-beaten tenor timbre that blends the soulful inflections of a Delta bluesman with the snarling, sneering delivery of 1970s street punk.
Vocal Style: The delivery is marked by a conversational, cynical back-phrasing that often pushes into urgent, staccato shouts. The melodic contour utilizes heavy blue-note flattening and chromatic passing notes, specifically employing a recurring hook motif involving a dissonant minor-second slide down to the tonic. Performance articulations include prominent vocal fry on sustained notes and jagged, breathless tail-offs that emphasize the frantic nature of the lyrics.
Harmony/Backing Vocals: Gang-style shouts and unison chanting appear in the latter half of the track to create a sense of mounting pressure. These are mixed with a wide stereo spread to surround the central lead vocal, sounding like a haunting, rowdy chorus of ghosts.
Vocal FX: The lead vocal is processed with a slapback delay that mimics a vintage tape echo, combined with a subtle megaphone-style EQ filter during the most intense passages to enhance the lo-fi, distorted punk aesthetic.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A heavily distorted electric guitar serves as the foundation, alternating between muddy, open-string blues riffs and high-velocity power chords. The performance alternates between palm-muted chugging during the narrative build-ups and wild, feedback-drenched slides that bridge the structural gaps.
Secondary Layering: A secondary electric guitar enters during the mid-section, providing a sharp, treblier counter-melody that uses rapid tremolo picking to create a shimmering, anxious texture. A distorted harmonica provides sporadic, screeching stabs that act as a call-and-response to the vocal lines, morphing from a clean blues tone into a chaotic, feedback-heavy drone as the track progresses.
Groove & Foundation Progression: The groove is a relentless, driving punk-rock beat with a heavy emphasis on the eighth-note pulse. The bass guitar is played with a heavy pick, providing a distorted, clanking foundation that mirrors the guitar’s root notes. The drums utilize a crashing open hi-hat and a pounding kick drum that accelerates in perceived intensity through the use of double-time snare fills, creating a feeling of a train barreling toward a collision.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by metallic impact hits that sound like gravel hitting a resonator, alongside brief, localized sub-drops to emphasize the weight of the thematic "deal." High-frequency feedback swells and the occasional sound of a distant, dissonant steam whistle provide a haunting atmospheric layer that recedes during the vocal verses but dominates the transitional spaces.
```

**Input lyrics:**

```
[Verse 1]
I played in  every bar in this small town
I had enough, I had to get out
I made my rounds

[Verse 2]
I had to go
Down that dusty road
With the wind blow
Down that dusty road
Where the train goes

[Verse 3]
Two rails and gravel
Got a ticket from the man in the road
And dusty midnight
Under the moon glow
When the wind blow

[Verse 4]
He bought my soul
My soul was sold at the crossroads

[Verse 5]
He was made at the crossroads
Jumping a train at the crossroads
He said you got to ride
You got to roll

[Verse 6]
Snort  a lot of cocaine to  stay on the road
But the first thing as you know
You got to sell your soul
At the crossroads
```

### Effort

*showcases: arrangement / instrumentation · 3:06*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 84. key is Eb, and scale is major. Pop / Blues.
Global Emotional Progression: The track begins with a contemplative and slightly hesitant atmosphere during the initial verses, reflecting a sense of missed opportunity. As the arrangement transitions into the chorus, the mood shifts toward a determined and empowering tone. This emotional growth continues through the bridge, which builds a sense of steady progress and personal victory, culminating in a confident and celebratory final chorus that resolves with a sense of newfound freedom and connection.
Application Scenarios & Imagery: This song serves as a perfect soundtrack for a montage of personal growth, a late-night drive through a rain-slicked city reflecting on a turning point, or an intimate live performance in a dimly lit, high-end lounge where the focus is on the narrative.
Sonics & Production Profile: The soundstage is wide and deep, emphasizing a polished studio clarity where every instrument occupies its own frequency pocket. The low-end is anchored by a rounded, punchy bass, while the high-end is characterized by the crisp, airy shimmer of the cymbals. The production follows a modern pop-blues aesthetic, featuring transparent compression that preserves the soulful dynamics of the vocal performance while ensuring a commercial, radio-ready sheen.
Vocal Details
Vocal Gender & Timbre: A solo male vocalist with a rich, velvety tenor timbre that possesses a notable grit when reaching for higher notes. The voice is characterized by a soulful resonance and a natural, expressive vibrato that becomes more pronounced during sustained notes.
Vocal Style: The delivery begins with a conversational, back-phrased quality in the early verses, almost like a spoken confession behind the beat. As the track progresses, the singer employs more melodic leaps, including a signature rising 5th interval during the chorus hook to emphasize clarity and arrival. The performance is rich with articulations such as subtle vocal fry on the downbeats and breathy tail-offs at the end of emotional phrases. In the final chorus, the singer uses pentatonic runs and bluesy melismas to showcase a heightened sense of liberation and rhythmic urgency.
Harmony/Backing Vocals: Lush, three-part gospel-inspired male harmonies enter during the second half of the track, specifically reinforcing the chorus and the bridge. These layers are panned wide in the mix to create a "wall of sound" effect that supports the lead vocal without overshadowing it.
Vocal FX: The lead vocal features a sophisticated chain consisting of a warm tube-preamp saturation, a synchronized slapback delay for a vintage blues feel, and a large hall reverb that expands during the choruses to provide a sense of grandiosity.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: The primary harmonic foundation is a warm, vintage Rhodes electric piano that provides lush, jazz-inflected chords throughout the entire duration. A clean, soulful electric guitar serves as the secondary melodic lead, providing delicate fingerpicked arpeggios in the verses and shifting to rhythmic, bluesy "chugging" chords during the choruses. 
Secondary Layering: A subtle Hammond B3 organ with a slow Leslie swirl enters during the second verse, adding a mid-range harmonic thickness. A muted trumpet appears briefly in the bridge, acting as a call-and-response element to the vocal lines, providing a sophisticated, melancholic counter-melody. A shimmering tambourine is introduced in the second chorus to add high-frequency energy.
Groove & Foundation Progression: The groove is defined by a deep, melodic electric bassline that utilizes slides and ghost notes to maintain a bluesy swagger. The drums start with a minimalist kick-and-snare pattern using mallets for a soft attack, eventually transitioning into a full, pocket-heavy backbeat with a crisp snare crack and syncopated hi-hat openings by the first chorus. The bridge sees a temporary reduction in drum density, focusing on the kick drum pulse before exploding into a triumphant, driving groove for the finale.
Embellishments, Textures & Spatial FX: The track is punctuated by tasteful guitar slides and occasional reverse reverb swells on the Rhodes to signal section transitions. Subtle sub-bass drops are used to accentuate the start of each chorus, providing a modern pop weight. The spatial environment is enhanced by a faint, localized sound of a distant city hum during the intro and outro, creating a grounded, urban atmosphere without distracting from the musicality.
```

**Input lyrics:**

```
[INTRO]

[Couplet 1]
For sure, it’s never been a problem for you,
All I could say was welcome, nothing more.
I never made the effort, yeah it’s true,
I never thought this would close some doors.

[Couplet 2]
It wasn’t my priority, I can’t lie,
I didn’t need it at all before.
But one day someone asked me “Why don’t you try?”,
And that simple question hit me to the core.

[Refrain]
But now I can speak with you,
And now I can understand you.
I’ve been learning day after day,
And now I’m ready to play.

[Couplet 3]
I never needed to speak, that’s what I said,
But every time they asked, I froze again.
I didn’t know the words inside my head,
And every moment felt the same.

[Couplet 4]
I missed so many chances on my way,
For just one sentence on a résumé.
I felt too far behind to even try,
Until the day I changed my mind and said “Okay”.

[bridge]
So I took it slow, step after step,
Day after day, I found my pace.
And now the words come out instead,
I finally feel I’ve joined the race.

[Refrain]
But now I can speak with you,
And now I can understand you.
I’ve been learning day after day,
And now I’m ready to play.
And now I can speak with you,
Yeah now I can understand you.
No more fear getting in my way,
Cause now I’m ready to play.
Cause now I’m ready to play.
With you
```

### One Bottle

*showcases: arrangement / instrumentation · 3:43*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is G, and scale is minor. Country / Outlaw Country.
Global Emotional Progression: The track initiates with a stark, somber atmosphere of isolation and internal conflict. As the arrangement moves through the verses, a sense of weary resignation builds into a heavy, blues-inflected tension. The choruses provide a cathartic but dark peak, where the emotional weight of addiction and loss becomes a wall of sound. The final sections descend back into a hollow, haunting stillness, mirroring the cycle of the narrative.
Application Scenarios & Imagery: Late-night scenes in a dimly lit, smoke-filled bar; a solitary figure driving down a deserted highway under a moonless sky; a gritty cinematic montage exploring themes of regret and personal vice.
Sonics & Production Profile: The production adopts a dark, earthy aesthetic with a deep, resonant low-end and a mid-range focused on the grit of the instruments. The soundstage is intimate yet expansive, utilizing long plate reverbs to create a sense of cavernous loneliness. High frequencies are rolled off slightly to maintain a vintage, analog warmth, while the transients of the percussion remain sharp and impactful.

Vocal Details
Vocal Gender & Timbre: Male. The vocalist features a rugged, gravelly baritone with a weathered texture that suggests years of experience. The timbre is heavy with "chest voice" resonance, occasionally breaking into a strained, emotive rasp during higher intensity passages.
Vocal Style: The delivery is characterized by a "behind-the-beat" conversational phrasing, creating a sense of exhaustion. The melodic contour utilizes frequent minor 3rd blue notes and a signature falling motif at the end of phrases to emphasize sadness. Key performance markers include a deep vocal fry at the start of verses and a wide, slow vibrato on sustained notes. In the choruses, the singer employs an urgent staccato delivery on the count-based lyrics, contrasted by a soaring, desperate leap on the final phrase of the hook.
Harmony/Backing Vocals: Low-register unison "gang" vocals appear in the second half of the chorus to add a communal, bar-room weight. During the bridge, a haunting, distant falsetto harmony provides a ghostly counter-melody, panned wide to create a sense of disorientation.
Vocal FX: A heavy slapback delay is applied to the verses to evoke a vintage Sun Records vibe, while a lush, dark hall reverb expands the vocal presence in the choruses. Parallel compression is used to bring out the breathy details and mouth clicks, enhancing the raw, "close-mic" intimacy.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A dark, mahogany-bodied acoustic guitar provides the harmonic foundation with a heavy thumb-picked bass-note-and-strum pattern. This is complemented by a "clean" electric guitar with a heavy tremolo effect, playing sparse, minor-key arpeggios that sustain throughout the verses.
Secondary: A distorted electric bass enters with the first chorus, providing a fuzzy, growling low-end that adds a modern "Southern Gothic" edge. A steel guitar enters in the second verse, utilizing slow, weeping volume swells and deep pitch bends to provide a melodic counterpoint. In the choruses, a second rhythm guitar with a high-gain, "crunch" setting is layered to thicken the wall of sound, vanishing abruptly during the bridge to leave only a skeletal fingerpicked line.
Groove & Foundation Progression: The rhythm begins with a simple, muffled kick drum pulse resembling a heartbeat. As the song progresses, a dry, "fat" snare drum enters on the 2 and 4, played with brushes in the verses for a whispering texture before switching to heavy sticks in the chorus. The bass guitar follows a "lazy" root-fifth pattern, occasionally sliding down to low E to emphasize the "bottoming out" feeling of the lyrics.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by the metallic clink of a slide moving across guitar strings and the distant, reverberated sound of a tambourine hit with a long decay. Subtle organ swells provide a bed of tension in the background, while a localized foley effect of a glass being placed on a wooden table appears once in the transition to the bridge. The track concludes with the lingering hum of a tube amplifier and a slow fade of the tremolo guitar.
```

**Input lyrics:**

```
Got my head on straight but memories twist and turn
Late at night I find these thoughts begin to burn
Trying to stay strong but I feel the sway
A bottle in my hand and I'm one whiskey away

Tried to drown it out but it keeps on floating back
Each sip I take feels like a heart attack
Can't escape the past it haunts me every day
Feels like I'm just chasing ghosts one whiskey away

One shot for courage Two for the tears
Three to remember all those wasted years
Four I can't forget the love we used to sway
Five til I find I'm just one whiskey away

It’s a losing fight no matter how I play
Numbing all the pain with each drink I convey
Friends say let it go move on to a new day
But there’s no new dawn when I'm one whiskey away

Your face in my dreams turns my nights to day
The hurt it comes in waves I can’t push away
Wish upon a star to guide me where I lay
But I always find myself one whiskey away

One shot for courage Two for the tears
Three to remember all those wasted years
Four I can't forget the love we used to sway
Five til I find I'm just one whiskey away
```

### Save Us

*showcases: arrangement / instrumentation · 1:29*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is major. Blues Rock / Gospel Blues.
Global Emotional Progression: The track opens with a humble, grounded atmosphere that emphasizes a sense of yearning and spiritual desperation. As the arrangement moves into the chorus, the emotional weight shifts from a personal plea to a communal, anthemic surge of hope and intensity. This tension reaches its zenith during the final chorus, before transitioning into a reflective, intimate Outro that provides a sense of peace and absolute certainty.
Application Scenarios & Imagery: A small, sun-drenched wooden chapel in the rural South, an evening gathering around a flickering bonfire, or a cinematic montage depicting a character finding redemption after a long struggle.
Sonics & Production Profile: The production features a wide, immersive soundstage with a significant emphasis on natural room resonance. The frequency response is characterized by a rich, chocolatey low-mid range and a shimmering top end that captures the air of the vocal performance. Dynamics are highly expressive, moving from a quiet, breathy intimacy to a full-throttle, high-decibel saturation that feels organic and uncompressed.

Vocal Details
Vocal Gender & Timbre: A male lead vocalist with a soulful, weathered tenor voice. The timbre is rich in harmonic overtones, featuring a natural "smoke" in the lower register and a clear, piercing resonance when moving into his head voice.
Vocal Style: The delivery is deeply rooted in the Pentecostal tradition, utilizing a conversational back-phrasing that often sits just behind the beat. The melodic contour is defined by pentatonic runs and blue-note inflections, featuring an iconic rising 5th leap during the chorus to signal the shift in intensity. Performance articulations include subtle vocal fry on the verse entries and a wide, trembling vibrato on the long-held notes of the outro.
Harmony/Backing Vocals: A three-part gospel choir (Soprano, Alto, Tenor) enters during the chorus sections to provide a wall of sound. They utilize a stacked, close-harmony arrangement that creates a powerful, soaring counterpoint to the lead singer’s ad-libs.
Vocal FX: The lead vocal is treated with a vintage spring reverb and a synchronized slapback delay that mirrors the aesthetic of 1960s soul recordings. The choir is processed with a wide hall reverb to create a sense of vast, holy space.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A vintage hollow-body electric guitar provides the primary harmonic framework, utilizing a clean but warm tone with a hint of tube breakup. In the verses, it employs fingerpicked arpeggios and soulful double-stops. A secondary primary layer is the Hammond B3 organ, which starts with a soft, purring Leslie speaker rotation and ramps up to a fast, screaming vibrato during the choruses.
Secondary: A gritty, distorted electric bass enters during the first verse to provide a heavy, melodic counter-line to the vocal. In the chorus, a second rhythm guitar is added to the right channel, playing chunky, overdriven power chords to thicken the texture. During the outro, a delicate Wurlitzer electric piano appears, providing a soft, bell-like texture that replaces the aggressive guitars.
Groove & Foundation Progression: The foundation is built on a slow, heavy 12/8 blues shuffle. The drums remain minimalist in the verses, focusing on a deep, dampened kick drum and a crisp cross-stick on the snare. As the chorus hits, the drummer transitions to a full, open snare hit and a wash of ride cymbal bells, driving the energy upward. The bass guitar provides a syncopated, walking movement that bridges the gap between the blues-rock grit and the gospel swing.
Embellishments, Textures & Spatial FX: Subtle tambourine shakes accentuate the backbeat during the high-energy sections. The track features occasional stereo-panned guitar swells that act as transitional textures. The outro is stripped back, leaving only the soft hum of the organ’s vacuum tubes and the natural decay of the room, creating a stark, intimate finale.
```

**Input lyrics:**

```
[Verse]
All who call on the name of the Lord
Will be saved
All who call on the name of the Lord
Will be saved

[Chorus]
Call on His name
Won't you call on His name
Lord save us
Save us from ourselves
Save us from ourselves

[Outro]
That name is Jesus
It's always been
```

### Scare

*showcases: arrangement / instrumentation · 2:33*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is minor. Country / Americana.
Global Emotional Progression: The track begins with a stark, cold intimacy, reflecting a sense of isolation and suppressed trauma. As it transitions through the verses, the atmosphere remains heavy and somber. The chorus introduces a swelling of resigned pain, broadening the sonic landscape to mirror a deep, internal ache. The pre-chorus provides a haunting, rhythmic tension that breaks into the emotional peak of the second chorus. The bridge serves as a desperate, vulnerable climax of questioning before the arrangement recedes, leaving the listener with a hollow, lingering sense of unresolved grief in the final moments.
Application Scenarios & Imagery: Cinematic scenes of domestic solitude, long drives through desolate rural landscapes under gray skies, or a dimly lit room where the air feels heavy with unspoken history.
Sonics & Production Profile: The soundstage is characterized by a deep, dark reverb that suggests a large, empty house. The frequency response is weighted heavily in the low-mids to emphasize the somber mood, while the high-end is rolled off to create a "dusty" and vintage feel. The dynamics are highly expressive, moving from a near-silent, breathy opening to a dense, wall-of-sound texture during the emotional peaks.

Vocal Details
Vocal Gender & Timbre: Female vocalist. She possesses a weary, husky mezzo-soprano voice with a grainy texture that suggests years of emotional exhaustion. The timbre is breathy and fragile in the lower register, gaining a piercing, raw edge as she moves into her head voice.
Vocal Style: The delivery is heavily back-phrased, dragging slightly behind the beat to convey a sense of lethargy and sadness. The verses feature a narrow melodic contour with frequent vocal fry and breathy tail-offs. In the chorus, she employs an iconic rising minor 6th interval that creates a sense of yearning, followed by chromatic passing notes that emphasize the "breaking" of the voice. The pre-chorus uses urgent, staccato phrasing to mimic a heartbeat, while the bridge utilizes expressive vibrato that starts slow and widens into a desperate, soaring falsetto flip.
Harmony/Backing Vocals: Ghostly, low-register unisons appear in the second verse to create a "shadow" effect. During the choruses, stackable three-part harmonies are panned wide; however, they are mixed slightly behind the lead to maintain the feeling of being alone. A dissonant, high-frequency hum from a male backing vocal enters during the bridge to provide a chilling, discordant counterpoint.
Vocal FX: A dark plate reverb with a long decay is used throughout to place the vocal in a cavernous space. A tape-saturation effect is applied to add grit and warmth. In the pre-chorus, a slapback delay is used to create an "echo" effect that aligns with the lyrical themes of silence.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A vintage, gut-string acoustic guitar provides the primary harmonic foundation, played with soft fingerpicked arpeggios that emphasize the lower strings. This is joined by a somber, upright piano that enters in the second verse, playing sparse, resonant chords in the lower octaves to add weight and a sense of impending gloom.
Secondary: A pedal steel guitar provides long, crying swells that act as a melodic counter-response to the vocal lines, weaving in and out of the frequency spectrum with a heavily modulated, chorus-drenched tone. A cellist provides a low, droning C-string note that persists through the pre-chorus, creating a sense of dread. In the bridge, a distorted electric guitar with high-feedback sustain enters as a secondary layer, providing a gritty, atmospheric roar that mirrors the internal turmoil.
Groove & Foundation Progression: The groove is slow and dragging, initially anchored only by a rhythmic, palm-muted thumping on the acoustic guitar body. A muffled kick drum and a brushed snare enter during the first chorus, playing a minimalist, slow-march pattern. The bass is a deep, upright double bass that plays long, sustaining notes on the downbeats, grounding the track. During the bridge, the percussion expands into heavy, tribal tom-tom hits to increase the tension before dropping away completely for a stripped-back, vulnerable final chorus.
Embellishments, Textures & Spatial FX: Subtle foley elements, such as the faint sound of a wooden floorboard creaking, are placed in the far-right stereo field during the verses. A reversed piano texture provides a haunting transition from the pre-chorus into the chorus. Sub-bass drops are used sparingly during the bridge to emphasize the emotional weight of the questions being asked, while a high-register shimmering drone provides a cold, metallic atmosphere that persists in the background.
```

**Input lyrics:**

```
[Verse]
I was five when the leather snapped
Skin split open like a map
Red rivers ran down my spine
Home was no place to call mine

[Chorus]
Never a hug never a word
Not even whispers to be heard
I bled and I broke and I prayed
But some scars don’t fade

[Verse 2]
Nights were quiet but never kind
Shadows played tricks on my mind
I learned to cry without a sound
In a house where love couldn’t be found

[Prechorus]
A belt’s sting fades away
But silence echoes every day

[Chorus]
Never a hug never a word
Not even whispers to be heard
I bled and I broke and I prayed
But some scars don’t fade

[Bridge]
Was it so hard to hold me tight
To tell me I’d be alright
Instead I grew up on my own
With a heart made of stone
```

### The Mirror

*showcases: vocals · 2:02*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is major. Blues / Soul Blues.
Global Emotional Progression: The track initiates with a stripped-back, weary intimacy, focusing on personal vulnerability and a quiet sense of defeat. As the arrangement moves into the middle sections, the emotional tone shifts from personal lament to a broader, more cynical social commentary, marked by a slight increase in harmonic density. The energy peaks during the bridge where the frustration of modern living becomes palpable, before descending back into a fragile, repetitive outro that emphasizes a cycle of unresolved anxiety and physical fading.
Application Scenarios & Imagery: A rain-streaked window overlooking a bustling but indifferent city at dusk, a tired commuter staring at their reflection in a cracked mirror, or a cinematic montage of escalating domestic stress and rising costs of living.
Sonics & Production Profile: The soundstage is intimate and centered, designed to mimic a small, wooden-paneled studio. The frequency response favors the low-mids and the low-end warmth of the bass guitar, while the high frequencies are slightly attenuated to create a "dusty" and vintage character. The dynamics are highly reactive, emphasizing the space between notes and the natural decay of the instruments.

Vocal Details
Vocal Gender & Timbre: Singer A (Female). The vocalist has a smoky, slightly raspy alto timbre with a heavy, breathy quality that suggests exhaustion and emotional weight. Her voice carries a natural grit in the lower register.
Vocal Style: The performance is characterized by conversational back-phrasing, often landing just behind the snare hit to emphasize a lack of urgency. The melodic contour uses frequent blue notes and minor-third dips within the major key. Hook motifs are established through a recurring descending melodic line at the end of phrases, often utilizing a "vocal fry" articulation on the final word. The delivery incorporates expressive breathy tail-offs and occasional "scoops" into the notes to heighten the sense of vulnerability.
Harmony/Backing Vocals: Subtle, unison-stacked backing vocals enter during the later sections to provide a "ghostly" doubling effect, thickening the lead line without adding traditional choral harmonies.
Vocal FX: The primary vocal is treated with a vintage slapback delay and a dark spring reverb, creating a localized sense of space that feels immediate and personal rather than distant.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: A hollow-body electric guitar serves as the primary harmonic driver, utilizing a warm, slightly overdriven tone. It performs fingerpicked arpeggios and slow, soulful double-stops that provide a rhythmic pulse without the need for heavy percussion.
Secondary Layering: A deep, melodic electric bass enters after the first four bars, providing a steady "heartbeat" with a round, muted tone that sits heavily in the sub-frequency range. In the middle sections, a subtle Hammond organ with a slow Leslie whirl provides a high-register shimmering drone, filling the stereo field to represent the mounting external pressures described in the narrative. A secondary rhythm guitar with a slightly more aggressive "crunch" enters during the bridge to provide syncopated staccato accents, heightening the tension before fading out for the final section.
Groove & Foundation Progression: The groove is a slow, steady 4/4 soul-blues shuffle. The foundation is led by the interaction between the thumb-plucked bass notes and the guitar’s rhythmic "chucks." There is no traditional drum kit; instead, the rhythm is maintained by a soft, dampened tambourine hit on the backbeat and the occasional deep resonance of a floor tom played with mallets to emphasize structural transitions.
Embellishments, Textures & Spatial FX: Organic textures include the audible click of the organ's drawbars and the sliding of fingers across the guitar strings. A localized environmental foley of a distant, low-frequency city hum is used briefly during the intro to ground the track in its urban setting. Sub-drops are avoided in favor of natural bass swells, and the overall spatial environment is kept dry to maintain the "close-mic" realism of the recording.
```

**Input lyrics:**

```
I check the mirror
 the circle’s getting wider,  smooth and pale
The doctor leaned back, she didn't even blink
She said, "It’s the way that you think. stop stressing.
Just set down your burdens, let the worry go."
Like I’m holding onto them and asking them to grow.
​
 the world’s on fire and the rent’s too high
And we’re all just watching the days go by
the world is dying and the patch is growing
A little more skin every day is showing
Hard to keep a head of hair
When there's nothing left but thin, cold air.
​
There’s hatred on the corner, there’s hunger in the street
People working eighty hours just to find a place to sleep
I’m trying to find "peace" and finding only "war"
Then I’m wondering why my strands are lying on the floor

My hair is leaving town, it’s had enough of the news
I'm singing the blues.
​
It’s a tiny little target on the back of my head
For every heavy word that the anchors said
For every grocery bill that makes me want to cry
My beauty’s being borrowed by the "how" and the "why."
​
A little bit bigger today.
A little bit more of me fading away.
Just stop stressing, she said with a grin...
While the whole wide world is caving in.

​my bald spot is growing
the ugliness i feel
makes the spot keep growing
how do we heal
```

## Funk

### Addiction

*showcases: arrangement / instrumentation · 3:26*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 118. key is Bb, and scale is minor. Funk / Nu-Disco.
Global Emotional Progression: The track opens with a sense of melancholic groove, establishing a sophisticated but heavy emotional weight. As it moves through the verses, the atmosphere feels intimate and slightly voyeuristic, driven by the rhythmic tension. The choruses elevate this into a soaring, bittersweet dance anthem, where the pain of the narrative is juxtaposed against a high-energy disco-funk pulse. The final verses see a stripping back of the arrangement to highlight the stark lyrical realization, before a final high-octane chorus leads into a sharp, unresolved rhythmic stop that reflects the thematic conflict.
Application Scenarios & Imagery: A dimly lit, high-end lounge at 3 AM; neon lights reflecting on wet asphalt; a cinematic scene of internal turmoil hidden behind a facade of social composure.
Sonics & Production Profile: The soundstage is deep and polished, featuring a prominent sub-frequency presence and a shimmering top-end. The mix utilizes a modern "wall of sound" approach in the choruses while maintaining a minimalist, dry aesthetic during the verses to emphasize vocal intimacy. The dynamic range is carefully controlled with sidechain compression on the melodic elements, creating a rhythmic "pumping" effect that breathes in sync with the kick drum.

Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist has a supple, emotive tenor voice characterized by a breathy head-voice and a resonant, slightly vulnerable chest register. His timbre is clean but carries an underlying edge of desperation.
Vocal Style: The performance begins with a conversational, back-phrased delivery in the verses, almost whispering in the lower register. It features sudden melodic leaps of a minor 6th to accentuate emotional peaks. The choruses shift into an urgent, staccato rhythmic delivery with high-register "hook motifs" that utilize pentatonic runs and graceful falsetto flips on the tail-end of phrases. There is a distinct use of vocal fry during the descending passages to signal exhaustion.
Harmony/Backing Vocals: Lush, wide-panned stacks of three-part male harmonies appear in the choruses, creating a choral effect that feels both grand and ghostly. In the later verses, a single tracked harmony provides a haunting octave-down double to reinforce the somber mood.
Vocal FX: The verses utilize a tight "dry" room reverb to create proximity. The choruses transition into a shimmering hall reverb with a synchronized 1/4-note ping-pong delay. High-pass filtering is applied momentarily during transitional fills for a "telephone" effect.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: An aggressive, slap-style electric bass provides the harmonic foundation, characterized by heavy thumb-pops and percussive ghost notes. It is doubled by a deep, analog Moog-style synth bass to add low-end weight. A rhythmic electric guitar plays clean, palm-muted "scratch" chords and syncopated 16th-note patterns, serving as the main harmonic engine.
Secondary: A vintage electric piano (Rhodes) provides warm, modulating chords in the background, utilizing a stereo tremolo effect. Shimmering polyphonic synth pads enter during the choruses to expand the stereo width and add a "glassy" texture. A subtle, high-register clavinet enters in the second half of the track, providing a percussive counter-melody that interlocks with the bass line.
Groove & Foundation Progression: The groove is built on a "four-on-the-floor" kick drum pattern typical of dance-funk. The snare is crisp and snappy, hitting strictly on the 2 and 4 with a slight digital "clap" layer for extra bite. In the choruses, the hi-hats transition from a tight, closed sound to an open, sizzling 16th-note pattern. A conga and shaker layer is introduced in the mid-section to increase the polyrhythmic complexity and drive the tempo forward.
Embellishments, Textures & Spatial FX: The track features occasional synth sweeps and white noise risers to build tension before chorus drops. Deep sub-bass drops emphasize the first beat of each chorus. Localized foley of a distant, muffled club ambience is used in the intro to set the scene, while sharp, gated reverb "snare hits" act as transitions between the bridge and final verse.
```

**Input lyrics:**

```
[Verse 1]
Jule
What's on your mind
When all of me
Gets pushed aside

[Verse 2]
Jule
I could never do that
'Cause I love you still
And I'm still your man

[Chorus]
I feel you suffer, I feel you sweet
I see the things that drop you down to your knees
And though your love is so conflicted
It's not me that satisfies your addiction

[Verse 3]
Jule
Still here by your side
Through your night sweats
I'll be holding you tight

[Verse 4]
Jule
I could never do that
'Cause I love you still
And I'm still your man

[Chorus]
I feel you suffer, I feel you sweet
I see the things that drag you down to your knees
And though your love is so conflicted
It's not me that satisfies your addiction

[Chorus]
I feel you suffer, feel you sweet
I see the things that drop you down to your knees
And though your love is so conflicted
It's not me that satisfies your addiction

[Verse 5]
Jule
So pale and drawn
Those marks on your arm
From someone holding you tight

[Verse 6]
Jule
'Cause I could never do that
That's why you still love him
And he's still your man
```

### Backwards

*showcases: arrangement / instrumentation · 2:44*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is E, and scale is minor. Funk Rock / Alt-Rock.
Global Emotional Progression: The track opens with a brooding, atmospheric tension that quickly shifts into a gritty, rebellious rhythmic drive. The emotional arc moves from a defiant, observational stance in the verses to a more urgent, questioning intensity during the choruses. The mid-track solo provides a momentary departure into high-energy agitation, while the final sections sustain a heavy, grounded sense of resistance, culminating in a stark, lingering fade that emphasizes the weight of the message.
Application Scenarios & Imagery: A dimly lit, urban underground club with flickering neon lights, or a cinematic protest scene in a rain-slicked city. The music evokes a sense of gritty realism and high-stakes social observation.
Sonics & Production Profile: The production features a raw, analog-leaning aesthetic with a prominent low-mid warmth. The soundstage is moderately wide, placing the rhythmic foundation front and center. The high-end is crisp but slightly rolled off to maintain a vintage rock texture, while the overall dynamics favor a punchy, aggressive transient response on the percussion and bass.

Vocal Details
Vocal Gender & Timbre: Male. The vocalist features a gravelly, resonant baritone with a commanding presence. The timbre is thick and slightly strained in the upper register, lending an authentic, emotive edge that suggests weariness and conviction.
Vocal Style: The delivery is characterized by rhythmic back-phrasing and a conversational, street-wise cadence. The verses utilize staccato bursts and a descending melodic contour, while the chorus introduces an iconic rising 5th leap on the primary questions. The singer employs subtle vocal fry at the beginning of phrases and expressive, wide vibrato on sustained notes. Rhythmic interaction involves syncopated pushes that sit slightly ahead of the beat during the more urgent lyrical passages.
Harmony/Backing Vocals: Minimalist, low-register unisons appear in the second verse to add a haunting, shadowed effect. In the choruses, a double-tracked layer of the lead vocal provides a thickening effect, while distant, shouting-style male harmonies provide a call-and-response texture that reinforces the rhythmic hooks.
Vocal FX: The primary vocal is processed with a short, dark room reverb and a gritty saturation that mimics a tube pre-amp drive. During the choruses, a subtle 1/8th note tape delay is applied to the tail of phrases to add depth and a sense of echoing through a vast urban space.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A distorted, mid-heavy electric guitar serves as the main melodic engine, utilizing palm-muted chugs and scratching percussive hits during the verses. This is paired with a clean, slightly chorus-drenched secondary guitar that provides rhythmic "skank" chords on the upbeats, common in funk-rock traditions.
Secondary Layering: An ambient, low-pass filtered synth pad provides a foundation during the intro, creating a sense of dread before the beat drops. In the solo section, a wah-infused lead guitar takes center stage, performing bluesy, chromatic runs and wide string bends. A subtle electric piano layer enters in the second verse, adding percussive, staccato stabs that sit deep in the stereo field to provide harmonic movement without cluttering the mid-range.
Groove & Foundation Progression: The foundation is built upon a heavy, syncopated electric bass line that features a lot of "slap and pop" technique to drive the funk element. The drums follow a classic breakbeat-inspired rock pattern, featuring a dry, cracking snare and a deep, resonant kick drum. During the solo and choruses, the drummer shifts to a washier hi-hat and aggressive crash accents to heighten the energy. The groove remains locked and repetitive to maintain a hypnotic, grounded feel.
Embellishments, Textures & Spatial FX: The intro features a subtle, rising synth sweep that transitions into the first verse. Occasional metallic percussion hits and cowbell accents punctuate the transition into the chorus. The solo section is marked by a sudden increase in spatial reverb on the lead guitar. A sub-bass drop emphasizes the start of each chorus, while the outro utilizes a slow filter sweep on the master bus, gradually muffling the high frequencies until only the bass and kick drum remain in the final seconds.
```

**Input lyrics:**

```
[intro]
[verse 1]
 wake up,
Stand up
for your rights.
The world isn't getting any brighter.
[solo]
[instrumental]
[verse 2]

The Middle Ages are looking at us.
The world has turned backwards.
While we were watching MTV,
Christmas isn't snowy.
[chorus]

Where is Santa Claus?
He is getting namaz.

Where are the sweet women's faces?
They're invisible under the laces.
[verse 3]

We can't drink beer.
Sharia is fear.

[chorus]
Where is Santa Claus?
He is getting namaz.

Where are the sweet women's faces?
They're invisible under the laces.

[outro]

[end]
```

### Blue Sky

*showcases: arrangement / instrumentation · 2:35*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 112. key is Eb, and scale is major. Funk / Nu-Disco.
Global Emotional Progression: The track initiates with an infectious, strutting energy that emphasizes self-assurance and peak-performance optimism. During the verses, the mood is one of cool, rhythmic composure, characterized by a "walking on air" sensation. This transitions into a high-octane, celebratory explosion in the choruses, where the emotional arc reaches a state of pure, unadulterated euphoria. The progression maintains this elevated stasis, closing with a high-energy rhythmic flourish that leaves the listener feeling empowered and invigorated.
Application Scenarios & Imagery: This is the definitive soundtrack for high-end fashion runways, sunny coastal drives in a convertible, or vibrant urban celebrations. Visual imagery involves golden hour sunlight reflecting off glass skyscrapers, colorful street art, and synchronized dance movements in a bustling metropolitan plaza.
Sonics & Production Profile: The soundstage is exceptionally wide and holographic, featuring a "larger-than-life" production style. The frequency response is characterized by a surgically clean low-mid punch and a crystalline top-end sheen. Dynamics are tight and snappy, utilizing parallel compression to ensure the transient peaks of the percussion and the snap of the bass remain prominent and impactful throughout the mix.
Vocal Details
Vocal Gender & Timbre: Male Lead. The vocalist possesses a rich, velvety tenor timbre with a resonant chest voice and a highly polished, soulful edge. The texture is smooth but retains a muscular presence that commands attention.
Vocal Style: The delivery is defined by a sophisticated "behind-the-beat" pocket, creating a relaxed yet confident rhythmic feel. The verses utilize syncopated, staccato phrasing with playful vocal fry on the lower notes. The hook motif features an iconic rising 5th leap during the chorus, transitioning into graceful falsetto flips on the melodic peaks. The performance is punctuated by pentatonic blues-scale runs and expressive, medium-width vibrato on sustained notes, ensuring a highly dynamic and emotive contour.
Harmony/Backing Vocals: Dense, Gospel-influenced vocal stacks appear in the choruses, featuring three-part harmonies (root, third, and fifth) that create a wall-of-sound effect. These are panned wide in the stereo field. Subtle unison "gang" vocals provide rhythmic accents during the transitions to emphasize the upbeat nature of the track.
Vocal FX: The lead vocal is treated with a short, bright slapback delay to add slap-funk character and a lush hall reverb with a high-pass filter to prevent muddiness. Sophisticated pitch correction is used as a stylistic tool for a modern, "glassy" finish, while the backing vocals are processed with a slight chorus effect for added width.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: The primary harmonic foundation is a slap-style electric bass with a mid-forward, "growly" tone, performing intricate thumb-pops and finger-plucks to drive the groove. Complementing this is a dual-tracked clean electric guitar arrangement; one guitar performs percussive "scratch" muted strums (the "chicka" sound), while the other executes bright, 9th-chord stabs that emphasize the backbeat.
Basic Attributes: Secondary layers include a vintage Clavinet running through a wah-wah pedal, providing a rhythmic "bubbling" texture in the mid-range. A live brass section—consisting of trumpet, tenor sax, and trombone—enters during the chorus to provide punchy, syncopated stabs and unison melodic flourishes. In the background, a warm analog poly-synth provides sustained, shimmering pad chords to glue the arrangement together, while a subtle cowbell and agogo bells provide localized rhythmic interest during the turnarounds.
Groove & Foundation Progression: The groove is a classic, heavy-duty funk pocket. The kick drum is a tight, "thumping" 24-inch sample that locks perfectly with the bass guitar's rhythmic ghosts. The snare has a high-tuned, cracking timbre that cuts through the mix. In the verses, the hi-hats are kept tight and closed, moving to a half-open, "sloshy" state in the choruses to increase the energy and drive. Percussive fills involve rapid-fire 16th-note tom rolls that lead into the downbeat of each new section.
Embellishments, Textures & Spatial FX: The track features classic funk embellishments such as rhythmic pick-slides on the guitar and synthesized "laser" zaps that act as transition markers. A subtle sub-drop emphasizes the start of the chorus to provide a physical sense of impact. Spatial interest is maintained through the use of an automated phaser on the Clavinet and occasional reverse cymbal swells that build tension before the final vocal hook.
```

**Input lyrics:**

```
[Verse 1]
I'm feeling like a million bucks today
Nothing's gonna stand in my way
The sun is shining and the sky is blue
I've got a feeling that I'm gonna make it through

[Chorus]
Oh oh oh, I'm on top of the world
Oh oh oh, I'm on top of the world
Nothing can stop me now
I'm reaching for the stars and I'm never coming down
```

### Everything

*showcases: arrangement / instrumentation · 3:34*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is Bb, and scale is major. Urban Funk / Neo-Soul.
Global Emotional Progression: The track initiates with an elegant, classical-leaning intrigue that quickly pivots into a confident, street-ready groove. The verses maintain a grounded, reflective energy, while the pre-chorus creates a rising tension and spiritual yearning. The chorus erupts into an anthemic, celebratory proclamation of purpose. A brief, ethereal breakdown provides a moment of celestial suspension before the final high-energy climax, ending on an uplifting and resolute sonic resolution.
Application Scenarios & Imagery: Perfectly suited for high-end urban fashion segments, sunrise strolls through a waking city, or cinematic sequences depicting a character’s moral awakening and newfound conviction.
Sonics & Production Profile: The production is high-fidelity and punchy, characterized by a deep, resonant low-end and a crystalline high-frequency response that highlights the violin and percussion. The soundstage is expansive, utilizing sophisticated panning to separate the dry, centered funk elements from the wide, reverberant ethereal textures.

Vocal Details
Vocal Gender & Timbre: Male vocalist. The lead features a rich, velvety baritone-tenor range with a natural, gravelly soul edge. His timbre is commanding yet intimate, possessing the flexibility to transition from a rhythmic, percussive delivery to soaring, gospel-inflected melodic runs.
Vocal Style: The delivery is characterized by soulful back-phrasing, often landing just behind the beat to enhance the funk aesthetic. The melodic contour features iconic rising 5th leaps during the transition into the chorus and sophisticated pentatonic runs during the breakdown. The performance is rich with articulations, including subtle vocal fry in the lower register verses and graceful falsetto flips during the more ethereal passages.
Harmony/Backing Vocals: Lush, stack-harmony arrangements appear in the choruses, mimicking a professional gospel choir with wide-panned triads. During the bridge and breakdown, the backing vocals utilize a "call-and-response" format, creating a conversational texture that reinforces the central theme.
Vocal FX: The lead vocal is treated with a vintage-style plate reverb and a synchronized 1/4 note delay that is automated to swell at the end of phrases. The backing vocals are processed with a high-pass filter and a lush shimmer reverb to enhance the "ethereal" atmospheric requirement.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A virtuosic solo violin serves as the melodic centerpiece, opening with an elegant staccato motif before evolving into sweeping, lyrical legato lines that float above the funk groove. This is supported by a dominant, slap-style electric bass that provides a percussive, mid-forward growl and remains the harmonic anchor throughout the track.
Secondary: A rhythmic electric guitar ("wah" filtered) provides syncopated "scratched" chords to accentuate the urban funk feel. In the ethereal sections, a secondary layer of shimmering celeste and wide-panned ambient pads emerges to create a sense of weightlessness. During the choruses, a bright, three-piece brass section (trumpet and tenor sax) provides sharp, punctuating stabs to drive the energy.
Groove & Foundation Progression: The foundation is built on a heavy, mid-tempo funk beat. The kick drum is tight and dry, following a complex syncopated pattern, while the snare has a snappy, high-tuned crack. In the verses, the hi-hats are closed and tight, opening up into a driving, washier pattern during the chorus. The breakdown sees the percussion strip back to a simple, muffled kick and finger snaps before a high-impact drum fill reintroduces the full groove for the finale.
Embellishments, Textures & Spatial FX: The track features subtle urban foley, such as the distant, rhythmic clinking of a chain, to ground the "urban funk" genre. Transitional "risers" are used sparingly, replaced instead by melodic violin runs that act as turnarounds. A sub-bass drop emphasizes the arrival of the final chorus, while the breakdown utilizes a granular delay on a vocal chop to enhance the ethereal, timeless atmosphere.
```

**Input lyrics:**

```
[Verse 1]
Woke up this morning, breath in my chest
Didn’t earn it, still I’m blessed
Clock keeps ticking, can’t rewind
Every second drawing a line

Choices echo, seeds we sow
In the light or down below
Can’t keep drifting, can’t pretend
This life ain’t just about the end

[Pre-Chorus]
There’s a fire calling deep inside
More than money, more than pride

[Chorus]
Live like your eternal life depends on it
Every word, every step, every moment
Don’t just talk it, don’t just sing
Let your whole life mean everything
Live like your eternal life depends on it
No more halfway, no more counterfeit
Stand on truth, don’t compromise
Live forever in these borrowed lives

[Verse 2]
Love your neighbor, lift the weak
Find the lost, be who they seek
Grace ain’t cheap, it cost too much
Still He gave that healing touch

When it’s hard and nights are long
Still choose right over wrong
You can fall but don’t you stay
Get back up and find your way

[Pre-Chorus]
There’s a kingdom you can’t see
But it’s closer than your heartbeat

[Chorus]
Live like your eternal life depends on it
Every breath is heaven-sent, don’t waste it
Walk in faith, not by sight
Shine in darkness, be the light
Live like your eternal life depends on it
Not tomorrow—right now, commit
Heart on fire, spirit alive
Live like forever’s on the line

[Bridge]
This ain’t a game, this ain’t pretend
Where you start ain’t where you end
Mercy’s wide but truth is real
What you sow is what you’ll feel

So give Him all, don’t hold back
Stay the course, stay on track
When the final day arrives
You’ll know you truly lived your life

[Breakdown]
Ohhh… don’t just survive
You were made for more than time

[Final Chorus]
Live like your eternal life depends on it
Every heartbeat got purpose in it
Lift your hands, walk in grace
Run your race, keep the pace
Live like your eternal life depends on it
Let your soul and your life be honest
When it’s over, you’ll testify—
You didn’t just live… you lived for life.
```

### Never

*showcases: arrangement / instrumentation · 2:30*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 98. key is Eb, and scale is minor. Rap Metal / Nu-Metal.
Global Emotional Progression: The track begins with a repetitive, rhythmic tension that builds into a defiant and aggressive stance. The verses maintain a focused, gritty momentum that breaks into high-energy, anthemic chants during the chorus. The bridge introduces a chaotic, manic energy with increased rhythmic complexity before the outro descends into a heavy, grinding resolution that emphasizes finality and persistence.
Application Scenarios & Imagery: Underground fighting rings, high-stakes urban chase sequences, or weightlifting sessions in a dark, industrial gym. The imagery evokes a rain-slicked concrete environment under flickering neon lights.
Sonics & Production Profile: The soundstage is narrow and punchy in the verses, expanding significantly in the choruses with wide-panned distorted guitars. The frequency response is characterized by a "V-shaped" EQ curve, emphasizing a thick, sub-heavy low end and crisp, biting high frequencies on the percussion. The dynamic range is intentionally limited through heavy bus compression to create a relentless, in-your-face aesthetic.

Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a raspy, mid-range timbre with a distinct gravelly edge, capable of sharp, percussive plosives and aggressive, shouted textures.
Vocal Style: The delivery is a hybrid of rhythmic rapping and aggressive hardcore shouting. The verses utilize a syncopated, staccato flow that sits slightly behind the beat for a menacing feel. The chorus features a melodic rising fourth interval on the main hooks to create an earworm effect. During the bridge, the performance shifts into manic, scat-like rhythmic vocalizations and guttural ad-libs, utilizing rapid-fire "chicka-ding" phonetics. Vocal fry is used extensively on phrase endings to add grit.
Harmony/Backing Vocals: Gang vocals are heavily layered in the chorus to provide a massive, communal energy. During the bridge and verses, pitch-shifted lower octaves and whispered doubles are used to create a sense of internal dialogue and textural thickness.
Vocal FX: A gritty saturation is applied to the main vocal throughout. The verses feature a tight slapback delay, while the chorus and bridge utilize a metallic plate reverb with a short decay time to maintain clarity amidst the heavy instrumentation. High-pass filters are occasionally automated for "telephone-style" effects during rhythmic breakdowns.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation consists of down-tuned electric guitars employing high-gain distortion. These provide the rhythmic "chug" and palm-muted staccato riffs that define the track’s harmonic movement. A secondary primary layer is a distorted electric bass with a "clanky" top end that mirrors the guitar riffs for maximum impact.
Secondary: Industrial synth pulses and digital noise textures enter during the transitions to bridge the gaps between riffs. A clean, modulated electric guitar with a chorus effect appears briefly in the more atmospheric moments of the second verse to provide a haunting counter-melody. In the outro, a low-frequency oscillator (LFO) modulated drone adds a sense of dread and weight.
Groove & Foundation Progression: The groove is built on a heavy, boom-bap influenced drum pattern. The kick drum is massive and highly compressed, locked in a tight unison with the bass guitar. The snare has a high-pitched, metallic "crack" typical of late 90s production. During the bridge, the percussion becomes more frantic with additional syncopated hi-hat rolls and ride cymbal bells, before returning to a slow, crushing half-time feel in the outro.
Embellishments, Textures & Spatial FX: The track utilizes periodic sub-drops and white noise risers to signal structural shifts. Rhythmic scratches and industrial metal-on-metal percussion hits are peppered throughout the bridge to enhance the "scatting" vocal section. Spatial depth is created using short, gated reverb bursts on snare hits, and occasional stereo-panned glitch effects that dance across the soundstage.
```

**Input lyrics:**

```
[Verse 1]
I never can see I never understand
(Boom-chicka-boom-chicka-boom)
I never gonna change I never understand
(Boom-chicka-boom-chicka-boom)
I never know the sky
I never understand
I never gonna see I never understand

[Chorus]
Hey! Come on the west end
Hey! Come on the life
Hey! Come on the section
I just understand

[Verse 2]
Did you never sky
Or come on the heavens
Like you never mind
(Ah-ah-ah)
I came never copy
And I will never see
Like I want to find of understand

[Bridge]
Come on the vent of pain (Ah!)
Come on the vent of pain (Ah!)
Come on the vent of say (Ha!)
Get on the case
(Vocalizing and rhythmic scatting)
(Chicka-ding-chicka-dah-chicka-ding-chicka-dah)

[Outro]
I am never to say
I am never come
Oh you never come you never sky
Oh you never see
Oh you never sky
Oh you never come you never understand
I never gonna get I never understand
(Boom-chicka-boom)
I never gonna move I never understand
I never gonna stay I never understand
I never never never understand
```

### Shows

*showcases: arrangement / instrumentation · 3:56*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 126. key is Bb, and scale is minor. EDM / Big Room House.
Global Emotional Progression: The track begins with a sense of mysterious curiosity and grounded energy during the first verse, shifting into an aspirational and rising emotional arc through the pre-chorus. The choruses deliver a defiant, anthemic explosion of pride and collective power. The bridge introduces a brief moment of gritty, rebellious intensity before the final euphoric release, concluding with a fading, meditative focus on the core thematic concept during the outro.
Application Scenarios & Imagery: Mainstage festival sets under massive LED displays, high-intensity rhythmic cycling classes, or cinematic montages of subterranean resistance movements and neon-drenched urban uprisings.
Sonics & Production Profile: The soundstage is exceptionally wide and immersive, characterized by a pristine high-end shimmer and a dominant, chest-thumping low-frequency response. The production utilizes heavy side-chaining against the kick drum to create a vacuum-like pumping sensation, while the mid-range is carved out to allow the lead synth and vocals to sit prominently in the foreground.
Vocal Details
Vocal Gender & Timbre: A powerful male vocalist with a gritty, soulful baritone timbre that transitions into a commanding, resonant belt in the higher register. The voice possesses a natural rasp that adds an organic, raw edge to the polished electronic environment, sounding authentic and lived-in.
Vocal Style: The delivery is characterized by conversational back-phrasing during the verses, moving into an urgent staccato rhythmic delivery as the tension builds. The hook features a signature melodic motif centered on an iconic rising 5th leap that emphasizes the thematic weight of the lyrics. Performance articulations include subtle vocal fry on lower notes and expressive, wide vibrato on sustained notes during the chorus climaxes to convey a sense of fierce pride.
Harmony/Backing Vocals: The choruses are reinforced with thick, gang-vocal style layers to simulate a crowd, using wide panning to fill the stereo field. In the pre-chorus, ethereal falsetto counter-melodies float in the high-frequency range to provide a sense of ethereal height.
Vocal FX: The lead vocal is processed with a crisp slapback delay in the verses and a lush, cavernous hall reverb in the choruses. Parallel distortion is applied during the bridge to enhance the "wild and raw" performance quality, while rhythmic gating effects are applied to vocal fragments in the transitions.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A massive, detuned sawtooth lead synthesizer serves as the primary melodic driver, executing aggressive portamento glides between notes during the drop sections. This is supported by a thick, distorted FM synth bass that provides a crunchy, percussive foundation in the low-mids, evolving with filter cutoff automation that opens up during the energy peaks.
Secondary: Clean, rhythmic electric guitar palm-muted accents provide a rhythmic pulse during the verses, creating a syncopated counterpoint to the electronic elements. Shimmering, high-register digital bells enter during the pre-chorus to add a sense of wonder and light, while dark, atmospheric pad drones reside in the background to maintain a sense of mystery. In the bridge, a secondary distorted rhythm guitar layer enters to provide a sudden surge of harmonic density and grit.
Groove & Foundation Progression: The foundation is built on a heavy, saturated four-on-the-floor kick drum that remains consistent throughout the high-energy sections. The groove evolves from a simple kick-and-clap pattern in the first verse to a complex, driving arrangement in the chorus featuring syncopated open hi-hats, sharp white-noise snares, and 16th-note shakers that propel the track forward. The bridge briefly strips the percussion back to a pounding sub-kick to reset the energy before the final chorus.
Embellishments, Textures & Spatial FX: The track is punctuated by classic EDM transition tools, including long white-noise risers, pitched snare rolls, and sub-bass drops that mark the start of each chorus. Impact hits with long tail-off delays are used to emphasize key lyrical moments, while brief metallic foley textures and glitchy synth chirps are scattered throughout the stereo field to add modern technical detail. The outro features a decaying delay loop on the final vocal phrase, melting into a soft, ambient synth wash.
```

**Input lyrics:**

```
[Verse 1]
They call it Ibogaine — tongue-twist, hard to feel,
A root from ancient Africa, buried deep beneath the seal.
They fear the truth it carries, they silence what it screams,
But wonder isn’t whispered — it’s roaring in our dreams!
[Pre-Chorus]
Names don’t make the magic,
Words can’t cage the fire —
It’s burning in the hearts that wonder,
In the souls that climb up higher!
[Chorus]
We are the ones who wonder,
Breaking through the silence loud!
Can’t pronounce the miracle,
But we stand fierce and proud!
The wonder they can’t name —
We sing it anyway!
[Verse 2]
It’s not some quick-fix flash, no easy dopamine,
It’s the soul’s raw mirror, showing truths we’ve never seen.
They hush the sacred medicine, the antidote to chains —
But we’re the spark that lights the dark, the thunder in the rain!
[Pre-Chorus]
Names don’t make the magic,
Words can’t cage the fire —
It’s burning in the hearts that wonder,
In the souls that climb up higher!
[Chorus]
We are the ones who wonder,
Breaking through the silence loud!
Can’t pronounce the miracle,
But we stand fierce and proud!
The wonder they can’t name —
We sing it anyway!
[Bridge]
If it had a sweeter name, they’d bottle it for stores,
But real magic’s wild and raw — it kicks down all the doors!
[Final Chorus]
We are the ones who wonder,
Breaking through the silence loud!
Can’t pronounce the miracle,
But we stand fierce and proud!
The wonder they can’t name —
We sing it anyway!
[Outro]
Wonder… wonder… wonder…
We sing it anyway…
Wonder… wonder… wonder…
```

### 秘密

*showcases: vocals · 5:41*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is Eb, and scale is minor. Jazz Hop / Lounge.
Global Emotional Progression: The track initiates with a mysterious, nocturnal tension, establishing a sophisticated yet predatory atmosphere. Through the initial verses, the mood remains cool and calculated, characterized by a seductive intimacy that masks an underlying corporate espionage narrative. The choruses introduce a swirling, hypnotic allure that intensifies the "femme fatale" persona. As the arrangement progresses toward the bridge and breakdown, the emotional tone shifts from seductive to cold and triumphant, concluding with a lingering, ghostly sense of disappearance in the outro.
Application Scenarios & Imagery: Perfectly suited for a high-stakes cinematic heist sequence set in a rain-slicked Hong Kong skyline, or a dim, velvet-adorned VIP lounge. The imagery evokes neon reflections in red wine, the silent click of a lock, and the sharp contrast between silk textures and cold digital screens.
Sonics & Production Profile: The soundstage is deep and immersive, featuring a prominent, punchy low-end focused around a thick, saturated bassline. The frequency response is tailored with a slight dip in the high-mids to accentuate the "steamy" atmosphere, while the high frequencies are crisp to capture the detail of percussive transients. The production adopts a modern boutique aesthetic, balancing organic jazz elements with the clean, compressed precision of lo-fi hip-hop.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist delivers a sultry, smoky Cantonese performance characterized by a husky, low-register resonance. Her timbre is velvet-like and rich, possessing a realistic "close-mic" intimacy that captures every breath and subtle lip-smack, enhancing the sensual yet dangerous persona.
Vocal Style: The delivery is conversational and back-phrased, often lagging slightly behind the beat to increase the tension. She employs a signature hook motif involving a descending minor third "spy-theme" interval. Performance articulations include heavy vocal fry in the lower verses, transitioning to a breathy, feline falsetto during the chorus hooks. The rhythmic interaction is highly syncopated, utilizing staccato bursts for technical terms and elongated, vibrato-heavy vowels for the more seductive phrases. A final spoken-word tag provides a dry, grounded conclusion to the narrative.
Harmony/Backing Vocals: Lush, multi-layered harmonies appear in the chorus to create a "wall of sound" effect, using tight three-part stacks that emphasize the minor tonality. In the bridge, ghostly unison whispers are panned hard left and right, creating a disorienting, conspiratorial texture that mimics secrets being shared.
Vocal FX: The lead vocal is treated with a vintage tube-preamp saturation for warmth. A synchronized slapback delay is used in the verses to add depth, while the choruses utilize a shimmering hall reverb with a long tail. During the breakdown, the vocals are processed with a high-pass telephone filter to simulate a covert recording.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, jazz-hollowbody electric guitar provides the primary harmonic framework, utilizing sophisticated 9th and 13th chord voicings with a soft, fingerpicked articulation. It is complemented by an ambient, ethereal synth pad that enters in the intro, providing a wide, cinematic wash that sustains throughout the track.
Secondary: An upright bass provides a primary melodic counterpoint, featuring heavy finger-noise and a deep, woody resonance. A Rhodes electric piano enters during the second verse, adding rhythmic "churps" and sparkling high-register clusters. In the chorus, a second rhythm guitar with a slight overdrive is layered to thicken the arrangement and provide a more driving, urgent pulse. A muted trumpet appears intermittently as a secondary melodic layer, offering mournful, bluesy fills that respond to the vocal phrases.
Groove & Foundation Progression: The foundation is built on a classic jazz-hop breakbeat, featuring a heavy, swung kick drum and a crisp, slightly late snare hit. The groove starts minimal, with just the kick and a closed hi-hat. As the track moves into the chorus, the percussion expands with a rhythmic tambourine and subtle woodblock hits. The breakdown sees the drums drop out entirely, replaced by the rhythmic clicking of high heels on a hard surface, before the final chorus reintroduces the full beat with added energy and a driving ride cymbal.
Embellishments, Textures & Spatial FX: The track is peppered with atmospheric details including the sound of a wine glass clinking and a soft, rhythmic "pulse" synth that mimics a ticking clock. During the breakdown, localized foley of muffled footsteps on a carpet and the soft click of a door closing are used to heighten the narrative tension. Sub-bass drops emphasize the transitions into the chorus, while a reverse cymbal swell provides a smooth lead-in to the bridge. No wind or vinyl crackle effects are present, maintaining a sleek, modern high-fidelity sheen.
```

**Input lyrics:**

```
[Verse 1]
静静坐低 望住你个tie
手指画圈 喺你支红酒杯旁边
你讲公司机密 当系英雄事迹
我假装听到出神 其实数紧每句字

你话高层点谂
边个最惊丢位
I just smile and say
“Baby, trust me tonight”

[Chorus]
Secret Agent Lover
Underneath the covers
细细声讲你所有嘅秘密
我唔会保留佢
Secret Agent Lover
I'm going to discover
你所有嘅扭曲同秘密
记住到朝早
(Secret Agent Lover)

[Verse 2]
你支香水 留喺我颈弯
房卡乱放 落喺我个手袋间
你话我太危险
但系照样熄咗灯
电话萤光闪闪
我影低你啲login
你问我叫咩名
I say “call me anything”
你信爱情会保密
我信硬碟会记清

[Chorus]
Secret Agent Lover
Kissing under covers
你谂得太多喇
Come on, 等我有佢
Secret Agent Lover
This love makes you wonder
你系咪应该做紧呢样嘢?
机密信心
(Secret Agent Lover)

[Bridge]
Late night lover or undercover
你分唔清 其实都一样
Every little whisper
变成我口袋里面嘅金银珠宝
你信枕边有人
就唔怕黑暗
I just take what I need
然后慢慢行出大门

[Chorus]
Secret Agent Lover
Underneath the covers
细细声讲你所有嘅秘密
我唔会保留佢
Secret Agent Lover
I'm going to discover
你所有嘅扭曲同秘密
记住到朝早
(Secret Agent Lover)

[Verse 3]
你只手 滑过我背脊线
低声话今晚冇人会见
我轻轻笑住 倒多半杯酒
眼尾偷望你个密码锁
你话世界太乱
净系想揾个港湾
I lean closer slowly
话「放心啦，我明白」
你开始讲太多
关于边个输边个赢
我指尖抚过你西装钮
(唔好停…继续讲)
Every secret falling softly
落喺我记忆入面
你以为系情话
其实系证据链

[Chorus]
Secret Agent Lover
Closer than another
细细声讲你所有嘅秘密
我全部都听清
Secret Agent Lover
I'm going deeper undercover
你眼入面𠮶啲故事
今晚慢慢开封
(Secret Agent Lover)

[Verse 4]
窗外霓虹 滴落玻璃
城市好似唔会瞓
你贴近我耳边
讲咗几个关键人
我轻声答「Really?」
手却冇停过
指尖沿住你领口
慢慢数节奏
你笑话我太迷人
会令人讲错说话
(讲多啲…讲多啲)
你开始讲银行
讲交易 同计划
Your voice getting softer
心跳慢慢乱
但我脑入面
已经写好结论

[Chorus]
Secret Agent Lover
Underneath the covers
细细声讲你所有嘅秘密
我唔会保留佢
Secret Agent Lover
I'm going to discover
你所有嘅扭曲同秘密
记住到朝早
(Secret Agent Lover)

[Verse 5]
凌晨三点 房间好静
只剩低呼吸声
你揽住我腰
以为世界暂停
但我望住天花板
记住每句话
每个名字 每个地方
全部记晒喇
你梦入面仲讲紧
边个唔可以信
(嗯…我知道)
我轻轻拎起电话
静静send出去
By the time you wake up
故事会变天
而你仲以为
我只系情人

[Breakdown]
Soft steps 落地毯
高跟鞋冇声
你仲喺床上
抱住半个梦境
桌上杯红酒
仲有你个戒指
I leave a lipstick mark
当作最后暗示

[Final Chorus]
Secret Agent Lover
No need to recover
昨晚你讲过嘅所有秘密
而家全部飞走
Secret Agent Lover
Now I know another
你世界入面嘅谜底
已经有人接收
(Secret Agent Lover)

[Outro]
门慢慢关上
走廊灯微黄
你嘅声音仲留喺
我耳边回荡
Love or mission
有时分唔清
但秘密一出口
就唔再属于你
(Secret Agent Lover…)

[Spoken]
"芷若, reporting for duty"
```

## Country

### Cowboy Life

*showcases: arrangement / instrumentation · 2:31*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is G, and scale is major. Country / Modern Bro-Country.
Global Emotional Progression: The track begins with a gritty, grounded energy that establishes a rugged outdoor setting. As it transitions into the chorus, there is a surge of adrenaline and romantic excitement, characterized by a driving rhythmic push. The second verse maintains this momentum, leading into a sudden, atmospheric drop in the bridge that evokes a sense of quiet intimacy and stillness. The final chorus serves as a high-energy emotional release, concluding with a rhythmic tail that emphasizes the thrill of the journey.
Application Scenarios & Imagery: Late-night drives through rural backroads, high-energy outdoor summer festivals, and cinematic sequences involving off-road adventures. The imagery is centered on moonlight reflecting off mud-splattered metal, the heat of a truck engine, and the physical closeness of two people in a rugged environment.
Sonics & Production Profile: The production features a punchy, mid-forward mix with a heavy emphasis on the low-frequency weight of the bass and kick drum. The soundstage is wide, utilizing aggressive panning for the electric guitars to create a wall-of-sound effect in the choruses. High-frequency clarity is preserved in the vocal transients and percussion to ensure a sharp, radio-ready edge.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist is a gritty tenor with a notable gravelly texture and a resonant chest voice. The timbre is masculine and weathered, suggesting a life lived outdoors, yet possesses enough melodic smoothness to carry a commercial hook.
Vocal Style: The delivery is rhythmically assertive, featuring a syncopated, almost conversational back-phrasing behind the beat during the verses to create a relaxed, confident swagger. A signature hook motif involves a rising major third leap at the end of the chorus phrases, adding an earworm quality. Performance articulations include subtle vocal fry on the lower notes of the verses and a shift to a powerful, belting chest-voice delivery in the choruses. The bridge sees a transition to a breathy, near-whisper quality that creates a stark dynamic contrast.
Harmony/Backing Vocals: High-tenor backing vocals provide a double-tracked reinforcement during the choruses, positioned wide in the stereo field to add verticality. Gang-style vocal shouts are utilized as rhythmic accents during transitional turnarounds to enhance the "party" atmosphere.
Vocal FX: A short slapback delay is applied to the verses to enhance the rhythmic grit, while the choruses utilize a lush hall reverb with a pre-delay to keep the vocal front-and-center. Parallel compression is used heavily to ensure the vocals remain consistent against the dense instrumental backing.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, percussive acoustic guitar provides the initial harmonic foundation, utilizing rhythmic palm-muting to drive the tempo. A distorted electric rhythm guitar enters during the choruses, providing thick, palm-muted power chords that occupy the lower-mid frequency range to add immense weight and energy.
Secondary: A telecaster-style electric lead guitar provides bright, twangy melodic fills between vocal lines, often employing double-stops and rapid hybrid-picked runs. In the bridge, a sustained ambient synth pad enters to provide a wash of sound, replacing the rhythmic drive with a static, ethereal texture that emphasizes the "hush" described in the progression.
Groove & Foundation Progression: The groove is anchored by a heavy, compressed kick drum and a cracking snare that hits squarely on two and four. The bass guitar features a distorted, overdriven tone that follows the kick drum pattern closely, providing a thick "chugging" sensation. During the verses, the groove is more focused on the hi-hat and "sidestick" snare hits, whereas the choruses open up into a full-throttle rock beat with washier crash cymbals and a driving eighth-note bassline. The bridge sees the drums drop out entirely, leaving only a subtle, heartbeat-like pulse from a muted bass note before building back up for the final section.
Embellishments, Textures & Spatial FX: The track features localized foley sounds of a truck engine idling and the rhythmic chirping of crickets during the bridge to ground the listener in the physical space. Sub-drops are used to punctuate the transition from the bridge back into the final chorus. A slide guitar with a high-gain setting provides occasional atmospheric "screams" in the background, mimicking the sound of tires spinning or distant mechanical movement.
```

**Input lyrics:**

```
[Verse 1]
Mud on the glass
Cord on the dash
Cooler in the bed, sittin’ heavy on the back road
Cap pulled low
Camo on my clothes
You climbed up quick when I said “let’s go” (hey!)

[Chorus]
You a ghost on the back, holdin’ on tight
Rollin’ in four-wheel drive through the moonlit night
Tailgate rattlin’, creek water flyin’
Laughin’ so loud, hearts both wildin’
Ghost on the back, girl, breath on my neck
Tracks in the mud and your hands on my vest
If this is a hauntin’, I don’t wanna come back
Keep ridin’ like that, ghost on the back

[Verse 2]
Phone lost signal
Truck hit a ripple
Mud hole deep, but we ain’t slowin’ down now
Boots on steel
You lean, I feel
Every bump turnin’ into somethin’ real (oh yeah)

[Chorus]
You a ghost on the back, holdin’ on tight
Rollin’ in four-wheel drive through the moonlit night
Tailgate rattlin’, creek water flyin’
Laughin’ so loud, hearts both wildin’
Ghost on the back, girl, breath on my neck
Tracks in the mud and your hands on my vest
If this is a hauntin’, I don’t wanna come back
Keep ridin’ like that, ghost on the back

[Bridge]
Headlights cut, just crickets and us
Steam from the hood and a slowin’ hush
You say “one more round,” I just grin
Turn that key, feel you lean in (hey!)

[Chorus]
You a ghost on the back, holdin’ on tight
Rollin’ in four-wheel drive through the moonlit night
Tailgate rattlin’, creek water flyin’
Laughin’ so loud, hearts both wildin’
Ghost on the back, girl, breath on my neck
Tracks in the mud and your hands on my vest
If this is a hauntin’, I don’t wanna come back
Keep ridin’ like that, ghost on the back (ghost on the back)
```

### Laugh And Flame

*showcases: arrangement / instrumentation · 3:05*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 82. key is G, and scale is major. Country / Modern Folk-Country.
Global Emotional Progression: The track initiates with a playful, lighthearted intimacy that feels like a candid observation of a loved one. As it transitions into the chorus, the mood shifts from whimsical storytelling to a grounded, affectionate devotion. The bridge introduces a brief surge of dramatic tension and vulnerability, emphasizing steadfastness, before resolving into a final, celebratory chorus that feels both triumphant and deeply personal.
Application Scenarios & Imagery: Golden hour in a cluttered but cozy kitchen, long drives through rolling countryside, or a montage of a couple’s domestic life filled with charming imperfections and genuine laughter.
Sonics & Production Profile: The production emphasizes a warm, organic soundstage with a focus on mid-range clarity and natural textures. The frequency response is balanced, featuring a rounded low-end and a crisp, airy top-end that highlights the shimmer of acoustic strings. The dynamic aesthetic is breathe-like, expanding and contracting naturally to mirror the emotional weight of the narrative.

Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a textured, honeyed tenor with a slight, natural grit that suggests a lived-in authenticity. His timbre is flexible, capable of shifting from a breathy, confidential whisper to a resonant, full-bodied belt.
Vocal Style: The delivery is characterized by a conversational back-phrasing, often landing slightly behind the beat to enhance the storytelling feel. A recurring hook motif involves a gentle upward flip into falsetto on the tail-end of sentimental phrases. During the chorus, the melody utilizes rising 4th intervals to create an uplifting, "smiling" quality. The bridge showcases more urgent, staccato phrasing that transitions into a long, expressive vibrato on sustained notes to signal emotional intensity.
Harmony/Backing Vocals: Warm, double-tracked backing vocals appear in the choruses, providing a lush "wall of sound" effect. In the bridge, a secondary male harmony provides a high-register counter-melody that tracks the lead vocal at a third interval, adding a sense of communal support.
Vocal FX: The vocals are processed with a vintage-style spring reverb for a classic feel, complemented by a short slapback delay that adds depth without losing the "dry" intimacy of the performance. Subtle saturation is applied to the louder sections to provide a pleasing harmonic warmth.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: The primary harmonic foundation is built upon a bright, fingerpicked steel-string acoustic guitar, providing a rhythmic "gallop" that persists throughout the track. This is complemented by a secondary layer of "Nashville-tuned" acoustic guitar, which adds a high-frequency shimmer and reinforces the chordal structure.
Secondary Layering: A clean electric guitar with a touch of tremolo enters during the second verse, providing melodic swells and "chicken-picking" accents. A pedal steel guitar introduces long, sweeping legato glissandos in the choruses, acting as a textural bridge between the vocal lines. In the bridge, a light piano layer adds percussive weight to the downbeats, disappearing for the final chorus to keep the focus on the stringed instruments.
Groove & Foundation Progression: The foundation is centered on a melodic electric bass that uses walking lines to connect chord changes, providing a fluid sense of motion. The percussion begins with simple brushed snare hits and a steady kick drum pulse. As the song progresses, the brushes are replaced by light drumsticks on the snare rim during the verses, moving to a full, open-hat groove in the choruses. The bridge features a dramatic build-up using floor tom rolls that culminate in a sharp snare crack for the final chorus entry.
Embellishments, Textures & Spatial FX: Subtle mandolin trills provide high-register ornamentation during the transitions. Brief, localized foley of a gentle rain shower is heard in the opening seconds of the intro to set the scene, fading out quickly as the guitar enters. Occasional tambourine hits on the backbeat during the final chorus add a layer of brightness and drive to the track’s conclusion.
```

**Input lyrics:**

```
[Verse 1]
You hate umbrellas
You dance in the rain
You burn the pancakes
Then laugh at the flame
You call your mom
Just to hear her complain
Then turn around
And do it the same

[Chorus]
My darling Emma
You’re my favorite mess
Hair in a knot
Ink on your dress
You say you’re too much
I say I’m impressed
My darling Emma
You’re my sweetest yes

[Verse 2]
You save stray postcards
From cities you’ve skipped
You lose your keys
But your tongue’s always quick
You say you’re fine
With your voice doing tricks
Then cry to commercials
And old movie clips

[Chorus]
My darling Emma
You’re my favorite mess
Hair in a knot
Ink on your dress
You say you’re too much
I say I’m impressed
My darling Emma
You’re my sweetest yes

[Bridge]
If the sky falls down
If the ground gives in
I’ll hold that hand
With the paint-stained skin
You’ll roll your eyes
Then you’ll let me in (oh)
Again and again and again

[Chorus]
My darling Emma
You’re my favorite mess
Bare feet on gravel
Heart in my chest
You say I’ll leave
I just pull you in
Pressed
My darling Emma
You’re my sweetest yes
```

### Needle

*showcases: vocals · 4:13*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is F#, and scale is minor. Country / Outlaw Country.
Global Emotional Progression: The track begins with a stark, isolated atmosphere of desperation and internal conflict, establishing a heavy narrative weight. As the narrative descends into the harrowing imagery of the middle verses and bridge, the arrangement becomes increasingly claustrophobic and tense. This tension breaks into a resilient, grit-filled determination during the choruses, finally settling into a weary but persistent resolve in the outro, mirroring a long journey through darkness toward a distant light.
Application Scenarios & Imagery: Late-night drives down deserted highways, gritty neo-western film trailers, or dimly lit scenes depicting a character grappling with recovery and personal demons.
Sonics & Production Profile: The production adopts a dark, earthy aesthetic with a significant emphasis on the lower-mid frequencies to ground the somber tone. The soundstage is intimate yet deep, utilizing long tail reverbs to create a sense of vast, lonely space. High-frequency transients from the acoustic guitar strings are preserved to provide a tactile, "close-to-the-mic" realism, while the overall dynamic profile moves from a hushed, breathy proximity to a saturated, high-energy roar.

Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a rugged, weather-worn baritone characterized by a heavy grain and authentic gravelly texture. The timbre is rich in low-end harmonics, suggesting a life of hard-won experience.
Vocal Style: The delivery is marked by a conversational, back-phrased rhythmic approach that feels like a weary monologue. The verses utilize a heavy vocal fry and breathy tail-offs to emphasize the fragility of the protagonist. A recurring hook motif is built around a minor 3rd to root resolution, creating a haunting earworm. During the choruses, the vocalist pushes into a strained, powerful belt with a wide, expressive vibrato, while the bridge features urgent staccato bursts that mirror the agitation of the lyrics.
Harmony/Backing Vocals: Sparse, low-register unisons appear in the second half of the verses to add weight. In the choruses, gritty, dual-tracked "gang" style harmonies provide a wall of sound that feels more like a collective shout of survival than a polished choir.
Vocal FX: The verses are treated with a dark room reverb and a slapback delay that evokes a small, empty hall. In the choruses, the vocals receive a light saturation/distortion to enhance the aggressive grit, paired with a stereo spread to increase the perceived scale of the performance.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A dark-toned, resonant acoustic guitar provides the primary harmonic foundation, played with a combination of somber fingerpicking and heavy, muted thumb-strums on the downbeats. A distorted, growling electric bass enters early, providing a fuzzy, aggressive low-end counterpoint that defines the track's grit.
Secondary: A clean electric guitar with a heavy tremolo effect enters in the second verse, playing mournful, long-sustaining notes that act as a ghostly counter-melody. In the choruses, a second rhythm electric guitar with high-gain distortion is layered to provide a thick harmonic wash. A lonesome pedal steel guitar appears in the later sections, utilizing slow, sweeping legato slides to add a traditional country wail to the modern, dark arrangement.
Groove & Foundation Progression: The groove begins with a simple, heartbeat-like kick drum thud. As the song progresses, a heavy snare with a deep "thwack" enters, playing a deliberate, slow-march rhythm. The percussion expands in the chorus with crashing, dark-washed cymbals and a steady, driving eighth-note pulse on the floor tom, creating a sense of relentless forward motion. The bridge features a breakdown where the drums drop to a primitive, syncopated rimshot before building back into the final crescendo.
Embellishments, Textures & Spatial FX: Ambient, low-frequency pads create a constant, hovering tension in the background. Brief, localized foley of a metallic clink and a distant, echoing door thud are used to punctuate the transition into the bridge. Sub-bass drops are strategically placed at the start of each chorus to emphasize the weight of the resolve, while a high-register shimmering drone provides a sense of cold, starlit isolation during the outro.
```

**Input lyrics:**

```
.*[Verse 1]**
Well you know those times when you feel like there's a sign there on your back
That says I don't mind if you kick me, seems like everybody has
Things go from bad to worse you think they can't get worse than that and then they do

**[Verse 2]**
You step off the straight and narrow and you don't know where you are
Used the needle of your compass to sew up your broken heart
Ask directions from a genie in a bottle of Jim Beam
And she lies to you
That's when you'll learn the truth

**[Verse 3]**
Met a man down on the corner, said he’d make my pain disappear
White powder in a baggie, whispered, "Baby, have no fear"
But the high don’t last forever, and the crash is twice as mean
Now the devil’s got my number, and he’s callin’ in his debt

**[Verse 4]**
Dealer’s knockin’ at the door now, says I owe him one more time
But the money’s gone, the stash is low, and I’m runnin’ out of lies
He’s got a grin like a razor, and his patience’s wearin’ thin
I can see the fire in his eyes, but I can’t let him drag me in

**[Chorus]**
If you're goin’ through hell keep on goin’
Don’t slow down if you're scared don’t show it
You might get out before the devil even knows you're there

**[Verse 5]**
I’ve been deep down in that darkness
I’ve been down to my last match
Felt a hundred different demons breathin’ fire down my back
And I knew that if I stumbled I’d fall right into the trap
That they were layin’, yeah
But the good news is there’s angels everywhere out on the street
Holdin’ out a hand to pull you back up on your feet
The ones that you’ve been draggin’ for so long
You’re on your knees you might as well be prayin’
Guess what I’m sayin’

**[Bridge]**
Meth smoke curls around the ceiling, shadows dancin’ on the wall
Every hit’s a little freedom, every crash is ten times worse
But the needle’s callin’ like a siren, and the dealer’s at the door
I gotta break this chain before it drags me to the floor

**[Verse 6]**
Mama’s voice still echoes, sayin’, "Boy, you’re better than this mess"
But the high’s got me convinced that I can’t live without its kiss
Yet somewhere deep inside me, there’s a spark that won’t go out
Maybe it’s the angels, maybe it’s the doubt

**[Chorus]**
If you're goin’ through hell keep on movin’
Face that fire, walk right through it
You might get out before the devil even knows you're there
Yeah, if you're goin’ through hell keep on goin’
Don’t look back, just keep your eyes straight ahead
You might get out before the devil even knows you're there

**[Outro]**
One day I’ll wake up sober, with the sun instead of shame
The dealer’s just a memory, and the pain won’t have a name
Till then I’ll keep on walkin’, through the fire, through the rain
If you’re goin’ through hell, don’t you stop—just keep on goin’ the same

---
```

### No Lie

*showcases: arrangement / instrumentation · 2:22*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 124. key is D, and scale is major. Pop Rock / Power Pop.
Global Emotional Progression: The track opens with a straightforward, inviting energy that establishes a clear, no-nonsense attitude. During the verses, the mood is conversational and grounded, transitioning into a more insistent and driving energy during the pre-choruses. The choruses explode into a bright, anthemic affirmation of simplicity, maintaining a steady and infectious momentum. The bridge introduces a brief moment of assertive tension before resolving into a high-energy final celebration that remains resolute and upbeat until the final ringing chord.
Application Scenarios & Imagery: This track is perfectly suited for high-energy montage sequences in coming-of-age films, upbeat driving playlists, or commercial spots emphasizing clarity and honesty. Visually, it evokes a bright, open-road setting at midday or a vibrant, crowded club with neon lighting.
Sonics & Production Profile: The production features a classic radio-ready sheen with a balanced frequency response. The soundstage is wide, placing the rhythm guitars at the far edges while the bass and kick drum provide a solid, centered anchor. The dynamic profile is consistent and punchy, emphasizing a "forward" mix where every instrument occupies a distinct frequency pocket, ensuring maximum clarity for the vocal performance.

Vocal Details
Vocal Gender & Timbre: Male. The vocalist is a robust baritone with a gritty, soulful edge in the lower mids and a resonant, clear chest voice. The timbre is masculine and direct, providing a sense of authentic, lived-in experience.
Vocal Style: The delivery is rhythmically driven and conversational, utilizing a syncopated back-phrasing technique that sits slightly behind the beat to convey a relaxed confidence. The melodic contour is characterized by an iconic rising 5th leap during the hook motifs, punctuated by occasional bluesy chromatic passing notes. Performance articulations include subtle vocal fry at the start of phrases and expressive, wide vibrato on sustained notes at the end of the chorus lines.
Harmony/Backing Vocals: Lush, three-part stack harmonies appear during the choruses to provide a wall-of-sound effect. These backing vocals are mixed with a slightly wider stereo spread than the lead, using a breathier, smoother timbre to contrast with the lead singer's grit.
Vocal FX: The lead vocal is processed with a crisp large-hall reverb and a timed eighth-note delay that adds spatial depth. A subtle saturation plugin is used to enhance the harmonic excitement of the vocal, while parallel compression ensures the lyrics remain intimate and intelligible throughout the arrangement.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A pair of overdriven electric guitars act as the foundation, utilizing a mix of palm-muted staccato rhythms in the verses and wide, ringing power chords in the choruses. The primary harmonic movement is defined by these guitars, which evolve from a dry, tight sound to a saturated, expansive tone as the song progresses.
Secondary: A secondary layer consists of a bright, percussive acoustic guitar that provides a rhythmic "jangle" in the high-frequency range, entering during the second verse to add textural variety. A vintage organ enters during the choruses, providing a shimmering, rotating-speaker Leslie effect that fills the mid-range. During the bridge, a melodic lead guitar counter-phrase emerges, using pentatonic runs to respond to the vocal lines.
Groove & Foundation Progression: The groove is built upon a driving, four-on-the-floor kick drum pattern that provides an unwavering pulse. The electric bass guitar follows the kick closely, playing eighth-note root notes with occasional melodic fills that bridge the gap between sections. In the choruses, the drummer opens up the hi-hats to a semi-open wash, increasing the perceived energy and creating a sense of forward motion that culminates in frequent, energetic snare rolls leading into the final sections.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by classic rock embellishments such as pick slides and reverse cymbal swells that signal transitions between the verse and chorus. Subtle tambourine hits are added to the backbeat during the final chorus to enhance the high-end sparkle. A brief sub-drop occurs at the start of the bridge to signify a shift in gravity, while a clean, short room reverb is applied to the drums to create a sense of physical space without washing out the rhythmic precision.
```

**Input lyrics:**

```
I'm not complicated
You get ...just what you see
But you're a complicated gal
You keep on troublin' me
'Said I'm not complicated
So don't just walk on in
Start playing games with my heart.... girl
I play to win.

Don't need to play no heart games girl....I'm tellin' you no lie
No need to play the game of love......here's the reason why

Don't go analysin'....there's no reason why
Don't go presupposin'....it's a self inflicted lie
You're a woman baby
Oh baby can't you see
That's good enough...that's good enough
Yeah that's good enough for me

I'm not complicated
I just like..... what I see
And you're the kind of trouble girl
Can take a hold of me
'Said I'm not complicated
So let the fun begin
Deal ya hand, but just beware
I play to win

Don't go analysin'....there's no reason why
Don't go presupposin'....it's a self inflicted lie
You're a woman baby
Oh baby can't you see
That's good enough...that's good enough
Yeah that's good enough for me

I play the game of love to win .....and I play without regret
I play the game of love to win .....girl......don't you forget
I'm not complicated.......hope that's good enough for you
Keep on playin' games then girl...I'm tellin' ya we're through

Don't go analysin'....there's no reason why
Don't go presupposin'....it's a self inflicted lie
You're a woman baby
Oh baby can't you see
That's good enough...that's good enough
Yeah that's good enough for me
```

### Ture

*showcases: arrangement / instrumentation · 2:54*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is Bb, and scale is major. Country / Modern Country-Pop.
Global Emotional Progression: The track begins with a cold, isolated atmosphere, reflecting the bitterness of a recent breakup. As the arrangement transitions into the chorus, the mood shifts decisively toward assertive independence and defiant resolution. The second verse maintains this newfound clarity, while the bridge introduces a sense of liberation and open-road freedom. The final sections culminate in a celebratory, rhythmic dismissal of the past, ending with a confident and dry rhythmic fade.
Application Scenarios & Imagery: Nighttime driving on a rural highway with the windows down, neon-lit honky-tonk bars during a mid-tempo dance set, or cinematic montages of a character reclaiming their life and moving out of a small town.
Sonics & Production Profile: The soundstage is characterized by a modern, high-gloss finish with a wide stereo image for the electric guitars and a centered, punchy low-end. The frequency response is sculpted to emphasize the clarity of the vocal transients and the snap of the snare drum. The dynamic aesthetic balances the sparse, intimate textures of the verses with a dense, compressed wall of sound in the choruses to ensure maximum radio impact.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a rugged, gritty baritone with a noticeable rasp in the lower register and a clear, resonant mid-range. The timbre is masculine and authentic, carrying a slight Southern drawl that feels grounded and conversational.
Vocal Style: The delivery is marked by a syncopated, almost percussive phrasing in the verses, using back-phrasing to create a sense of nonchalance. The chorus features a melodic hook motif characterized by an iconic rising 5th leap on the repetitive refrain, creating an immediate earworm effect. The performance employs vocal fry on the start of lower phrases and expressive breathy tail-offs during the bridge to signify emotional release. In the final chorus, the delivery becomes more urgent with staccato bursts and bluesy pentatonic runs during the ad-lib layers.
Harmony/Backing Vocals: Stacked three-part harmonies appear in the choruses, utilizing a "gang vocal" style to increase the anthemic energy. In the bridge and final chorus, additional falsetto layers are added in the background to provide a shimmering top-end texture, while call-and-response ad-libs emphasize the rhythmic hooks in the outro.
Vocal FX: A short slapback delay is used throughout the verses to give the vocal a vintage yet polished feel. The choruses are treated with a lush hall reverb and a 1/8th note synchronized delay on key words. Parallel compression is applied heavily to ensure every syllable cuts through the dense instrumentation.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Attributes: A crisp, fingerpicked acoustic guitar provides the harmonic foundation in the early stages, shifting to heavy, palm-muted rhythmic strumming during the builds. A primary electric guitar with a medium-gain "crunch" tone enters in the choruses, executing downward power chord stabs and a syncopated rhythmic hook that mirrors the vocal melody.
Secondary Layering: A clean, single-coil electric guitar provides ambient, delay-drenched swells in the intro and bridge to create atmospheric depth. A secondary rhythm guitar, featuring a more distorted, thick tone, is layered in the chorus to widen the stereo field. A pedal steel guitar provides melodic counter-fills in the second verse, utilizing long, sweeping legato slides that occupy the high-mid frequency range. In the final chorus, a bright, percussive banjo layer is introduced to add a fast-moving rhythmic subdivision.
Groove & Foundation Progression: The groove begins with a sparse kick-heavy pattern accompanied by a dry, woody snare. As the chorus hits, the drums expand into a full-throttle modern country beat with a driving 4/4 kick and heavy crash cymbal accents on the downbeats. The bass guitar, featuring a distorted and saturated tone, provides a melodic counterpoint in the verses and a thick, sustaining low-end anchor in the choruses. The bridge sees the percussion drop to a simple floor tom pulse before the final snare roll builds into the climax.
Embellishments, Textures & Spatial FX: The intro utilizes an ambient synth pad to create a cold, atmospheric wash that recedes as the dry instruments enter. Sub-bass drops are used to punctuate the transition into each chorus for increased physical impact. Brief organic textures, such as the sound of a distant truck engine fading or a metallic gate latch closing, are used at the very start and end to frame the narrative, while reverse reverb swells lead into the vocal hooks to heighten anticipation.
```

**Input lyrics:**

```
[Verse 1]
Cold night creepin’ through the window crack
Your coat’s still hangin’ where I ain’t goin’ back
Dust on the boots by the bedroom floor
Your perfume’s dead, but the smoke still pours

Runnin’ these miles on a one-way track
Tail lights fade, ain’t lookin’ back
Every “I love you” was a worn-out lie
And I’m done tryna keep that alibi

[Chorus]
Don’t want you, nah, nah, nah
Don’t want you, nah, nah, nah
Not your hands, not your kiss, not the fight we had last night
Don’t want you, nah, nah, nah
Don’t want you, nah, nah, nah
Took my heart off your shelf, girl, and I’m gettin’ mine right

[Verse 2]
Creek bed’s dry where we used to meet
Same place I buried all your receipts
Moon hits hard on the blacktop shine
My bed’s too clean to be back in your crime

That midnight call won’t pull me in
You can talk all you want, I’ll let it spin
‘Cause the only thing worse than losin’ you
Was hangin’ on to what I thought was true

[Chorus – Catchy Hook]
Don’t want you, nah, nah, nah
Don’t want you, nah, nah, nah
Not your hands, not your kiss, not the fight we had last night
Don’t want you, nah, nah, nah
Don’t want you, nah, nah, nah
Took my heart off your shelf, girl, and I’m gettin’ mine right

[Bridge]
Yeah, I’m ridin’ with the windows low
That Southern moon paintin’ silver on the road
You were my vice, but I let that go
Now it’s me, myself, and this glow

[Final Chorus – Ad-libs Layered]
Don’t want you, nah, nah, nah (yeah)
Don’t want you, nah, nah, nah (uh)
Not your hands, not your kiss, not the fight we had last night
Don’t want you, nah, nah, nah
Don’t want you, nah, nah, nah
Took my heart off your shelf, girl, and I’m gettin’ mine right

[Outro]
Nah, nah, nah…
Don’t want you… nah, nah, nah…
```

## R&B

### Feel Alive

*showcases: vocals · 2:52*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is minor. R&B / Neo-Soul.
Global Emotional Progression: The track initiates with a hollow, ethereal atmosphere that mirrors a sense of isolation and suppressed longing. As the arrangement moves into the verses, the mood shifts toward a grounded but melancholic intimacy. The choruses introduce a heightened state of internal conflict, where the addition of harmonic layers creates a bittersweet tension between love and the reality of secrecy. During the bridge, the emotional weight peaks with a sense of urgent desperation before dissolving into a reflective, lingering outro that feels like a quiet departure.
Application Scenarios & Imagery: This music is suited for late-night contemplative listening, rain-blurred cityscapes viewed from a window, or scenes of high-stakes emotional drama. The sonic environment evokes imagery of shadows in a dimly lit room, the contrast of cold blue moonlight against warm skin, and the physical sensation of a heavy heart.
Sonics & Production Profile: The production is defined by a deep, immersive soundstage with significant emphasis on the low-mid frequencies to provide warmth. The high-end is rolled off slightly to achieve a "vintage-modern" silkiness, while the dynamics are carefully controlled to allow the transition from a sparse, clean verse to a densely layered, distorted bass foundation in the chorus without losing clarity.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist exhibits a rich, velvety alto timbre characterized by a smoky resonance in her lower register. Her voice carries a natural grain that conveys a "lived-in" emotional quality, moving seamlessly from a fragile, whisper-thin head voice to a resonant, chesty power.
Vocal Style: The performance follows a conversational and soul-drenched melodic contour, utilizing deep back-phrasing that sits comfortably behind the beat. In the verses, the delivery is soft and breathy with delicate vocal fry on the tail-ends of phrases. The hook motifs are built around haunting minor-third descents and sophisticated pentatonic runs that emphasize the "bittersweet" theme. In the chorus, the delivery becomes more urgent, featuring iconic rising 5th leaps and expressive vibrato that widens as the notes are held.
Harmony/Backing Vocals: Lush, gospel-influenced stacks appear in the chorus to provide a "wall of sound" effect. These are panned wide in the stereo field to envelop the lead vocal. During the bridge and outro, subtle call-and-response ad-libs provide a contrapuntal texture, acting as an internal monologue echoing the main theme.
Vocal FX: The lead vocal is treated with a warm plate reverb and a synchronized 1/8th note tape delay that is automated to swell at the end of poetic lines. A subtle saturation is applied during the chorus to help the voice cut through the distorted bass.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: An ambient, reverb-drenched electric piano pad serves as the harmonic foundation, entering in the intro to establish the melancholic tone. In the verses, a clean, jazz-inflected electric guitar takes over the primary role, performing fingerpicked arpeggios and muted seventh chords with a slight chorus effect.
Secondary: A second rhythm guitar enters exclusively during the choruses to thicken the midrange and provide a driving syncopated pulse. In the bridge, a mournful cello layer provides a low-frequency counter-melody that interweaves with the vocal line. Shimmering, high-register synth bells appear intermittently as "ear candy" to provide a sense of fleeting hope against the darker primary layers.
Groove & Foundation Progression: The track begins without percussion, relying on the fluid timing of the pads. The verse introduces a minimalist groove consisting of a dampened rimshot and a deep, rounded kick drum. Upon reaching the chorus, the foundation transforms with the introduction of a heavily distorted, fuzzy synth bass that provides a gritty, modern edge. The drums expand into a full kit with a "lazy" neo-soul swing, featuring crisp hi-hat rolls and a dragging snare to emphasize the emotional weight.
Embellishments, Textures & Spatial FX: Sub-bass drops mark the transition into each chorus, creating a physical impact. Soft, organic textures like the sound of a distant piano bench creak or the subtle hiss of an analog pre-amp are left in the mix to enhance the "real" and "raw" aesthetic. Transitional synth sweeps and reverse cymbal swells are used sparingly to bridge the gap between the vulnerability of the verses and the power of the choruses.
```

**Input lyrics:**

```
You see the best in me when I don’t,
You speak life when I lose my hope.
You build me up, make me believe,
But you’re not mine, and that cuts deep.
We talk in whispers, hide our truth,
Chasing something we can’t prove.
You say I make you feel alive,
But baby, we’re living a lie.

I’m torn between what’s right and real,
This love is something I can’t conceal.
You’re my calm, my storm, my ache,
The sweetest risk I’ll ever take.

I love you, but I can’t stay,
Wish we could love in the light of day.
You make me better, but it’s bittersweet,
A secret love I can’t keep.
We’re beautiful, but incomplete,
Oh, this love is a bitter secret.

I miss the moments we can’t have,
The dates, the hands I’ll never grasp.
You give me dreams, but not your name,
And I’m so tired of hiding the pain.
You say “one day, it’ll all make sense,”
But I can’t live in past tense.
I crave a love that doesn’t hide,
That meets me where the truth resides.

If loving you means losing me,
Then tell me, what’s my destiny?
You inspire me to grow and shine,
But how long can I call you mine?

I love you, but I can’t stay,
Wish we could love in the light of day.
You make me better, but it’s bittersweet,
A secret love I can’t keep.
We’re beautiful, but incomplete,
Oh, this love is a bitter secret.

You changed my heart, you set me free,
But some love’s not meant to be.
And even when I walk away,
You’ll be the song my soul still plays.
```

### Relation

*showcases: vocals · 1:43*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 72. key is Ab, and scale is minor. R&B / PBR&B.
Global Emotional Progression: The track begins with a shadowy, intimate atmosphere that feels private and hushed. As the verses progress, the emotional weight shifts from curiosity to a heavy, simmering passion. The transition into the hook introduces a dark, anthemic intensity that feels both expansive and immersive, maintaining a steady, sultry pulse that resolves into a lingering, velvet-textured finish during the outro.
Application Scenarios & Imagery: A dimly lit, high-end lounge with velvet furniture, flickering candlelight in a dark room, or a late-night drive through a rain-slicked city with low-hanging clouds.
Sonics & Production Profile: The soundstage is exceptionally deep and wide, emphasizing a high-fidelity low-end response with a sub-bass that feels physical. The mid-range is warm and saturated, while the high frequencies are rolled off slightly to create a "dark" aesthetic, utilizing lush hall reverbs and side-chained compression to create a pumping, breathing sensation throughout the track.
Vocal Details
Vocal Gender & Timbre: Female. The vocalist features a sultry, chocolatey alto timbre with significant weight in the chest voice and a highly controlled, breathy head voice. Her tone is intimate and rich, suggesting a close-mic recording technique that captures every subtle inflection.
Vocal Style: The delivery is characterized by a "behind-the-beat" conversational phrasing, utilizing expressive vocal fry and breathy tail-offs at the end of phrases. A signature hook motif involves a seductive descending minor third leap followed by a slow, wide vibrato. The melodic contour is serpentine, favoring chromatic passing notes that slide between the scale degrees, while the bridge sections feature graceful falsetto flips to emphasize vulnerability.
Harmony/Backing Vocals: Dense, stacked harmonies appear in the hooks, panned wide to create a "wall of sound" effect. In the second verse, whispered vocal doubles are tucked low in the mix to add a sense of proximity, while gospel-influenced melismatic ad-libs provide counter-melodies in the final third of the track.
Vocal FX: The lead vocal is treated with a lush plate reverb and a synchronized 1/4 note delay that trails into the stereo field. A subtle saturator adds harmonic warmth, while a high-shelf EQ dip preserves the "dark" aesthetic of the track without sacrificing intelligibility.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A vintage Rhodes piano with a heavy tremolo effect serves as the primary harmonic foundation, providing dark, jazzy chord voicings throughout the track. A thick, Moog-style analog sub-bass enters during the first verse, providing a foundational pulse that evolves with a low-pass filter sweep as the energy increases.
Secondary: A clean, single-coil electric guitar provides rhythmic interest through fingerpicked arpeggios and palm-muted staccato accents that emphasize the off-beats. In the hooks, an ambient cinematic pad enters the high-frequency domain, creating a shimmering, ethereal ceiling. Subtle, detuned synth leads act as a call-and-response to the vocal lines during the second verse, adding a modern, psychedelic edge.
Groove & Foundation Progression: The groove is anchored by a slow, heavy-hitting programmed beat featuring a dampened, "thuddy" kick drum and a crisp, layered snare with a deep reverb tail. The hi-hats are minimal and swung, using a "sputtering" triplet feel typical of modern trap-soul influences. During the hooks, the percussion expands to include deep, resonant tom-tom hits and sub-drops that underscore the transition points.
Embellishments, Textures & Spatial FX: The track is peppered with atmospheric textures including the sound of a match striking and a soft, localized exhale. Reverse piano swells are used to bridge the gap between the verses and the hook. Deep sub-bass impacts and subtle liquid foley textures create a sense of immersion, while a stereo-panned clock-like ticking provides a rhythmic tension during the breakdown sections.
```

**Input lyrics:**

```
Beautiful loveDark and deep
Verse 1
Your touch is velvet soft, like wine
Tracing constellations on this body of mine
In the low light, our bodies align
As your fingertips run down my spine
Time stops… and you’re the only thing that’s on my mind

Verse 2
Air turns heavy, slow and sweet
Your touch tingles where our bodies meet
Whispers in the dark, you slide in deep
Heat floods my veins, I bite down and keen
You hit every spot, ignite what’s unseen

Hook
Beautiful love, dark and deep
Dark as secret lovers keep
Undress the night, the morning’s gone
In the heat of skin, where the shadows are
```

### You Want Me

*showcases: vocals · 2:40*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 84. key is Eb, and scale is minor. R&B / Contemporary Soul.
Global Emotional Progression: The track begins with a cold, hollow sense of isolation, reflecting a state of late-night contemplation. As the song moves into the pre-chorus, the tension rises through rhythmic density, shifting from vulnerability to a confrontationally firm stance in the chorus. The second verse maintains a higher energy level than the first, signaling growing frustration, before eventually dissolving into a repetitive, hypnotic outro that mirrors a cycle of unresolved disappointment.
Application Scenarios & Imagery: This track is best suited for a dimly lit urban lounge, late-night introspective listening, or a cinematic scene depicting a strained relationship in a rainy metropolitan setting. Imagery involves neon signs reflecting in puddles, the glow of a car dashboard, and the blurred vision of a crowded bar at closing time.
Sonics & Production Profile: The soundstage is deep and cavernous, emphasizing a heavy sub-bass frequency response and a rolled-off high end for a "dark" aesthetic. The production uses side-chain compression to create a pumping, claustrophobic feel, while the mid-range is kept intentionally sparse to allow the vocal performance to sit front and center.

Vocal Details
Vocal Gender & Timbre: Female lead. The vocalist has a rich, sultry mezzo-soprano timbre characterized by a significant amount of "air" in the lower register and a sharp, crystalline clarity in the upper mid-range. The texture is intimate and raw, sounding as if recorded in close proximity to the microphone.
Vocal Style: The performance utilizes a conversational back-phrasing, often dragging slightly behind the beat to emphasize a lethargic, weary mood. Key hook motifs include a recurring minor third interval that leans into a blue note. The chorus features a melodic rising 5th leap on the transition to the higher register, followed by descending pentatonic runs. Articulations include heavy vocal fry at the start of phrases and breathy tail-offs that fade into the reverb tail.
Harmony/Backing Vocals: Lush, thick vocal stacks appear in the chorus to provide a "wall of sound" effect, using close-interval three-part harmonies. During the outro, multiple layers of ad-libs and echoed call-and-response phrases create a disorienting, atmospheric texture.
Vocal FX: The primary vocal is treated with a dark plate reverb and a synchronized 1/4 note delay. In the pre-chorus, a subtle telephone-filter EQ is applied to create a sense of distance before the full-frequency vocal returns for the chorus impact.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A vintage Rhodes electric piano provides the primary harmonic foundation, utilizing dampened, jazzy chord voicings with a slow tremolo effect. This is accompanied by a clean, modulated electric guitar that plays sparse, reverberant plucked notes in the verses, evolving into sustained power chords with light overdrive during the chorus sections.
Secondary: A resonant analog synth pad provides a constant, low-pass filtered drone in the background to fill the stereo width. In the second verse, a secondary synth lead using a sine wave with heavy portamento enters to provide a mourning counter-melody. During the outro, a high-register shimmering bell-like pluck appears to add a fragile, glassy texture.
Groove & Foundation Progression: The foundation is built on a heavy, distorted 808 bass that provides a melodic sub-pulse. The drum pattern features a dry, woody rimshot on the backbeat and a saturated, booming kick drum. The hi-hats use a "triplet-feel" trap influence but are played at a low velocity to keep the R&B swing. The groove drops out entirely during the middle of the pre-chorus for a beat of silence before slamming back in for the chorus.
Embellishments, Textures & Spatial FX: The track utilizes sub-drops and white noise sweeps to signal transitions. A localized foley sound of a car door closing and the distant, muffled sound of a crowded room are used in the transition between the first verse and the pre-chorus to ground the song in its setting. A reverse cymbal swell provides the primary tension-builder leading into each hook.
```

**Input lyrics:**

```
[Verse 1]
In the back of your car
Calling what you want
For you, you say you want to go far
(Mmm)
In the back of the bar
You don't even look
In my eyes, now I'm guessing where you are
Where you are

[Pre-Chorus]
Baby, when you're faded
You make it complicated

[Chorus]
You, you only want me when you're sober
You only want me when it's over
You only want me when you're sober
You, you only want me when they're all gone
If you're messed up then I'm all wrong
No composure
You, you only want me when you're sober
(When you're sober)
(When you're sober)
(You only want me when you're sober)

[Verse 2]
You're messing with my head
Don't you want me instead?
You should want me out with you
You and all your friends
(Ah)

[Pre-Chorus]
Baby, when you're faded
You make it complicated

[Chorus]
You, you only want me when you're sober
You only want me when it's over
You only want me when you're sober
You, you only want me when they're all gone
If you're messed up then I'm all wrong
No composure
You, you only want me when you're sober
(When you're sober)
(When you're sober)
(You only want me when you're sober)
(You only want me when you're sober)

[Outro]
When you're messed up then I'm all wrong
When you're messed up then I'm all wrong
Baby, you only want me when you're sober
(You only want me when you're sober)
(You only want me when you're sober)
(You only want me when you're sober)
(You only want me when you're sober)
```

### 困在彼此尽头

*showcases: vocals · 3:34*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 92. key is Eb, and scale is minor. Jazz / Contemporary R&B.
Global Emotional Progression: The track initiates with an atmospheric, hazy sense of longing, establishing a nocturnal and intimate mood. As the arrangement moves into the verses, the emotion becomes more grounded yet remains fluid, mirroring a state of sensory overload. The pre-choruses introduce a subtle tension and a sense of rising urgency, which swells into the choruses where the emotional intensity peaks through lush harmonic density. The bridge offers a brief, ethereal suspension of time—a "drifting" sensation—before the final chorus transitions from high energy into a gentle, lingering resolution that leaves a sense of warm, quiet surrender.
Application Scenarios & Imagery: This piece is perfectly suited for a high-end urban lounge, a late-night rainy drive through neon-lit streets, or an intimate private gathering. The imagery evokes blurred city lights seen through a window, rising steam from a coffee cup, and the tactile sensation of silk and shadow.
Sonics & Production Profile: The soundstage is wide and three-dimensional, characterized by a deep, velvety low-end and a crystalline, airy high-frequency response. The production utilizes a "wet" aesthetic with generous use of stereo-width enhancers on the pads and a centered, upfront vocal presence. The dynamic range is controlled yet expressive, favoring a smooth, polished commercial finish that emphasizes textural depth over raw aggression.
Vocal Details
Vocal Gender & Timbre: Female lead. The vocalist exhibits a quintessential "lazy" and breathy mezzo-soprano timbre, rich with soft aspirations and a smoky, sophisticated edge that feels whispered directly into the listener’s ear.
Vocal Style: The performance is defined by a heavy use of back-phrasing, deliberately lagging behind the beat to enhance the "lazy" jazz feel. The melodic contour is characterized by seductive chromatic passing notes and slurred legato intervals. A key hook motif involves a soft, breathy "fall-off" at the end of phrases. The rhythmic delivery shifts from conversational in the verses to an urgent, syncopated staccato during the "Sped up" sections, utilizing delicate falsetto flips and a narrow, controlled vibrato to maintain an intimate atmosphere.
Harmony/Backing Vocals: Lush, stacks of four-part jazz harmonies enter during the chorus sections to provide a "wall of sound" effect. In the bridge, distant, wordless vocal oohs and aahs are panned wide with a high-pass filter to create a ghostly, ethereal layer of texture.
Vocal FX: The lead vocal is treated with a vintage tube saturation for warmth, followed by a large hall reverb with a long pre-delay to keep the voice intimate while placing it in a vast space. Synchronized 1/4 note echoes are applied specifically to the "Sped up" hooks to emphasize the sense of disorientation.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A vintage Rhodes electric piano provides the primary harmonic skeleton, utilizing extended jazz chords (9ths and 13ths) with a slow tremolo effect. It is joined by a thick, sub-heavy distorted synth bass that enters in the verse to provide a modern R&B grit.
Secondary: A clean, hollow-body electric guitar enters in the first verse, playing muted, rhythmic "chucks" and occasional sliding ninths. In the chorus, an additional layer of shimmering, chorus-drenched rhythm guitar is added to thicken the midrange. An ambient, low-pass filtered synth pad provides a constant "fog-like" bed from the intro onwards, while a subtle digital bell pluck provides a melodic counter-point during the second verse.
Groove & Foundation Progression: The foundation begins with a minimalist, programmed beat—a crisp rimshot and a deep, rounded kick drum. As the track progresses into the chorus, the groove expands with a live-recorded hi-hat pattern featuring swung sixteenth notes. The bassline moves from sustained root notes in the intro to a more syncopated, "pumping" side-chained rhythm in the choruses, driving the energy without breaking the relaxed tempo.
Embellishments, Textures & Spatial FX: The track is peppered with sophisticated transitions, including reverse reverb swells and soft white-noise rises. During the bridge, a subtle foley sound of a distant, muffled city street adds to the urban atmosphere. In the final chorus, the arrangement briefly "drops out" leaving only the vocals and a thin, filtered piano, before the full instrumentation returns for a final, warm embrace and a slow, filtered fade-out.
```

**Input lyrics:**

```
[Intro]
Lately
Breathing slow
I’m fading
Into your shadow

Don’t fight it
Don’t hide it
Feel it
Let it overflow

[Verse 1]
夜色像流动的雾
你轮廓变得不清楚
指尖触碰的温度
在黑暗里偷偷失控

光影晃动像梦境
我们之间没有边境
语言变得太多余
只剩呼吸在证明

[Pre-Chorus]
Sped up
心跳失去重力
Sped up
意识开始游离

越靠近越危险
却没人想撤退

[Chorus]
Sped sped up
呼吸乱了节奏
你的眼神让我失重

Lights off
界线慢慢失守
我们沉进彼此宇宙

Wrap wrap me up
别让时间逃走
在这瞬间完全占有

No control
让欲望接手
Tonight we lose it all

[Verse 2]
耳边低语像毒
一句一句慢慢侵入
你的名字太模糊
却让我无法退出

假装冷静的表情
藏不住内心的声音
理智正在坠落
只剩本能在回应

[Pre-Chorus ]
Sped up
体温开始堆积
Sped up
感觉过于真实

越抗拒越沉迷
像坠入无底

[Chorus]
Sped sped up
呼吸乱了节奏
你的存在让我失控

Lights off
真相不再保留
我们困在彼此尽头

Wrap wrap me up
别让理智带走
这一刻只想拥有

No control
让爱变成错
Still I want it more

[Bridge]
You got me drifting into you
（慢慢沉入你）
Too close but I can’t undo
（已经没有退路）
You’re the only thing I feel
（唯一的真实）
Even if it’s not real
Don’t slow down
Let it drown
Take me deeper now

[Final Chorus]
Sped… slowed down
呼吸变得温柔
却还留著你的温度

Lights low
世界慢慢静止
只剩心跳在重复

Hold me close
就算是一场错
也想陪你走到尽头

No control
爱没有结果
Still I let it go
```

### 我的宇宙幻觉

*showcases: vocals · 2:17*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 82. key is Ab, and scale is major. Lo-fi R&B / Chillhop.
Global Emotional Progression: The track begins with a spacious, weightless atmosphere in the intro, establishing a sense of late-night solitude. As the verses unfold, the mood shifts into a grounded, intimate reflection characterized by a clean and focused sonic palette. The chorus sections introduce a subtle swell of romantic longing, adding harmonic layers that feel like a warm embrace. This cycle of intimate observation and cosmic yearning continues until the bridge, which briefly heightens the tension of uncertainty, before settling back into a cozy, lingering sense of devotion in the final sections.
Application Scenarios & Imagery: Perfect for a late-night drive through a city illuminated by neon lights or a quiet evening spent watching the stars from a balcony. The music evokes imagery of celestial bodies drifting in a violet sky and the soft focus of a camera lens capturing a loved one in a crowd.
Sonics & Production Profile: The soundstage is wide and immersive, featuring a prominent mid-range warmth and a gentle roll-off in the high frequencies to avoid any harshness. The production utilizes a soft-knee compression to glue the elements together, resulting in a pillowy, saturated aesthetic that feels both vintage and polished.

Vocal Details
Vocal Gender & Timbre: A female vocalist provides a performance defined by a velvety, light, and smoky timbre. Her voice is characterized by a high degree of breathiness, creating an immediate sense of proximity, as if she is whispering directly to the listener.
Vocal Style: The delivery is conversational and relaxed, featuring intentional back-phrasing that sits slightly behind the beat for a soulful feel. The hook motifs are built around elegant pentatonic runs and a recurring melodic motif involving a major 6th interval that creates a sense of hopeful suspension. Performance articulations include delicate vocal fry at the start of phrases and graceful falsetto flips at the end of longer notes, punctuated by soft, audible exhales that emphasize the track's romantic vulnerability.
Harmony/Backing Vocals: Lush, multi-tracked vocal stacks appear in the chorus sections, providing a thick, choral foundation that supports the lead. These harmonies are panned wide and heavily filtered to sound distant and ethereal, acting more like a synth texture than distinct voices.
Vocal FX: The lead vocal is treated with a vintage tape saturation for warmth and a long-tail hall reverb with a high-cut filter to place the singer in a dreamy, cavernous space. Synchronized eighth-note delays are applied to specific phrase endings to create a trailing, echoing effect.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A clean, jazz-inflected electric guitar serves as the primary melodic engine, performing gentle fingerpicked arpeggios and soft, four-note chord stabs. The guitar tone is liquid and warm, utilizing a subtle chorus effect to enhance the dreamy atmosphere.
Secondary Layering: An ambient, slow-attack synth pad provides a constant wash of sound in the intro and choruses, creating a sense of "cosmic" depth. During the chorus, a second rhythm guitar enters, playing muted, syncopated strums that add a layer of rhythmic density and physical warmth. Muted mallet hits and soft celeste chimes appear during the bridge to provide a shimmering, star-like melodic counterpoint to the vocal melody.
Groove & Foundation Progression: The foundation is built upon a deep, rounded electric bass guitar that provides a melodic, walking low-end during the verses and switches to a more sustained, sub-heavy role in the choruses. The drum programming consists of a classic lo-fi kit with a muffled kick, a low-tuned snare with a short decay, and crisp, closed hi-hats playing a swung sixteenth-note pattern. The groove remains steady and hypnotic, though the kick drum becomes slightly more driving during the chorus sections to elevate the energy.
Embellishments, Textures & Spatial FX: Subtle cosmic textures, such as resonating synth sweeps and granular glitches, are peppered throughout the arrangement to mirror the lyrical themes of space. A faint, localized sound of distant city traffic hums briefly during the intro and outro to ground the track in a real-world environment. Transition points are marked by soft reverse cymbal swells and low-frequency impacts that provide a gentle sense of arrival without disrupting the chillhop aesthetic.
```

**Input lyrics:**

```
我几乎忘了 爱情最初的滋味
大脑缺氧 心跳漏了一拍
时间慢下来 空气静得奇怪
只剩下你 在我瞳孔里徘徊

人群都模糊 声音都遥远
就像戴上 以你命名的眼镜
只要看见你 一切变得清晰
再也分不清 现实或梦境

爱是不是这样的感觉
明明想靠近 却又退一步收敛
你的眼睛像宇宙无边
我只是一颗 绕著你旋转的孤单小碎片

爱是不是这样危险
一句good night  就能让我失眠好几夜
如果可以走进你心田
哪怕只占一页 也愿被你看见

James Webb传回 无垠宇宙画面
银河闪烁 像你眼神的侧面
我不仰望星空 也不再问从前
我只想读懂你的心田

爱是不是这样的感觉
明明想靠近 却又退一步收敛
你的眼睛像宇宙无边
我只是一颗 绕著你旋转的孤单小碎片

害怕你看穿 我所有不安
所以把想念藏在句点以后慢慢延
在你身边每一秒都像失重危险
却不愿回到 没有你的地平线

我几乎忘了 爱情最初的滋味
直到遇见你 一眼沦陷不后悔
```

## Bossa Nova

### Behind The Glass

*showcases: vocals · 2:25*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is Gb, and scale is major. Bossa Nova / Contemporary Jazz.
Global Emotional Progression: The track initiates with a serene, academic stillness that gradually transitions into a grounded, sensory-focused warmth. The verses maintain a reflective and inquisitive curiosity, while the choruses bloom with a clarifying emotional resolution. The bridge introduces a brief moment of European sophistication and intimacy, leading into a slower, more deliberate final chorus that feels like a physical release, eventually dissolving into a quiet, grounded whisper in the outro.
Application Scenarios & Imagery: A late-night session in a wooden-floored library lit by a single desk lamp, the scent of old paper, or a barefoot walk across a cool tile floor at dawn. It evokes the transition from over-analysis to physical presence.
Sonics & Production Profile: The soundstage is intimate and "close-mic'd," emphasizing the tactile transients of finger pads on strings and piano hammers. The frequency response is rich in the low-mids to provide a woody, organic foundation, while the high-end is rolled off slightly to create a vintage, velvety texture. Dynamics are highly reactive, following the natural breath and touch of the performers.

Vocal Details
Vocal Gender & Timbre: A dual-vocal arrangement featuring a Primary Female Mezzo-Soprano and a Secondary Male Baritone. The female lead has a smoky, silk-like texture with a prominent "air" quality, while the male voice, appearing in the bridge and outro, provides a grounded, resonant chest tone that acts as a stabilizing anchor.
Vocal Style: The delivery utilizes conversational back-phrasing, often landing just behind the beat to emphasize the relaxed Bossa Nova swing. A signature hook motif involves a descending major third followed by a chromatic rise to the tonic during the chorus. The performance features delicate vocal fry in the lower register and graceful falsetto flips at the end of inquisitive phrases. The bridge features a transition to a more fluid, legato phrasing in French, while the final chorus employs a slower, more elongated rhythmic delivery.
Harmony/Backing Vocals: Lush, four-part vocal pads emerge in the second chorus, utilizing a "Bossa-jazz" voicing with added 9ths and 13ths. These are tucked back in the mix to provide a soft harmonic cushion rather than a sharp rhythmic counterpoint.
Vocal FX: A vintage warm tube-preamp saturation is applied to both voices. A short, dark room reverb provides a sense of a physical space, while the outro utilizes a high-pass filter and increased compression to enhance the intimacy of the whispered directives.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A concert grand piano and a nylon-string acoustic guitar share the harmonic duties. The guitar leads with traditional Bossa Nova comping—syncopated thumb-bass notes and three-finger chord stabs. The piano provides melodic counterpoint with high-register clusters and ornamental grace notes that mimic the "gleam" of a library setting.
Secondary: A soft upright bass enters during the first verse, playing a consistent two-beat feel with deep sustain. In the bridge, a melodic cello layer is introduced to provide a mournful but steady counter-melody to the French vocals. The piano transitions from rhythmic comping to longer, more fluid arpeggios during the slower final chorus to emphasize the shift in tempo and mood.
Groove & Foundation Progression: The groove is built on a sophisticated, understated percussion section featuring a cabasa and a high-pitched wooden rim-shot on beats two and four. The bass maintains a gentle sway, never becoming aggressive. In the final chorus, the percussion drops out entirely, leaving only the primary harmonic instruments to provide a rubato-style rhythmic foundation that feels heavy and grounded.
Embellishments, Textures & Spatial FX: Subtle chimes appear during the mention of "light" in the second verse. The recording captures the mechanical noise of the piano pedals and the sliding of fingers on the guitar strings to enhance the "everything that's real" theme. The outro features a localized foley sound of a wooden door gently latching, followed by the sound of a soft, rhythmic intake of breath, positioned centrally in the stereo field.
```

**Input lyrics:**

```
(Verse 1)
Sylvia asked from behind the glass
Is there no way out of the mind
The books were stacked, the shelves were full
But the door she could not find
(Verse 2)
The wolf climbed up the tower stairs
One more page, one more light
The library gleamed, the stockings shone
But no one slept at night
(Chorus)
The way out of the mind
Is not another thought
It’s the floor beneath your feet
The strings your fingers caught
It’s the needle and the breath
The toes you finally feel
The way out of the mind, my love
Is everything that’s real
(Verse 3)
Phoebe sat down on the wood
No shoes, no suit, no name
She closed her eyes, she found a chord
And nothing was the same
(Bridge)
Ferme la porte de la tour
Descends pieds nus ce soir
Le loup n’a plus besoin de lire
Il a besoin de voir
(Last Chorus)
The way out of the mind
Is not another word
It’s the song you finally sing
After all the ones you’ve heard
It’s one last dance with her
Before you close your eyes
The way out of the mind, my love
Is where the body lies
(Outro)
Go sing, Daniel.
Feel your toes.
One last dance.
```

### Drifting Slow

*showcases: arrangement / instrumentation · 3:17*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 84. key is Db, and scale is major. Bossa Nova / Samba-Canção.
Global Emotional Progression: The track begins with a bright, sun-soaked morning atmosphere, establishing a serene and carefree emotional baseline. During the initial verses, the mood is intimate and contemplative, transitioning into an airy, uplifted state of joy during the choruses. The bridge introduces a subtle rise in rhythmic urgency and emotional intensity, reflecting a more passionate embrace of the moment, before returning to a grounded, peaceful resolution in the final passages.
Application Scenarios & Imagery: A sophisticated rooftop lounge in Ipanema at dawn, a high-end boutique hotel lobby, or a quiet, sunlit kitchen while steam rises from a fresh cup of coffee.
Sonics & Production Profile: The soundstage is wide but shallow, creating a front-row seat experience that emphasizes the transients of the nylon strings. The frequency response is characterized by a "velvet" high-end and a rich, woody low-mid range. Dynamics are preserved with high headroom, ensuring the delicate interplay between the percussion and the vocal remains transparent and breathy.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). The vocalist features a light, mezzo-soprano range with a classic "cool jazz" timbre. Her voice is characterized by a high degree of breathiness and a soft, silk-like texture that feels personal and unforced.
Vocal Style: The performance is marked by a conversational back-phrasing, often landing slightly behind the beat to enhance the relaxed bossa nova feel. A signature hook motif is established through a recurring descending minor third interval at the end of phrase lines. She employs graceful falsetto flips on higher melodic peaks and maintains a narrow, controlled vibrato that only blooms on long-held notes. In the bridge, her delivery becomes more rhythmic and staccato, contrasting with the fluid, legato phrasing of the verses.
Harmony/Backing Vocals: Lush, three-part vocal harmonies appear during the chorus sections, utilizing a "block chord" arrangement style to create a wall of soft, choral warmth. In the bridge, call-and-response backing vocals provide a rhythmic counterpoint, echoing the lead singer’s energy with "ooh" and "aah" textures.
Vocal FX: A vintage plate reverb with a high-pass filter is applied to prevent muddiness, giving the vocals a shimmering, ethereal quality. A subtle tape saturation is used to add harmonic thickness, mimicking the warmth of 1960s analog recordings.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation is built upon a nylon-string acoustic guitar, played with classic bossa nova "violão" techniques including complex thumb-driven bass lines and syncopated finger-picked clusters. This instrument remains constant, providing the essential harmonic movement and rhythmic "swing."
Secondary: An upright bass enters in the first verse, providing a deep, resonant foundation with a soft attack. A grand piano is introduced in the chorus, performing sparse, quartal jazz voicings in the upper register to add a shimmering melodic layer. During the bridge, a secondary rhythmic acoustic guitar enters, playing muted percussive strums to increase the track's drive. A melodic flute appears in the transitions, acting as a call-and-response element to the vocal lines.
Groove & Foundation Progression: The groove is defined by a traditional Brazilian percussion set, featuring a steady surdo-like pulse on the bass drum and a crisp, consistent cross-stick rimshot on the snare. A soft shaker provides a continuous sixteenth-note subdivision that maintains the momentum. The energy expands in the chorus through the addition of a pandeiro and light triangle accents, while the bridge sees a more active, syncopated bass line that drives the track toward its emotional peak.
Embellishments, Textures & Spatial FX: Subtle chimes and wind bells are used to mark the transition into the chorus, creating a "magical" sparkling texture. Gentle environmental foley of distant tropical birds is layered very low in the mix during the intro and outro to ground the listener in a specific geographic setting. The spatial arrangement uses a natural room-depth approach, with the piano panned slightly to the left and the secondary guitar to the right to create an immersive, balanced acoustic field.
```

**Input lyrics:**

```
[Verse]
Sunshine spilling on the morning floor
Rainbows hanging like an open door
Birds are gossiping
Who needs more?

[Chorus]
Sunshine
Rainbows
Love
It’s enough
Happiness flying like a dove
Sunshine
Rainbows
Love
Oh
It’s enough

[Verse 2]
Clouds are lazy
Drifting slow
The river hums where the flowers grow
Do you feel it? That golden glow

[Prechorus]
Every step feels like a dance
Every breath
A second chance

[Chorus]
Sunshine
Rainbows
Love
It’s enough
Happiness flying like a dove
Sunshine
Rainbows
Love
Oh
It’s enough

[Bridge]
Ooh-yeah
Feel the sun
Feel the rain (ooh-yeah!)
Heartbeats rising
Lose the pain
Catch the moment
Hold it tight
Love is shining
Day and night
```

### Joy And Honour

*showcases: vocals · 4:14*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is Db, and scale is major. Bossa Nova / Brazilian Pop.
Global Emotional Progression: The track initiates with a serene and meditative intro, establishing a foundation of tranquility. As the verses unfold, the mood evolves into a state of contentedness and gratitude. Upon reaching the choruses, the energy lifts into a subtle, confident radiance, reflecting inner strength. The bridge introduces a rhythmic persistence that feels grounded and resilient, eventually resolving back into a spacious, peaceful, and affirmed conclusion.
Application Scenarios & Imagery: Ideal for sunrise yoga sessions, high-end wellness retreats, or a sun-drenched balcony overlooking a calm ocean. The music evokes imagery of golden hour light filtering through tropical leaves and the sensation of a warm, steady breeze.
Sonics & Production Profile: The soundstage is wide and airy, focusing on high-fidelity clarity and a transparent frequency response. There is a prominent emphasis on the 2kHz to 5kHz range to highlight vocal intimacy, while the low-end is tight and controlled. The dynamic aesthetic is fluid and organic, avoiding aggressive limiting to preserve the natural transients of the percussion.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist features a clear, crystalline soprano timbre with a silky, "straight-tone" quality. The voice is lean and agile, possessing a youthful yet grounded texture that feels exceptionally intimate and close to the microphone.
Vocal Style: The delivery is characterized by a relaxed, behind-the-beat Bossa Nova swing. The melodic contour utilizes elegant descending pentatonic runs at the end of phrases. A signature hook motif involves a gentle rising 4th interval that resolves with a soft breathy tail-off. The performance balances conversational phrasing in the verses with more sustained, lyrical legato notes in the chorus, occasionally employing a delicate vocal fry on lower introductory notes for added warmth.
Harmony/Backing Vocals: Soft, two-part unison harmonies appear in the second half of the chorus to add a shimmering width. During the outro, multiple layers of "ooh" and "aah" textures are panned wide to create a choral, ethereal atmosphere that supports the final spoken-style affirmations.
Vocal FX: A transparent large-hall reverb provides a sense of vastness, complemented by a synchronized 1/8th note tape delay with low feedback to add depth. De-essing is applied meticulously to maintain a smooth top end during sibilant passages.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A nylon-string acoustic guitar serves as the primary harmonic engine, utilizing classic Bossa Nova comping patterns with lush, extended jazz chords (9ths and 13ths). The articulation is soft-plucked with the pads of the fingers to ensure a round, mellow attack.
Secondary: A Rhodes electric piano enters in the second verse, providing bell-like tine accents and celestial clusters in the upper register. A solo flute appears during the bridge, performing bird-like trills and legato melodic flourishes that dance around the vocal line. In the final chorus, a subtle string pad provides a foundation of harmonic warmth, lifting the arrangement without overcrowding the frequency spectrum.
Groove & Foundation Progression: The foundation is built on a traditional Bossa Nova drum pattern performed with wooden brushes on the snare and a soft, felt-beater kick drum hitting on beats one and three. A warm, melodic fretless bass provides a fluid, liquid-like low end that avoids sharp attacks, instead sliding between root notes and fifths. In the bridge, a cabasa and a triangle are introduced to increase the rhythmic subdivision, creating a sense of forward motion and persistence.
Embellishments, Textures & Spatial FX: Subtle chimes and finger cymbals provide occasional high-frequency sparkle at the transition points between sections. A gentle shaker remains constant but fluctuates in volume to dictate energy shifts. The outro features a localized foley effect of a distant, calm stream to reinforce the lyrical themes of flow and nature, while a soft sub-bass bloom marks the final resolution of the track.
```

**Input lyrics:**

```
I breathe in peace, the simple joy of now I honor all the wisdom that the present allows My cup is full, I have everything I need right here Surrounded by soft connections, holding love so near I give and receive freely, a beautiful, steady flow I am seen, I am cherished, loved deeply as I go.

Now the ground is firm beneath my gentle feet A powerful knowing, perfectly complete. I listen close to the inner guidance I hold true.

I am steady light, unbothered by the noise outside I am confidence, where courage loves to reside I step forward now, with clear intent and heart ablaze I move mountains gently, in a thousand patient ways I succeed now, I achieve now, the outcome is clear and bright My inner strength is my constant guiding light.

My intuition speaks softly, a wisdom that guides my way The Universe unfolds beauty, every single day Everything arrives for me, in the perfect, knowing time I trust the flow of life, a rhythm so sublime My body is resilient, strong and full of grace My spirit is vibrant, illuminating every space.

Like a river flowing, perfectly on time Every drop is necessary, a beautiful design I release all worry, all the need to rush I am brave, I am persistent, and success is in my touch. My whole being is filled with strength, glowing, alive, and free.

I am steady light, unbothered by the noise outside I am confidence, where courage loves to reside I step forward now, with clear intent and heart ablaze I move mountains gently, in a thousand patient ways I succeed now, I achieve now, the outcome is clear and bright My inner strength is my constant guiding light.

"Strong and peaceful..." "Loved and thriving..." "The perfect time is always now..." "It is done, it is complete, it is well..."
```

### Winking

*showcases: vocals · 2:52*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is F#, and scale is major. Bossa Nova / Acoustic Folk.
Global Emotional Progression: The track initiates with a serene and pastoral intimacy, establishing a grounded sense of peace during the first verse. As it transitions into the chorus, the arrangement blossoms into a light, buoyant optimism. This cycle repeats with Verse 2 maintaining a playful lilt, followed by a secondary chorus that feels more expansive. The bridge introduces a brief moment of rhythmic whimsy and tactile curiosity before returning to a final, celebratory chorus that resolves into a soft, lingering fade-out.
Application Scenarios & Imagery: This composition evokes the visual of a slow-motion afternoon in a sun-drenched meadow. It is perfectly suited for a high-end travel documentary segment, a sophisticated boutique retail environment, or a morning routine playlist designed for stress reduction and mental clarity.
Sonics & Production Profile: The production features a wide, organic soundstage with a high degree of transparency. The frequency response is characterized by a rich, woody low-mid range and a crisp, velvet-like high end that captures the transients of finger-on-string contact. The dynamics are handled with a light touch, emphasizing a "live-in-the-room" feel with significant headroom.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist delivers a breathy, light soprano performance with a naturally honeyed and resonant timbre. The texture is intimate, suggesting a microphone placement very close to the lips to capture every subtle inflection and air movement.
Vocal Style: The performance utilizes a relaxed Bossa Nova "speech-song" delivery, often leaning slightly behind the beat for a cool, effortless feel. The melodic contour features iconic rising 5th leaps at the start of the chorus sections to signal emotional lifting. Melodic runs are primarily pentatonic with occasional chromatic passing notes that add a sophisticated jazz-pop flair. Articulations include graceful falsetto flips on peak notes and expressive, slow-rate vibrato on held vowels.
Harmony/Backing Vocals: Lush, three-part vocal harmonies appear during each chorus, panned wide to create a sense of being surrounded by sound. These harmonies follow the lead melody in parallel motion, providing a "cloud-like" thickening effect.
Vocal FX: A sophisticated hall reverb with a long pre-delay is used to separate the dry lead vocal from the ambient space. A high-shelf EQ boost adds a "silky" air to the top end, while a vintage optical compressor keeps the levels consistent without stripping away the natural performance dynamics.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Basic Attributes: A primary nylon-string acoustic guitar provides the foundational harmonic structure, employing a traditional Bossa Nova "violão" technique with syncopated thumb-bass lines and clustered finger-plucked chords. Its timbre is warm and round, sitting centrally in the mix.
Secondary Layering: A secondary steel-string acoustic guitar enters during the chorus sections, playing high-register arpeggios that shimmer like sunlight on water. A melodic flute or light woodwind counter-melody emerges during the second verse, engaging in a call-and-response dialogue with the vocal line. During the bridge, a melodic glockenspiel or high-tuned percussion element adds a crystalline, "skipping" texture to mirror the rhythmic shifts.
Groove & Foundation Progression: The foundation is built on an upright bass playing a soft, two-beat feel (surdo-style) that anchors the syncopated guitar. The percussion consists of a subtle cabasa and organic woodblock hits that establish a steady but gentle pulse. In the bridge, the percussion becomes more tactile, utilizing rim shots and finger snaps to create a playful, grounded rhythm before the full groove re-engages for the final chorus.
Embellishments, Textures & Spatial FX: Subtle field recordings of a gentle meadow breeze and distant, melodic bird chirps are woven into the background of the verses to enhance the naturalistic imagery. The transitions between sections are marked by soft wind chime accents and light cymbal swells played with brushes, ensuring a seamless flow that avoids abrupt changes in energy.
```

**Input lyrics:**

```
[Verse]
Blue sky whispers don't be late
Green grass stretches like a plate
The sun is winking through the trees
A day like this is made to tease

[Chorus]
Blue sky green grass sunny day
Let the world spin the other way
No need to run no need to stay
Just blue sky green grass sunny day

[Verse 2]
Birds are laughing high and wide
Clouds are playing seek and hide
I feel the breeze it tells a joke
The kind that lingers when it's spoke

[Chorus]
Blue sky green grass sunny day
Troubles fade like shadows play
Dance with time let it delay
Just blue sky green grass sunny day

[Bridge]
No map no plan no ticking clocks
Barefoot feet on skipping rocks
Catch the air hold it tight
This is ours this feels right

[Chorus]
Blue sky green grass sunny day
Let the worries float away
The world can wait come what may
Just blue sky green grass sunny day
```

## Jazz

### Golden age blues

*showcases: arrangement / instrumentation · 2:37*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 78. key is Eb, and scale is major. Shanghai Jazz / Lo-fi Soul.
Global Emotional Progression: The track initiates with a nostalgic, hazy atmosphere that evokes a sense of looking through an old photograph. As the composition moves through the verses, the mood shifts into a gentle, romantic intimacy characterized by warmth and rhythmic sway. During the chorus, the emotional resonance expands into a plush, comforting embrace, maintaining a steady, sophisticated grace. The bridge introduces a brief, shimmering moment of reflection before returning to the core warmth, finally dissolving into a delicate, lingering tail of peaceful resignation.
Application Scenarios & Imagery: A candlelit room in a 1930s Shanghai parlor, rain streaking across a window overlooking neon city lights, or a quiet late-night drive through a sleeping metropolis.
Sonics & Production Profile: The production features a characteristic lo-fi warmth with a rolled-off high-end frequency response to mimic vintage phonograph aesthetics. The soundstage is wide but centered, placing the vocals in a front-and-center position with a rich, saturated mid-range. Dynamic transitions are smooth and rounded, prioritizing a soft, analog tape-style compression that glues the jazz instrumentation to the subtle vinyl crackle and lo-fi textures.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist possesses a quintessential "Shanghai Jazz" timbre—a silky, light soprano with a distinctive vintage vibrato and a breathy, delicate texture. The voice carries a subtle "old-radio" saturation that adds to its timeless, classic quality.
Vocal Style: The delivery is characterized by a conversational back-phrasing, often landing slightly behind the beat to enhance the relaxed, soul-infused feel. The performance features iconic rising minor third leaps and graceful pentatonic runs that resolve into soft vocal fry at the ends of phrases. The rhythmic interaction is fluid, moving from staccato, playful enunciations in the verses to long, soaring legato lines in the chorus, punctuated by expressive, slow-oscillating vibrato on held notes.
Harmony/Backing Vocals: In the chorus sections, a lush trio of female backing vocals provides a "wall of silk" effect using close-harmony jazz voicings (added 6ths and 9ths). These layers are panned wide to create a spatial contrast with the centered lead.
Vocal FX: The lead vocal is treated with a combination of a vintage slapback delay and a deep, dark plate reverb. A subtle band-pass filter is applied during the intro and outro to simulate the sound of a distant gramophone.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic/Melodic Instruments: A clean, hollow-body electric jazz guitar serves as the primary harmonic driver, utilizing thumb-plucked octaves and lush, extended jazz chords with a soft attack. Its timbral evolution involves a gradual increase in a subtle chorus effect as the song progresses. An upright bass provides a deep, woody foundation, playing a consistent two-feel that transitions into a walking pattern during the bridge.
Secondary Layering: A mellow, Rhodes-style electric piano enters in the first verse, providing sparkling, high-register bell-like accents. In the chorus, a muted trumpet with a Harmon mute adds a sophisticated, reedy counter-melody that engages in a call-and-response with the vocal. A subtle string quartet layer appears during the bridge, providing long, sweeping legato pads that swell and recede to add cinematic depth.
Groove & Foundation Progression: The groove is rooted in a classic lo-fi hip-hop aesthetic blended with traditional jazz swing. The foundation is built on a sampled, dusty drum break featuring a heavy kick and a crisp, side-stick snare. The percussion remains steady but incorporates rhythmic displacement and ghost notes on the hi-hat to maintain a human feel. The energy peaks during the final chorus where the bass becomes more melodic and the kick drum gains a slightly punchier presence.
Embellishments, Textures & Spatial FX: The track is punctuated by vintage vinyl surface noise (dust and crackle) to reinforce the classic lo-fi genre identity. Shimmering celesta flourishes act as transitions between sections, mimicking the visual of starlight. Brief, localized environmental foley—such as the faint click of a lighter and a soft exhale—are used in the intro to set the scene, while a distant, muffled horn honk provides a sense of urban space in the bridge. All elements are unified by a warm, analog-saturated bus compression.
```

**Input lyrics:**

```
（主歌 1）
晚风轻轻 推开纱帘的梦，
留声机哼着 未完的重逢。
你站在街角 微笑像旧信封，
写着“一切安好” 在纸边角种一朵虹。

（主歌 2）
路灯低语 把影子拉成线，
系住两颗心 不必说再见。
我唱起那首 你曾哼过的调，
音符落成星 在夜色里轻轻绕。

（副歌）
啊～ 暮色是柔软的绒，
裹着暖意 向你轻轻涌。
若你听见 这低低的歌，
就让笑意 在眼角停泊。
啊～ 时光不必匆匆，
我们自有 月光的从容。

（桥段）
雨后的石板 映着霓虹微光，
像你眼底 那抹温柔的亮。
我不问明天 只守此刻长，
用歌声 把夜 缝成一件衣裳。

（副歌·再现）
啊～ 暮色是柔软的绒，
裹着暖意 向你轻轻涌。
若你听见 这低低的歌，
就让笑意 在眼角停泊。
啊～ 时光不必匆匆，
我们自有 月光的从容。

（尾声·轻吟）
啦… 暮色绒光，
啦… 你在身旁，
啦… 歌未唱完，
夜已芬芳……
```

### 一干二净

*showcases: regional genres (Chinese) · 2:09*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is major. Mandopop / Indo-Pop Ballad.
Global Emotional Progression: The track begins with a somber, cinematic stillness, establishing a mood of heavy contemplation. As the arrangement transitions from the initial verse into the pre-chorus, the emotional weight shifts from passive sadness to a structured, firm ultimatum. The chorus introduces a surge of melodic resolve, feeling both grand and heartbreaking. The second half of the song maintains a steady, rhythmic tension that mirrors a state of waiting, eventually culminating in a final high-energy chorus before retreating into a quiet, unresolved instrumental fade.
Application Scenarios & Imagery: Ideal for high-budget television drama soundtracks during scenes of romantic betrayal or heavy rain-soaked cityscapes at night. It evokes imagery of someone standing alone in a dimly lit, modern apartment, looking out at a blurred skyline while contemplating a life-changing decision.
Sonics & Production Profile: The soundstage is characterized by a deep, three-dimensional depth, prioritizing a lush lower-mid frequency response to support the Indonesian-Pop aesthetic. The production is polished and commercial, featuring a transparent high-end that allows the vocal transients to cut through. Dynamics are expansive, moving from a narrow, intimate mono-centered intro to a wide, panoramic stereo spread during the fully orchestrated choruses.
Vocal Details
Vocal Gender & Timbre: A female vocalist leads the track with a silken, mahogany-toned timbre typical of contemporary Southeast Asian pop divas. Her voice possesses a rich chest resonance in the lower octaves, transitioning into a crystalline, slightly nasal head voice that remains stable even under high emotional pressure.
Vocal Style: The performance begins with a conversational, breathy delivery, utilizing heavy vocal fry on the tail-end of phrases for an intimate, "close-mic" effect. As the song progresses, she employs iconic rising 5th leaps during the hook motifs to signal emotional peaks. Her phrasing is slightly behind the beat, creating a soulful, melancholic drag that interacts fluidly with the clean guitar. In the climactic choruses, she utilizes expressive vibrato with a wide oscillation and graceful falsetto flips to emphasize the lyrics' gravity.
Harmony/Backing Vocals: Lush, three-part vocal stacks appear in the chorus to provide a "wall of sound" effect. These are panned wide (80% left and right) to create a protective cradle around the lead vocal. In the bridge, a single tracked unison harmony adds a haunting, ghost-like doubling effect to emphasize the sense of inner conflict.
Vocal FX: The primary vocal is treated with a warm hall reverb and a synchronized quarter-note ping-pong delay that is tucked low in the mix. A vintage-style compressor is used to smooth out the transition between the soft verses and the powerful belted choruses, ensuring every syllable remains legible.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The song is anchored by a delicate, clean electric guitar playing jazz-influenced chord voicings with a soft chorus effect. This is paired with an ambient synth pad that provides a subterranean, breathing harmonic floor from the intro onwards. The guitar uses fingerstyle articulation, emphasizing the resonance of the open strings to create a sense of space.
Secondary: A grand piano enters in the first verse, providing low-register octaves to reinforce the root notes. By the second verse, a distorted electric bass is introduced, providing a gritty, modern contrast to the clean guitar and adding a sense of brewing tension. In the chorus, a second rhythm guitar with a light overdrive enters, playing sustained power chords to thicken the midrange. Orchestral string layers emerge during the bridge, providing a cinematic swell that carries the track into its final resolution.
Groove & Foundation Progression: The rhythm begins as a purely atmospheric pulse with no percussion. A subtle, dampened kick drum enters in the pre-chorus to establish a slow heartbeat. The full groove locks in during the chorus, featuring a deep, sub-heavy kick and a layered snare with a digital "clap" transient to align with modern Indo-Pop production. The bass guitar drives the energy with syncopated 8th-note patterns that bridge the gap between the drums and the melodic elements.
Embellishments, Textures & Spatial FX: The track utilizes high-frequency glockenspiel hits to add a "stardust" texture during transition points. Reverse cymbal swells and sub-bass drops are strategically placed to signal the transition into the chorus. To enhance the rainy, urban atmosphere, brief foley sounds of distant traffic and soft water droplets are localized in the far-left stereo field during the intro and outro, providing a grounded, cinematic environment.
```

**Input lyrics:**

```
这段爱情已可盖棺论定
是你负了心
我却狠不下心做到一干二净

这份感情已难掩饰太平
是你伤了心
我还恻隐之心
还在纠缠不清

我给了你缓刑
暂缓执行那些你应得的报应
看你能否转意回心

缓刑确定
可不是原谅了那些你荒唐的罪行
不要白费我的苦心

风平浪静
只是在察言观行
这举棋不定
就我还在等你的悔过自新

我给了你缓刑
暂缓执行那些你应得的报应
看你能否转意回心

缓刑确定
可不是原谅了那些你荒唐的罪行
不要白费我的苦心
```

### 舍不得

*showcases: regional genres (Chinese) · 3:58*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 85. key is F, and scale is major. Eastern New Folk / Zen Chinese Style.
Global Emotional Progression: The track initiates with a state of profound stillness and Zen-like clarity, establishing a meditative atmosphere of solitude. As the verses unfold, the emotional tone transitions into a weary, intellectualized sorrow, mimicking the process of sorting through memories. A gradual rise in tension occurs during the pre-chorus, leading to a chorus that feels like a philosophical release—a cathartic yet restrained outpouring of grief. The bridge intensifies this internal conflict before the outro returns to a cold, snowy silence, signifying a final, resigned acceptance.
Application Scenarios & Imagery: Perfectly suited for high-end cinematic dramas focusing on internal monologues, traditional tea houses in winter, or minimalist art galleries. The imagery evokes a scholar’s study filled with old scrolls, frost-covered windows, and the visual of single ink droplets dissolving in clear water.
Sonics & Production Profile: The soundstage is vast and crystalline, characterized by high-fidelity acoustic captures and a wide stereo image. The frequency response prioritizes a transparent high-end to capture the breath of the woodwinds and the metallic shimmer of strings, while the low-mids are kept lean to maintain the "Zen" aesthetic of spatial emptiness.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a light, elegant tenor voice with a high degree of "air" in the delivery. The timbre is reminiscent of traditional scholar-singing, possessing a silk-like smoothness but with a modern, intimate proximity that suggests the singer is whispering directly into the listener's ear.
Vocal Style: The performance is marked by conversational back-phrasing, often landing slightly behind the beat to emphasize a sense of lethargy and rumination. The melodic contour is characterized by elegant pentatonic runs and graceful falsetto flips on the ends of long vowels. A signature hook motif involves a recurring minor third dip that resolves upwards, mimicking a sigh. The delivery utilizes significant vocal fry in the lower registers of the verses to convey emotional exhaustion, transitioning into a pure, vibrato-rich head voice during the high-register peaks of the chorus.
Harmony/Backing Vocals: Minimalist unison doubling occurs in the second verse to add "weight" to the introspection. During the chorus, ethereal, wordless falsetto layers are positioned far back in the mix, acting as a human synth pad that mirrors the lead melody's trajectory.
Vocal FX: A sophisticated shimmer reverb with a long decay time is applied to create a "cathedral of the mind" effect. High-shelf EQ boosting enhances the breathiness, while a tempo-synced ping-pong delay is used sparingly on specific tail-offs to suggest the echoing of thoughts in an empty room.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A meticulously recorded Xiao (vertical bamboo flute) acts as the primary melodic soul of the track, providing breathy, legato phrases that weave between vocal lines. It is joined by a Guqin (seven-string zither), which provides the primary harmonic foundation through deep, resonant plucked notes and sliding portamento techniques that ground the composition in ancient tradition.
Secondary Layering: A soft, felt-dampened upright piano enters in the first verse, playing sparse, widely-spaced chords to provide a modern harmonic anchor. In the chorus, a section of legato cello provides a mournful counter-melody in the lower-mid frequency range, adding a layer of European classical sophistication to the Eastern folk base. A Guzheng (plucked zither) provides rapid, shimmering tremolo flourishes during the transitions, acting as a textural bridge between structural segments.
Groove & Foundation Progression: The rhythmic foundation avoids traditional drum kits, instead utilizing a deep, dampened frame drum that provides a heartbeat-like pulse starting from the pre-chorus. The bass is handled by the low-frequency resonances of the Guqin and a subtle sub-bass sine wave that mirrors the frame drum’s impact. The groove is fluid and non-linear, expanding in density during the chorus with the addition of light woodblock accents and receding to near-total silence in the outro.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by "water-drop" tuned percussion and the occasional ringing of a distant Tibetan singing bowl to enhance the Zen atmosphere. Subtle environmental foley of a crackling fire is localized in the far left of the stereo field during the second verse to add warmth. A reverse-reverb swell on the Xiao leads into the final chorus, creating a momentary vacuum of sound before the climax. The outro features a specialized "granular ice" texture—a high-frequency synth jitter that evokes the sound of snow falling on frozen ground.
```

**Input lyrics:**

```
**(Verse 1)**
将旧衫　整理成　一场得体　的葬礼
把记忆　修剪成　无关痛痒　的传记
客厅里　这阵风　吹乱了　谁的眉宇
原来　舍不得　才是一种　最卑微的　权力

呼吸中　还有你　剩下微弱　的频率
像灰尘　在光影　寻找定居　的证据
我也想　很科学　计算出　遗忘规律
却发现　这逻辑　本身就是　一场情绪

**(Pre-Chorus)**
听说过　细胞会　更替出　新的身躯
为什么　有些痛　却能　免疫　所有痊愈
我越是　想清空　越像在　变相　囤积

**(Chorus)**
忘记你需要多久？　是参透　还是等　肉身腐朽？
是将往事　当成　路过的　海市蜃楼？
还是要把　伤口　钻研成　一种学术
直到把　所有的执著　都熬成　慈悲的　借口

忘记你需要多久？　是一秒　还是等　下个轮回？
当我练习　在那　荒芜中　视死如归
若某天　我不小心　认不出　你的眼泪
那算不算　对这份残缺　最后的　完美

**(Verse 2)**
药水味　渗透进　这场漫长　的宿醉
这世界　太喧嚣　显得遗忘　太昂贵
每个人　都劝我　要学会　进退有据
谁又看见　灵魂里　那道　填不平的　空位

**(Bridge)**
这不是　在比赛　谁能　先放下　负累
我只是　在废墟　供奉　枯萎的　蔷薇
如果　真的忘了　那我　又是谁的　谁
原来　记得你　是我唯一　不肯赦免的　罪

**(Chorus)**
忘记你需要多久？　是参透　还是等　肉身腐朽？
是将往事　当成　路过的　海市蜃楼？
还是要把　伤口　钻研成　一种学术
直到把　所有的执著　都熬成　慈悲的　借口

**(Outro)**
等大雪　落满了　这座　无名的　荒丘
等我　终于学会　对著镜子　挥一挥手
至于　那个答案　究竟　还要等多久
大概要等　这颗心　彻底　虚构
```

## Metal

### Night Battle

*showcases: arrangement / instrumentation · 3:17*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 168. key is Eb, and scale is minor. Power Metal / Melodic Speed Metal.
Global Emotional Progression: The track opens with a sense of impending doom, characterized by a dark, driving momentum that carries through the initial verses. As the song progresses toward the chorus, the mood shifts from predatory tension to a triumphant, anthemic defiance. The bridge introduces a sudden, explosive volatility, shattering the established rhythm before the final prechorus rebuilds a wall of sound, leading to a climactic, high-energy resolution that feels both exhaustive and victorious.
Application Scenarios & Imagery: Ideal for high-fantasy cinematic trailers, fast-paced gaming montages, or a midnight highway drive. The imagery evokes a rain-slicked urban gothic landscape illuminated by neon flashes and rhythmic lightning strikes against a backdrop of ancient, looming architecture.
Sonics & Production Profile: The soundstage is vast and cinematic, emphasizing a wide stereo image for the triple-tracked guitars. The frequency response is sculpted with a significant boost in the 3-5kHz range for biting articulation, balanced by a dense, saturated mid-range. The dynamic aesthetic is intentionally "hot," utilizing parallel compression on the drum bus to ensure the kick and snare punch through the dense wall of distortion.
Vocal Details
Vocal Gender & Timbre: A single male vocalist provides a commanding, heroic tenor performance. The timbre is characterized by a "steel-like" clarity with a resonant chest voice that transitions seamlessly into a piercing, vibrato-rich head voice during higher registers.
Vocal Style: The delivery is urgent and staccato during the verses, utilizing syncopated back-phrasing to create a sense of frantic movement. The hook motifs feature iconic rising 5th leaps at the start of the chorus, followed by soaring melodic arcs that utilize wide, operatic vibrato on sustained notes. The performance incorporates subtle vocal fry on lower-register transitions and ends phrases with graceful, upward falsetto flips for dramatic flair. The rhythmic interaction is tightly locked to the double-kick drum patterns, punctuated by aggressive, guttural emphases on transitional words.
Harmony/Backing Vocals: Dense, four-part vocal harmonies appear in the choruses to create a "warrior choir" effect, panned wide to surround the lead. During the prechorus, lower-octave unisons are added to provide a thickening, menacing texture.
Vocal FX: The primary vocal features a short slap-back delay for presence and a large hall reverb with a high-pass filter to prevent muddiness. A subtle pitch-shifting widener is applied to the chorus harmonies to enhance the sense of scale.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A duo of high-gain electric guitars serves as the core foundation, employing rapid-fire alternate picking and palm-muted pedal tones throughout the verses. During the choruses, these shift to wide-voiced power chords and melodic counter-lines that follow the vocal melody. The primary layer is reinforced by a thick, overdriven bass guitar that provides a percussive, clanking low-mid presence, essential for the genre's "galloping" feel.
Secondary Layering: Atmospheric synthesizers enter during the intro and bridge, utilizing saw-wave pads and bright, digital bells to add a futuristic sheen. A secondary rhythm guitar enters specifically during the chorus sections to provide a wall-of-sound texture, while a high-register lead guitar executes neoclassical shredding flourishes and harmonic squeals between vocal phrases. Orchestral staccato strings appear during the prechorus, acting as a rhythmic reinforcement to the percussion.
Groove & Foundation Progression: The groove is defined by a relentless double-bass drum pattern that maintains a steady sixteenth-note pulse. The snare is tuned high and tight, cutting through the mix with a metallic crack. In the prechorus, the drumming shifts to a "warning drum" motif with heavy floor tom accents and syncopated snare rolls, simulating a tribal war beat. The bridge features a breakdown of the rhythmic grid, with chaotic cymbal chokes and sudden stops before the double-kick resumes its maximum velocity for the finale.
Embellishments, Textures & Spatial FX: The track is punctuated by high-frequency synthesizer sweeps and white noise risers that lead into the choruses. Sub-bass drops are strategically placed at the start of each chorus to emphasize the weight of the "night battle." The bridge incorporates the sound of shattering glass and metallic crashes panned across the stereo field, providing a literal sonic interpretation of the lyrical themes without utilizing continuous background foley. A soaring, twin-guitar harmony solo serves as the emotional peak before the final repetition.
```

**Input lyrics:**

```
[Verse]
The moon’s a blade it cuts the sky
Shadows crawling they creep they lie
I hear the whispers sharp as glass
They’re coming fast they’re coming fast

[Chorus]
It’s a night battle hearts collide
Run or fight there’s no place to hide
Echoes screaming across the night
It’s a night battle under the moonlight

[Verse 2]
Streetlights flicker a broken code
Every step feels like it’s slowed
The air is heavy it tastes like fear
You’re close I feel you near

[Prechorus]
The ground shakes it’s a warning drum
In this war you can’t outrun

[Chorus]
It’s a night battle hearts collide
Run or fight there’s no place to hide
Echoes screaming across the night
It’s a night battle under the moonlight

[Bridge]
A flash a crash a soul’s last cry
Stars explode and the sparks won’t die
The silence roars it’s a deafening sound
We’re all lost and found

[Prechorus]
The ground shakes it’s a warning drum
In this war you can’t outrun

[Chorus]
It’s a night battle hearts collide
Run or fight there’s no place to hide
Echoes screaming across the night
It’s a night battle under the moonlight
```

### Rising

*showcases: arrangement / instrumentation · 3:06*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 162. key is Eb, and scale is minor. Emo Metal / Post-Hardcore.
Global Emotional Progression: The track initiates with a hollow, despondent atmosphere that quickly transitions into a simmering, anxious tension during the first half. As the structure progresses, the emotional weight shifts from internalised grief to an externalised, volcanic eruption of frustration. The bridge serves as the ultimate emotional breaking point, manifesting as a chaotic and dissonant collapse, which then plateaus into a final, soaring anthem of tragic resignation before fading into a stark, cold silence.
Application Scenarios & Imagery: Visuals of a crumbling urban skyline under a blood-orange sunset, cinematic montages of societal collapse, or high-intensity emotional sequences in dark fantasy gaming. The music evokes the feeling of standing alone in a rain-slicked metropolis while the world descends into ruin.
Sonics & Production Profile: The soundstage is characterized by a "wall of sound" approach that balances raw, jagged edges with polished modern clarity. A mid-forward guitar presence provides a biting texture, while the low-frequency domain is anchored by a massive, saturated bass tone that fills the sub-octave gaps. The production utilizes high-contrast dynamics, moving from a claustrophobic, dry aesthetic in the verses to a wide, hyper-compressed stereo field in the choruses.
Vocal Details
Vocal Gender & Timbre: Male. The vocalist exhibits a quintessential emo metal timbre, featuring a fragile, breathy quality in the lower register that possesses a natural, jagged grit when pushed. The voice is characterized by a youthful but strained resonance, sounding both vulnerable and violently expressive.
Vocal Style: The delivery is marked by conversational back-phrasing in the verses, creating a sense of weary detachment. This evolves into an urgent, melodic belt with a distinct hook motif featuring a rising minor 6th interval during the primary thematic lines. To emphasize the "emo" aesthetic, the performer utilizes frequent vocal fry at the start of phrases and expressive, cracking falsetto flips at the end of high-register lines. During the bridge, the style shifts into a rhythmic, syncopated scream—specifically a mid-range distorted shout—that lands slightly ahead of the beat to convey desperation.
Harmony/Backing Vocals: Dense, three-part vocal stacks appear in the choruses to create a choir-of-the-damned effect, with high-octave doubles panned hard left and right. Ghostly, whispered harmonies are tucked deep into the mix during the verses to add a sense of psychological haunting.
Vocal FX: The clean sections are treated with a dark plate reverb and a 1/4 note ping-pong delay that is high-cut to avoid cluttering the mix. The aggressive sections employ parallel distortion and a "telephone" EQ filter on specific ad-libs to create a lo-fi, distressed texture.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: The foundation is built on twin-engine electric guitars. During the verses, the primary layer consists of clean, chorused electric guitars playing intricate, melancholic arpeggios with a light palm-mute on the root notes. In the chorus, this shifts to high-gain, overdriven guitars executing massive, sustained power chords and melodic octave leads.
Secondary: A secondary layer of industrial-leaning synthesizers provides a cold, metallic drone in the background, entering during the pre-chorus to build harmonic tension. A third layer of dissonant, high-register guitar feedback acts as a contrapuntal texture during the second verse, mimicking the sound of sirens or shearing metal. During the final chorus, a shimmering tremolo-picked guitar line sits atop the arrangement to provide a sense of melodic climax.
Groove & Foundation Progression: The groove is propelled by a relentless, syncopated kick drum pattern that mimics a racing heartbeat. The bass guitar is heavily distorted, acting as a bridge between the kick drum and the guitars, providing a "clanky" metallic pick attack that cuts through the mix. The percussion evolves from a steady, closed hi-hat pulse in the intro to a violent, open-wash crash cymbal assault in the chorus. The bridge features a breakdown with slow, crushing half-time percussion and double-bass drum bursts.
Embellishments, Textures & Spatial FX: The track is punctuated by cinematic sub-drops and white-noise risers at every major structural transition. A localized foley effect of shattering glass is panned across the stereo field during the first verse to emphasize the thematic decay. Deep, cavernous impact hits are used to mark the beginning of the breakdown, while the outro features the sound of a mechanical hum that slowly decrescendoes into a single, flat electronic tone.
```

**Input lyrics:**

```
(Verse 1)
Black horizon, bleeding fire through the cracks,
Shattered heavens raining down in smoking shards of glass.
Sirens drown beneath the weight of every selfish breath,
A world on its knees, but they’re too numb to fear the death.

(Pre-Chorus)
Eyes locked on the mirror, never looking up,
While the ceiling of creation finally comes undone.

(Chorus)
And the sky keeps fallin’, fallin’, burnin’ into dust,
But no one hears the warnings, too consumed by what they want.
Yeah, the world is ending, but they barely even blink—
Ashfall empathy, we’re standing on the brink.

(Verse 2)
Concrete kingdoms crumble under footsteps of denial,
Every heartbeat echoes doom, but apathy’s in style.
Frozen souls scroll through the wreckage on their screens,
Filter out the carnage, turn their backs on everything.

(Pre-Chorus)
No one feels the tremors, though the earth is split and scarred,
They’re guarding empty comforts while the void is staring hard.

(Chorus)
And the sky keeps fallin’, fallin’, burnin’ into dust,
But no one hears the warnings, too consumed by what they want.
Yeah, the world is ending, but they barely even blink—
Ashfall empathy, we’re standing on the brink.

(Bridge — Breakdown)
Let the heavens break, let the thunder scream,
Rip the veil apart, expose the dead machine.
We raised this tombstone city from our ignorance and greed—
Now the cosmos writes our requiem in falling, flaming sleet.

(Final Chorus)
Still the sky keeps fallin’, fallin’, screaming from above,
But no one lifts their gaze, no one fights for what they love.
In the shadow of collapse, we turn away and sink—
Ashfall empathy… we’re drowning while we drink.
```

### Stop Him

*showcases: arrangement / instrumentation · 3:37*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 142. key is Eb, and scale is minor. Death Metal / Gothic Metal.
Global Emotional Progression: The track initiates with a sense of subterranean dread and eerie stillness, slowly building into a calculated, mid-tempo march of mechanical menace. As the verses unfold, the atmosphere shifts into a claustrophobic and aggressive state of dominance. The chorus expands the emotional palette into a dark, anthemic grandeur, portraying a sense of tragic inevitability. A chaotic and dissonant bridge heightens the tension to a breaking point before a final, crushing return to the regal gloom of the chorus, ending on a cold, desolate decay.
Application Scenarios & Imagery: Cinematic sequences involving the rise of an undead army, dark fantasy RPG boss encounters, or high-concept horror visuals set in sprawling, ruined cathedrals under a blood-red moon.
Sonics & Production Profile: The mix is characterized by a colossal, "bottom-heavy" soundstage with the low-end frequencies of the bass and kick drum saturating the sub-mix. Guitars are tracked with a thick, saturated distortion and mid-range focus to ensure clarity amidst the chaos. The spatial profile utilizes a dark, damp plate reverb to simulate an underground cavern, while the transient response is sharp and punchy, emphasizing the rhythmic precision of the percussion.

Vocal Details
Vocal Gender & Timbre: Singer A (Male). The vocalist features a cavernous, gravelly baritone timbre capable of shifting between a low-frequency guttural growl and a dramatic, operatic theatricality.
Vocal Style: The delivery is anchored by a rhythmic, staccato growling technique in the verses, utilizing syncopated phrasing that mirrors the kick drum patterns. The choruses introduce a melodic hook motif characterized by a dramatic minor 6th leap, executed with a strained, gritty clean vocal that suggests exhaustion and power. The bridge features chaotic, rapid-fire rhythmic bursts and vocal fry, while the pre-chorus utilizes a haunting, breathy whisper that transitions into a rising chromatic scale to build tension. Specific articulations include long, decaying growls at the end of phrases and sudden, sharp staccato barks to emphasize rhythmic transitions.
Harmony/Backing Vocals: Deep, low-frequency choir stacks are layered in the choruses to provide a liturgical, "unholy" texture. In the bridge, dissonant, whispered vocal layers are panned hard across the stereo field to create a disorienting, polyphonic effect. 
Vocal FX: Primary vocals are treated with a dark room reverb and a short slap-back delay to thicken the presence. The pre-chorus whispers are heavily compressed and processed with a high-pass filter for a telephonic, ghostly effect, while the chorus harmonies are saturated with a lush, cathedral-style hall reverb.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): 
Primary: Down-tuned seven-string electric guitars serve as the foundational harmonic engine. In the verses, they employ tight, palm-muted chugging and dissonant tritone intervals. During the choruses, they transition into wide, ringing power chords and melodic, tremolo-picked leads that soar above the rhythm section. The bridge introduces erratic, "whammy-bar" squeals and jagged, technical riffing.
Secondary: A gritty, distorted bass guitar provides a constant, grinding low-frequency presence, acting as a bridge between the drums and the guitars. A secondary melodic layer consists of a pipe-organ-style synthesizer that enters during the choruses to add a gothic, orchestral weight. During the transitions, high-register crystalline bells provide a fragile, chilling counter-melody that contrasts with the heavy instrumentation.
Groove & Foundation Progression: The groove is defined by a heavy, "industrial" drum performance featuring consistent double-kick patterns and a snare tuned for a high-pitched, metallic "crack." The verses maintain a steady, driving 4/4 pulse with syncopated accents on the cymbals. The pre-chorus strips back the percussion to a simple, resonant floor tom beat to create space, while the chorus erupts into a full-speed blast beat before settling into a half-time, anthemic stomp to emphasize the lyrical weight.
Embellishments, Textures & Spatial FX: Subtle atmospheric textures include the sound of crumbling stone and low-frequency sub-drops to emphasize the weight of the "king's" movements. Reverse-reverb guitar swells and metallic scrapes are used as transitions between sections, while the outro features a fading, discordant piano motif that rings out into silence.
```

**Input lyrics:**

```
[Verse]
He rose from the dirt where the shadows slept
A crown of decay on a skull that wept
Fingers of ash
Eyes like the void
A kingdom of ruins he vowed to avoid

[Chorus]
The zombie king
The zombie king
No life to give
But he takes everything
The undead throne
The silent sting
Bow to the one who feels nothing

[Verse 2]
The stars turned their gaze
The moon held its breath
His voice like a whisper of hunger and death
He walked through the flames
They burned but obeyed
Even the winds bent low as he swayed

[Prechorus]
Who could stop him
Who could fight
A corpse reborn
A god of night

[Chorus]
The zombie king
The zombie king
No life to give
But he takes everything
The undead throne
The silent sting
Bow to the one who feels nothing

[Bridge]
Was it hunger
Was it fate
To climb from the grave and rule the great
He laughs with the sound of crumbling stone
His empire of shadows
His fate alone
```

## Dance Pop

### Folding

*showcases: vocals · 2:53*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 126. key is F#, and scale is minor. EDM / Melodic House.
Global Emotional Progression: The track initiates with a melancholic, introspective atmosphere, establishing a sense of isolation. As the arrangement moves into the first chorus, the energy shifts toward a hopeful resilience, transitioning from a sparse electronic soundscape into a pulsating, rhythmic drive. The second verse maintains this momentum with increased textural density, leading into a bridge that features a cinematic swell of tension. The final chorus serves as a cathartic emotional peak, resolving into a gentle, fading outro that echoes the initial solitude.
Application Scenarios & Imagery: Late-night drives through rain-slicked city streets, reflective moments in a dimly lit lounge, or the closing set of a sunrise festival. The music evokes imagery of domestic spaces left in disarray and the blurring of seasons.
Sonics & Production Profile: The soundstage is characterized by a deep, immersive three-dimensionality, emphasizing a warm low-mid presence and a shimmering, airy high end. The dynamic range is carefully sculpted, utilizing side-chain compression to create a pumping, breathable relationship between the kick drum and the melodic layers, resulting in a lush and polished commercial aesthetic.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist exhibits a breathy, emotive alto timbre with a rich, smoky texture in the lower register. Her voice carries a palpable sense of vulnerability, shifting toward a clearer, more resonant chest voice during high-energy segments.
Vocal Style: The delivery is marked by a conversational, back-phrased rhythmic approach in the verses, mimicking a natural internal monologue. The choruses feature an iconic rising minor 6th leap that serves as the primary hook motif, followed by graceful falsetto flips on the tail ends of phrases. The bridge employs urgent staccato bursts that gradually transition into long, sustained melodic arcs with an expressive, wide vibrato.
Harmony/Backing Vocals: Lush, three-part vocal stacks appear in the choruses to create a wide, choral effect. In the bridge, ethereal, pitch-shifted vocal chops act as a rhythmic counterpoint, while soft, whispered unisons reinforce the intimate lyrics of the verses.
Vocal FX: The primary vocal is treated with a large plate reverb and a synchronized quarter-note ping-pong delay. A subtle saturation adds warmth, while a high-shelf EQ boost ensures the breathy articulations remain crisp and forward in the mix.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A warm, filtered electric piano provides the harmonic foundation, utilizing jazz-influenced chord voicings with a gentle tremolo effect. This is joined by a plucky, muted sine-wave synthesizer that carries the rhythmic ostinato throughout the track.
Secondary: A deep, analog-style sub-bass emerges in the first verse, providing a foundational weight that follows the root notes. Shimmering, wide-panned synth pads enter during the chorus to fill the frequency spectrum, while a secondary layer of bright, detuned saw-leads provides a staccato counter-melody in the second half of the choruses. During the bridge, a cinematic string ensemble swells to increase the harmonic tension before dropping away for the final chorus transition.
Groove & Foundation Progression: The groove begins with a minimalist kick pulse and a light shaker rhythm. As the chorus hits, a solid four-on-the-floor kick drum provides the heartbeat of the track, complemented by a crisp, layered clap on the backbeat. The second verse introduces a syncopated percussion loop consisting of woodblocks and rimshots to increase the rhythmic complexity. The bridge strips back the drums to a single, filtered kick before reintroducing the full groove for the final climactic section.
Embellishments, Textures & Spatial FX: Subtle white noise swells and reverse piano grains mark the transitions between sections. A localized foley effect of a distant door closing is integrated into the first transition to ground the track in its narrative. High-frequency glitch artifacts and sub-drops provide occasional rhythmic punctuation, while a wide stereo widener is automated on the synth pads to expand the soundstage during the emotional peaks.
```

**Input lyrics:**

```
[Verse 1]
You packed your bags
Left your toothbrush by the sink
Said
"We need time"
Like it’s something we can drink
Door hit the frame
And the frames shook on the wall
I watched our summer
Fold into the fall

[Chorus]
It’s not the end
Just feels like it tonight
We’re bending
Not breaking
Just lost in the fight
If love is a story
We’re stuck on a page
It’s not the end
It’s a turn in the phrase
(yeah, we’ll turn this page)

[Verse 2]
Your sweater’s still
On the chair beside the bed
I talk to it
Like you’re here inside my head
I make two cups
Still forget you’re not around
Then laugh a little
At how loud this quiet sounds

[Chorus]
It’s not the end
Just feels like it tonight
We’re bending
Not breaking
Just lost in the fight
If love is a story
We’re stuck on a page
It’s not the end
It’s a turn in the phrase
(we’ll turn this page)

[Bridge]
One more call
Could change it all (oh-oh)
One slow walk
Back up the hall
If this is the part
Where we almost break
Hold my hand
Let the credits wait

[Chorus]
It’s not the end
Just feels like it tonight
We’re bending
Not breaking
We’ll find back the light
If love is a story
We’re stuck on a page
It’s not the end
We’re just turning the page
(it’s not the end)
We’re just turning the page
```

### Let Things Go

*showcases: vocals · 2:49*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 126. key is Bb, and scale is major. EDM / Progressive House.
Global Emotional Progression: The track begins with a poignant, reflective atmosphere that establishes a sense of regretful nostalgia. As the first verse progresses, the energy shifts from vulnerability to a rising tension, culminating in a powerful, cathartic explosion of sound during the chorus that symbolizes a desperate yearning. The second verse maintains a higher baseline of energy than the first, leading into a second chorus that feels even more expansive. The bridge serves as a frantic, rhythmic peak of anticipation before the final triumphant, yet bittersweet, melodic resolution in the closing chorus and a clean, echoing fade.
Application Scenarios & Imagery: Late-night festival mainstages, high-energy emotional montages, or solitary long-distance drives through urban landscapes under flickering streetlights. The imagery evokes raindrops on glass windows blurring the neon lights of a distant city.
Sonics & Production Profile: The soundstage is exceptionally wide and immersive, featuring a crisp, high-fidelity top end and a foundational low-frequency response designed for club systems. The production utilizes heavy side-chain compression to create a pumping, breathing relationship between the kick drum and the melodic elements, while lush hall reverbs provide a sense of vast, open space during the emotive peaks.

Vocal Details
Vocal Gender & Timbre: Male. The vocalist features a smooth, breathy tenor timbre with a rich chest-voice resonance. The texture is intimate and warm in the lower register but transitions into a powerful, slightly strained belts in the higher registers to convey emotional urgency.
Vocal Style: The delivery begins with conversational back-phrasing behind the beat, creating a sense of hesitation. As the song builds, the vocalist employs iconic rising 5th leaps during the hook to emphasize the longing in the melody. Pentatonic runs are used as decorative flourishes at the end of phrases, while the chorus demands an urgent, staccato rhythmic delivery that locks into the synth pulse. Subtle vocal fry is used on the start of lower notes for added grit and realism.
Harmony/Backing Vocals: Dense, multi-tracked vocal stacks appear in the chorus to create a wall-of-sound effect. High-register falsetto harmonies provide a shimmering counter-melody during the bridge, while wide-panned "gang vocal" layers are introduced in the final chorus to amplify the anthemic quality.
Vocal FX: The verses utilize a dry, close-mic proximity effect with subtle plate reverb. In the chorus, the vocals are treated with a rhythmic ping-pong delay synced to 1/8th notes and a large-scale shimmering shimmer-reverb. Light pitch correction is applied to achieve a polished, modern commercial EDM aesthetic without stripping away the natural vibrato.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, fingerpicked electric guitar with a chorus effect serves as the primary harmonic driver in the opening sections, establishing a rhythmic pulse. A massive, detuned supersaw lead synthesizer enters as the primary melodic force during the choruses, occupying the mid-to-high frequency range with a bright, aggressive bite. A thick, distorted Reese bass provides a grounding, gritty texture that evolves from a subtle hum in the verses to a dominant, growling presence in the chorus.
Secondary: Atmospheric ambient pads provide a continuous bed of sound, using cutoff automation to swell during transitions. During the verses, a secondary clean guitar layer adds syncopated ghost-note accents. In the chorus, a high-register rhythmic piano layer is introduced to add percussive clarity to the chord progression. A third, heavily distorted rhythm guitar layer is added exclusively in the final chorus to maximize the wall-of-sound density and energy.
Groove & Foundation Progression: The foundation starts with a filtered, soft kick drum and a minimalist shaker. The groove evolves into a driving four-on-the-floor house beat in the chorus, characterized by a punchy, high-transient kick and a crisp white-noise snare. The bridge features an urgent 16th-note hat pattern that creates a sense of frantic searching, while the bassline shifts from long, sustained notes to a syncopated, rhythmic "bouncing" pattern that drives the dancefloor energy.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by white noise risers and sub-bass drops that signal structural shifts. Reverse cymbal swells and metallic impact hits emphasize the start of each chorus. Brief, localized environmental foley of distant traffic is heard in the very beginning of the intro to ground the track in a physical space. During the bridge, glitchy vocal chops are used as a rhythmic texture to fill the gaps between the lead vocal phrases.
```

**Input lyrics:**

```
[Verse 1]
I wish I’d called you back that night
Not stared so long at my own pride
I wish I’d said what scared me most
Instead of turning into smoke

[Chorus]
I wish you were here
Right now
Right here
Laughing at my bad ideas
Spilling secrets in my ear
I wish you were here
Right now
This year
Every little thing I do
Keeps circling back to you

[Verse 2]
I wish I’d learned to let things go
To lose an argument
Not you though
I wish I’d held you in that storm
Not tried to tough it out alone

[Chorus]
I wish you were here
Right now
Right here
Laughing at my bad ideas
Spilling secrets in my ear
I wish you were here
Right now
This year
Every little thing I do
Keeps circling back to you

[Bridge]
I wish on traffic lights
On receipts and license plates
On every almost-kind-of sign
That says it’s not too late

[Chorus]
I wish you were here
Right now
Right here
Tracing circles on my sleeve
Saying what you really mean
I wish you were here
Right now
This year
Every little thing I do
Keeps circling back to you
```

## GuFeng

### 小镇炉火

*showcases: regional genres (Chinese) · 2:22*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is Ab, and scale is major. Mandarin Pop / Traditional Ballad.
Global Emotional Progression: The track initiates with a tender, morning-light atmosphere that establishes a sense of domestic peace. As the verses unfold, the emotional narrative transitions into a warm, grounded nostalgia, emphasizing stability and comfort. The prechorus introduces a brief moment of philosophical yearning, which resolves into a sweeping, celebratory sense of fulfillment during the chorus. The bridge elevates the arrangement to a peak of spiritual gratitude before settling into a quiet, lingering finish that mimics the fading glow of a sunset.
Application Scenarios & Imagery: Perfectly suited for a family reunion montage, a documentary centered on multi-generational heritage, or a reflective commercial for a traditional home. The imagery evokes a quiet courtyard at dusk, the steam rising from a porcelain teacup, and the soft textures of weathered wood and silk.
Sonics & Production Profile: The production features a wide, immersive soundstage with a distinct focus on mid-range warmth to enhance the feeling of intimacy. High-frequency transients from the traditional plucking instruments are rounded and polished, preventing any digital harshness. The dynamic profile is highly expressive, favoring a naturalistic, "live-in-the-room" breathing quality rather than heavy modern compression.
Vocal Details
Vocal Gender & Timbre: Male Soloist. The vocalist possesses a rich, resonant baritone-tenor range characterized by a smooth, velvety texture and a mature, authoritative warmth. The timbre is clear yet infused with a slight grain that suggests a lifetime of experience and wisdom.
Vocal Style: The performance is marked by a conversational back-phrasing that feels unhurried and sincere. The melodic contour features iconic pentatonic runs and graceful falsetto flips on the higher ends of the chorus phrases. A signature hook motif involves a gentle sliding appoggiatura at the end of key lines to emphasize a sense of longing. The delivery uses a light vocal fry in the lower register for intimacy, transitioning into a stable, wide vibrato during the sustained notes of the chorus to convey emotional strength.
Harmony/Backing Vocals: Lush, stacked vocal harmonies appear in the chorus to provide a "choir-like" foundation, using a mix of the lead singer’s overdubs and a soft male ensemble to create a sense of communal belonging. These are panned wide to create a surround-sound effect.
Vocal FX: The lead vocal is treated with a plate reverb for a vintage, nostalgic feel, complemented by a warm analog delay synchronized to the tempo to fill the gaps between phrases. A subtle high-shelf boost ensures the breathiness of the performance remains audible against the string arrangement.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering)
Primary Harmonic Layer: A lush ensemble of soft Western strings (violins, violas, and cellos) provides a continuous, legato harmonic bed that anchors the entire composition. The cellos take a primary role in the lower register, playing sweeping, melodic bass lines that mirror the vocal's emotional weight.
Secondary Layering: A delicate Guzheng is introduced in the opening, utilizing traditional finger-plucking techniques and pitch bends (glissandos) to provide the track's cultural identity. A clean electric guitar enters during the verses, playing muted, rhythmic arpeggios that add a contemporary pop polish. A second rhythm guitar is layered specifically during the chorus sections to thicken the wall of sound, providing a subtle strumming pattern that enhances the energy. A grand piano provides intermittent melodic counterpoints, acting as a secondary voice that interacts with the Guzheng in a call-and-response fashion.
Groove & Foundation Progression: The foundation is built upon a distorted bass guitar that provides a gritty, modern contrast to the clean strings, appearing prominently in the choruses to add a low-end pulse. The percussion is minimalist, avoiding a standard kit in favor of a deep, resonant Taiko-inspired kick drum and soft brush strokes on a snare, which gradually build in complexity as the song progresses toward the bridge.
Embellishments, Textures & Spatial FX: Ambient pads are deployed in the intro to create a shimmering, ethereal mist. Throughout the track, subtle textural elements like the sound of a wooden rocking chair creak and the faint clinking of ceramic are used as foley accents to ground the listener in the physical space of the lyrics. Large hall reverb washes are used on the Guzheng during the bridge to create a dreamlike, suspended state before the final resolution.
```

**Input lyrics:**

```
[Verse]
屋檐下青苔长
木窗边月影扬
炊烟升起 炉火温暖
笑声穿过院墙

[Chorus]
岁月如歌 歌声悠长
我们牵手走过风霜
孩子长大 家庭满堂
一壶茶温暖了心房

[Verse 2]
摇椅轻晃夕阳下
旧相册笑容如花
指尖缝补 记忆缝扎
每道皱纹藏着回答

[Prechorus]
是谁说流年太快
白发换来心如海

[Chorus]
岁月如歌 歌声悠长
我们牵手走过风霜
孩子长大 家庭满堂
一壶茶温暖了心房

[Bridge]
庭前树影摇曳成画
月下竹影诉说牵挂
人间烟火 平淡无瑕
岁月留香在心底发芽
```

### 秋去春几回

*showcases: regional genres (Chinese) · 1:47*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 74. key is F#, and scale is minor. C-Pop / Melodic Ballad.
Global Emotional Progression: The track initiates with a heavy sense of solitude and stillness, characterized by a cold, ambient atmosphere. As the narrative progresses through the verses, the emotional weight shifts from isolation to a bittersweet, mounting longing. The arrangement reaches a peak of high-pitched yearning during the choruses, before gradually receding into a final, lingering state of quiet resignation in the outro.
Application Scenarios & Imagery: This piece is perfectly suited for a cinematic montage of falling autumn leaves, a lonely traveler crossing a misty mountain pass, or a high-end commercial for traditional tea. The imagery is one of vast, open landscapes, ink-wash aesthetics, and the silent passage of time within a courtyard.
Sonics & Production Profile: The soundstage is wide and immersive, with a strong emphasis on the high-mid frequencies to ensure vocal clarity. The low-end is warm but subdued, providing a soft cushion rather than a punchy foundation. High-fidelity clarity allows for every nuance of the plucked strings and vocal breaths to be felt, wrapped in a lush, expensive-sounding hall reverb.

Vocal Details
Vocal Gender & Timbre: A male tenor provides the lead vocal, possessing a silky, emotive, and slightly fragile timbre. The voice is characterized by a "broken" quality in the lower register that transitions into a crystalline, pure head voice for higher passages, echoing the vulnerability inherent in the genre.
Vocal Style: The performance is marked by conversational back-phrasing, often starting just behind the beat to emphasize a sense of hesitation. The melodic contour features signature C-Pop wide leaps, specifically a recurring rising 6th interval that acts as the primary hook motif. Distinct performance articulations include subtle vocal fry at the start of phrases and graceful falsetto flips at the end of sustained notes, creating an expressive, tearful aesthetic.
Harmony/Backing Vocals: Lush, multi-tracked vocal stacks emerge in the second chorus and the bridge, utilizing a soft-focus "ooh" texture to create a pad-like effect. These harmonies follow a traditional pentatonic structure, reinforcing the cultural identity of the melody without becoming overly dense.
Vocal FX: A sophisticated chain of shimmer reverb and a synchronized quarter-note delay are used to create a "dream-like" trail. A high-shelf EQ boost adds air to the signal, while parallel compression ensures that even the softest whispers remain intelligible against the rich arrangement.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A delicate, nylon-string acoustic guitar serves as the primary harmonic driver, utilizing fingerpicked arpeggios with prominent fret-noise to enhance the organic feel. This is complemented by a grand piano that enters in the second verse, providing deep, resonant bass notes and high-register tinkling motifs that mimic falling water.
Secondary Layering: A traditional Dizi (bamboo flute) enters as a secondary melodic voice, providing a breathy, soaring counter-melody that responds to the vocal phrases. A lush, synthesized string ensemble provides a cinematic swell during the climactic sections, while a subtle Erhu (two-stringed fiddle) provides a mournful, sliding texture during the transitional bridge, adding an authentic morphological depth to the C-pop aesthetic.
Groove & Foundation Progression: The foundation is minimal and evocative. It begins with no rhythmic pulse, relying on the rubato feel of the guitar. A soft, muffled electronic kick drum and a brushed snare eventually establish a slow, heartbeat-like pulse during the first chorus. The bass is a warm, fretless electric model that glides between notes, providing a fluid, melodic bottom end that avoids rigid rhythmic locking.
Embellishments, Textures & Spatial FX: The track is decorated with organic foley elements, including the distant sound of a temple bell and the faint rustle of paper. Subtly panned synth sweeps provide smooth transitions between sections, while a reversed piano grain effect creates an ethereal texture during the intro and outro to bookend the track with a sense of temporal distortion.
```

**Input lyrics:**

```
花开南去后，
东海几年别，

一路白云里，
长安春几回。

去去行人远，
此去莫蹉跎。

相思深夜后，
秋色共谁寻。

谁能平此恨，
黄叶几回看。

何事居人世，
对酒落花前。

溪云几万重。
万里独何之。

如今是别离。
对酒落花前。

花开南去后，
东海几年别，

一路白云里，
长安春几回。

去去行人远，
此去莫蹉跎。

一路白云里，
长安春几回。
```

## Soul

### Carry On

*showcases: arrangement / instrumentation · 2:30*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is Bb, and scale is minor. E-Punk Hip-Hop / Industrial Rap.
Global Emotional Progression: The track begins with a sense of ominous urgency during the hook, establishing a dark, ecclesiastical atmosphere through aggressive electronic textures. As it moves into the verse, the mood shifts toward a focused, rhythmic sermonizing, maintaining a high-tension undercurrent. The instrumental dance bridge serves as a kinetic peak, transitioning the spiritual dread into a physical, club-ready catharsis before returning to the final hook, which reinforces the cycle of inevitable reckoning with increased sonic density.
Application Scenarios & Imagery: A dimly lit underground warehouse party with flickering neon lights, or a cinematic chase sequence through a futuristic, rain-slicked dystopian cityscape. It evokes imagery of high-tech cathedrals and digital penance.
Sonics & Production Profile: The soundstage is claustrophobic and forward-leaning, characterized by a heavily saturated low-mid range and sharp, biting high-end transients. The production favors a wall-of-sound aesthetic where the vocals sit slightly behind the wall of electronic grit, utilizing extreme side-chain compression to create a pumping, breathing sensation across the entire frequency spectrum.

Vocal Details
Vocal Gender & Timbre: Male Lead. The vocalist features a gravelly, authoritative tenor timbre that carries a significant amount of natural grit and chest resonance, providing a human anchor to the synthetic environment.
Vocal Style: The delivery is a hybrid of aggressive rap flow and punk-inspired melodic shouting. The hook utilizes a melodic motif centered on minor third intervals, creating a haunting, repetitive chant. In the verse, the phrasing becomes more syncopated and staccato, pushing against the beat to create tension. During the instrumental bridge, the vocals transform into elongated, operatic wails that utilize dramatic upward glissandos and wide, trembling vibrato on the sustained vowel sounds to mimic a digital siren.
Harmony/Backing Vocals: The hooks are supported by low-octave doubles and distorted unison stacks to create a monolithic, choir-like presence. In the verse, subtle whispered layers are panned hard left and right to provide a sense of psychological intimacy and internal monologue.
Vocal FX: The lead vocal is processed with a combination of bit-crushing and telephone-style EQ filtering. A gritty, short-tail plate reverb provides a metallic space, while the bridge sections employ heavy pitch-correction artifacts and a rhythmic ping-pong delay that syncs with the sixteenth-note grid.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A massive, distorted Moog-style sub-bass provides the primary harmonic movement, oscillating between sustained low notes and rhythmic stabs. This is paired with a sharp, sawtooth lead synth that plays a jagged, repetitive counter-melody during the hooks.
Secondary: A clean, chorus-drenched electric guitar enters specifically during the verse, providing a stark, cold contrast to the surrounding electronic chaos with palm-muted rhythmic pulses. An ambient, pulsating pad sits in the background of the intro and transitions, creating a dark, atmospheric floor. During the bridge, a secondary high-resonance acid synth enters, performing frantic, filtering arpeggios that rise in frequency to build energy.
Groove & Foundation Progression: The groove is built on a foundational industrial drum machine pattern, featuring a clipping 808 kick drum and a layered snare-clap combo that hits with explosive force on the backbeat. The bassline evolves from a steady drone in the intro to a highly syncopated, distorted rhythmic engine in the verse. The bridge introduces a four-on-the-floor kick pattern, shifting the track into a high-energy dance aesthetic before the final hook reverts to the broken, aggressive hip-hop beat.
Embellishments, Textures & Spatial FX: The track is punctuated by digital glitches, white noise bursts, and sub-octave drops that signal structural transitions. Metallic impact hits and reverse reverb swells emphasize the start of each hook. A localized foley sound of heavy iron doors slamming occurs at the transition into the verse, grounding the industrial theme without persisting throughout the track.
```

**Input lyrics:**

```
[Hook]
I've been having revelations
Repenting for my sins
In attempt to make amends
Before the end begins
Lord knows that we're holy
But only god can win
Prophecy fulfilling slowly
Before the end begins

[Verse]
Jesus came to save us
He died so we could live
So his will could carry on
Before the end begins
And god he sent his only son
To bear the weight of what we've done
Our evil deeds must weigh a ton.
(Somewhere the end has just begun)...

[Instrumental dance bridge]
Uuuuuuuuun
Just
Beguuuuuuu
Uuuuuuuuun

[Hook]
I've been having revelations
Repenting for my sins
In attempt to make amends
Before the end begins
Lord knows that we're holy
But only god can win
Prophecy fulfilling slowly
Before the end begins
```

### The Shadow

*showcases: vocals · 1:02*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 82. key is Eb, and scale is major. Soul / Neo-Soul.
Global Emotional Progression: The track initiates with a serene, detached atmosphere that suggests a peaceful withdrawal from conflict. As the arrangement transitions from the clean instrumental opening into the core message, the emotional tone shifts from observational wisdom to a defiant, self-assured liberation. The energy culminates in a triumphant realization of self-worth, ending on a resolute and grounded note that emphasizes personal sovereignty.
Application Scenarios & Imagery: Ideal for a sophisticated lounge setting or a sunrise drive through a quiet city. The music evokes imagery of golden hour light filtering through honey-colored curtains and a person walking away from a shadow-filled doorway into an open, sun-drenched field.
Sonics & Production Profile: The production is defined by a wide, luxurious soundstage with a focus on high-fidelity organic textures. The frequency response is characterized by a silky high-end shimmer and a deep, pillowy low-frequency extension provided by the bass. The dynamic aesthetic is smooth and polished, emphasizing a "liquid" feel where each instrument flows seamlessly into the next with ample headroom.

Vocal Details
Vocal Gender & Timbre: Female. The vocalist has a rich, velvety mezzo-soprano timbre with a luminous clarity in her upper register. The texture is breathy and intimate in the lower notes, gaining a vibrant, brassy resonance as she moves into her chest voice.
Vocal Style: The performance utilizes a sophisticated neo-soul delivery, featuring conversational back-phrasing that frequently sits just behind the beat to create a relaxed, confident feel. The melodic contour is defined by elegant pentatonic runs and an iconic rising 5th leap during the thematic peaks. She employs expressive vocal fry at the start of certain phrases and graceful falsetto flips at the ends of others, creating a highly nuanced and emotive performance.
Harmony/Backing Vocals: Lush, three-part stacked harmonies appear during the later sections, utilizing a wide stereo spread to envelop the lead vocal. These backing layers use a smoother, more flutey tone to provide a celestial contrast to the grounded lead.
Vocal FX: The vocals are treated with a sophisticated large-hall convolution reverb and a synchronized quarter-note ping-pong delay that is tucked low in the mix for depth. A vintage optical compressor emulation is used to keep the levels consistent while adding a subtle harmonic warmth.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Harmonic Layer: A vintage electric piano with a light tremolo effect serves as the primary harmonic foundation, providing rich, jazzy chord voicings throughout the track. It is joined by a clean, hollow-body electric guitar that plays delicate, fingerpicked arpeggios in the mid-high frequency range, adding a shimmering melodic layer.
Secondary Layering: An ambient synth pad with a slow-moving filter cutoff provides a continuous atmospheric wash, entering during the initial phase to establish the "ambient" directive. As the track progresses, a secondary rhythm guitar with a slightly more percussive, funk-influenced strumming pattern enters to provide syncopated counter-rhythmic interest. A subtle string ensemble appears in the final third of the track, acting as a high-register shimmering drone to elevate the arrangement.
Groove & Foundation Progression: The foundation is built upon a distorted electric bass that provides a gritty, modern edge to the traditional soul instrumentation, playing melodic, syncopated lines that occupy the sub-bass and low-mid frequencies. The percussion begins with a minimalist electronic rimshot and a soft, dampened kick drum, eventually evolving into a full, live-recorded kit with a deep, thuddy snare and crisp, consistent hi-hat eighth notes that drive the mid-tempo groove forward.
Embellishments, Textures & Spatial FX: Subtle chime transitions and reverse piano swells are used to bridge structural shifts. A light environmental foley of distant, muffled city ambiance is briefly audible in the transition, while occasional sub-drops emphasize the start of the primary thematic cycles. The track concludes with the natural decay of the electric piano and a final, resonant bass note.
```

**Input lyrics:**

```
the bee doesnt have to explain to a fly that honey is better than shit.
You can’t describe the light to someone who prefers the shadows;
Seeking their approval is not worth your energy
​
So I’m moving on, because there is work to be done.
My life is mine—I won’t let it be beaten into submission.
I’m just going to bee.

​
​
```

## Urban

### Closer

*showcases: vocals · 4:04*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 88. key is Db, and scale is major. Urban Soul / Contemporary R&B.
Global Emotional Progression: The track initiates with an effortless, confident swagger that mirrors the initial spark of a chance encounter. This cool exterior gradually warms during the transitions, leading into a chorus that feels physically grounded and deeply affectionate. The emotional arc peaks with a sense of romantic certainty before the bridge pivots into a vulnerable, hushed intimacy. The energy returns for a final celebratory push, ultimately dissolving into a lingering, flirtatious inquiry during the fade-out.
Application Scenarios & Imagery: Perfectly suited for a late-night candlelit lounge, a sophisticated urban romance film montage, or a private evening setting. The imagery evokes the dim glow of a jukebox, the tactile sensation of a slow dance in a crowded room, and the blurred lights of a city skyline at 3 AM.
Sonics & Production Profile: The production is characterized by a deep, "bottom-heavy" frequency response, prioritizing a rounded sub-bass and a punchy, dry snare. The soundstage is intimate yet wide, utilizing lush stereo imaging for the background textures while keeping the lead vocal and bass strictly centered to maintain a sense of physical presence. The dynamic range is carefully controlled to ensure a smooth, professional sheen that feels both expensive and organic.

Vocal Details
Vocal Gender & Timbre: A male vocalist delivers the lead performance, featuring a velvety baritone timbre with a rich, resonant chest voice. The texture is smooth and supple, capable of transitioning into a silky head voice for higher melodic flourishes, maintaining a consistent "expensive" tonal quality throughout.
Vocal Style: The delivery is marked by a conversational, behind-the-beat phrasing that emphasizes the urban soul aesthetic. The artist employs a signature hook motif featuring a rising major third interval on the key resolutions. Phrasing is highly syncopated in the verses, moving into long, emotive legato lines in the chorus. The bridge requires a dramatic shift to a "whisper-singing" technique, utilizing heavy vocal fry and breathy tail-offs to convey extreme proximity. Melodic contours are embellished with graceful pentatonic runs and subtle chromatic passing notes that bridge the gaps between the primary chord tones.
Harmony/Backing Vocals: The choruses are bolstered by tight, three-part male harmony stacks that provide a lush, gospel-influenced bed. These harmonies utilize a "wash" effect, panned hard left and right to envelop the lead. During the bridge and outro, call-and-response ad-libs appear, acting as a secondary rhythmic counterpoint to the lead melody.
Vocal FX: The lead vocal is treated with a vintage tube-saturation emulation for warmth and a short, dark room reverb to simulate an intimate physical space. A synchronized 1/8th note delay is applied selectively to the ends of phrases in the verses to fill the gaps, while the backing harmonies are processed with a high-pass filter and shimmering chorus effect to separate them from the main vocal.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A clean, jazz-influenced electric guitar serves as the foundation, performing sophisticated seventh-chord inversions with a light chorus effect. In the verses, it utilizes palm-muted stabs and rhythmic scratches to drive the movement. A deep, slightly distorted electric bass provides the melodic backbone, locking into a pocket-heavy groove that defines the urban soul genre.
Secondary: A vintage Rhodes piano enters in the second half of the verses, providing shimmering chord extensions and liquid-like melodic fills. During the chorus, a secondary rhythm guitar is introduced, playing muted funk-style ostinatos that thicken the midrange. In the bridge, the arrangement strips back to just the clean guitar and a high-register, shimmering sine-wave synth drone that creates a sense of suspended time. A subtle string ensemble enters in the final chorus to provide a cinematic swell before the instruments begin to drop out for the outro.
Groove & Foundation Progression: The groove is anchored by a mid-tempo breakbeat featuring a crisp, layered snare and a soft, rounded kick drum. The hi-hats maintain a swung sixteenth-note pattern, providing a sophisticated rhythmic tension. The bass line evolves from a simple two-note pulse in the intro to a busy, syncopated funk line in the chorus. During the bridge, the percussion drops out entirely, leaving only a subtle finger-snap on the backbeat to maintain the pulse before the full kit re-enters for the final climax.
Embellishments, Textures & Spatial FX: Subtle atmospheric pads create a warm bed of sound that bridges the frequency gap between the bass and the guitars. A localized foley sound of a jukebox mechanism clicking is heard briefly before the second verse to ground the narrative. Transitional elements include soft wind-chime textures and reverse reverb swells that lead into the choruses. The outro employs a gradual low-pass filter sweep on the secondary instruments, leaving only the bass and a final vocal phrase to linger in the silence.
```

**Input lyrics:**

```
​[Verse 1]
I was leaning back, without a care
Didn't see you there, fingers through your hair
Wasn't looking for a soul to lay me bare
Out of nowhere, you were standing there
The way you looked, the way you moved your eyes
Had me hooked, I feel it deep inside
​[Chorus]
I want your hands right here on my hips
(Pull me closer)
Till your love lands right on my lips
(Win me over)
I never, ever planned on this
(Maybe if we go there)
We’ll never have to wonder if...
So baby, just give me a kiss
​[Verse 2]
Your simple "hello" had me in a trance
All I could think was, do I have a chance?
Will you put your hands all over me?
How long 'til we’re wrapped in ecstasy?
Then just like that, the jukebox started playing
"Chemical Romance"—you asked, "Are you dancing?"
And I said...
​[Chorus]
I want your hands right here on my hips
(Pull me closer)
Till your love lands right on my lips
(Win me over)
I never, ever planned on this
(Maybe if we go there)
We’ll never have to wonder if...
So baby, just give me a kiss
​[Verse 3]
One single dance turned into all night
I never planned to see the morning light
The way you moved swept right through my mind
Your presence seemed to wash away the time
One final question's burning on my mind:
Where will we find ourselves tonight?
Your place or mine?
​[Bridge]
(Music strips back, quiet and intimate)
Slow down, baby, don’t say a word
Just let this moment breathe
I don’t need your entire world
Just what you see in me
If this connection lasts tonight
Let’s make it something sweet
If it’s more than a fleeting spark
Then baby, fall into me
​[Chorus]
I want your hands right here on my hips
(Pull me closer)
Till your love lands right on my lips
(Win me over)
I never, ever planned on this
(Maybe if we go there)
We’ll never have to wonder if...
So baby, just give me a kiss
​[Outro]
(Fading out)
Your place or mine?
Just give me a kiss...
(Fall into me)
[End]
```

### Forever

*showcases: vocals · 2:27*

**Prompt (Structured Caption):**

```
[Global Metadata]
Basic Attributes: bpm is 96. key is Eb, and scale is minor. Pop Urban / Modern Rhythm.
Global Emotional Progression: The track initiates with a steady, calculated poise, establishing a cool and guarded emotional foundation. As the arrangement moves into the core rhythmic sections, the mood shifts toward a resilient, unwavering strength, reflecting a sense of modern urban romanticism. The tension builds through the mid-section, transitioning from emotional distance to a grounded acceptance, culminating in a lush, harmonically rich conclusion that balances grit with vulnerability.
Application Scenarios & Imagery: Late-night drives through a neon-lit metropolis, sophisticated urban lounges, or cinematic scenes depicting a complex interpersonal dynamic within a modern architectural setting.
Sonics & Production Profile: The soundstage is deep and immersive, characterized by a prominent sub-bass presence that anchors the frequency spectrum. High-end clarity is prioritized for the vocal and percussion, while the mid-range is intentionally carved out to provide space for the primary instrumental layers. The dynamic profile is highly polished, utilizing side-chain compression to allow the rhythmic elements to breathe against the melodic textures.

[Vocal Details]
Vocal Gender & Timbre: Female. The lead vocalist features a velvety, soulful timbre with a sophisticated rasp in the lower register. The voice is crystalline and agile, capable of shifting from a breathy, intimate delivery to a commanding, resonant belt that cuts through the urban production.
Vocal Style: The performance is characterized by conversational back-phrasing, moving fluidly between a rhythmic, percussive delivery and long, soaring melodic lines. A signature hook motif involves a descending minor third leap, creating a memorable earworm effect. The delivery utilizes delicate vocal fry in the verses to convey intimacy, transitioning into expressive vibrato and pentatonic runs during the more emotionally heightened sections.
Harmony/Backing Vocals: Dense, wide-panned vocal stacks appear in the later sections to create a lush harmonic bed. These layers utilize close-harmony triads and octaves, providing a shimmering choral effect that reinforces the lead melody without overwhelming the central narrative focus.
Vocal FX: The primary vocal is treated with a precise digital delay synchronized to the tempo and a large hall reverb with a high-pass filter to prevent muddiness. Subtle pitch correction is used as an aesthetic choice to achieve a sleek, modern pop sheen, while parallel saturation adds warmth to the mid-frequencies.

[Arrangement]
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: An ambient, ethereal synth pad provides a wide atmospheric wash during the opening, creating a sense of vast spatial depth. This is accompanied by a clean electric guitar, featuring a chorus-drenched tone and fingerpicked arpeggios that establish the harmonic progression.
Secondary: A heavily distorted electronic bass enters to provide a gritty, aggressive counterpoint to the clean melodic elements, occupying the low-frequency domain with a sustained, saturated growl. An additional rhythm guitar, utilizing a slightly overdriven, mid-forward tone, enters during the high-energy sections to provide syncopated chordal stabs and melodic thickening. A subtle, high-register crystalline bell synth provides a shimmering counter-melody during the bridge, acting as a delicate textural accent.
Groove & Foundation Progression: The groove is built upon a syncopated urban beat, featuring a crisp, layered snare and a heavy, rounded kick drum that emphasizes the downbeat. The rhythmic foundation evolves from a minimalist, spacious pattern into a dense, driving groove as the second rhythm guitar and percussion layers—including sharp hi-hat rolls and wooden rimshots—are integrated to increase the track's momentum and energy.
Embellishments, Textures & Spatial FX: The track features cinematic sub-drops and white noise sweeps to signal structural transitions. Brief vocal chops are processed with a telephone-style EQ and dispersed throughout the stereo field to add modern rhythmic texture. Strategic silences and sudden instrumental drop-outs are utilized to emphasize key vocal delivery moments, while a soft, pulsing rhythmic synth flourish provides a sense of perpetual motion in the background.
```

**Input lyrics:**

```
No worries, it’s all fine, it’ll be good somehow,
We’re a bond forever, we’re solid now.
I’m cold like a stone, you’re strong like the ground,
That’s the perfect match – you a man, me a woman found.
You’re good to me, so I bend your way,
I see that you love me, that you fight, you stay.
Just don’t let me get bored, don’t cross that line,
Stay cool and I’ll drop my guard in time.
Cold blood runs through me, but I know how to love,
I’m just waiting for the moment you knock me off my feet, my love.
It’ll be okay, I’m not a hungry beast,
I want you the way you want me.
Love goes on… everything’s okay.
I’m hard like stone,
And you’re gentle, kind.
If you weren’t here beside me,
Who knows where we’d end up, where we’d find our time.
One side always has to bend a little more,
I’m the other side, thinking for both, to keep the score.
So we can be good, so things feel right,
No one’s perfect,
But we can always be our best tonight.
```

## EDM

### Dream

*showcases: arrangement / instrumentation · 2:25*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 126. key is Ab, and scale is major. EDM / Progressive House.
Global Emotional Progression: The track begins with a sense of focused, quiet inspiration that steadily builds into a driving, creative momentum. The verses maintain a grounded energy that surges into an uplifting and euphoric chorus, representing the realization of artistic vision. The bridge introduces a heightened sense of urgency and adrenaline, leading into a final, high-lift climax before resolving into a triumphant, lingering conclusion.
Application Scenarios & Imagery: High-energy creative workspaces, late-night driving through illuminated urban environments, or the celebratory peak of a summer festival set. The imagery evokes vibrant ink flowing across digital canvasses, neon light reflecting off glass, and the visceral rush of bringing an abstract idea into physical reality.
Sonics & Production Profile: The soundstage is expansive and panoramic, characterized by a pristine high-end shimmer and a tightly controlled, punchy low-end. High-fidelity production ensures every layer is distinct, with a clear focus on the mid-range for vocal presence, while the dynamic range is optimized for a powerful, floor-filling presence through heavy parallel compression and polished limiting.
Vocal Details
Vocal Gender & Timbre: A solo male vocalist delivers the performance, featuring a rich, resonant tenor timbre with a slight gravelly texture in the lower register. The voice is characterized by a warm, breathy quality in the intimate sections that transforms into a powerful, belt-focused resonance during high-energy passages, ensuring a highly realistic and emotive human presence amidst the synthetic instrumentation.
Vocal Style: The delivery is conversational and rhythmic in the opening, utilizing syncopated phrasing that sits slightly behind the beat for a relaxed feel. As the track progresses, the melodic contour shifts toward iconic rising 5th leaps and soaring pentatonic runs during the hook. The performance incorporates expressive vocal fry on the start of phrases and graceful falsetto flips at the end of melodic lines to convey emotional depth, maintaining an urgent staccato burst rhythm during the bridge.
Harmony/Backing Vocals: Lush, wide-panned vocal stacks appear in the chorus to create a wall-of-sound effect. These consist of three-part harmonies and a lower octave double that adds weight and authority to the central hook. During the bridge, ethereal "ooh" and "aah" textures are layered in the background, treated with a high-pass filter to sit above the lead.
Vocal FX: The lead vocal is treated with a combination of short slap-back delay for thickness and a large hall reverb with a two-second tail for spatial depth. De-essing is applied to maintain a smooth top end, while subtle saturation adds harmonic warmth. A rhythmic trance-gate effect is briefly applied to backing vocals during the transition to the final chorus for a modern electronic texture.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A warm, analog-style pluck synthesizer serves as the primary melodic engine, providing a rhythmic, oscillating foundation that evolves from a muted filter state to a fully open, bright lead. This is supported by a thick, layered supersaw pad that enters during the chorus to provide harmonic density and a sense of grandeur.
Secondary: A rhythmic digital bell sequence provides a high-frequency counter-melody during the verses, adding a shimmering, clock-like precision. In the pre-chorus, rising white-noise oscillators and tension-building synth stabs emerge to signal the transition. During the bridge, a secondary acid-inspired 303 bassline provides a growling, filtered movement that acts as a call-and-response to the vocal phrases, vanishing just before the final lift.
Groove & Foundation Progression: The foundation is built on a solid, weightless sub-bass that locks perfectly with a crisp, punchy four-on-the-floor kick drum. The groove starts with just the kick and a subtle shaker, expanding in the chorus to include a bright, metallic clap on the backbeat and syncopated 16th-note closed hi-hats. The bassline transitions from a steady root-note pulse in the verses to a more melodic, driving rhythm in the chorus to enhance the track's forward motion.
Embellishments, Textures & Spatial FX: The arrangement is punctuated by cinematic sub-drops and crystalline synth sweeps that mark the beginning of new phrases. Impact hits with long, shimmering reverb tails emphasize the arrival of the chorus. Brief, localized foley sounds of a digital pen scratching on a tablet are used as a rhythmic accent in the transitions, while pitch-shifted vocal chops provide a melodic texture in the post-chorus breaks, creating a modern, high-gloss aesthetic.
```

**Input lyrics:**

```
(Verse 1)
I grab my pen, heart starts to race,
Time to escape, to claim my space.
Each stroke of ink breathes life anew,
Worlds awaken where dreams come true.
(Chorus)
I’m weaving tales untold, characters bold,
Adventures unfold in colors and gold.
Through ink and paper, I carve my way,
In this realm of wonder, forever I stay.
(Verse 2)
From the shadows of mind, stories ignite,
Panels bloom under late-night light.
Lines and curves carry all my soul,
Where impossible dreams find control.
(Chorus)
I’m weaving tales untold, characters bold,
Adventures unfold in colors and gold.
Through ink and paper, I carve my way,
In this realm of wonder, forever I stay.
(Bridge)
Every stroke sparks a rush inside,
Bringing visions I can’t hide.
In this endless sea of creation,
I chase the thrill, my true salvation.
(Chorus – with lift)
I’m weaving tales untold, characters bold,
Adventures explode in stories retold.
Through ink and paper, I find my fire,
In imagination’s glow, I never tire.
(Outro)
So I’ll keep creating, with passion so free,
This world of my making is where I belong—me.
Pen in hand, heart open wide,
In stories forever, my spirit will ride.
```

## Folk

### 月色

*showcases: regional genres (Chinese) · 1:59*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 82. key is Ab, and scale is major. Contemporary Folk / Electronic Crossover.
Global Emotional Progression: The track initiates with a sense of solitary longing and quietude during the opening verse, characterized by an intimate acoustic setting. As the first chorus emerges, the emotional energy swells into a bittersweet romanticism, buoyed by the introduction of rhythmic elements. The instrumental solo provides a reflective bridge, shifting the mood toward a more poignant, melancholic realization. The final repetition of the verse and chorus solidifies a journey from hopeful yearning to a sophisticated, tragic acceptance, finally dissolving into a hollow, ethereal stillness during the outro.
Application Scenarios & Imagery: This composition evokes the image of a moonlit riverbank at midnight, where the reflection of the moon on moving water mirrors a restless heart. It is perfectly suited for high-end cinematic sequences involving internal monologues, or as a late-night listening experience for emotional catharsis and introspection.
Sonics & Production Profile: The production features a high-fidelity, hybrid soundstage where organic acoustic textures coexist with crisp, digital transients. The frequency response is characterized by a rich, low-mid warmth from the guitar and vocals, contrasted against the deep sub-frequencies and sharp, clicking high-end of the electronic beats. A wide, lush stereo image is used for the ambient layers, while the rhythmic core remains tightly centered.

Vocal Details
Vocal Gender & Timbre: A male vocalist provides a warm, velvety tenor performance. The timbre is breathy and intimate, featuring a natural grain that suggests vulnerability and physical proximity to the microphone.
Vocal Style: The delivery is conversational and narrative, utilizing back-phrasing to create a relaxed, folk-influenced timing. The melodic contour is defined by a signature hook motif featuring a descending major third that resolves into a gentle vibrato. Performance articulations include subtle vocal fry on low-register starts and graceful falsetto flips during the emotional peaks of the chorus. The phrasing alternates between legato connections in the verses and more rhythmic, syncopated pulses that lock in with the electronic beats during the refrain.
Harmony/Backing Vocals: In the chorus sections, the lead is reinforced by whispered double-tracking and a low-octave unison layer to add weight. During the second half of the chorus, distant, ethereal "ah" vocables are panned wide to simulate the "songs from the opposite bank" mentioned in the thematic cues.
Vocal FX: A sophisticated chain of warm analog saturation is applied to the lead, complemented by a large hall reverb with a long pre-delay. Subtle rhythmic delay taps are audible on the ends of phrases in the chorus to enhance the sense of space.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary Layering: The foundation is a meticulously recorded steel-string acoustic guitar. It employs a hybrid picking style—combining thumb-plucked bass notes with delicate fingerstyle arpeggios in the high register to provide both harmonic structure and a rhythmic pulse. The guitar remains the constant thread throughout the entire lifecycle of the track.
Secondary Layering: A warm, analog-style synth pad enters during the intro, providing a soft ambient floor. Upon reaching the chorus, a distorted electric bass enters, providing a gritty, modern contrast to the clean acoustic guitar. During the instrumental solo, a clean electric guitar with a chorus effect takes the lead, performing a lyrical, blues-inflected melody characterized by slow slides and expressive bends. In the final chorus, a second rhythmic electric guitar layer is added, playing muted power-chord pulses to increase the perceived density and urgency of the arrangement.
Groove & Foundation Progression: The groove is a sophisticated blend of organic and synthetic elements. While the verse relies on the internal rhythm of the guitar, the chorus introduces a programmed electronic beat featuring a deep, rounded kick drum and crisp, "glitch" style hi-hats. The bassline provides a syncopated, driving force that pushes against the laid-back vocal delivery, creating a compelling rhythmic tension that peaks in the final chorus before dropping out for the sparse, acoustic-led outro.
Embellishments, Textures & Spatial FX: The track is punctuated by subtle electronic textures, including reverse-reverb vocal swells and soft white-noise rises that transition between sections. Small, crystalline bell-like synth plucks appear intermittently to mimic the "sparkling ripples" of a moonlit river. The outro concludes with the gradual fading of the electronic elements, leaving only the acoustic guitar and a final, lingering sub-bass note that slowly decays into silence.
```

**Input lyrics:**

```
[Verse 1]
河上的月色
异样的明朗
我对着它想念
想念我的情郎

[Chorus]
有这么一个夜晚
隔岸的歌声
使我们的心荡
我们偎着吻着
羞看漫烂的波光

有这么一个夜晚
隔岸的歌声
断我们的心肠
我们愁了泣了
背向漫烂的波光

[Instrumental Solo]

[Verse 1]
河上的月色
异样的明朗
我对着它想念
想念我的情郎

[Chorus]
有这么一个夜晚
隔岸的歌声
使我们的心荡
我们偎着吻着
羞看漫烂的波光

有这么一个夜晚
隔岸的歌声
断我们的心肠
我们愁了泣了
背向漫烂的波光

[outro]
```

## Hiphop

### The Hit

*showcases: vocals · 1:35*

**Prompt (Structured Caption):**

```
Global Metadata
Basic Attributes: bpm is 108. key is G, and scale is minor. Hip Hop / Funk
Global Emotional Progression: The track opens with a focused, industrial-tinged atmosphere that quickly transitions into a playful yet high-stakes rhythmic drive. The energy is calculated and precise during the verses, mirroring a state of deep concentration. The choruses act as a celebratory release, broadening the sonic spectrum with a vibrant, celebratory funk aesthetic. As the track progresses, the intensity builds toward a peak of rhythmic bravado in the final third, concluding with a sharp, punchy rhythmic resolution.
Application Scenarios & Imagery: A fast-paced holiday hustle in a modern urban apartment, rhythmic montages of artisanal craftsmanship, or high-energy festive retail environments. The visual imagery involves crisp metallic edges, bright festive patterns, and rapid-fire hand movements.
Sonics & Production Profile: The production features a heavy, saturated low-mid range to emphasize the funk elements, contrasted by surgically sharp high-end transients. The soundstage is intimate during the verses, focusing on the center-channel vocal, but expands significantly in the choruses with wide-panned melodic layers. A dry, "in-your-face" aesthetic dominates the percussion, providing a tactile, percussive feel to the entire mix.
Vocal Details
Vocal Gender & Timbre: Male. The vocalist exhibits a charismatic, gritty tenor with a distinctive rhythmic elasticity. The timbre is lean and agile, allowing for rapid-fire delivery without losing clarity, possessing a natural rasp that adds a layer of street-wise authenticity to the holiday-themed narrative.
Vocal Style: The delivery is characterized by a "on-the-beat" urgency, utilizing syncopated back-phrasing that dances around the snare hits. The performance features iconic rising 5th leaps at the end of key phrases to create a sense of triumph. Notable articulations include staccato bursts during the technical descriptions and a relaxed, swaggering lean during the conversational interludes. Pentatonic melodic runs are occasionally employed during transitions to bridge the gap between rap and funk melody.
Harmony/Backing Vocals: Dense, three-part soul-inspired harmonies appear during the choruses to provide a lush, wide-stereo contrast to the mono-focused verses. Ad-libs are peppered throughout the stereo field, utilizing "shout-along" unison textures to emphasize the rhythmic cadence of the hook.
Vocal FX: The lead vocal utilizes a parallel saturation chain for presence and a tight room reverb to simulate a physical studio space. High-pass filtering is applied during specific breakdown moments to create a "telephone" effect, while the choruses feature subtle chorus and thickening agents on the backing layers.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: A highly distorted, growling electric bass serves as the primary melodic engine, providing a heavy, rhythmic pulse that dictates the funk-hop hybrid feel. This is complemented by a clean, percussive electric guitar that utilizes palm-muted scratches and sharp 9th-chord stabs to maintain a high-frequency rhythmic counterpoint.
Secondary: A gritty, analog synth lead enters during the second half of the verses, providing a snake-like counter-melody that weaves through the vocal gaps. During the bridge, a bright, vintage-style electric piano adds harmonic depth with syncopated rhythmic clusters. A layer of shimmering, high-register bells provides a subtle holiday-themed melodic wash in the background of the choruses.
Groove & Foundation Progression: The foundation is built on a heavy, "swing-quantized" drum machine groove. The kick drum is massive and short-tailed, locking in perfectly with the distorted bass. The snare is a hybrid of a classic clap and a high-tuned wooden rimshot, providing a crisp "snap" on beats two and four. The hi-hats evolve from a closed, tight pattern in the intro to a loose, "sloshy" open-hat feel during the peak energy moments of the final chorus.
Embellishments, Textures & Spatial FX: The track features localized foley sounds of metallic scissor snips and the tactile "zip" of adhesive tape, rhythmically integrated into the percussion track. Sub-bass drops emphasize the start of each chorus, while reverse-reverb vocal swells act as transitions between the verses and the hook. Short, punchy brass-section hits are used as rhythmic exclamation points during the final verse to heighten the funk aesthetic.
```

**Input lyrics:**

```
Yeah, I gotta wrap, stack the paper, fold the flap,
Tape it down, flip it ‘round, put the ribbon on the back.
All these boxes in my room, man it’s lookin’ like a trap,
But it’s Christmas on the grind — yeah, you know I gotta wrap.

Hit the store, get the roll, pick the pattern with the shine,
Candy cane, snowflake — everything lookin’ fine.
Got the scissors in my hand like I’m ’bout to cut a rhyme,
And this tape runnin’ out like it’s racing against time.

Corners crisp, lines tight, yeah I’m foldin' with precision,
Presentation on point — that’s a holiday decision.
Got the bows color-coded, you would think I’m on a mission,
If gift-wrapping was a sport, I’d be leading the division.

Yeah, I gotta wrap, stack the paper, fold the flap,
Tape it down, flip it ‘round, put the ribbon on the back.
All these boxes in my room, man it’s lookin’ like a trap,
But it’s Christmas on the grind — yeah, you know I gotta wrap.

I’m the elf with the heat, call me Santa’s right-hand,
Every present in the pile got a Will-made brand.
Got the tags all marked, got the pen in command,
If the wrapping game’s a beat, I’m the one who runs the band.

Gift bag? Nah man — I’m a wrapper with pride,
I’m the reason that the tree lookin’ fancy on the side.
With a crease so clean you could use it as a guide,
I bring holiday swagger — I’m the wrap-certified.

From the stockings to the sleigh, I’m the one they call to play,
Got that peppermint drip like it’s froze in a display.
If the season had a hustle, I’d be wrappin’ every day —
Merry Christmas, keep it rollin’, now unwrap it right away!

Yeah, I gotta wrap, stack the paper, fold the flap,
Tape it down, flip it ‘round, put the ribbon on the back.
All these boxes in my room, man it’s lookin’ like a trap,
But it’s Christmas on the grind — yeah, you know I gotta wrap.
```

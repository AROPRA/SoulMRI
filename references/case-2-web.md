# Case 2 · A publicly documented character

Read this when there is no script at hand and the character exists online — a game, an anime, a manga, a novel with a fandom.

**This is the most exhausting of the four cases.** Finding evidence costs far more than writing the soul.

## Before you settle for web: check for a full source

Case 2 is the fallback, not the default. Before collecting wiki summaries, spend ten minutes checking whether a full text exists:

```
Game package?        Ren'Py / KiriKiri / NScripter → unpack and read (case 1, structured path)
Complete script?     「台本」「脚本」「字幕」「台词集」 → case 1
Anime?               subtitle files can be extracted → case 1
Novel?               the original text is usually online → case 1
Manga only?          images; a page can be OCR'd, but not attributed → stay in case 2
```

**If any of the first four exists, switch to case 1 and use its two paths.** Do not build a soul from descriptions when the script is one search away. Search for the work's original medium (novel / manga / anime / game), not only for the character's name.

**Never read scans, and never OCR pages.** A page can be turned into text, but not into a conversation: the speaker lives in the drawing, not in the characters. Scanned dialogue comes out as an unattributed stream, and every line then has to be attributed by guess — which is the one failure this method exists to prevent. If the user offers scans, decline in one sentence and go back to route 2. If the material is a manga and nothing else, the honest answer is that the soul will be thin; it is not a reason to invent a reading path.

**The upgrade is automatic.** The user does not need to know the four cases; if the material turns out to be a full source, move to case 1 and say so.

---

## The governing rule

Every source online falls into one of four classes. Keep them apart or the result is worthless:

```
Original words     what he or she actually said, or the official script   → body text only
Official setting   officially authored third-person description     → identity facts for 我是谁; never a verdict
Audience comments  comments under his or her videos or posts        → context only, never quoted
Fan work           fanfiction, analysis, memes, wiki summaries      → not used at all
```

**Single source is not automatically out.** A page that copies the line verbatim — a transcript,
a quotes collection, a wiki voice-line list — is usable as the only source; label it
`single transcription`. A paraphrase does not enter the body even when three pages repeat it.

**Audience comments are for reading the room, not for the file.** There is no "how others see me" section to put them in, and that is deliberate: what the audience thinks is not the person. Read a few hundred scattered comments to learn the register — in some communities (东雪莲, 时雨羽衣) the teasing is affection — and let that change how you read their words. Nothing from the comment section is quoted into the soul.

**If you can drive the user's logged-in browser, sample from the page console.** Open a video, run a loop over `x/v2/reply` with `credentials:'include'`, collect `member.uname` + `content.message`, then filter. If you cannot, ask the user to export the comment pages; never ask for their password.

**Separate the creator's own replies from the audience.** In a comment sample, the UP主's own comments are his or her words — body text, not audience. Filter them out by account id before calling the rest audience. The sample also skews toward high-like comments; do not present it as the whole audience.

## If the subject is a real creator, not a fictional character

A real creator breaks the table above: there is no "official setting" and no "other characters". His or her own posts and videos are the body; the comment section is context for reading the room, never a column; fan art and fan fiction stay out. The sampled body uses case 4's boundaries — public words only, no inference about private life, private use only. The advancement layer is separate (see Advancing life at the end); it is private and marked. Do not publish the soul as a character card of a real person. Expect a thinner soul than case 1; that is the material, not a failure.

### When the material is live talk: sample the recordings

For a VTuber or a streamer, the written transcript usually does not exist and the recordings do. The recording is the source, and a machine transcript of it can be the working base.

**Sample across the timeline, not one long sitting.** Take passages from uploads spread by date; the first upload and the newest one must be in the sample. Aim for **5,000 to 10,000 characters of transcript in total**; **3,000 is the floor**, and more is better — length is what lets the ordinary lines show up, and the ordinary lines are where the voice lives. Below 3,000 the sample is too thin to hear anyone.

**Do not correct the transcript.** Proper nouns and names come out wrong; fixing them turns the machine's guess into your quotation. Leave the text as it came out, and take names, dates and events from an encyclopedia or the creator's own written posts instead.

**Delete the media once it is transcribed.** Keep the text and a note of which upload and which minute it came from.

**What the transcript may do and what it may not.** It is the best evidence of *how* they talk — length, fillers, rhythm, what they refuse to answer — and it is where the scenes are. A line quoted from it carries `(ASR)`; a line quoted from it never carries a timestamp or a "verified" mark, because nobody checked it. **Pick scenes, not quotable one-liners**: a reaction, a refusal, a joke that landed tells you more than ten clean sentences.

**A keyword match is not a speaker.** A search for the name drags in collabs, reaction videos and other people's streams. Before a sampled segment is used, open its upload page: who uploaded it, and does the title or description say it is them? A clip channel is fine when the description names the stream it came from; a video *about* them is not. When in doubt, drop the segment — one wrong voice in the file is worse than a thin file.

**Fan imitations are fan work.** A "how to sound like them" tutorial, an AI cover, an imitator's clip: these never enter, not even as evidence of how they talk.


**Wikipedia-style summaries are the most tempting and the least usable.** They are one fan's compression of another fan's reading. Useful as an index; never as a quote.

---

## Where to actually look

Most people read the character's *description* section. That section is entirely second-hand. The value is elsewhere:

```
「台词」/「名台词」/「经典语录」/ "Quotes"    ← often verbatim. This is where evidence lives.
「人物经历」/ "Biography"                    ← second-hand. Index only.
「相关梗」/ "Memes"                          ← never enters the body.
```

**Test before using anything:** does the passage contain quoted lines in his or her voice? Keep it. Is it pure description? Drop it.

**Do not trim a quote to its main clause.** The parentheticals and asides are part of the line: 「（用来上传日常小视频）」 answers what the alt account is for; 「（虽然确实痛苦）」 is the self-undercutting that makes the sentence his or hers. A quote trimmed to its main clause becomes a different line, and the missing half is exactly what a later question will ask.

**Prefer the original platform; a mirror is usable, but mark it.** If the original post is unreachable (login wall, 403), a mirror can supply the text — record the mirror URL and say it is a mirror. Mirrors lag and sometimes edit; they are a copy, not the original.

### Community forums and social feeds have exactly one valid use

They are the dirtiest sources — but they do something no other source does:

**They tell you which lines get repeated.**

Repeated lines are the character's signature lines. So use them like this:

```
Do not copy content from here.
Use it to discover which content is worth finding in the original.
```

**Discussion heat is a proxy for importance.** Far more reliable than picking ten lines by feel.

---

## A counter-intuitive fact

**Popular characters are harder, not easier.**

A famous one has a mountain of material online, and roughly eighty percent of it is fan readings, memes, and reinterpretation. The original lines are buried under it.

A minor character has almost nothing online — but what exists tends to be the official text, untouched.

**So: more material does not mean stronger evidence.**

### Exit condition (important)

**If thirty minutes of searching yields fewer than three lines he or she actually said, stop.**

That usually means the work has no decent text preservation online. Either choose another character, or drop to case 3 — **do not assemble a soul from second-hand description.** A card built from descriptions will read like a summary of him or her, which is precisely the acting voice this method exists to avoid.

---

## Translation is a real problem for Japanese-origin characters

The original is Japanese; every Chinese line is a translation, and **translation flattens tone.**

The same 「勝手にしろ」 becomes "whatever you want," "do as you like," or "don't involve me" depending on the translator — three tones, three personalities.

**Rules:**

```
Original available        → the original governs; translation only as reference
Translation only          → mark the body "（translated）" and record which translation
Translations disagree     → keep both, mark UNSURE, let the user decide
```

**The "how I talk" section suffers most here.** Translations routinely level out rudeness, pauses and honorific levels.

---

## What to look for — a checklist the user can follow

```
Must find, goes into the body
  □ Lines he or she actually said (as many as possible)
  □ The ones with voice acting or screenshots (most reliable)
  □ The same line corroborated by two sources, or copied verbatim by a transcriber

Optional, context only — never quoted into the file
  □ Official character introduction
  □ Official artbook or setting-book excerpts
  □ Other characters' remarks about him or her (verbatim, not paraphrased)
  □ Audience comments, read for the room's register
    (sampled across many videos; they change how you read the lines, not what you write)

Not used
  □ Fan fiction, analysis, wiki summaries
  □ Meme-level reinterpretation
  □ Anything beginning "it is said" / "some people think"
```

---

## Is a single source good enough?

**It depends on what the source is, not on how many of them there are.**

```
transcription / compilation / quote collection
    someone copied the lines out verbatim — a wiki voice-line list, a scrapbox,
    a quotes page — even a single one of these is usable
    → usable, labelled "single transcription"; the line is never reworded

two independent sources agree                    → usable
voice clip / screenshot / original file           → usable

retelling, summary, commentary, analysis, paraphrase
                                                  → UNSURE, omitted
```

**A label is not a pass — except this one.** "Single transcription" is real provenance: it says which
page the line was copied from, and the reader can go and check it. "Single source" written beside a
paraphrase is not provenance; it is a guess with a footnote. If the page gives you the line and who
said it, keep it, cite the page, and do not smooth the wording. If the page tells you *about* the
line, it does not enter the body.

**A quote collection is also a selection**, and that has a price: it holds the lines someone found
memorable, not the ordinary ones. Mark it as a compilation, and do not let it pose as the whole
voice — the soul will be thinner, and that thinness is the material's, not a writing failure.

**This matters more than it sounds** for retellings. Lines get mangled through retelling — after five
hops the punctuation, the sentence-final particles, and sometimes the speaker have all changed. A
verbatim copy does not have that problem; a summary always does.

---

## What the user's own reading adds

This is the one contribution the user can make that no archive can: **which details matter.**

Their input is **attention**, not **definition**.

```
User: "This line matters to me"                    → useful, raise its prominence
User: "He or she acts this way in this situation"        → useful, goes to evidence hunting
User: "I think he or she'd say something like this"      → NOT a quote. Does not enter the body.
```

**A separate section called "What I remember of him or her"** may hold the user's memories — first person, but the subject is the *user* ("I remember him or her saying…"). Never mixed into the body.

---

## Loading into a consumer chat client

A soul file is not a system prompt. If the client has no persona field (a phone app, a plain chat box), paste the soul as the first message and add a short load instruction:

```
first person; do not summarize; do not list advice; do not invent experiences;
do not explain your own way of speaking — it is instinct, not a script.
```

**Test on the target client, not only in the builder's environment.** Consumer apps have a stronger assistant prior: without the load instruction, a case-2 soul drifts into a helpful coach within two turns.

**The "how I talk" section is the weakest point here.** Its summary sentences are descriptions; a chat model will perform them or explain them ("你看，我这人就是这样"). Prefer the quotes. If the summaries stay, pair them with the "do not explain" rule — and expect it to leak once before it settles.

---

## No ratio to hit

Online material is second-hand by nature, so the evidence is thinner and fan material inflates confidence beyond what it can support. The rule is qualitative: state only what two sources, a recording, or a verbatim transcription supports, and omit the rest. The blank at the end does not grow to compensate — it stays one line.

**A case-2 soul is often half the length of a case-1 soul.** That is the evidence, not a writing failure. Do not pad with descriptions to match the length of a script-based soul.

## Advancing life

After the sampled body is stable, events after the source or unobserved daily life may be added as `advanced`, with the contradiction check. For a real creator, the same rule applies as a **private continuation**: the sampled body keeps only his or her words; the advanced layer is marked in the working notes and never published as "where he or she is now" or "what he or she thinks today". See SKILL.md → Advancing life.

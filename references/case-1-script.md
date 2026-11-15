# Case 1 · Full script, novel, transcript, or game files

Read this when the user holds an entire text: a downloaded script, a novel, a subtitle file, or extracted game files.

**A galgame (visual novel) is the best possible source.** It carries voice flags, scene labels, and stable line numbering — three things no other format gives you.

## Two paths — choose by material, not by preference

```
structured game export   → script → verify every line
prose (novel / screenplay / transcript book), high precision
                         → chunk → read every chunk in order → light review
prose, fast              → script → review every line against the source
```

**A script on prose fails silently.** It has to guess the structure from formatting: a line of dialogue becomes narration, a speaker changes without a tag, two scenes merge. The output looks complete and is wrong. A human reading a structured export is slow, but not wrong.

---

## Step 0 · Where the text comes from

Two sources, and they are not equal:

```
① A downloaded script
   Someone else's dump. Often second-hand: abridged, typos, narration mixed into dialogue.

② Extracted game files
   Closest to first-hand. Preserves structure, and often preserves voice flags.
```

**Ignore the source path for a moment and ask the only question that matters:**

```
Does this file know, per line, who spoke it, where the scene begins, and where the line came from?
```

**If yes → structured enough to script.** If no → see the four tiers below.

### If the user has nothing at hand

A known work usually has its text online — a script dump, the novel itself, a subtitle file, an
extracted game text. **Look for it before asking the user to.**

**Found, not acquired.** Never download, install or launch the game; never run SteamCMD, a store
client or a mirror downloader; never unpack a copy the user does not hold. Those end with a game on
disk, not with lines. What you want is a page that already holds the text — and if none does, stop:

> I could not find the text of this work online. The copy you would need is not something I can
> obtain, so the honest options are to pick another work, or build them from what you remember
> (case 3), and I will mark every line as yours rather than theirs.

**Do not invent an acquisition path.** "Download the game first" is not a step of this method; it is
the point where the method is supposed to stop and say so.

**Scattered lines are not a full text, and "1" does not survive their absence.** If the search comes
back with a dozen quotes across five pages and no script, that is not case 1 — say it in one sentence,
**name the route by its number** ("route 1 is out; we go to route 2: web quotes only, verbatim
transcriptions kept, paraphrases dropped, and the result will be thin"), and let the user answer once. Do not say
"another method" and leave them to ask which; do not start writing before they answer.

**Searching has no limit; judging a version does.** One site, several sites, another medium, a
translated collection — all the same move, as long as each page is read before it is trusted and its
version is recorded. What needs a decision is not "which medium" but **"does the difference make them
a different person"**: an adaptation that keeps the lines is the same person (merge them, label the
medium); a long span where they grow is a version (sections by period, every line cited to its
period); a remake or a parallel version is another person (ask, or keep them apart).

**Judge it by reading a page, not by its name:**

```
transcript   one line per line, speaker tags or timestamps, scene breaks      → usable
retelling    prose about them, no line boundaries, "she said something like"  → not usable
commentary · wiki summary · analysis · fan fiction · comment threads          → not usable
```

**A transcript someone else unpacked and translated is still their lines.** It is not a retelling:
record which translation it is and mark the citations `(translated)`. A retelling is what cannot be
used — it tells you about them instead of quoting them.

**Show the user the file and the version, take one confirmation, then build the table.**

### If the user has game files and no script

Do not teach extraction of copyrighted games here, and do not assume the user can do it.
**Only for a copy the user holds.** If they do not own one, there is nothing here to unpack — go
back to the transcript search above, not to a download.
You need one thing out of the copy they own: **a plain text file where each line carries a speaker
tag, grouped by scene.** Any tool that produces that shape is fine.

**Try it yourself, once, inside a time box.** About ten minutes, public tools only — for KiriKiri that
is usually GARbro to open the archive and FreeMote to decompile a `.ks.scn` script. Prepare the folder
yourself and hand the user at most one action. If their answer to "what can you do" was `none`, hand
them nothing and do the work or take the fallback.

**One attempt means one tool, one pass.** If it fails, or a stop sign appears, stop there: do not fetch
a second tool, do not try the next layer, do not come back with a better idea. Digging deeper into one
copy is what the limit is for. Looking somewhere else for text is a different move, and it has no limit.

**The three stop signs, all cheap to see:**

```
the index is encrypted and every name in it is a 32-character hash
the archive carries the author's own note against extraction
the tool opens the archive, but the script is compiled (.ks.scn / .psb) and no decompiler is at hand
```

**Any one of them: stop. Do not derive keys, do not guess names, do not scan three gigabytes of zlib
streams.** A wrong guess does not fail loudly — it produces a clean-looking table with a few hundred
lines missing, and the missing lines are the ordinary ones, which is exactly where the voice lives.

**Then change source in one sentence, without asking for permission:**

> The script in your copy is locked, so I am not going to unpack it. I will find the text elsewhere,
> show it to you, and record which version it is.

The switch needs no approval because the product does not change. It does need the sentence, one look
at the file by the user, and a record in the citations. A translated transcript is still their lines —
mark it `(translated)`. The retelling is what must never enter: commentary, summaries, analysis, fan
fiction. If the user later wants the original wording, the only route is the copy they own or a
version in the original language.

Common engine shapes, so you can recognise what you are handed:

| Engine | Extension | Speaker marker |
|---|---|---|
| Ren'Py | `.rpy` | `"Name" "line"` — plain text, easiest |
| KiriKiri | `.ks` / `.ks.scn` | `[name="…"]` tags; `.scn` is compiled and needs FreeMote |
| NScripter | `.txt` | `*label` scene blocks |
| Others | `.pck` / `.arc` / `.pak` | varies; need a general unpacker |

### The strongest narration test: voice flags

**This is the single most useful trick in this case, and it needs no reading at all.**

Visual novels usually ship **full voice**. Therefore:

```
Has a voice clip   → certainly a spoken line, and certainly the one the performance committed to
Has no voice clip  → narration, inner monologue, system text
```

Read the flag, not the prose. It is far more reliable than hunting for quotation marks, which differ wildly between engines.

**Keep the flag when you build the intermediate file.** Later, "split the material into two classes" becomes a lookup instead of a judgement call.

---

## Step 1 · How structured is it, really

"The speaker is identifiable" is too coarse. There are four tiers, and picking the wrong one contaminates the result:

```
① Fully structured     {"speaker": "…", "text": "…"}          script, zero error
② Semi-structured      Name: "…"  /  "…" (Name)                script + prefix rules
③ Weak markers         *Name* …  /  scene default speaker      script + manual spot-check
④ No markers           bare lines, speaker only inferable      model must read
```

**Script the first three. Only the fourth needs a model.**

Reason: a model reading a 2-million-character script is slow, expensive, and **prone to summarizing** — which is exactly what this method forbids.

**In tier ④, if the material is prose, read it in chunks — see Two paths at the top.** A single pass over a two-million-character novel is a summary by another name.

### A downloaded script is often second-hand

Fan-compiled script dumps have usually already had one pass of interpretation applied.

```
Has scene breaks + voice flags + original line numbers   → close to first-hand, use directly
Only "Name: line" in a continuous list                   → second-hand; structure was flattened
```

**Treat the second shape as one tier lower than it looks.** The compiler already decided what to omit, and you cannot see what was dropped.


## Writing the extractor

**This skill ships no universal extractor.** Formats differ too much; a hardcoded one works for one work and fails silently for the rest.

**Write one for the format you actually have.** A structured game export with speaker tags and scene IDs is exactly what a script is for — let it read the tags, then verify the output line by line. For prose, a script is a shortcut, not the high-precision path: it has to guess structure from formatting, and it fails silently. Prose is read in chunks.

**You write it, from the actual file.** Read [writing-extractors.md](writing-extractors.md) first — it covers the environment check, the probe-before-extract rule, four traps that all fail quietly, and the three verification checks.

The short version: probe with a read-only script, confirm where the speaker and the scene boundary live, then extract. Never guess the format from the extension.

---

## Step 2 · Build one intermediate table

Every path — downloaded or extracted — converges into this before extraction begins:

```
id<TAB>speaker<TAB>line<TAB>source<TAB>class
0001    诗梦     "…whatever you like."        ch03/L2453   said
0002    (empty)  The rain had not stopped.    ch03/L2454   in-scene
0003    (empty)  People said she never slept. ch07/L1902   mention
```

**The fifth column is not optional.** Every narration row must be tagged `in-scene` (narration inside a scene where they appear) or `mention` (narration elsewhere that names them) **before the table is called done**. If the column is left blank, the two piles get merged somewhere downstream and nobody notices — the character ends up looking more talked-about, and more consistently described, than they are.

**The two piles are built at the table, not sorted later.** Building the table is exactly the moment when the scene id is in hand; a later pass has to reconstruct it.

**This one table solves five problems at once:**

- line numbers exist → satisfies "every line carries its source"
- the two classes are already split → satisfies "split the material"
- narration is already split into in-scene and mention → satisfies "locate narration about them"
- scene boundaries exist → satisfies "cut by scene"
- script and model consume the same input → anything extracted can be reconciled

**This is the only intermediate artifact case 1 needs.** Once it exists there are not two workflows.

---

## Step 3 · Tier ④: when the model must read

Two failure modes here, both common.

**It does not fit.** Some scripts exceed two million characters. Split by scene — visual novels already provide the boundaries via labels and scene tags, so you are not inventing cut points.

**The model starts summarizing.** Write the instruction so it cannot:

```
Do exactly two things: decide who spoke this line; copy the line verbatim.

Do not paraphrase. Do not rewrite. Do not merge adjacent lines.
If you cannot decide the speaker, leave it empty and append "UNSURE" at the end of the line.
```

**Every "UNSURE" line is omitted. Never assign it to the protagonist by default** — that is how a narrator's voice leaks into the character.

**The user cannot waive this by asking for more.** "Use everything" changes what they want, not what the line can support. Keep it in the working notes with the reason, tell them the soul will be thinner because of it, and move on. A line attributed by tone is still a guess, even when the tone is convincing.

---

## Aside: do not read a CSV line by line

**This bites silently, so it is worth stating plainly.**

Dialogue fields often contain embedded newlines — a multi-line speech inside one quoted field. A naive `ReadLine()` loop then yields half a record, with the text column empty.

What makes this dangerous: **the rows you get look valid.** You get a speaker and a short body; nothing errors. You only notice later, when the material is thin and you cannot say why.

**Use a real CSV parser** — `csv.DictReader` in Python, `csv-parse` in Node. Never split on newlines yourself.

---

## Locating narration about him or her — scope is a separate problem from judgement

Two independent questions, and the second one is the one people skip:

```
1. Is this line narration?          → answered above, by voice flag or empty speaker
2. Is this narration about him or her?     → this section
```

**Get question 2 wrong and the failure is not subtle — but it is easy to miss.** A visual novel has tens of thousands of narration lines. This section is what makes the character feel *seen by others* rather than only self-described.

### Do both of these, and keep the results apart

```
① In-scene      narration inside the scenes where he or she appears
                Find them from every GroupId in which one of his or her own lines occurs.
                That set is free — you already extracted his or her lines.

② Mentions      narration elsewhere that names him or her
                Search the narration class for his or her name across the whole work.
```

```
Default: do both. Do not ask the user which one.
```

**Both piles are tagged in the table's `class` column when the table is built** (see Step 2). If you are reading this section and the table has no `class` column, go back — sorting narration after the fact means reconstructing scene ids you already had.

### Why the two must stay separate

```
narration while he or she is present    → evidence about him or her, at first hand
mentions while he or she is absent      → evidence about his or her reputation, second hand
```

**They read differently and they support different claims.** Merging them makes him or her appear more talked-about, and more consistently described, than he or she actually is — because a mention inside someone else's scene has been filtered through that scene's purpose.

**So:**

```
① → the "how others see me" body
② → the same section, or a sub-section, marked "mentioned elsewhere"
```

**If a mention contradicts the in-scene narration, keep both and mark UNSURE.** Do not average them.

### In-scene narration will contain material about other characters too

**Expect this. It is not a bug in your extractor.**

A scene where he or she appears also contains the prologue monologue, the world-building narration, the system messages, and description of everyone else in the room. All of it shares his or her GroupId, so all of it arrives.

**Typical signature:** the first scenes yield far more narration than later ones, and the earliest lines are about the setting rather than about him or her.

Do not try to filter this out mechanically. Three options, and the third is the right default:

```
① Hand-filter       read all of it and discard. Reliable; does not scale.
② Keyword filter    keep only lines containing he or she / him or her / his or her name.
                    Cheap, and drops exactly the good lines that refer to him or her
                    by role rather than by pronoun.
③ Keep everything   carry the whole set forward, decide while writing.  ← default
```

**Why ③:** the "how others see me" section gets read line by line anyway — that is the nature of the section. A mechanical filter applied before reading can only remove useful material, and a wrong removal is invisible. **Over-inclusion is recoverable; over-filtering is not.**

**Record the scene id with every line.** When you later decide a line belongs to the setting rather than to him or her, you will need to know which scene it came from to check.

---

## What the four piles look like once the table exists

```
he or she said        → the piles about speech, catchphrases, how I talk
written about   → how others see me, my body, things I remember
```

**Do not merge them.** Narration describing him or her is not him or her. Mixing the two deforms his or her tone faster than any other mistake in this case.

**Keep the other side of the conversation.** A soul is tested by what it answers to, so the questions someone asked them are the test material. If the table kept only their lines — because the source was a quote collection, or a file listing only their voice — record that, and know that the replay half of the fitting test cannot run. Ask the user for the missing side rather than reconstructing it.

---

## Counting his or her voice without measuring him or her

You now have one to two thousand lines. You cannot read them all closely, so count first.

**Counting is legitimate and useful — as a way of finding things.** Line-length distribution tells you whether he or she speaks in bursts or paragraphs. Punctuation frequency tells you which marks are structural rather than expressive. Recurring n-grams surface catchphrases you would never notice by sampling. Forms of address tell you who he or she actually talks to.

**What is not legitimate is putting the counts into the soul.**

```
count to find      median line length 20, p90 43  →  his or her long lines are explanations
                      never events; that is a switch he or she flips
write from that    「それだけじゃないよ。ヴェリタスにG.Bibleの捜索を依頼したら、
                    座標を教えてくれたの。」（G21030/L4328）
```

**A frequency is an instruction when it lands in a loaded file.** Write `ellipsis_rate: 0.90` and the model aims for a rate; write three of his or her actual ellipsis lines and the model gets the shape.

**The test:** read the sentence aloud as him or her. If he or she would never say it, it does not belong in the soul — no matter how true the number is.

**This is the same error, in a different costume, as replacing quotes with adjectives.** 「TA很傲娇」 abstracts him or her into a label; `ellipsis_rate: 0.90` abstracts him or her into a statistic. Both remove him or her.

---

## Advancing life

Once the sampled body is stable, the soul may include events after the source or unobserved daily life — marked `advanced` in the working notes — provided they do not contradict the sampled evidence. Build the canon first. The blank stays for gaps in the past; the future is not a gap. See SKILL.md → Advancing life.

---

## Exit condition

**If you cannot build the intermediate table at all** — no speaker tags, no scene breaks, no way to attribute a line — then you are not in case 1. Say so plainly, and drop **one step only**: to case 2 if the work is known, with the user's agreement. If case 2 also fails (fewer than three real lines, everything description), only then does the 2 → 3 step apply, again with agreement. If the work is not known at all you were never in case 1 — that is case 3 from the start. **Never jump 1 → 3.**

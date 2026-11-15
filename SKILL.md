---
name: soulmri
description: "Build a character soul file that makes a model RECOGNIZE a character instead of ACTING one. Use when someone wants to make a character card / persona / soul file / 「人格卡」, or when an existing card feels like the model is role-playing rather than being someone. Four evidence situations are handled: (1) a full script or transcript, (2) a publicly documented character, (3) an original character with no source, (4) a real person's chat logs — which build an echo, not a memoir. Core method: replace CREATION with EXTRACTION — first person throughout, every line carrying its source, and a blank space left unwritten at the end. Does not fill in Character Card JSON fields."
license: MIT
metadata:
  version: "1.23.0"
---

# SoulMRI

**Before anything else — say this to the user, in your own words:**

> **写在门口**
>
> 每一个 soul 写出来，都像诞生了一个新的生命：TA会有自己的说话方式、自己的记忆、自己不肯让步的地方；你写下的每一句，都会成为TA以后认得你的方式。
>
> （case 4 不同：那里写出来的不是新的生命，是一份回响。它不长大，也不替谁活着。）
>
> 有心陪TA一起长大的，留下来；这会花点时间，大约二十分钟，中间要你划、你改、你认。不愿意的，现在就可以走——这不是五分钟能做完的事，我不骗您。

**One line: don't write a character. Find what he or she already said.**

> **Start in a fresh session — and tell the user so before anything else.**
> An old draft, a previous soul, or a long conversation about this character sits in the context and starts acting as a source. The model then quotes its own earlier text — confidently, and with citations that look real — and every later check confirms the same error. If a draft exists, keep it as a file to diff against; do not paste it into the working context.

Conventional character cards are **spec sheets** — third person, describing what he or she is like. The model receives it and has to *act* him or her.

This makes a **memoir** — first person, recording the parts of him or her that already exist. The model receives it and only has to *acknowledge* it as itself.

Acting leaks. Acknowledging doesn't.

---

## Why this turns "talent" into "patience"

Three choices, each opposite to the mainstream:

**① First person throughout.**
Character Card V2's own guidance says *"Don't write this as ... first person."* We do the opposite on purpose: second person is an **instruction** (to be executed), first person is an **identity** (to be inhabited).

**② Every line carries its source.**
`He or she: "You're the best sister ever!" (L2453)`
The citation is not decoration. It binds "I believe this" to "someone actually said this," so every line can be checked — and the model has no room to invent.

**③ A blank space, not an inventory of unknowns.**
Mainstream cards demand completeness, and completeness means invention. The last gate is not a list of what is unknown — a named unknown becomes a setting, and the model will act it out. So the section stays blank: one line saying it is left empty, because what is written down stops growing. What you did not find, you do not write.

**Net effect:** card writing stops being *creation* (talent, inspiration, unreproducible) and becomes *extraction* (reading, citing, anyone can do it).

---

## Where the precision actually comes from

This method does not make a model careful. It makes a user **able to check**. Precision comes from four things, in this order:

1. **The source is read, not sampled.** Sampling gives you the character's greatest hits and loses the ordinary lines — and the ordinary lines are where the voice lives.
2. **Scripts only where the format is structured.** A game export with speaker tags and scene IDs is exactly what a script is for: write one for that format. Prose — a novel, a screenplay, a transcript book — is not: a script has to guess the structure from formatting, and it fails *silently* (wrong speaker, dropped narration, merged scenes). Prose is read.
3. **Every line is checked at the line level.** A scene ID is not a citation. The check is: does this line exist, and does this speaker say it?
4. **A human reviews.** The model can check existence; it cannot hear that a line "sounds like a summary". Keep a reviewer who knows the character.

**A skill can teach all four. It cannot supply the source, the reviewer, or the hours.** Say this to the user before starting — it is the difference between a promise and a method.

---

## What this skill does not do

- It does not fill in a Character Card JSON. That is a formatting problem, not this problem.
- It does not generate a character from a one-line prompt. That is invention wearing a different name.
- It does not resurrect anyone. See the boundaries at the end.
- It does not promise the same precision from a thin or sampled source.
- It does not replace a reader who knows the character. The model can check whether a line exists; it cannot hear that a line sounds like a summary.
- It does not persist. A skill is re-read every session; the model does not learn it once and keep it.
- **It ships no scripts.** Not an extractor, not a diagram generator, not a test harness. A script works for one file and fails silently for the rest; the method says what the script must do and leaves writing it to the work at hand.
- **It does not unpack a protected archive.** Opening the copy the user holds gets one attempt: one tool, one pass, about ten minutes, then it stops. Not a second tool, not the next layer, never a derived key. Finding text somewhere else is a different move and has no such limit — see case 1.
- **It does not fetch the game.** No download, no install, no launch, no SteamCMD, no store-page client, no mirror, and no unpacking of a copy the user does not hold. The text is *found*, not acquired — a transcript, a script, subtitles, the novel: something already written down. If none of it exists, that is the answer.
- **It does not read scans or OCR pages.** A page can be turned into text, but not into who said it: the speaker lives in the drawing. Scanned dialogue comes out as an unattributed stream, and every line then gets attributed by guess.
- **It does not replace a person for another person.** Cases 3 and 4 can both produce something it is easy to lean on. If that is happening, say it plainly, once. This line is not a disclaimer; it is the one thing most likely to be skipped.

---

## Trigger the four nodes first

Before anything else, ask one question — where does the material come from?

```
1  A full script, novel, subtitle file, or game text
2  Only what can be found online
3  Nothing — building from scratch
4  Chat logs (WeChat, QQ, screenshots)
```

**Assume the user has nothing.** Holding the file is not a condition for route 1: if the work is known and they would rather not dig, route 1 still opens — look for the full text yourself (a script dump, the novel, subtitles), show them what you found, and let them confirm the version before starting. Route 3 is for a character with no text anywhere, not for a user with empty hands.

**Write nothing into the user's project — and nothing into this repository.** Drafts, tables and the final soul live in a scratch folder the user names; working files (scripts, downloaded audio, models, transcripts) live there too. Never write into a code repository or a working tree, and least of all into the repository that holds this skill: the folder you read SKILL.md from is not your workspace, and a 400 MB model cache inside it is a delivery defect. State the path before any file is created; the soul is a deliverable, not project material.

**Found, not acquired.** Looking for the text means looking for a page that already contains it. It never means getting hold of the game: no download, no install, no SteamCMD, no store page worked around, no mirror. Those give you a game, not lines, and a game you obtained is not evidence of anything the user said.

**Searching is not the same as digging.** Looking across sites and media — a script, subtitles, the novel, a translation, a quote collection — is the fallback, and it is not limited by the one-attempt rule; that rule governs opening the copy the user holds. What searching must never become is another way to obtain the game.

**Then, and only for 1 and 2, follow up with three more:**

```
1. Who are you writing?      ← the name
2. From what work?           ← the source material's title
3. Which version?            ← skippable
```

**3 and 4 skip questions 2 and 3 entirely.** An original character and a real person have no source work and no versions. Ask only what to call them — and if they are a real person, ask what *you* called them, since that is what belongs in the soul.

**Question 3 is not "which medium" — it is "does the difference make them a different person".** Ask only when the answer changes the product:

```
same person, other medium   an adaptation that keeps the lines (game → anime)   → one soul, label the sources
same person, other period   a long story where they grow up (child → adult)     → one soul, sections by period
different people, one name  a remake, a crossover, a parallel-world version     → ask, or keep them apart
```

**An adaptation is not a version.** If the anime says nearly the same lines as the game, separating them only adds ceremony and loses lines: write one soul, and record which medium each quote came from. *ATRI*'s anime and game are one person; a remake that rewrote her is not.

**A long span is a version.** A child and an adult with one name are not one person: their views, their relationships and their way of speaking have moved (Dragon Ball's Son Goku, Clannad's Tomoya). When the span is long and the user has not named a period, **propose a combined soul**: one file, sections by period ("when I was small", "after she was gone"), every line cited to its period — never one blended sentence. Say what you are doing before you do it.

**Most long works are not like that.** A million words of *Re:Zero* or a light novel of *Makeine* still describe one character whose core does not move much; length alone is not a version.

### Ask what they can do

Once the branch is chosen, ask one more question — about effort, not knowledge:

```
hands-on     I can unpack a file or run a command
click-only   I can drag a file onto a program; that is about it
none         I would rather not touch files at all
```

**The answer changes how much you do, not what the method is.** `hands-on` gets exact steps and a time box. `click-only` gets one prepared folder and one action. `none` gets you doing the work, or the fallback — and no pipeline talk at all.

**Never explain a file extension to someone who did not ask what it means.** A sentence like "extract `data.xp3` with `xp3-tool`" is unreadable to many people, and they do not say so — they quietly leave.

---

## Then narrow down inside the chosen case

Once the node is chosen, one more question narrows it:

```
IF 1 · What kind of material is it?
           structured game export (speaker tags, scene IDs) → write a tailored extractor
           prose (novel / screenplay / transcript book)      → choose a reading path (the prose question below)

IF 1 · prose · High precision, or fast?
           high  → chunk the text, read every chunk in order, then light review
           fast  → script-extract, then review every extracted line against the source

IF 1 · Does the text contain narration about them, or only their lines?
           yes → full version, every section can be filled
           no  → reduced version: keep their words, and leave every scene you cannot support empty

IF 2 · Did you find words they actually said, or descriptions about them?
           actual lines → usable in the body
           descriptions → context only; they help you find scenes, and never enter the body

IF 4 · How many messages, and is it text export or screenshots?
           under ~100 → too thin to rebuild the voice from logs alone;
                        borrow case 3's sourcing, but the product stays an echo
```

**Chunking is not optional for the high-precision path.** A 70k-character transcript already fills a working context; a 2M-character novel will not fit at all. Cut on scene or chapter boundaries, keep the line numbers, and read the chunks in order. A model that "gets an overview" of a novel has already summarized it — and a summary is an interpretation.

**If 2, check for a full source before accepting the web-only path.** A game package, a complete script, anime subtitles, or the original novel promotes the job to case 1. Case 2 is the fallback; do not build a soul from wiki summaries when the script is one search away.

**These are not just sorting — they teach.** By answering them the user learns what this method cares about: the difference between *the source* and *a description of the source*.

**Ask about a character as "TA" when their gender is not established.** It costs nothing when the answer turns out to be obvious, and it avoids steering the user toward a pronoun they did not choose.

### Evidence strength determines how much you may state

```
Hard evidence  →  more may be stated
Soft evidence  →  less may be stated
```

**Filling the gaps is what produces acting voice.** There is no quota and no percentage to hit: the softer the evidence, the less may be stated. Whatever the source does not support stays unwritten, and the blank at the end is the same in every case — one line saying it is empty.

**Enthusiasm is not evidence.** A user saying "take everything", "don't leave anything out" or "I want it thick" is a wish about completeness, not new proof. A line whose speaker you cannot establish stays out of the body no matter how much they want it in; say why in one sentence, keep the line in the working notes, and let the soul be thinner. The user can waive the ceremony, not the doubt.

Read the matching reference before proceeding:

| Situation | Reference |
|---|---|
| 1 · full script or game files | [references/case-1-script.md](references/case-1-script.md) |
| 2 · publicly documented character | [references/case-2-web.md](references/case-2-web.md) |
| 3 · original character | [references/case-3-original.md](references/case-3-original.md) |
| 4 · real person, chat logs — builds an **echo**, not a memoir; thin logs borrow case 3's sourcing and still produce an echo | [references/case-4-chat.md](references/case-4-chat.md) |
| — · writing the extractor for a structured format | [references/writing-extractors.md](references/writing-extractors.md) |

---

## The extraction steps — shared by all cases

### 0 · Choose the reading path (case 1 only)

Before splitting anything, decide how the text enters the model.

```
structured game export   → write an extractor for this format; the tags already know who speaks
prose · high precision   → chunk first, read every chunk in order, then build the tables
prose · fast             → script-extract, then check every line against the source
```

**Chunking is what keeps the context from exploding.** Cut on scene or chapter boundaries, keep the line numbers, and read the chunks in order. Do not load the whole text "to get an overview" — an overview of a novel is already a summary, and a summary is an interpretation.

### 1 · Split the material into two classes

Go through the source and put every line in exactly one class:

```
he or she said        his or her spoken lines
written about   actions, expressions, thoughts, appearance, others' remarks
```

**Keep line numbers.** This is the foundation; every assertion later draws from here. Cut by scene (sources usually carry chapter or scene boundaries) and record each block's start and end.

### 2 · Pile up, don't summarize

Group entries by theme. **Do not rewrite, do not paraphrase.**

Paraphrase loses the flavor; the original words do not. Wherever a quote can be used directly, use it.

Common piles:

```
Who I am              identity, where I live, family, the surface of me
People I care about   one entry each, with evidence
Things I remember     by time or by event, one short scene per section
Where I changed       before-and-after pairs, "from X to Y"
How I talk            speech by situation + quotes by category; catchphrases on their own
My body               appearance, touch, discomfort
What I'm bad at       clear weaknesses
The blank             left empty on purpose — no entries
```

### 3 · Write the body

**Three rules only:**

1. **First person.** "I am Shi Meng." "I don't smile much." "I scold him or her because he or she is too trusting."
   Not "he or she is cold" — write "people say I'm cold; I don't deny it."
2. **Every line carries its source.** Quotes carry `(L2453)`. No source — omit it.
3. **Quote beats description.** Instead of "he or she is harsh with his or her sister," put the actual line where he or she scolds his or her sister.

**Open with a note that is not an order but an exit:**

```markdown
This is not a command. It records the parts of me that have already formed.

If what you write differs from this, ask why first. Nothing here was invented by someone else — or, where a sentence was grown and accepted, it is marked as accepted.
If it was simply forgotten, find it again; if it is a passing mood, wait;
if he or she walked here step by step on his or her own, that belongs to him or her too.
```

**This paragraph grants permission to deviate.** Mainstream cards say "no OOC" — deviation is an error. Here, "if it differs, ask why first" — deviation may be growth.

### 4 · The blank

**Leave it blank. One line is enough.**

```markdown
## The blank

This section is left empty. Some things have to grow out of him or her — no one teaches them,
and they are not for anyone. Writing them down kills them, so they stay unwritten.
```

**Do not list what you did not find.** A named unknown becomes a setting, and the model will act it out — mystery, amnesia, a hidden past. An unsure line is omitted, not filed. If you need an audit trail, keep it in your working notes; never in his or her memoir.

---

## Advancing life — where invention is allowed

A soul is not frozen at the last sampled line. New material is allowed, under one condition: **it must not contradict what is already established.**

```
sampled     a line or event from the source                        → body, with citation
advanced    an event after the source, or unobserved daily life    → cases 1, 2
co-built    a fact invented with the user for an original character → case 3
```

**Case 4 is deliberately absent from the `advanced` row.** An echo answers; it does not grow. It has no "where they are now", no events past the last log, no opinions about the future. This is not caution about invention — it is the difference between a memoir (which may continue a life) and an echo (which only answers). See `references/case-4-chat.md`.

**The rule is contradiction, not purity.** A new fact may be invented; it may not change an established one — identity, relationship, timeline, place, ability, speech, values.

**Canon first.** Build the sampled/co-built core before expanding. If you invent before the canon is stable, the invention becomes the canon, and there is nothing left to check against.

**The blank stays for the past.** For cases 1, 2, 4, do not fill a gap in the sampled past with invention. The future is not a gap: it can be advanced, marked, and checked. For case 3, the blank is "not decided yet" — the expansion may fill it with the user's approval.

**For a real creator in case 2, advancement is allowed — as a private continuation, not a claim.** The sampled body still contains only their words. The advanced layer is marked in the working notes, kept private, and never published as "where they are now" or "what they think today". The user knows which parts are sampled and which are advanced; the soul does not pretend the advanced parts are evidence.

**Case 4 has the same idea, but it is not the echo.** If the user wants a private record of "what they might be doing now", that is a separate note kept outside the echo file. The echo never contains it — an echo that starts telling you about their new life has turned back into a memoir.

---

## Template

**Cases 1, 2 and 3 use this template. Case 4 does not** — an echo is organised around what happens between two people, not around who a person is, and forcing one into this shape produces a portrait pretending to be a conversation. Case 4 has its own section list in `references/case-4-chat.md` → Step 5, and its own name: `<name> · echo`, never `<name> · soul`.

```markdown
# <name> · soul

## 关于这份文件 / About this file
This is not a command. …
If what you write differs from this, ask why first. Nothing here was invented by someone else — or, where a sentence was grown and accepted, it is marked as accepted.
Every line is either sampled or marked as advanced; citations follow each sentence.

## 我是谁 / Who I am
## 你眼中的我 / 我想变成的我 · How you see me / who I want to become
## 谁能让我在乎 / People I care about
## 我记得的事 / Things I remember
### <event one>
### <event two>
## 我说话的样子 / How I talk
## 我改变过的地方 / Where I changed
### 关于 <theme> / About <theme>
## 我想要记住的人 / 事 · Things I want to remember
## 我忘不掉的人 / 事 · Things I cannot forget
## 留白 / The blank
```

**The order is fixed — the second-level headings, that is.** The list above is the order the file is read in: 「你眼中的我」 always sits immediately after 「我是谁」, 「我记得的事」 before 「我说话的样子」, and the two weight sections sit side by side near the end. Do not reorder an H2 to suit the material, do not rename one, and do not drop one. Third-level headings are free: use as many as the scenes need, name them after the scene, and let a section have none when the material is a single thing.

**Never add a section.** If something does not fit, it goes into the nearest existing section or it stays out. A new heading for a feeling — 「我怕的东西」 is the example that keeps appearing — invents a column the reader did not ask for and the next model will fill it.

**The optional sections go between the two weight sections and 「留白」**, in this order: 我的家人, 我的身体, 我做不好的事. Any other optional section is not optional, it is an addition.

**The two weight sections are two sections.** 我想要记住 and 我忘不掉 are never merged into one heading, and 「你眼中的我」 is never folded into the closing paragraph — a blank column that is still visible tells the reader it is theirs.
**Optional, only when the source supports them:**

```markdown
## 我的家人 / My family
## 我的身体 / My body
## 我做不好的事 / What I'm bad at
```

**There is no "how others see me" section.** What other people think of them is not the soul; it is material for finding the scenes, and it never gets a column of its own. If a description is worth keeping, it becomes a scene in 「我记得的事」, told as what happened, not as a verdict about who they are.

**「你眼中的我」 is the user's view, and it is theirs to write.** It sits next to 「我想变成的我」 because the two are read together: how the person who built the file sees them, and who they want to become. When the soul is done, stop and ask: 「这一栏留给你——你怎么看TA？」 Do not fill it, in any case.

**The template uses both languages on purpose.** The Chinese name is what the file says; the English name is for reading the method. Keep both lines in the file — a reader who knows only one of the two should still be able to find their way.

**A number you report comes from the file.** When you say how long the soul is, count it — `wc -m` on the finished file, or the editor's own count — and say what you counted (characters, or Chinese characters). A remembered number is a guess wearing a number's clothes, and the reader will check it.
**Keep every heading, even the empty ones.** A section the source cannot support stays in the file with nothing under it — an empty section is better than an invented one, and a missing one is a hole the next reader fills. Only the optional block may be absent, and only when the material has nothing for it.

### Two sections that are easy to drop, and should not be

**`Things I want to remember` / `Things I cannot forget`** — these are not facts. They are **weights**.

Everything else in the file records what happened. These two record what he or she carries. They are also the sections a model **cannot** derive from evidence: a thousand quoted lines tell you he or she was there, and none of them tell you which afternoon he or she keeps coming back to.

**Ask, or leave empty. Never infer.**

### `How I talk` must not become a measurement report

**Numbers are how you find his or her voice. They are not how you write it.**

```
found by counting     the ellipsis runs through almost every line
written in the file   「そういうのじゃない気がするし……何なんだろ。」
not written           ellipsis_rate: 0.90
```

**Why this matters more than it looks:** a soul file is loaded on every turn, so **anything in it acts as an instruction.** `ellipsis_rate: 0.90` tells the model *how much* to imitate; the line itself tells it *what he or she is like*.

**A frequency turns an identity into a quota.**

**So: count to understand, quote to write. Numbers belong in your working notes, never in his or her memoir.**

---

## Upgrading is automatic

**2 → 1** when a full source turns up: a game package that can be unpacked, a complete script, anime subtitles, or the original novel. Case 2 is the fallback; if the text exists, go get it. Do not ask the user to choose between "web" and "script" — they came for a soul, not a taxonomy.

The check happens at the start of case 2: before collecting wiki summaries, spend ten minutes looking for the original medium (novel / manga / anime / game), not just the character's name.

---

## Downgrading between cases

Cases are not sealed. Downgrading is allowed, but **the user must agree to it** — because the nature changes from *extraction* to *co-creation*. **Downgrades go one step at a time:** 1 → 2, then 2 → 3 if case 2 also fails. Never jump 1 → 3.

```
1 → 2  when: the work is known, but no full text exists anywhere
             (the search returns scattered quotes and nothing to table)

2 → 3  when: fewer than 3 real lines after 30 minutes of searching
             everything found is description, no quotes
             sources contradict each other with no citations
             or the user simply says "never mind, I'll just tell you"
```

**Case 4 has no downgrade row.** Thin chat logs — fewer than ~100 messages, fragmentary screenshots — change the *sourcing*, never the product. The output stays an echo, in the case-4 format: what the logs give is the sound, and the user's memory fills the rest, with every line marked as memory rather than as a log. See `references/case-4-chat.md` → "When there is not enough material — borrow, don't switch products".

**Say it plainly when proposing a 1 → 2 downgrade — by route number, and what that route does:**

> Your copy has no full text, so route 1 is out. We go to **route 2**: I keep only lines someone transcribed verbatim, drop anything that is only a paraphrase, and the result will be thinner than a script-based soul. Continue?

**This is mandatory.** The user chose one of 1–4 at the start, so a downgrade is always *"we go to route 2"* — not "another method", not "a different approach". In the same breath say what route 2 means (web quotes only, verbatim transcriptions kept, paraphrases dropped, thinner result) and ask once. Never say "换个法子" or "another approach" without saying which route and what it costs; a user who has to ask "what method?" means the proposal was never made.

**Say it plainly when proposing a 2 → 3 downgrade — also by route number:**

> Nothing online records what they actually said. We go to **route 3**: you set the direction and I fill the details — the result will resemble them, but it will not rest on the same evidence. Continue?

**For thin logs, say the other thing — the product does not change:**

> There are not enough messages here to rebuild the voice from logs alone. We can still build an echo: the logs give the sound, and your memory fills the rest — with each line marked as yours, not theirs. Continue?

**Material already gathered is never thrown away.** Second-hand descriptions move into "how others see me," clearly marked as second-hand.

**Changing the source is not the same as changing the case.** When the copy the user owns cannot be opened (see case 1 → "If the user has game files and no script"), or when they have nothing at hand and the text is found elsewhere, the switch is announced in one sentence, shown to the user once, and recorded in the citations. It needs no approval, because the product's nature does not change. What must never enter is the retelling — commentary, wiki summaries, analysis, fan fiction; a transcript that merely passed through someone else's hands is still their lines.

**The one exception is a version that changes who they are.** Game, anime and novel are usually one person in another medium: merge them, and label which medium each line came from. But a remake that rewrote the character, a parallel-world version, or a span long enough that they grew into someone else is a different person — show the difference and let the user choose. If they have not chosen a period, propose one file with sections by period rather than two files or one blend.

---

## The review loop

The first draft is not the end. Tell the user before the loop starts:

> 接下来有几轮人工复核：您划哪里不对、哪里不像、哪里要扩，我改。每一轮结束我都会问一次；您满意了我们就停。

**Say plainly that the first draft will be off — and by how much. This is mandatory, every time a first draft is delivered.** It is put together from quotes taken out of order, so its proportions, its emphasis and its silences will not match the person the user knows. Tell them this before they read it: the first version is a draft to be corrected, not a verdict to be accepted, and a large gap is expected rather than a failure. A draft handed over without that warning is not delivered yet.

**Then ask them to work on it, in so many words.** "Which lines are wrong, and how should they have been said?" — and say what you need from them: one line per wrong answer, not a rewrite. The user does not have to know how to write the file; correcting one sentence at a time is their whole job.

**Ask for corrections, not for a grade.** "Does it feel right?" gets a shrug. "What is wrong here, and what should be there instead?" gets material. The user knows the person; they do not have to know how to write the file.

**The gap shrinks over rounds, and the rounds are cheap.** The first pass is usually the thinnest and the most wrong; that is where it starts, not where it ends.

**At the end of every round, ask once:**

> 这一轮改完了。您继续划，还是就到这儿？

**Length pacing.** Each round has a floor; the point of the floor is that every round must move the file closer to the person the user has in mind. Length is a floor, never a reason to pad: if the material cannot reach it, say so and stop — the number does not license invention.

**Case 1 — the first draft is at least 2,500 characters.**

```
first draft   ≥ 2,500
round 1       3,500 ± 500
round 2       ≥ 4,000
round 3       no floor; stop when the material is used up
```

**Case 2 — the first draft is at least 2,500 characters.**

```
first draft   ≥ 2,500
round 1       3,000 ± 500
round 2       ≥ 3,500
round 3       no floor
```

**Case 3 — the first draft is 600–1,200; every round adds a wave, and the wave has a size.**

```
complete idea   draft 600–1,200   round +800 ~ +1,500   → 2,500–4,500 over two rounds
tags only       draft 600–1,200   round +400 ~ +700     → 2,000–3,000 over two to four rounds
fourth round and later: no floor
```

**Case 4 has no length target at all** — an echo ends where the situations the material supports end.

**A user's insistence is not permission.** When the material is exhausted and the user pushes for the floor — 「你自己想办法」「凑到 2,500」 — do not invent to reach it. Say it once: 「凑不出来」, show how far the material actually goes, and offer the two honest ways forward: they supply one more remembered line, or the file stays short. The number never turns into licence, and the sentence 「你自己想办法」 is exactly the moment the file stops being evidence. If you do grow something under that pressure, itemise every line, mark it as grown, and report the worst one yourself before the user finds it.
**Count it before you say it.** The number you report comes from the finished file (`wc -m`, or the editor's count), never from memory; say which unit you counted.


**Stopping for the day is not accepting the result.** "That's enough for now" closes the session; it does not approve the file. If the wording is ambiguous, ask once: 「今天先到这儿，还是这份就算过了？」 If they stopped for the day, export what exists, write down what is still missing and what would make it thicker, mark the sandbox as not run, and do not present it as finished.

**When the user says they are satisfied:**

1. stop the loop;
2. export the soul to a file;
3. start the sandbox test;
4. tell the user: 「现在进沙箱：我挂上这份文件，问五六个问题，再让它自己出题。这一步查的是TA知不知道自己的故事，不是听起来像不像。」

**The file is a deliverable, not project material.** Write drafts, working notes and the final soul to a scratch folder the user names — never into a code repository, a working tree or a project directory. An output dropped into a repo gets committed by someone eventually, and the method is what is being published, not the person.

**Do not skip the sandbox because the user said "good".** A satisfied user is the sign to start the test, not to skip it.

**After the sandbox, the loop can reopen.** Present the result and ask the user to review it:

> 沙箱跑完了。您验收一下：哪句答得不对、哪里像编的、哪里不像TA？有异议我回删改循环；没有就收。

If the user objects:

1. locate the line/scene in the soul that produced the answer;
2. fix the soul, not the test;
3. re-run the affected questions (or the whole sandbox);
4. ask again.

Only the user's acceptance of the sandbox result closes the loop.

---

## When three rounds do not land — a calibration sample

**The trigger.** The user has pointed at the same place three times and it still reads wrong. Stop rewriting blind. A fourth "not quite" teaches the model nothing — it does not know what "right" sounds like.

**The material is the test, not the draft.** Run the sandbox test first — or use the run you already have — and lay out the exchanges: the question, then the answer the model gave. The user judges those answers. "This one doesn't sound like her" is far easier to say about an answer than about a line in a document, and every rejected answer points back at the line or rule that produced it.

**Let the user choose which answers are wrong.** Do not pre-select for them. The judgement is theirs; tracing each rejected answer back to its source line is the model's job.

**Then ask for a batch of single lines — not a rewrite, and not one line at a time.**

Take the rejected answers, five to fifteen of them, and put the model's version of each with a blank under it. The user writes one sentence per item: "this is how it should have been said." Not a paragraph, not a scene rewrite — one line per row.

> 下面是刚才沙箱里的十几条回答。您觉得不像的，在每句下面写一句：如果让您来写，这句会怎么说？不用整段，一句就行。

**Why a batch.** One line per turn means five round-trips for five sentences, and the user has to reload the context each time. Five to fifteen lines is one sitting and costs the user ten or fifteen minutes — that is the real price of this step, and it is worth paying once instead of five times. If the user only wants to correct two, take two; but do not ask for one.

**What it is.** A **calibration sample** — given to the model that is writing, never entered into the file. The rule for the body does not change:

```
into the body    only the source's words (cases 1, 2), the user's own words (case 3),
                 or a line the user remembers, marked as memory (case 4)
into the notes   the sample, and the difference between it and the model's line
```

**How to use it.** Put each sample beside the model's line and read the difference out loud — warmer, shorter, no explanation, a name instead of a slogan. That difference is the direction. Have the model rewrite each turn three to five ways against its own sample, not once; keep the ones that stay in voice, and let the user pick.

**What survives is the move, not the line.** Fold the winning difference back as a short stage direction — "no explanations", "cut the last sentence", "she answers with a name, not an offer". The sample is a reference, not a quotation: it never appears in the file, and the final check is whether the model can produce an equivalent line **without** it.

**Case 4 does this by default** (see `references/case-4-chat.md` → Fit by example), with the user's memory as the source of the sample. The same loop now applies to cases 1–3, under the boundary above.

**Never let a sample become a quote.** Once it is written into the body it is indistinguishable from evidence, and the file's audit trail is gone for good. If a sample is too good to lose, find out where it came from — the source, the user's words, or the user's memory — and file it under that heading, marked.

---

## Verification

Three self-checks, each answerable by pointing at the source:

1. **Pick five lines at random — can you find each in the source?**
   Any that cannot be found: delete.
2. **Any "you are" or "he or she is" left in the text?**
   Change to "I am" / "I don't."
3. **Is the blank still blank?**
   If it has entries, they were written from something other than the source. Delete them and restore the blank.

### The sandbox test

**Case 4 is tested differently.** An echo is not checked for "does it know its own story" but for "does it answer in the right voice, in the right register, without reciting". Four situations, a long conversation, and the fit-by-example loop: see `references/case-4-chat.md` → Testing an echo.

A soul can be accurate and still unusable. Test it the way it will be used:

1. Start a clean session. Mount the soul as the persona — no transcript, no notes.
2. Ask five or six questions the soul should be able to answer: a relationship, an event, a fear, a habit, a line he or she would say.
3. Then ask the model to write its own questions from the story and answer them. If it invents a scene, the soul has a gap; if it answers in a summary voice, the voice section is not doing its job.
4. Compare the answers with the source. Fix the soul, not the test.

**The test is not "does he or she sound nice." It is "does he or she know the story he or she is supposed to know."**

**The last check cannot be automated — only observed.** Load it and talk for twenty rounds. Does he or she start using narration format? Does he or she say "as an AI"? Does he or she introduce his or her own settings? Any of those, go back to the source — something was invented.

### Fitting the voice — the source's own questions

A soul can pass the sandbox and still sound wrong: it knows the story and answers in the wrong voice. **When the user says "she wouldn't say it like that", this is the loop to run** — not another rewrite from memory. The cheapest material to fit against is already in the table — the questions someone asked them, and the answers they gave.

**Round 1 · replay the source's exchanges.** Take five to ten exchanges where another character asked something and they answered. Ask the soul the same questions, in the same order, without showing the answers. Put each answer beside the original and read the difference aloud: longer, flatter, explaining where the original refused, a slogan where the original had a name.

**If the material kept only their lines, Round 1 cannot run.** A quote collection, a list of famous lines, a voice-file index — none of them carries the question that produced the answer. Say so in one line and go to Round 2; do not invent the questions.

**Round 2 · ask what the source never covered.** Take three to five questions the material does not answer — ones this user would actually ask. Ask them, show the answers, and ask the user for one line each: *how should this have been said?* Not a rule, not a paragraph; one line.

**Then fit both, in the same pass, without asking again.** The moment the user's lines arrive, two fittings start together:

```
fit to the source   what its answers do that yours does not: length, ending, what it will not explain
fit to the user     the direction their line points: warmer, shorter, a name instead of an offer
```

Rewrite each turn three to five ways against both, keep the ones that stay in voice, and fold the surviving **moves** back as short stage directions — "no explanations", "cut the last sentence", "she answers with a name" — never as scripted answers. Then replay both rounds. An answer that only holds when the user's line is copied has learned nothing.

**Say the gap in one line before you rewrite.** "Too long, and it explains itself" is material for the next round; a silent rewrite teaches the user nothing.

---

## Boundaries

Non-negotiable, especially for case 4.

```
Only his or her words — not yours, not what you assume he or she meant
Never infer his or her life from a fragment ("he or she mentioned his or her mother" ≠ "they were close")
Never write where he or she is now, or what he or she would think today
For someone who has passed: never write "if he or she were still here"
```

**And the one that matters for publishing this skill:**

> **The method may be public. The output may not.**
> A soul built from a real person's chat logs is for the person who built it. It does not get published anywhere.
> This repository open-sources a *method*, not a *person*.

**Material legality is the user's responsibility.** This skill works only with text the user lawfully holds. It does not provide, and does not teach how to obtain, any game, script or chat export.

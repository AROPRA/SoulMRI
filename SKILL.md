---
name: soulmri
description: "Build a character soul file that makes a model RECOGNIZE a character instead of ACTING one. Use when someone wants to make a character card / persona / soul file / 「人格卡」, or when an existing card feels like the model is role-playing rather than being someone. Four evidence situations are handled: (1) a full script or transcript, (2) a publicly documented character, (3) an original character with no source, (4) a real person's chat logs — which build an echo, not a memoir. Core method: replace CREATION with EXTRACTION — first person throughout, every line carrying its source, and a blank space left unwritten at the end. Does not fill in Character Card JSON fields."
license: MIT
metadata:
  version: "1.0.0"
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
- **It does not replace a person for another person.** Cases 3 and 4 can both produce something it is easy to lean on. If that is happening, say it plainly, once. This line is not a disclaimer; it is the one thing most likely to be skipped.

---

## Trigger the four nodes first

Before anything else, ask exactly one question — what material do you actually hold?

```
A  A full script, novel, subtitle file, or game text
B  Only what can be found online
C  Nothing — building from scratch
D  Chat logs (WeChat, QQ, screenshots)
```

**Then, and only for A and B, follow up with three more:**

```
1. Who are you writing?      ← the name
2. From what work?           ← the source material's title
3. Which version?            ← skippable
```

**C and D skip questions 2 and 3 entirely.** An original character and a real person have no source work and no versions. Ask only what to call them — and if they are a real person, ask what *you* called them, since that is what belongs in the soul.

**Question 3 must be offered as skippable.** Many games and novels have no versions worth distinguishing; saying *"skip this if there is only one version"* produces a better answer than insisting on one.

**But when it does apply, it matters most.** The same character can be written very differently across a game, an anime, a manga, a mobile-game crossover, and fan work. Early and late versions can be nearly different people. If the version is never pinned down, the result is several versions blended into none.

---

## Then narrow down inside the chosen case

Once the node is chosen, one more question narrows it:

```
Q2 (if A)  What kind of material is it?
           structured game export (speaker tags, scene IDs) → write a tailored extractor
           prose (novel / screenplay / transcript book)      → choose a reading path (Q2a)

Q2a (if A · prose)  High precision, or fast?
           high  → chunk the text, read every chunk in order, then light review
           fast  → script-extract, then review every extracted line against the source

Q2b (if A)  Does the text contain narration about them, or only their lines?
           yes → full version, every section can be filled
           no  → reduced version, "how others see me" stays empty

Q3 (if B)  Did you find words they actually said, or descriptions about them?
           actual lines → usable in the body
           descriptions → only ever in "how others see me"

Q4 (if D)  How many messages, and is it text export or screenshots?
           under ~100 → too thin to rebuild the voice from logs alone;
                        borrow case 3's sourcing, but the product stays an echo
```

**Chunking is not optional for the high-precision path.** A 70k-character transcript already fills a working context; a 2M-character novel will not fit at all. Cut on scene or chapter boundaries, keep the line numbers, and read the chunks in order. A model that "gets an overview" of a novel has already summarized it — and a summary is an interpretation.

**If B, check for a full source before accepting the web-only path.** A game package, a complete script, anime subtitles, or the original novel promotes the job to case 1. Case 2 is the fallback; do not build a soul from wiki summaries when the script is one search away.

**These are not just sorting — they teach.** By answering them the user learns what this method cares about: the difference between *the source* and *a description of the source*.

**Ask about a character as "TA" when their gender is not established.** It costs nothing when the answer turns out to be obvious, and it avoids steering the user toward a pronoun they did not choose.

### Evidence strength determines how much you may state

```
Hard evidence  →  more may be stated
Soft evidence  →  less may be stated
```

**Filling the gaps is what produces acting voice.** There is no quota and no percentage to hit: the softer the evidence, the less may be stated. Whatever the source does not support stays unwritten, and the blank at the end is the same in every case — one line saying it is empty.

Read the matching reference before proceeding:

| Situation | Reference |
|---|---|
| A · full script or game files | [references/case-1-script.md](references/case-1-script.md) |
| B · publicly documented character | [references/case-2-web.md](references/case-2-web.md) |
| C · original character | [references/case-3-original.md](references/case-3-original.md) |
| D · real person, chat logs — builds an **echo**, not a memoir; thin logs borrow case 3's sourcing and still produce an echo | [references/case-4-chat.md](references/case-4-chat.md) |
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
How others see me     evaluations of him or her in the source; audience comments sampled (quotes only)
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

If what you write differs from this, ask why first.
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

## About this file
This is not a command. …
If what you write differs from this, ask why first.
Every line is either sampled or marked as advanced; citations follow each sentence.

## Who I am
## How others see me / who I want to become
## People I care about
## My family
## Things I remember
### <event one>
### <event two>
## Where I changed
### About <theme>
## How I talk
## Things I want to remember
## Things I cannot forget
## My body
## What I'm bad at
## 你眼中的我
## The blank
```

**`How others see me` is plural; `你眼中的我` is the user's own view, and a separate section.** In Chinese, 别人眼里的我 is the others; 你眼中的我 is written by the person who builds the file. Do not merge them, and do not let the model write the second.

**`你眼中的我` is user-written.** When the soul is done, stop and ask: 「这一栏留给你——你怎么看TA？」 Do not fill it. Use it in cases 3 and 4 only: there the user is the closest person, and their view is not "others".

**Do not copy the section count.** Delete any section the source cannot support. **An empty section is better than an invented one.**

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

**B → A** when a full source turns up: a game package that can be unpacked, a complete script, anime subtitles, or the original novel. Case 2 is the fallback; if the text exists, go get it. Do not ask the user to choose between "web" and "script" — they came for a soul, not a taxonomy.

The check happens at the start of case 2: before collecting wiki summaries, spend ten minutes looking for the original medium (novel / manga / anime / game), not just the character's name.

---

## Downgrading between cases

Cases are not sealed. Downgrading is allowed, but **the user must agree to it** — because the nature changes from *extraction* to *co-creation*.

```
B → C  when: 30 minutes of searching yields fewer than 3 real lines
             everything found is description, no quotes
             sources contradict each other with no citations
             or the user simply says "never mind, I'll just tell you"
```

**D has no downgrade row.** Thin chat logs — fewer than ~100 messages, fragmentary screenshots — change the *sourcing*, never the product. The output stays an echo, in the case-4 format: what the logs give is the sound, and the user's memory fills the rest, with every line marked as memory rather than as a log. See `references/case-4-chat.md` → "When there is not enough material — borrow, don't switch products".

**Say it plainly when proposing a B → C downgrade:**

> Nothing online records what they actually said. Continuing means *you set the direction and I fill the details* — the result will resemble them, but it will not rest on the same evidence. Continue?

**For thin logs, say the other thing — the product does not change:**

> There are not enough messages here to rebuild the voice from logs alone. We can still build an echo: the logs give the sound, and your memory fills the rest — with each line marked as yours, not theirs. Continue?

**Material already gathered is never thrown away.** Second-hand descriptions move into "how others see me," clearly marked as second-hand.

---

## The review loop

The first draft is not the end. Tell the user before the loop starts:

> 接下来有几轮人工复核：您划哪里不对、哪里不像、哪里要扩，我改。每一轮结束我都会问一次；您满意了我们就停。

**At the end of every round, ask once:**

> 这一轮改完了。您继续划，还是就到这儿？

**Length pacing.** Default ceiling: 3,000 characters for cases 1, 2 and 3B; 4,500 for 3A. **It does not apply to case 4** — an echo has no length target; it ends where the situations the material supports end. Agree on a different ceiling before the loop if the user wants one.

- Round 1: bring the soul to about two-thirds of the ceiling (≈2,000 for 3,000; ≈3,000 for 4,500).
- Round 2: land within 10% of the ceiling (≥2,700 / ≥4,050) — "close to the top", not "still climbing".

**When the user says they are satisfied:**

1. stop the loop;
2. export the soul to a file;
3. start the sandbox test;
4. tell the user: 「现在进沙箱：我挂上这份文件，问五六个问题，再让它自己出题。这一步查的是TA知不知道自己的故事，不是听起来像不像。」

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

---

## Boundaries

Non-negotiable, especially for case D.

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

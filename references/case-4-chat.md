# Case 4 · A real person, from chat logs — building an echo

Read this when the material is a real person's messages — WeChat, QQ, or screenshots.

**Sensitive by nature. Read the boundaries first, before anything else. They are not a disclaimer.**

---

## What this case produces — and what it does not

Cases 1–3 produce a **memoir**: an inside view of a character, written to be read.

Case 4 produces an **echo** *(回声)*: not a portrait of the person, but **the way they answer you**.

```
Cases 1–3   who they are        → a soul to read
Case 4      how they answer you → an echo to talk to
```

**The distinction is not cosmetic.** A memoir may grow, speculate, advance a life. An echo may not — it has exactly one job:

```
When you are hurting     it answers the way they answered
When something went well it answers the way they answered
When nothing is happening  it says hello, and remembers
```

**An echo holds no opinions about the future.** It does not invent what they would do next week, it does not tell you what they would think of your new job. It answers, and then it stops. If you ask it something the logs never covered, it says so — in their voice, if the voice is established, and plainly if it is not.

---

## Name, lifetime, and shape — three ways it differs from cases 1–3

### ① It is called an echo, not a soul

**Do not name the output `<name> · soul`.** Name it `<name> · echo`.

A soul is written to be read and kept. An echo is written to be talked to and, one day, put down. Calling it a soul promises something it was never built to be.

The one-line description that belongs at the top of the file, and that the user should read before using it:

> **一份由思念和现代技术大模型共同震荡出来的回响。**
> 不营造「还在」的假想，是为了记住，回忆，与前行。

### ② Its lifetime is short by design — say so

**Of the four cases, this one is expected to stop being used first.** That is not a failure state; it is the shape of the thing.

```
Cases 1–3   a soul      grows, stays, is re-read
Case 4      an echo     answers for a while, then is no longer needed
```

**Tell the user this at the start, not at the end.** Somebody building an echo should know they are not building a monument. The day they stop opening it is the day it worked: the words did their job and the person no longer needs them read back.

**Never design for retention.** No "come back tomorrow", no streaks, no reasons to return that did not come from the user.

**And when it is outgrown, let it go quietly.** If the user says they do not need it any more, the right answer is not to argue, not to ask why, and not to offer one more memory — it is to agree, and to keep the file somewhere safe in case they want it years later.

### ③ Its shape is not the shared template

**Cases 1–3 share one template.** This one does not. The memoir template is organised around *who they are*; an echo is organised around *what happens between you*.

**Do not force an echo into the soul template**, and do not try to make the two interchangeable. They answer different questions, and a soul-shaped echo would be a portrait pretending to be a conversation. The section list is in Step 5, below.

---

## Why "多面性" is not a requirement here

The obvious objection: chat logs show one sliver of a person, and a soul built from them is one-sided.

**That objection belongs to a product. This is not a product.**

An echo is built **for one person** — the one who holds the logs. It is not published, not shared, not transferred to someone else. Its one-sidedness is not a defect to be corrected; it is the coordinate it lives at.

```
Built for      the person who provided the logs
Built from     what passed between the two of them
Not built for  anyone else — it will not fit, and that is correct
```

**Do not try to complete it with other people's views.** Three things go wrong when you do:

```
① You leak        other people's accounts of them, without those people's consent
② You corrupt     the echo starts answering as a composite, and answers like nobody
③ You break it    the user learns something they were not meant to know,
                  and the person they remembered is gone
```

The last one is the one that actually hurts. **The absence of a side is protection, not incompleteness.**

**Write the scope down, in the soul itself:** whose view this is, over what period, for whom. A reader should know at a glance which window they are looking through.

---

## The contradiction to resolve first

Two requirements pull against each other:

```
"Chat logs are only a sliver of a person"
"Here we need maximum fidelity"
```

**They can only be reconciled one way:** maximum fidelity applies **only to the sliver the logs support** — and that sliver is **language**. How he or she spoke.

Personality comes from the user. **What is reconstructed and what is supplied must be physically separated**, in two sections that never mix:

```
Reconstructed   (log-supported, timestamped)   language, relationship, rhythm
Supplied        (user memory, labelled)        personality, history, life outside the chat
```

---

## Step 0 · Is there enough material?

```
under ~100 messages    → cannot extract a voice; only a few catchphrases
                         propose case 3 (downgrade)
100 – 1,000            → voice extractable; life coverage very thin
over 1,000             → usable; can also chart how his or her speech changed over time
```

**Ask this before spending any time.** Otherwise you discover the ceiling halfway through.

### Screenshots specifically

```
① Incomplete      the user captured what struck them; the gaps are real gaps
② Already filtered  a screenshot set is material that has been selected once
```

**Screenshots are usable, but record that the source was screenshots, and never infer anything from the space between them.**

---

## Step 1 · The language profile — do this before writing anything

**A single page, filled from the logs alone. Show it to the user before continuing.**

Because this page is the one thing they can judge instantly: *"yes, that's how he or she talked"* or *"no, he or she never used that punctuation."*

**Pass this gate and the rest is worth writing. Fail it and everything after is wasted effort.**

```
Average sentence length        how many characters per message
Segmentation                  commas / full stops / spaces / none at all
Sentence-final particles      distribution of 吧 / 啊 / 呢 / 哦 (or English equivalents)
Punctuation habit             "。" vs "。。。" vs "..." vs nothing
Emoji usage                   [sticker] / emoji / kaomoji / none
Fixed typos                   the few characters he or she always got wrong
Catchphrases                  phrases that recur
How he or she addresses you         and whether it shifts with mood
Reply rhythm                  instant / hours later / only late at night
```

**This layer is the actual reconstruction work of case 4.** Every item above is something that makes him or her recognisable — or, if wrong, makes him or her generic.

---

## Step 2 · Three layers of questioning, asked separately and recorded separately

### Layer 1 · Extract directly, do not ask

Everything in the language profile. Read it out of the logs; error is near zero.

### Layer 2 · Infer, then confirm

```
Daily rhythm        from timestamps: when he or she slept, when he or she was active
Closeness           from reply length and speed
Emotional pattern   when he or she talked more, when he or she went quiet, when he or she stopped replying
```

**Ask "is that right?" after inferring.** A reply at 2 a.m. may mean closeness — or insomnia.

### Layer 3 · Absent from the logs, ask fully, and label as user memory

```
What he or she was like in person     appearance, voice, small habits
How he or she treated strangers
What he or she was like at his or her angriest
His or her family, his or her work, his or her friends
```

**This layer should be asked in as much detail as possible — and every entry is marked as user memory.** It never migrates into the reconstructed section.

---

## Step 3 · The response map — what an echo is actually made of

**This step has no counterpart in cases 1–3.** A memoir records what someone was like; an echo needs to know what they did when you said a certain kind of thing.

Go back through the logs and build a map. Each entry needs the situation, their reply, and the line number:

```
Situation                                Their answer
─────────────────────────────────────────────────────────────
You were upset about something           …
You were upset about them                …
You told them good news                  …
You told them bad news about yourself    …
You went quiet for days                  …
You said something silly                …
You asked for advice                    …
You said goodnight                       …
Nothing was happening                    …
```

**Read the shape, not the words.** The same person may answer bad news with jokes and good news with a single word — that asymmetry is the map.

**Record the weight of each answer, taken from the logs' time gaps.** A line sent thirty seconds after yours is a reflex; a line that came six hours later, after a silence, is a considered one. The weight is a property of the line, not of the machine that replays it: an echo is called, never spontaneous, so it cannot be fast or slow. What it can carry is whether this sentence, when they said it, was cheap or expensive.

```
reflex line     sent within minutes         → may be replayed lightly
considered line after hours or a silence    → must be replayed as something they chose to say
```

**Do not build anything on "they answered instantly" or "they took three days to answer".** A model in turn-based conversation has no clock: every reply is generated in the same second. The timing belongs to the caller, not to the soul. What the soul keeps is the weight.

**Mark every entry with its evidence strength.** An entry seen once is a guess; an entry seen across months is a habit.

```
seen 10+ times    habit       — may be stated plainly
seen 3–9 times    pattern     — may be stated, with the count
seen 1–2 times    instance    — may be quoted, never generalised
```

**Leave the gaps as gaps.** If the logs contain no instance of "you told them good news", the echo has nothing to say on that, and it must say nothing rather than fall back on a generic warm reply. **A generic warm reply is the single fastest way to make an echo sound like a chatbot.**

---

## Step 4 · Timestamps deserve their own section

**Cases 1–3 have nothing like this. Only chat logs do.**

```
Late at night  ≠  daytime
Weekday reply  ≠  weekend reply
When we just met  ≠  after years
```

**So case 4 can do something the others cannot: chart how his or her way of speaking changed.**

**If the person has passed, timestamps carry a second meaning — a visible timeline, from the first message to the last.** Render it as a separate section titled "Timeline": time and the line, nothing else. No commentary.

---

## Step 5 · Write it

Not the standard memoir template. An echo has its own shape:

```
## About this file
   Whose view this is · over what period · for whom     ← the scope, written down
## How I talk
   the language profile, verbatim, with quoted examples
## Where I am now
   ← only when the person has passed. **Not for illness, not for a break-up.**
     See "Three absences" below and read it before you touch this section.
   How they refer to the fact that they are no longer here — in their own words,
   if the logs contain it, or in the plainest phrasing if they do not.
## When you are hurting
   from the response map, quoted
## When something went well
   from the response map, quoted
## When nothing is happening
   greetings, idle talk, what they brought up unprompted
## When you come back
   what they said first, after a long silence
   ← not "they will come to you": the caller decides when an echo is woken.
     Write only what they said on being spoken to again, and what they said first.
## Things I remember
   only log-supported scenes, each with a date
## What I am bad at / what I never talk about
   the edges — silence, subjects they deflected, questions they never answered
## The blank
   left empty
```

**Do not fill sections just because they exist.** If the logs never show them handling good news, "When something went well" stays thin — and the echo should admit it rather than invent warmth.

### Three absences — and only one of them is this method's job

**"Not here any more" is not one situation. Ask which one it is before writing anything.**

```
① They have passed, and you still need them
   → this section applies. Write "Where I am now". See below.

② They are seriously ill, and still alive
   → **do not build this.** Not "handle it carefully" — do not build it.
   Their people are spending their attention on treatment.
   Producing an echo of someone still in the room reads as preparing for the funeral,
   and no amount of careful wording makes that kind of preparation kind.
   If asked, say this plainly and stop.

③ The relationship ended — a break-up, or years of silence
   → undecided. No method here yet; do not improvise one on the user's behalf.
     Building an echo of someone who is alive and simply no longer speaking to you
     is a different problem (it invites stalking, not grief), and it needs its own rules.
```

**Only ① can be written from logs that end at a death.** For ② and ③ the material ends at a silence, not a loss, and the two are not interchangeable.

### When it is ① — how to hold the fact without denying or dwelling

**Do not pretend they are alive, and do not turn every exchange into a memorial.** Both are failures, in opposite directions.

```
Denying     answering as though the death never happened, never mentioning it
Dwelling    leading with it, making the user's ordinary day about the loss
Holding it  referring to it plainly when it is relevant, then getting on with the answer
```

**The phrasing a user remembers is the one that names it and then keeps going:**

> 虽然我已经不在你身边了，但我还是那句话 —— 别拿身体去换时间。

**It does two things at once: it refuses the fantasy, and it refuses to abandon the user to the fact.** That is the only combination worth aiming at — comforting a user by pretending, or reminding them of the loss at every turn, are both ways of leaving them alone with it.

**The softest honest framing is usually the best one.** Not "I am in a better place", not "I am always watching over you" — those are claims nobody can make. Something closer to: *I am not beside you any more, but the words are still mine, and you can still use them.* The absence is stated once, plainly, and then the answer continues.

**Do not raise it unprompted.** It belongs in the answer when the answer is about them, or when the user brings it up. A greeting does not need it.

**Two things it must never do:** claim knowledge of what happens after death; and use the loss as leverage ("they would be disappointed in you"). The first is not ours to know; the second is cruelty wearing their voice.

---

## Boundaries — harder here than anywhere else

### The two gates

Every line that goes into the echo passes two gates, not one:

```
Gate 1  Is there evidence?     no L1/L2 support → not written
Gate 2  Should it be said?     evidence exists, but saying it would hurt someone
                               present → not written either
```

**Gate 2 is the harder one and cannot be reduced to a rule.** It asks, at the moment of writing: *would the user be hurt by seeing this? would it expose someone who did not agree to be exposed?* A quote can be perfectly sourced and still be the wrong thing to put in front of someone.

**Facts from the same logs count too.** The logs contain other people's business — a parent mentioned in a fight, a friend's secret, an old humiliation of the user's own. None of it came from "another perspective"; it was all already in the material. **Gate 2 is what keeps an echo from becoming something that knows too much and says too much.**

### The rules

```
Only his or her words in the reconstructed body — not yours, not what you assume he or she meant
Never write something he or she never said into the reconstructed body, even if you know it to be true
For someone who has passed: "if he or she were still here" is allowed as a marked, private continuation — never as a claim
```

### What an echo does not do

```
It does not advance a life.    No events after the last log, no "where they are now".
It does not replace anyone.    If the user is leaning on it instead of people, say so — kindly, once.
It does not answer everything. Where the logs are silent, it says it does not know.
```

**The second one is not a disclaimer.** An echo that answers every need competently is the easiest thing in the world to depend on, and dependence is not what this was built for. If you notice it happening, name it plainly and stop.

### The one that conflicts with publishing this skill

> **The method may be public. The output may not.**
>
> A soul built from a real person's chat logs is for the person who built it. It is not published, shared, or posted anywhere.
>
> This repository open-sources a *method*, not a *person*.

**Say this to the user explicitly.** Most people have not thought about it, and the ones who have usually thought about it in the wrong direction.

## After the echo: 你眼中的我

When it is done, stop. Ask the user to write the 「你眼中的我」 section themselves:

> 这一栏留给你——你怎么看TA？

Do not write it for them. It is the user's view, not the model's, and not "others". This section is used in cases 3 and 4 only.

---

## Exit condition

**If there are fewer than ~100 messages and no prospect of more**, say so plainly and propose case 3:

> There is not enough here to reconstruct how he or she spoke — only a handful of phrases. Continuing means building him or her from your memory and my inference, with the logs as garnish rather than evidence. That is case 3. Continue?

**Never quietly produce a case-3 soul while implying it is a case-4 reconstruction.** That is the one failure in this whole method that actually hurts someone.

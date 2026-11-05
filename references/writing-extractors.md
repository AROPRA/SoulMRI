# Writing the extractor yourself

Read this before extracting anything at scale.

**This skill ships no universal extractor.** Formats vary too much — one export puts the
speaker in a leading tag, the next puts it in a trailing parenthesis, the third has no speaker
at all. A hardcoded script works for exactly one work and fails silently for every other.

**So you write the extractor for the format you actually have.** This page is how to do that
without producing garbage. It applies to **structured exports only**; prose (a novel, a
screenplay, a transcript book) is not scripted — it is read in chunks (case 1, Two paths).

---

## Step 0 · What is available

Check before writing anything:

```bash
node --version
python --version    # or python3 --version
```

Either is fine. **Python is usually the better choice for this job** — `csv` and `json` are in
the standard library and handle quoted multi-line fields for free.

### If neither is installed

Try the platform package manager first, in this order:

```
Windows   winget install Python.Python.3.12
          winget install OpenJS.NodeJS.LTS
macOS     brew install python
Linux     sudo apt install python3      (or dnf / pacman)
```

**If the install fails — no permission, no network, corporate proxy — stop and hand the user
the command.** Do not keep trying variants; the user knows their network better than you do.

Give them something they can paste, including the version pin, for example:

```
winget install --id Python.Python.3.12 -e
python -m pip install --upgrade pip
```

**Report what you tried and what failed.** A user told "Python is missing and I could not
install it" will sort it out in a minute. A user told "an error occurred" will give up.

---

## Step 1 · Probe before extracting

**Never write the real extractor first.** Write a probe that only reads and prints, and answer
these four questions from its output:

```
① Where does the speaker live?      Its own column? A prefix? A trailing tag? Nowhere?
② Where do scene boundaries live?   A group id, a label line, a filename, or nowhere?
③ What markup is embedded?          Colour codes, ruby, style tags, control directives?
④ Can a field contain a newline?    If yes, line-oriented reading is wrong — use a CSV/JSON parser.
```

A probe is twenty lines and saves an hour. Print the first three records **in full**, plus a
frequency count of the first token of whichever field looks like it holds the speaker.

**Print the raw record, not a parsed summary.** A summary hides the structure you are trying
to see.

---

## Classify by sampling, never by tag name

**This is the mistake that costs the most and looks the least like a mistake.** Tag names in game exports are internal, abbreviated, and almost never mean what they appear to mean.

Two real examples from one export:

```
[s]    looks like "smile" (an expression tag)   → actually the protagonist's lines
#st    looks like "start" (a control directive) → actually narration / performance text
```

**Both guesses were wrong, and both produced a plausible-looking corpus.** The first turned the protagonist's dialogue into "unknown speaker"; the second threw away every narration line as a directive.

### The procedure

```
① Enumerate every distinct tag with its frequency
   Sort descending. The top ten usually account for almost everything.

② Sample three to five lines per tag
   Read the actual text under that tag. Read it in the original language if
   that is what you have — do not judge from a translation.

③ Assign the class from the content, not from the name
   Possible classes: explicit speaker / narration / unsourced dialogue / directive.

④ Write the table into the script as a comment
   Tag → class → why. The next person (or the next you) will need it.
```

### The four classes worth distinguishing

```
explicit speaker    a name is present and reliable
narration           the narrator's voice: scene description, inner monologue, system text
unsourced dialogue  quoted speech with no name attached — still someone speaking
directive           camera, waits, layout. Nothing to extract.
```

**Narration and unsourced dialogue must not be merged.** Narration is the narrator's voice; unsourced dialogue is still a character speaking. Merging them puts narration into the character's mouth — or, worse, attributes the protagonist's lines to the character you are building.

**When you cannot tell whether an unsourced line is the protagonist or a bystander, check the surrounding records.** The first line of a scene often establishes who is present.

---

## One record may hold several people

**This is the most destructive trap in this document, and it is invisible at every stage.**

A single text record often carries a **list** of directives, not one. Real example:

```
3;모모이;04                          ← Momoi changes expression. No line.
5;미도리;04;언니 때문이잖아아아!!      ← the actual speech, spoken by Midori
#5;shake
#5;em;[!]
```

**The text field next to this record belongs to the *last* segment that carries a body — Midori's line — not to the first segment, which merely says Momoi changed his or her expression.**

### What reading the first segment does

```
attribution   his or her name is attached to someone else's line
omission      his or her own line, when it follows another character's expression
              change, is dropped entirely
```

**Both directions at once.** In one real run this produced 1,286 lines; after the fix, 1,358 — and fourteen lines spoken by his or her sister had been attributed to him or her.

**Nothing errors. The output looks like a plausible corpus**, which is why the check below is not optional.

### The rule

```
Split the field on newlines.
Walk the segments backwards.
Take the first segment that carries a body — an index/name/expression prefix
followed by text, or a narration prefix followed by text.
That segment's speaker owns the line.
```

### How to notice you have this problem

**Pick any quoted line where he or she says something strongly emotional, and read the surrounding records.** If the record's raw field starts with a different character's name, you have it.

**A cheap global check:** count how many extracted lines contain forms of address he or she would not plausibly use. A sudden cluster of an unusual address term is the signature — in the run above, one term appeared 17 times, and 14 of those belonged to another speaker.

---

## Step 2 · Traps already paid for

Four of these cost real time. Each fails **quietly**.

### ① Reading a CSV line by line

**Symptom:** every row looks valid, but the text column is empty or truncated.

**Cause:** a quoted field contains a newline, so one record spans several lines. `ReadLine()`
returns half of it.

**Fix:** a real parser. `csv.DictReader` in Python, `csv-parse` in Node. Never split on newlines.

**This is the worst trap on the list** because nothing errors. You only notice later, when the
material comes out thin and you cannot explain why.

### ② The speaker is inside another field

**Symptom:** there is no speaker column, yet the dialogue clearly has speakers.

**Cause:** the export concatenated speaker and text into one field, usually with a separator.

**Fix:** split that field on its separator and inspect the pieces. The leading tokens are almost
always metadata — an index, a name, an expression code — and the last piece is the line.

**Watch for several shapes in the same file.** A real export can mix
`3;name;expr;text`, `#na;name;text`, and `#all;hide` in one column, with the first carrying
dialogue and the last two being directives.

### ③ Voice flags may be empty

**Symptom:** you planned to use "has voice clip" as the dialogue/narration test, and the voice
column is null everywhere.

**Fix:** fall back to the empty-speaker test — a record with text but no speaker is narration.
Voice flags are the better signal when present; empty speaker is the universal one.

### ④ The name is not spelled the way you assume

**Symptom:** your filter returns zero lines, or returns only lines where the character is
mentioned rather than speaking.

**Cause:** the export is in the original language, or in romanisation, or the display name
differs from the internal name.

**Fix:** search for the name first and read what comes back before filtering on it. **Confirm
you are matching the speaker position, not the text position** — otherwise you collect
everyone talking *about* him or her, which looks like a rich result and is the wrong corpus entirely.

---

## Step 3 · Verify the extraction

Three checks, all cheap:

```
count     Does the number of extracted lines match what the probe suggested?
sample    Open the source at three random extracted lines. Does each one match?
empties   What fraction of rows have an empty text field? Anything above a few percent
          means the parser is still missing something.
```

**The sample check is the one people skip.** It catches every trap above, because a
half-parsed line fails to match the source at the point where it was cut.

---

## Step 4 · When to stop scripting

**If the format resists a regex — inconsistent separators, speakers only inferable from
context, markup nested arbitrarily — stop.**

Switch to the model-reads-it path (tier ④ in case 1), with the instructions to copy verbatim
and mark `UNSURE`. If the material is prose, this is not a fallback — it is the high-precision
path: chunk it and read every chunk. It is slower and costs more, but it degrades honestly.

**The bad outcome is not "slow".** The bad outcome is a script that half-works, produces a
plausible-looking table, and is never suspected.

---

## Step 5 · Write the intermediate table

Whatever the source, emit the same shape:

```
id<TAB>speaker<TAB>line<TAB>source
0001     name     "the line"     G21010/L4122
```

- `speaker` empty means narration — this is the two-class split, recorded rather than judged
- `source` must be re-findable: a group id plus a line number, or a filename plus offset
- strip display markup, keep the words

**Once this table exists, everything downstream is format-independent.** That is the point of
building it: the extraction ends, and the method begins.

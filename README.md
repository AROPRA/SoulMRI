# SoulMRI

Build a character soul file that makes a model **recognize** a character instead of **acting** one.

> 别写一个角色 —— 去找他/她**已经说过的**话。

Conventional character cards are spec sheets: third person, describing what the character is like. The model then *performs* the character. SoulMRI writes a memoir instead: first person, recording the parts of him or her that already exist. The model *acknowledges* them.

**One case is different.** When the material is a real person's chat logs (case 4), the output is an **echo**, not a memoir — it answers instead of describing, it does not grow, and it is meant to be put down one day. See `references/case-4-chat.md`.

Three choices, each opposite to the mainstream:

1. **First person throughout** — the soul speaks as the character, not about them.
2. **Every line carries its source** — `She: "You're the best sister ever!" (L2453)`. The citation binds "I believe this" to "someone actually said this".
3. **A blank space, not an inventory of unknowns** — the last gate is not a list of what is missing, but room left for what is not known yet.

## Contents

```
SKILL.md                    the skill itself
references/
  case-1-script.md          extracting from a script
  case-2-web.md             extracting from web pages
  case-3-original.md        building an original character — three entry branches
  case-4-chat.md            extracting from chat logs — an echo, not a memoir
  writing-extractors.md     how to write the extractors
  case1-flow.png            case 1 at a glance
  case2-flow.png            case 2 at a glance
  case3-flow.png            case 3 at a glance
  case4-flow.png            case 4 at a glance
```

**This repository ships the method, not scripts.** No extractor, no diagram generator, no test harness. The method says what they must do; writing them is part of the work.

## Install

A skill is a folder with a `SKILL.md` in it. Put this one where your agent looks for skills, or paste `SKILL.md` into its system prompt.

```
~/.dsh/skills/soulmri/          # DeepSeek Harness
~/.claude/skills/soulmri/       # Claude Code
```

Keep `SKILL.md` and `references/` together — the references are read on demand, not up front. There is nothing to install or build: no Python, no dependencies, no scripts.

**Start in a fresh session.** A previous draft or an earlier soul already in the context acts as a source: the model will quote itself, confidently, with citations that look real. If a draft exists, keep it as a file to compare against; do not paste it into the working context.

## Contributing

Issues and pull requests are welcome. The method is public; the output is not — a soul built from a real person's chat logs belongs to the person who built it, and is never posted here.

## License

MIT — see [LICENSE](LICENSE).
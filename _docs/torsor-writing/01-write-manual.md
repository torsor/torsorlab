---
title: write-manual
tool: torsor-writing
slug: write-manual
permalink: /tools/torsor-writing/write-manual/
order: 1
summary: a skill to take a folder containing a project, and write a user manual for it.
howto_lead: >-
  new to this? open a folder holding the project you want documented in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a user manual for the project in this folder
notes:
  - title: the preface comes first
    text: >-
      it is written before any chapter, because it settles who the reader is and
      what problem brought them here. everything after inherits that.
  - title: this page's siblings
    text: >-
      the three manual-backed pages on this site — paper-guide, critical-guide,
      review-and-repair — were written with this skill. they are the worked
      examples.
---

a Claude Code skill. point it at a folder containing a project and it reads what
is there — the code, the README, whatever design notes exist — and writes a
user's manual for it.

the manual covers what the project is, how to use it, and what to do when it
misbehaves. direct, conversational prose rather than reference documentation —
the register of someone explaining their tool to a colleague who has just sat
down at it.

## how it goes

it proposes a chapter outline for you to approve first. then it scaffolds a directory
from the shared commons, writes the preface, writes the chapters one at a time,
and writes the quick-reference appendix last, once there is something to collect.

the default voice is `01-direct`. a more digressive `02-wandering` exists; ask for
it by name at the outline stage.

## invoke

```
/write-manual ~/code/myproject
/write-manual the thing CLI, source at ~/gits/thing
```

## produces

a self-contained book directory: LaTeX source, plus PDF, HTML, EPUB, and Markdown
built from it, with its own `Makefile`, its own copy of the converter, and a
`STYLE.md` recording the voice it was written in. `make check` verifies the build,
and the publication pass inspects a sample of pages by eye before the manual is
called finished.

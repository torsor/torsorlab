---
title: research-room
slug: research-room
tagline: a folder template for doing sustained mathematical research with an agent — one that accumulates understanding while you keep hold of the questions.
value: your questions, evidence, and changes of direction stay in files you can return to when a session ends or a new one begins.
status: released
repo: https://github.com/torsor/research-room
howto_lead: >-
  open Claude Code or Codex in an empty folder where you want the room, and say:
howto_say: >-
  get the research-room template from https://github.com/torsor/research-room and set this folder up as a research room for my project; guide me through the choices I need to make
order: 2
manual: true
manual_blurb: a full user's manual, written for someone about to work in a room.
docs_eyebrow: the room
docs_heading: how it is put together
---

## getting it

a template repository. copy it, replace the placeholders, and start working in
it. there is nothing to install and nothing to run.

your agent can make the copy and walk you through the setup using the instruction
above. the commands below are for making the copy yourself.

```sh
git clone https://github.com/torsor/research-room.git my-project
cd my-project
rm -rf .git && git init
```

then work through [starting a room](/tools/research-room/starting-a-room/) —
four placeholders and a config path, and the room is yours.

the template ships problem-neutral: no people, no institutions, no private
paths, no session identifiers, no unpublished mathematics, and no inherited
project history. `PUBLICATION_CHECKLIST.md` carries the checks to run before
making a room of your own public.

### license

the template is distributed under Apache-2.0, which covers the template files
as distributed. you choose your own license for the notes, manuscripts, and
computations you add afterwards, subject to the licenses of any template
material you keep.

---
title: starting a room
tool: research-room
slug: starting-a-room
permalink: /tools/research-room/starting-a-room/
order: 1
summary: the five steps between copying the template and working in it.
notes:
  - title: replace every placeholder
    text: >-
      the template is deliberately problem-neutral. anything left in angle
      brackets is a gap the agent will read as literal text.
  - title: before you make it public
    text: >-
      PUBLICATION_CHECKLIST.md carries the checks. a research room accumulates
      private paths and unpublished mathematics by design; publishing one is a
      deliberate act with a list attached.
---

copy the template, then five steps.

1. **replace the placeholders.** `<PROJECT TITLE>` and the rest, in
   `AGENTS.md`, `conventions.md`, and `goals/question-template.md`.
2. **name the first question.** rename `goals/question-template.md` for it.
3. **set the path.** in `.codex/config.toml`, replace
   `<ABSOLUTE-PATH-TO-RESEARCH-ROOM>`.
4. **check the model instructions.** review `.codex/README.md` — the
   model-instruction snapshot may need refreshing for the Codex model you are
   using.
5. **before posting it anywhere**, run the checks in
   `PUBLICATION_CHECKLIST.md`.

## getting the copy

```sh
git clone https://github.com/torsor/research-room.git my-project
cd my-project
rm -rf .git && git init
```

dropping the template's history is deliberate: the room's own history should
start with your project, not with the template's development.

## the first thing the agent reads

`conventions.md`, then the relevant file in `goals/`, then only the artifacts
the current question needs. it does not reread the whole archive every turn,
which is the habit the folder structure exists to make unnecessary.

so `conventions.md` is worth filling in properly before the first session. it
carries the definitions, the notation, and the standing assumptions — the
things that would otherwise be re-established, slightly differently, every
time.

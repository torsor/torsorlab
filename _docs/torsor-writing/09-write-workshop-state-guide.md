---
title: write-workshop-state-guide
tool: torsor-writing
slug: write-workshop-state-guide
permalink: /tools/torsor-writing/write-workshop-state-guide/
order: 9
summary: a skill to take a live workshop's working record, and write up where the work stands.
howto_lead: >-
  new to this? open the workshop folder in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a state guide for the work in this folder
notes:
  - title: labels are carried verbatim
    text: >-
      the docent translates; it never re-grades. silently upgrading a conjecture to
      a theorem while expositing is the failure this skill is shaped against.
  - title: write a new dated artifact
    text: >-
      never overwrite last week's state guide. the progression has to stay visible.
---

a Claude Code skill. point it at a live workshop and it reads the room's own
working record and writes up where the work currently stands, for a collaborator
who has to steer it.

same shape as its siblings, with five deliberate differences.

the corpus is **the room's own live record** rather than external sources,
distilled into `state-notes/`. the spine is **the confidence ledger** — solid,
provisional, open, skeptical — harvested from the room's own labels rather than
decided by the writer. the reader is a collaborator steering live work, not a
student learning an idea. the voice is **present-tense, dated, and
commit-stamped**: as of this commit, the room has this. and time is structural —
a mandatory chapter on what changed and what might change, with corrections and
dead ends as first-class content rather than footnotes.

it leads with the ledger, not with the best result.

## invoke

```
/write-workshop-state-guide the specialization room, for a collaborator
/write-workshop-state-guide where does the workshop stand
```

## produces

a dated snapshot — `guide/<YYYY-MM-DD>-<slug>-state/` — in the house format, listed
in the docent's guide stream, with `state-notes/` kept alongside.

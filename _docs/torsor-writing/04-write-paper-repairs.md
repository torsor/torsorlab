---
title: write-paper-repairs
tool: torsor-writing
slug: write-paper-repairs
permalink: /tools/torsor-writing/write-paper-repairs/
order: 4
summary: a skill to take the problems a critical guide found, and write the repairs into a copy of the paper's own source.
notes:
  - title: it needs a critical guide first
    text: >-
      the input is a critical-guide package and its issues.yaml. without one it
      refuses rather than improvising a ledger of its own.
  - title: it repairs, it does not rewrite
    text: >-
      deciding what the paper should claim is a different act. the boundary
      between the two is the subject of most of the skill.
---

a Claude Code skill. point it at a paper that already has a critical guide and it
works out the mathematics that closes each issue that guide found, audits every
repair adversarially, and writes the ones the paper itself *forces* into a copy of
the authors' own source as tracked changes.

what comes back is a corrected source that compiles two ways — changes marked up
for review, or silently in place — plus the repairs that were worked out but not
adopted, shown in position so you can browse and choose, plus a report of what no
repair reaches.

nothing is applied silently and nothing is decided for you. a repair goes in only
when there is exactly one way to make the text consistent with what the paper
already demonstrably contains. everything else is proposed, tagged, and left for
you to accept or reject.

it does not skip the mathematics. "one would need to show that the adjunction
extends" is not a repair; the argument gets written.

## invoke

```
/write-paper-repairs ~/papers/descent/
/write-paper-repairs ~/papers/descent/critical-guide/
```

it is usually easier to run it as the second half of
[write-review-and-repair](../write-review-and-repair/), which sequences the
examination and the repairs and checks the handoff between them. that page covers
the repair stage at working depth — the triage, the dispositions, the markup
states, and what the markup cannot do.

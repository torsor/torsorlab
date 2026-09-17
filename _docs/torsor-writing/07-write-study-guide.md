---
title: write-study-guide
tool: torsor-writing
slug: write-study-guide
permalink: /tools/torsor-writing/write-study-guide/
order: 7
summary: a skill to take a target result in the Stacks project or Kerodon, and write a reading route to it.
howto_lead: >-
  new to this? open any folder you want the guide written into in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a study guide routing me through the Stacks project to <the result you want>
notes:
  - title: citation is not pedagogical dependence
    text: >-
      the dependency closure is a superset skeleton, not a reading list. triage —
      read closely, skim, black-box for now — is the editorial act that carries
      the guide.
  - title: profiles are memories, not authorities
    text: >-
      the frontier gets reconfirmed at the start of every guide. one question
      against a wasted book.
---

a Claude Code skill. name a result you want to reach in a large tag-addressable
corpus — the Stacks project, Kerodon — and a reader, and it computes a reading
route through the corpus to that result and writes it up as a guide.

where [write-topic-guide](../write-topic-guide/) must *carry* an exposition
because no source does, this corpus already contains excellent exposition with
explicit dependencies. so the guide's value is elsewhere: **selection, ordering,
motivation, and triage**.

four things are particular to it. **the reader profile persists** — background and
a per-corpus *frontier*, recorded in the corpus's own coordinates, in a file that
outlives any one guide. **the spine is computed**, not composed: the dependency
closure of the targets from the corpus citation graph, pruned by the frontier. the
route is edited, never invented. **triage is the core editorial act** — every stop
is marked read closely, skim, or black-box for now, and every black-box is named
both in its chapter and in a ledger in part I, with when to return to it. and
**checkpoints move the frontier**: each milestone ends in a checkpoint, and a
passed checkpoint is an update written back into the profile.

that last part is the point of the system. a guide that ends without offering the
frontier update has not finished.

## the shape

```
phase 0    load or create the profile, reconfirm the frontier
phase A    targets -> route -> milestones -> triage  (you approve the spine)
phase A'   targeted digests of the spine's tags      ->  source-notes/*.md
phase B    author and build                          ->  the guide
close      offer the frontier update
```

## invoke

```
/write-study-guide route me through the Stacks project to fppf descent
/write-study-guide what should this student read in Kerodon to get to straightening
```

## produces

a guide directory in the house format, plus an updated reader profile.

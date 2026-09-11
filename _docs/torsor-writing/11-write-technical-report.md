---
title: write-technical-report
tool: torsor-writing
slug: write-technical-report
permalink: /tools/torsor-writing/write-technical-report/
order: 11
summary: a reproducible account of an experiment, written for a skeptical reader.
notes:
  - title: the evidence ledger is a gate
    text: >-
      no conclusion gets drafted that the ledger cannot support. the gate comes
      before the prose, not after it.
  - title: negative results are in scope
    text: >-
      positive, negative, inconclusive, exploratory, comparative, ablation,
      reproduction, capability-evaluation — the report shape is the same.
---

turns protocols, run logs, outputs, tests, evaluator notes, interventions, and
repository state into a reproducible account of an experiment: the question, the
methods, the results, the validation, the failures, the limitations, and the next
experiment.

it is written for a reader who does not believe you yet. provenance is frozen
first, then every run and artifact is audited into an evidence ledger, and the
ledger gates what may be claimed. only then does it fix a six-sentence spine and
a section plan for you to approve, and only then does it write.

failures and limitations are first-class sections rather than a closing
concession.

## the shape

```
phase 0   scope the report, freeze provenance   ->  experiment brief + reader profile
phase A   audit runs, artifacts, validation     ->  report-notes/*.md   (evidence gate)
phase B   six-sentence spine and section plan   ->  you approve the claims
phase C   author, build, inspect                ->  the report, four formats
```

## invoke

```
/write-technical-report the overnight run in ~/experiments/2026-09-sweep/
```

## produces

a report in the house format — LaTeX source with PDF, HTML, EPUB and Markdown —
with the run manifest, evidence ledger, and artifact index kept alongside.

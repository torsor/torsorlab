---
title: write-critical-guide
tool: torsor-writing
slug: write-critical-guide
permalink: /tools/torsor-writing/write-critical-guide/
order: 3
manual: true
summary: a skill to take one mathematical paper, and catalog the potential issues in it, indexed and analyzed.
howto_lead: >-
  new to this? open a folder holding the paper's LaTeX source or PDF in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a critical guide for the paper in this folder
notes:
  - title: findings, never a disposition
    text: >-
      accept, reject, major revision — none of these appears anywhere in the
      package as a judgment about the paper, and neither does "I recommend". the
      decision carries your name.
  - title: the errors are not symmetric
    text: >-
      a defect reported that is not there costs the authors weeks and costs you
      your credibility. a missed comma costs a reader three seconds. the process
      does not treat these as though they were the same.
  - title: a clean bill, or an unopened box
    text: >-
      the package says what was verified and came out clean, and what was not
      checked at all, with reasons. where the coverage ends is where your own work
      starts.
---

a Claude Code skill. point it at one mathematical paper and it reads the paper and
catalogs the potential issues in it — each one located in the source, graded by
consequence, and tested against attempts to refute it before it is written down.
it reaches no verdict; that part stays yours.

here is the work it is doing for you. you said yes to refereeing a paper, and the
paper is fifty pages long, and three
of those pages are a computation you would have to redo yourself to believe. or a
committee has asked what you think of work outside your area. or a student wants
to build on a result and would like to know, before spending a year on it,
whether the result is actually there.

the labor is the same in all three cases and it is mostly invisible. read the
paper closely enough to find the potential issues in it. check that the cited lemma
says what the paper uses it for. work out whether the gap in section 4 is a gap
or a compression. and then — the part that costs the most and shows the least —
convince yourself that each thing you are about to call an error really is one,
because you are going to put your name on it.

`write-critical-guide` does that labor and hands back the result. it runs
unattended: point it at a paper and it goes to completion without asking
anything.

## findings, never a verdict

a critical guide is the material a judgment gets written from, not the judgment.
hold that distinction and the rest follows; lose it and the output becomes a
referee report with no name on it, which is the one thing it must not be.

it is the evaluative sibling of [write-paper-guide](../write-paper-guide/). a
reading guide takes the paper as given and expands where the paper compresses, so
the reader can keep moving. a critical guide asks whether the paper holds, and
where the paper compresses it stops and says so: what is missing, how much it
matters, whether the gap can be closed. the two are not alternatives — a reading
guide is the *input*, commissioned first at proof depth for a reader who is
refereeing. the critical work is done on top of that reading.

### it tries to refute a finding before writing it down

every finding that would be graded major goes to three independent skeptics
first. each gets the paper and the finding and is told to **refute** it — to find
the argument the finding claims is missing, the hypothesis it claims is
undischarged, the reading under which the notation is consistent. they default to
refuted when genuinely uncertain, and none of them knows what the others
concluded. two or more refutations and the finding is dropped, or demoted if a
weaker true version survives. the drop is recorded with its refutation rather
than silently discarded.

claims about the literature get this treatment at every grade, because nothing
else checks them and they are the most quotable sentences in the package. every
priority or duplication charge also gets a chronology check — when each work
first appeared *publicly*, preprint date rather than publication date. a
duplication charge that dissolves on dates alone is the commonest false positive
in the whole pipeline.

the effort spent checking scales to what being wrong would cost, not to how
likely the error seems.

### grades measure consequence, not length

| grade | meaning |
|---|---|
| `major` | affects correctness, or a reader cannot follow without reconstructing the argument |
| `minor` | should be fixed, but the reader gets there |
| `trivial` | copy-editing |

a misprinted subscript that makes two displays contradict each other is major. a
paragraph of clumsy prose is trivial. the item that takes three words to state
can be the one that breaks the theorem.

## how it reads a paper

it reads the paper, then runs four sweeps in parallel — mathematical, reference,
typographical, and contextual — and feeds their output into the refutation pass.
surviving findings are promoted into `issues.yaml`, the ledger every artifact in
the package is generated from. that generation step is the engineering that keeps
the prose and the annotations from drifting apart: the guide, the issue list, and
the annotated sources all come from one record.

each finding carries an anchor into the paper's source, which is what lets the
annotations land at the passage they concern rather than near it.

## what comes back

```
critical-guide/
  00-guide.pdf         summary + issue list
  01-summary.md        hand-written prose
  02-issues.md         generated, point by point
  03-repairs.md        repairs with a clear route
  repairs/             the multi-route dossier
  issues.yaml          the ledger
  annotated-<cat>.tex  one per category
  annotated-<cat>.pdf  compiled, colour-coded
  Makefile  README.md
```

`review-notes/` sits beside it and is not part of the handover — it is the audit
trail, holding the sweeps, the refutations, and the findings that were dropped
and why, so a finding you doubt can be traced back to how it was reached.

the build is verified rather than assumed. five gates before handover: `make`
exits zero from a clean tree; every annotated document reports ok; the guide PDF
passes the same mechanical gate rather than a lesser one; the issue tables break
across pages with their headers repeating; and every annotated passage is
confirmed present in the submitted PDF. the hand-back then reports where the
package is, the count of findings by category and grade, what the refutation pass
dropped, and what was not verified — every quantity measured from the files
rather than carried over from an earlier run.

## long papers, and corrections

a work too long for one pass is examined in chunks: reconnaissance first, then a
carry file that moves context between chunks, then a synthesis. a finished guide
can also be corrected — the skill verifies the correction first without changing
anything, applies it narrowly, then regenerates the package and reports a
changelog.

## what it is not

not a referee report: it carries no signature and reaches no disposition. not a
reading guide. not a rewrite — where the authors' prose is defensible and merely
not yours, it is left alone, and a preference is never reported as an error. not
a survey.

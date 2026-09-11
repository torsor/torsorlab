---
title: write-review-and-repair
tool: torsor-writing
slug: write-review-and-repair
permalink: /tools/torsor-writing/write-review-and-repair/
order: 5
manual: true
summary: a skill to take one mathematical paper, find potential issues, and mark up the repairs.
notes:
  - title: written is not accepted
    text: >-
      stage two's output is a marked-up build. running both stages back to back
      adopts nothing; the person reading the result decides, tag by tag. even the
      applied repairs are applied to a copy.
  - title: the handoff can go stale
    text: >-
      if the authors post a new version between the stages, the ledger's anchors
      stop matching and repairs get aimed at passages that no longer exist. stage
      two checks and stops.
  - title: the clean build is not a revised paper
    text: >-
      it is what the paper would say if these specific changes were adopted,
      produced so you can read the result in context. sending it on as the
      corrected version skips the step the whole pipeline is built around.
---

a Claude Code skill. point it at one mathematical paper and it runs the two skills
above end to end: first it examines the paper and grades the potential issues in it,
then it works out the repairs and marks them into a copy of the source.

finding the potential issues in a paper is the part everybody talks about. working
out what would resolve them is the part that takes the afternoon.

you have found the gap in section 4. now: is it fillable? with what hypothesis?
does adding that hypothesis break example 3.7? does it change what theorem 1.1 is
claiming? and once you have decided all that, where exactly in fifty pages of
someone else's LaTeX do the sentences go?

## two stages, one handoff

| stage | what it does |
|---|---|
| [`write-critical-guide`](../write-critical-guide/) | reads the paper and produces a `critical-guide/` package: a graded, located issue ledger, annotated sources, and a typeset guide. it surfaces and grades issues; it reaches no verdict. |
| `write-paper-repairs` | consumes that package, works out the mathematics, and writes the forced repairs into a copy of the paper's own source as tracked changes. it shows what it did not adopt in position, and reports what cannot be repaired. |

the pipeline itself is thin. it sequences two skills that already run unattended
and already share a handoff on disk, and carries no examination or repair
judgment of its own. the interesting parts belong to the stages.

**the handoff is a file.** stage one writes `critical-guide/issues.yaml`; stage
two reads it. that is the entire interface, which means the orchestrator holds
almost no state — the only thing carried forward is where the package landed.
that is what keeps the pipeline light enough to run over a long paper without the
examination crowding out the repairs.

it also means the stages compose in other ways. you can examine a paper today and
repair it next month, or examine it, read the guide, decide the findings are
wrong, and never repair it at all. if a `critical-guide/` package already exists
the pipeline reuses it and goes straight to repairs — examination is the
expensive half. say explicitly that you want it regenerated if the paper has
changed.

## how the repair stage works

it triages before touching any mathematics: absence is not the same as positive
error, and repairs are decided in **groups** rather than item by item, because a
repair that is defensible on its own page can be inconsistent with one three
sections later.

then it works out the repairs — actually works them out. "one would need to show
that the adjunction extends" is not a repair. then every repair is audited
adversarially before it can land.

then each group gets a disposition: **apply**, **propose**, or **escalate**. very
few are applied, and that is the design. a repair is applied only when it is
*forced* — when there is exactly one way to make the text consistent with what
the paper already demonstrably contains. everything else is proposed, tagged, and
left for you.

finally it builds twice and verifies both.

## what comes back

```
<paper folder>/
  paper.tex                 the original, never modified
  critical-guide/           stage one's package
    00-guide.pdf  issues.yaml  annotated-*.pdf
  paper-repaired.tex        the working copy
  paper-repaired-notes.pdf  marked up
  paper-repaired-clean.pdf  applied changes only
  04-proposed.md            why each proposal
```

start with `paper-repaired-notes.pdf`. it is the document the whole pipeline
exists to produce, and everything in it is tagged, so you can move between it and
the issue list without translating.

| state | in the notes build | in the clean build |
|---|---|---|
| applied | struck-out red original, blue replacement | replacement silently in place |
| proposed | purple, labelled, replacement shown in position | absent |
| removed | framed and greyed, labelled | gone |

every change carries its issue tag and a footnoted note saying why. an unexplained
diff is not a repair. proposals show their full replacement text where the
replacement would go, so you never have to open another file to learn what a
proposal says.

a proposal never consumes a statement number — counters are frozen inside a
proposal block, so a proposed replacement for theorem 4.2 prints as theorem 4.2
rather than pushing everything after it down by one. that is what makes the two
builds comparable at all.

### answering by tag

the hand-back names the tags, and the tags are how you reply — *apply M-5 and
M-31*. that is not treated as a text edit: each named proposal moves to applied,
the coherence check runs again against everything already applied, and both
builds are rebuilt and re-verified.

## what the markup cannot do

a proposal cannot add a bibliography entry; such a source is cited as plain text
and flagged. a tag inside mathematics is boxed so it cannot break across lines,
and a tag on a long display can push the line. the markup has been verified
against `amsart` and `elsarticle`; a third document class may behave differently,
and the place to find that out is a trivial change rather than a deep one.

some findings have no repair at all, and those are reported as such rather than
patched over.

# working on this site

pointers for anyone — human or agent — writing or editing torsorlab.

## voice

**lowercase prose.** sentences, headings, titles, nav labels, and front-matter
strings all start lowercase. proper nouns keep their capitals (Claude Code,
LaTeX, Rust, Danny Krashen), and so do acronyms (AI, PDF, EPUB, HTML). the
uppercase mono labels in the design — eyebrows, status chips, table headers, the
wordmark — are typography, not prose; leave those alone.

**we, not the lab.** the work is collaborative and the writing should say so.
"we are exploring", "we have been developing", "our work". avoid third-person
descriptions of torsorlab as an entity that acts on its own ("the lab builds…",
"torsorlab is the name under which…").

**"credit" appears at most once on the whole site.** it is a heavy word and it
frames the work as a ledger. the one use lives on the about page. everywhere
else, say what we are doing and who is doing it, and let attribution follow from
that. "collaboration", "together", "with" do most of the work.

**say what a thing is, not what it is not.** prefer the concrete. a tool
description should tell a reader what they can do with it.

**no hype.** no "powerful", "seamless", "revolutionary". the tools are useful;
that is the claim.

## the rest

`README.md` has the structure: where to edit what, the collection front matter,
and how the design is put together. it is the single copy — don't restate it
here, and update it there when it changes.

two things worth knowing before you write:

- run `make check` before committing. it asserts the collections are wired
  correctly.
- the doc pages are deliberately minimal right now. the fuller shape (what it
  writes / who for / prerequisites / a worked invocation / marginalia) is
  supported by the layout whenever the prose arrives — you do not need to
  restructure anything to grow one.

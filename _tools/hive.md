---
title: hive
slug: hive
tagline: a fleet console for Claude Code and Codex sessions running in tmux on always-on boxes.
status: released
repo: https://github.com/torsor/hive
order: 4
docs_pending: true
---

your laptop sleeps. the boxes do not. `hive` is how we see every agent session
across the fleet, reach one, and move work between machines.

## the shape of it

one box is the **hub** and stays up. every box runs a **host** daemon that owns
its own sessions, tmux, and transcripts. clients talk HTTP to the hub, and the
hub polls each host. SSH is used only for install and attach — not for the
day-to-day.

| binary | role |
|---|---|
| `hive-host` | per-box daemon: sessions, tmux, transcripts |
| `hive-hub` | always-on aggregator and action proxy |
| `hive` | the CLI — `status`, `say`, `stop`, `run` |
| `hive-panel` | a desktop GUI, over the hub's HTTP and SSE |
| `hive-web` | a phone console, served from the hub |

written in Rust. shared types live in `crates/hive-protocol`.

## getting it

production deploys go through Ansible; your fleet's inventory lives in
`~/.hive/fleet/`, never in the repo. the short version, from the repo's own
README:

```sh
make install-ops              # deploy helper, on the control node
cd ansible && ansible-playbook site.yml -K
cargo install --path crates/hive-cli
hive status
```

`ansible/README.md` in the repo carries the copy step, the converge order, and
the operational detail.

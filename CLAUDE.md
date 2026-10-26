# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal, hand-maintained Ubuntu Desktop configuration guide. It is documentation plus
companion config files, not an application. There is no build or package step; the one check
is `bin/check-readme` (see Editing README.md). The primary deliverable is `README.md`: a long
(~2,900 line) step-by-step walkthrough for setting up a fresh Ubuntu LTS install (system
tweaks, package installs, dev tooling, GUI fixes). Everything else in the repo exists to
support that guide.

## Branches are release channels, not features

Each Ubuntu LTS release lives on its own long-lived branch: `16.04`, `18.04`, `20.04`,
`24.04`, plus the older `15.10` and `master` (remote only). A branch's `README.md` is
tailored to that release (the first line names the version, e.g. "Configuration of Ubuntu
24.04 LTS").

- GitHub's default branch is `16.04` (`origin/HEAD` points at it); active work currently
  happens on `24.04`.
- There is no `22.04` branch. `24.04` was forked from `20.04` (merge base `5830995`), so
  `20.04` is its parent when comparing releases.
- Version-specific changes (a package that moved PPAs, a command that changed between
  releases) belong on that version's branch only. Do not assume a fix applies across all
  branches. Confirm which Ubuntu version a change targets before editing.
- Cross-version improvements (a new tool worth documenting everywhere) may need cherry-picking
  to multiple branches; mention this rather than silently editing one.
- The README's intro paragraph links the sibling release branches. A new release branch
  needs an entry there on every branch whose list should show it.

## Repository layout

- `README.md`: the guide. Edits here are the main work.
- `os/`: config files laid out by their **destination path on the system**. Drop the `os/`
  prefix to get the real target: `os/etc/profile.d/ps.sh` becomes `/etc/profile.d/ps.sh`,
  `os/home/.bashrc` becomes `~/.bashrc`. A README link to a file there doubles as the copy
  instruction, so keep the structure accurate.
- `files/`: binary assets the guide links to (e.g. emulator BIOS). Linked with `?raw=1`.
- `fonts/` and `notes/`: a font with its author's notes, and standalone how-to notes. Neither is
  linked from the README on this branch (the font steps install from `~/Downloads/Fonts`).
- `bin/check-readme`: checks the README's TOC and links. Its tests are in `tests/`, and
  `.github/workflows/readme.yml` runs both on every push and pull request to `24.04`.
- `docs/superpowers/`: design docs and implementation plans.

## Editing README.md

- After editing, run `bin/check-readme`, and `python3 -m unittest discover -s tests` after
  changing the checker. It requires the TOC to list every heading in order with the right
  anchor and indentation, every in-page and repo link to resolve, and no link to be
  branch-relative.
- It opens with a hand-maintained **Table of Contents** built from in-page anchor links
  (`[Section](#section)`). When you add, remove, or rename a heading, update the matching TOC
  entry and verify the anchor slug: GitHub lowercases, drops punctuation except `-` and `_`,
  and turns each space into a hyphen (`Apache: Enable php-mcrypt & mod_rewrite` becomes
  `#apache-enable-php-mcrypt--mod_rewrite`). A renamed heading silently breaks its TOC link,
  and so does a TOC target that lost its `#`. Keep one TOC item per line; indentation
  decides the nesting.
- GitHub suffixes duplicate heading anchors with `-1`, `-2`. Give a new subheading its
  parent as a prefix (`Apache: Installation`) instead of relying on the suffix.
- Fenced code blocks hold shell comments at column 0 (`# redis-server can write ...`), which
  a plain `grep '^# '` reports as top-level headings. Skip fenced blocks when scanning
  headings.
- Link repo files with relative paths (`os/etc/...`, `files/...?raw=1`) so they follow the
  branch being viewed. Link another release branch by its absolute URL
  (`https://github.com/akalongman/ubuntu-configuration/tree/20.04`): GitHub resolves a
  relative `tree/20.04` against the current file's blob path, which gives a 404 at
  `/blob/24.04/tree/20.04`.
- The guide is organized top-level by intent: `Optional Configurations`, `Installation
  Packages` (System Tools, Other Tools, Development, Gaming), `Customizations`, `Ubuntu
  Fixes`, `GUI`, `Virtual Machine Related`, `Synchronize Configurations`, then the short
  `Chrome Addons`, `Other Applications` and `Clean System`. Place new content under the
  section that matches reader intent rather than appending to the end.
- Commands the reader pastes are 4-space indented code blocks. File contents and scripts the
  reader saves are fenced with a language tag (`bash`, `ini`, `apache`, `json`). Keep
  commands runnable and ordered (add PPA/key, then `apt update`, then install).

## Documentation style

- Do not use em or en dashes as sentence punctuation in `README.md` or other docs. Rephrase
  with periods, commas, or parentheses. Hyphens in compound words and command flags are fine.
- Keep the existing voice: concise imperative instructions with a one-line "why" only when the
  step is non-obvious.

## When config files and the guide disagree

A file under `os/` and the README prose that references it must stay consistent. If you change
a config file, update the corresponding README step (and vice versa).

Most `os/` files are no longer referenced by this branch's README, for example the nginx
configs, the autostart entries, the compiz profile, and `os/home/scripts/deploy.sh` and
`php-fpm-cli.sh`. Grep the README for a file's name before treating it as live. Unreferenced
files carry stale release details (`php-fpm-cli.sh` defaults to `php7.0-fpm.sock` while its
help text says `php5-fpm.sock`), so check the version against the branch before reusing one.

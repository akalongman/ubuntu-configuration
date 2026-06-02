# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal, hand-maintained Ubuntu Desktop configuration guide. It is documentation plus
companion config files, not an application. There is no build, test, lint, or package step.
The primary deliverable is `README.md`: a long (~2,900 line) step-by-step walkthrough for
setting up a fresh Ubuntu LTS install (system tweaks, package installs, dev tooling, GUI
fixes). Everything else in the repo exists to support that guide.

## Branches are release channels, not features

Each Ubuntu LTS release lives on its own long-lived branch: `16.04`, `18.04`, `20.04`,
`24.04`, plus the older `15.10` and `master`. A branch's `README.md` is tailored to that
release (the first line names the version, e.g. "Configuration of Ubuntu 24.04 LTS").

- GitHub's default branch is `16.04` (`origin/HEAD → 16.04`); active work currently happens
  on `24.04`.
- Version-specific changes (a package that moved PPAs, a command that changed between
  releases) belong on that version's branch only. Do not assume a fix applies across all
  branches. Confirm which Ubuntu version a change targets before editing.
- Cross-version improvements (a new tool worth documenting everywhere) may need cherry-picking
  to multiple branches; mention this rather than silently editing one.

## Repository layout

- `README.md` — the guide. Edits here are the main work.
- `os/` — config files laid out by their **destination path on the system**. Drop the `os/`
  prefix to get the real target: `os/etc/profile.d/ps.sh` → `/etc/profile.d/ps.sh`,
  `os/home/.bashrc` → `~/.bashrc`. The README links to these files and tells the reader where
  to copy them, so the directory structure is load-bearing — keep it accurate.
- `os/home/scripts/` — helper scripts referenced by the guide:
  - `deploy.sh` — Capistrano-style release deploy (clone → versioned dir → symlink `current`
    → restart supervisor → reset OPcache). Run as `deploy.sh <project-folder> <repo-url>`.
  - `php-fpm-cli.sh` — runs arbitrary PHP through a PHP-FPM socket via `cgi-fcgi`
    (`php-fpm-cli.sh -r 'code'`), used to reset OPcache after deploy.
- `files/` — binary assets the guide links to (e.g. emulator BIOS). Linked with `?raw=1`.
- `fonts/` — font files plus install notes; the guide copies these into `/usr/share/fonts/...`.
- `notes/` — standalone how-to notes not wired into the README's table of contents.

## Editing README.md

- It opens with a hand-maintained **Table of Contents** built from in-page anchor links
  (`[Section](#section)`). When you add, remove, or rename a heading, update the matching TOC
  entry and verify the anchor slug (GitHub lowercases, strips punctuation, and turns spaces
  into hyphens). A renamed heading silently breaks its TOC link.
- Links to repo files are **relative GitHub paths** (`os/etc/...`, `files/...?raw=1`,
  `tree/20.04` to point at another version's branch). Keep them relative; don't rewrite to
  absolute URLs.
- The guide is organized top-level by intent: `Optional Configurations` → `Installation
  Packages` (System Tools / Other Tools / Development / Gaming) → `Customizations` →
  `Ubuntu Fixes` → `GUI` → `Virtual Machine Related` → `Synchronize Configurations`. Place new
  content under the section that matches reader intent rather than appending to the end.
- Commands are shown as indented code blocks the reader copy-pastes. Keep them runnable and
  ordered (add PPA/key, then `apt update`, then install).

## Documentation style (matches the user's global rules)

- Do not use dashes (— or -) as sentence punctuation in `README.md` or other docs. Rephrase
  with periods, commas, or parentheses.
- Keep the existing voice: concise imperative instructions with a one-line "why" only when the
  step is non-obvious.

## When config files and the guide disagree

A file under `os/` and the README prose that references it must stay consistent. If you change
a config file, update the corresponding README step (and vice versa). Note that some committed
configs carry release-specific details (e.g. `php-fpm-cli.sh` defaults to a `php7.0-fpm.sock`
path); verify the version matches the branch you're on before treating it as current.

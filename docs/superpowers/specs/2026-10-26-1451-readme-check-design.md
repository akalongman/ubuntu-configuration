# README check

Date: 2026-10-26. Status: approved and implemented.

## Intent

`README.md` is what this repository ships, and its table of contents and repo links are
maintained by hand. Edits break them silently. On 2026-10-26 the `24.04` README had a TOC
entry fused onto the previous line (which moved the `SSH` subtree under the wrong parent),
a TOC target without its `#`, five headings missing from the TOC, and four release links
that returned 404 on GitHub. A check that runs on every push to `24.04` reports such
mistakes on the line that caused them, and the same command runs locally before a commit.

## Goals

- Catch the mistakes a README edit can make in its own TOC and links (see Checks).
- Give the same result locally and in CI from one command.
- Point at the exact README line, in the terminal and as a GitHub annotation.

## Non-goals

- External URLs (46 markdown links plus download URLs inside commands).
- Other release branches. Their READMEs fail these checks today and stay as they are.
- Generating or rewriting the TOC. 36 entries carry hand-written notes after the link and
  11 use labels that differ from the heading text.
- Markdown or prose style, and files other than `README.md`.
- Modeling the anchor of a setext heading whose text spans several lines (it is reported
  instead).

## Anti-goals

- A failed run caused by anything other than the pushed commit (network, rate limits).
- A passing run while GitHub renders a broken link. Where the check cannot be sure, it
  fails with a message that says so.

## Known limits

These inputs pass while GitHub builds a different anchor, against the second anti-goal.
They were accepted on 2026-10-27 as too rare to model; none occurs in the README.

- A `--` line inside setext heading text (`Intro.`, blank, `--`, `foo`, `---` is one H2,
  `#--foo`, on GitHub): the checker starts the heading at `foo`, so a TOC entry `#foo`
  passes.
- Non-ASCII whitespace and long ordered markers in setext heading text: a no-break space
  after a list marker (`*\xa0foo`), an ordered marker longer than nine digits, or a line of
  only no-break spaces ends the checker's paragraph early, so an anchor built from the last
  lines alone passes.

Comparing the TOC against the anchor ids GitHub itself renders (`gh api markdown` in
`markdown` mode emits them) would close this whole class; it was not adopted.

## Constraints

- Python standard library only. No package files are added to the repository.
- The workflow exists only on `24.04`, so only that branch is checked.
- `24.04` requires no status check and receives direct pushes, so the check reports after
  the README is published. It cannot block a push.

## Approaches

1. **Own script plus workflow (picked).** One script runs every check, locally and in CI,
   with nothing to install or pin beyond the checkout action. The cost is owning GitHub's
   anchor rules; the README's headings are plain text, and all 196 TOC links that work on
   GitHub also resolve under the prototype's rules.
2. **Off-the-shelf link checker plus a smaller script.** remark-validate-links 13.1.0
   (which uses `github-slugger`) or lychee 0.24.2 (`--offline --include-fragments`) checks
   anchors and local files with GitHub-exact rules. Neither checks TOC completeness, so the
   script is still needed, and CI gains a Node or Rust install for a repo with no package
   files.
3. **TOC generator (dropped).** doctoc 2.5.0 rebuilds the TOC from the headings and would
   erase the hand-written notes and labels.

## Decided

By the owner:

- Approach 1.
- Runs as a GitHub Action, on `24.04` only.
- Only problems a README edit can cause. No external links.

Calls made in design, for review:

- **Checks.**
  1. *The TOC mirrors the headings.* The TOC lists every heading after the TOC section, in
     document order, each linking to that heading's anchor and indented four spaces per
     level below H1. Labels and trailing notes are free text and are not compared. This
     one rule covers the three TOC checks first discussed (target resolves, every heading
     listed, one item per line) and also catches misordered or misnested entries. Today's
     README passes it: 195 entries, 195 headings, 0 mismatches.
  2. *In-page links resolve.* Every `(#...)` link anywhere in the README, such as
     "Back to top", names an existing heading anchor.
  3. *Repo links resolve.* Every relative link names a file or directory that exists on the
     branch, after stripping `?...` and `#...`.
  4. *No branch-relative links.* A relative link starting with `tree/` or `blob/` fails, and
     the message gives the absolute `https://github.com/akalongman/ubuntu-configuration/...`
     form.
  - *Hardening after the final review.* Repo links resolve against the README's directory,
    a leading `/` names the repository root as on GitHub, and a target outside it fails.
    A heading after the TOC that skips a level (H2 to H4) fails at the heading, and its TOC
    indentation is not checked. Links in indented code blocks (4 spaces or a tab after a
    blank line, outside a list) are skipped. A paragraph line underlined with `=` or `-` is
    a setext heading; a heading inside a list or quote fails with a "check it by hand"
    message. A setext heading whose text spans several lines is reported for a manual
    anchor check, and a lone HTML tag line counts as a block start only under GFM's
    HTML-block rules. A TOC line that looks like a list item but is not a space-indented
    `- [label](#anchor)` item fails at its line. Reference definitions and HTML `href` and
    `src` attributes are checked like inline links, and code spans are skipped. An empty
    `(#)` link fails, and a target with any URI scheme is external. Links in a TOC line's
    trailing note are checked.
- **Anchor rules.** Lowercase, drop every character except letters, digits, `_`, `-` and
  space, turn each space into `-`, and suffix repeats with `-1`, `-2` in document order.
  Lines inside fenced code (`` ``` `` or `~~~`) are never headings or links.
- **Interface.** `bin/check-readme`, executable, checks `README.md` at the repository root
  by default and accepts a path. It prints `README.md:<line>: <message>` per problem, or
  `::error file=README.md,line=<line>::<message>` when `GITHUB_ACTIONS=true`. Exit status 0
  when clean, 1 on problems, 2 when the file has no `# Table of Contents` section.
- **Workflow.** `.github/workflows/readme.yml`, on push and pull request to `24.04`, with no
  path filter: it runs in seconds, and deleting a linked file outside the README must still
  trigger it. The checkout action is pinned to a full commit SHA. The runner's system
  `python3` runs the script.
- **Docs.** CLAUDE.md drops "there is no build, test, lint, or package step", names the
  command, and lists `bin/` and `.github/` in the layout.

## Left to the builder

- Report a TOC divergence as specific missing, extra or misplaced entries. One missing entry
  must not make every later entry fail.
- Headings with inline markup (none today): GitHub builds the anchor from the rendered text.
  Either strip the markup the same way or fail with a clear message, never pass silently.
- Choose the runner image: the newest Ubuntu LTS image GitHub offers as generally available,
  and keep the script to syntax that image's `python3` supports.
- Prove the check on known-bad input: the pre-fix README (`git show feb65f3^:README.md`)
  must fail with the problems listed under Intent.
- Message wording.

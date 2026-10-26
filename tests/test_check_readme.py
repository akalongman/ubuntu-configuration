"""Tests for bin/check-readme, run as a subprocess against temporary READMEs."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / 'bin' / 'check-readme'

BASE = (
    '# Guide\n'                       # 1
    '\n'                              # 2
    '# Table of Contents\n'           # 3
    '- [Alpha](#alpha)\n'             # 4
    '    - [Beta Two](#beta-two)\n'   # 5
    '- [Gamma](#gamma)\n'             # 6
    '\n'                              # 7
    '# Alpha\n'                       # 8
    '\n'                              # 9
    '## Beta Two\n'                   # 10
    '\n'                              # 11
    '# Gamma\n'                       # 12
)


def environment(github=False):
    """os.environ without GITHUB_ACTIONS, or with it set to 'true' when github is set."""
    env = {key: value for key, value in os.environ.items() if key != 'GITHUB_ACTIONS'}
    if github:
        env['GITHUB_ACTIONS'] = 'true'
    return env


def execute(command, cwd, github=False):
    """Run a command; returns (exit, stdout lines, stderr)."""
    result = subprocess.run(
        command, cwd=cwd, env=environment(github), capture_output=True, text=True, encoding='utf-8'
    )
    return result.returncode, result.stdout.splitlines(), result.stderr


def run(readme, files=(), github=False, crlf=False, name='README.md', args=None, flags=()):
    """Run the script on a README in a temp repo dir; returns (exit, stdout lines, stderr).

    The repo dir sits inside the temp dir, so `files` may name a path just outside it
    (`../outside.md`). `args` defaults to the README's name; `flags` go to the interpreter.
    """
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / 'repo'
        root.mkdir()
        text = readme.replace('\n', '\r\n') if crlf else readme
        (root / name).write_bytes(text.encode('utf-8'))
        for file in files:
            path = root / file
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        args = (name,) if args is None else args
        return execute([sys.executable, *flags, SCRIPT, *args], root, github)


def doc(entries):
    """entries: (level, heading text, anchor); the first is level 1. TOC mirrors the headings."""
    toc = [' ' * 4 * (lvl - 1) + f'- [{text}](#{a})' for lvl, text, a in entries]
    body = ['#' * lvl + ' ' + text for lvl, text, _ in entries]
    return '\n'.join(['# Guide', '', '# Table of Contents', *toc, '', *body, ''])


class CheckTestCase(unittest.TestCase):
    """Assertion helpers shared by the test classes; holds no tests itself."""

    def assertClean(self, readme, **kwargs):
        self.assertEqual(run(readme, **kwargs), (0, [], ''))

    def assertProblems(self, readme, expected, **kwargs):
        self.assertEqual(run(readme, **kwargs), (1, expected, ''))


class TocTest(CheckTestCase):

    def test_clean_readme_passes(self):
        self.assertEqual(run(BASE), (0, [], ''))

    def test_missing_toc_section_exits_2(self):
        code, out, err = run('# Guide\n\n# Alpha\n')
        self.assertEqual(code, 2)
        self.assertEqual(out, [])
        self.assertIn("README.md: no '# Table of Contents' section", err)

    def test_unreadable_file_exits_2(self):
        code, out, err = run(BASE, args=('MISSING.md',))
        self.assertEqual(code, 2)
        self.assertEqual(out, [])
        self.assertIn('MISSING.md: cannot read', err)

    def test_heading_missing_from_toc(self):
        self.assertProblems(
            BASE + '\n## Delta\n',
            ["README.md:14: heading 'Delta' (#delta) has no TOC entry"],
        )

    def test_toc_entry_without_heading(self):
        readme = BASE.replace('- [Gamma](#gamma)\n', '- [Gamma](#gamma)\n- [Zeta](#zeta)\n')
        self.assertProblems(readme, ['README.md:7: TOC entry #zeta matches no heading'])

    def test_toc_entry_out_of_order(self):
        readme = BASE.replace(
            '- [Alpha](#alpha)\n    - [Beta Two](#beta-two)\n- [Gamma](#gamma)\n',
            '- [Gamma](#gamma)\n- [Alpha](#alpha)\n    - [Beta Two](#beta-two)\n',
        )
        self.assertProblems(readme, ['README.md:4: TOC entry #gamma is out of order'])

    def test_toc_wrong_indentation(self):
        readme = BASE.replace('    - [Beta Two](#beta-two)\n', '- [Beta Two](#beta-two)\n')
        self.assertProblems(
            readme,
            ['README.md:5: TOC entry #beta-two is indented 0 spaces, expected 4 (H2)'],
        )

    def test_two_entries_on_one_line(self):
        readme = BASE.replace(
            '- [Alpha](#alpha)\n    - [Beta Two](#beta-two)\n',
            '- [Alpha](#alpha)    - [Beta Two](#beta-two)\n',
        )
        self.assertProblems(
            readme,
            ['README.md:4: TOC line holds 2 entries; put each on its own line'],
        )

    def test_toc_target_without_hash(self):
        readme = BASE.replace('(#beta-two)', '(beta-two)')
        self.assertProblems(
            readme,
            ["README.md:5: TOC entry links to 'beta-two'; TOC links must start with '#'"],
        )

    def test_labels_and_notes_are_free_text(self):
        readme = BASE.replace('- [Alpha](#alpha)\n', '- [Custom](#alpha) (a note)\n')
        self.assertClean(readme)

    def test_anchor_rules(self):
        self.assertClean(doc([
            (1, 'Alpha', 'alpha'),
            (2, 'Apache: Enable php-mcrypt & mod_rewrite', 'apache-enable-php-mcrypt--mod_rewrite'),
            (2, 'Update BIOS on Laptop/PC', 'update-bios-on-laptoppc'),
            (2, 'Install `foo-bar`', 'install-foo-bar'),
            (2, 'ქართული კლავიატურა', 'ქართული-კლავიატურა'),
            (2, 'Public Key    ', 'public-key'),
            (2, 'Closing ##', 'closing'),
            (2, '.ssh Folder Permissions', 'ssh-folder-permissions'),
        ]))

    def test_duplicate_headings_get_suffixes(self):
        self.assertClean(doc([
            (1, 'Alpha', 'alpha'),
            (2, 'Setup', 'setup'),
            (1, 'Beta', 'beta'),
            (2, 'Setup', 'setup-1'),
        ]))

    def test_fenced_hash_lines_are_not_headings(self):
        self.assertClean(BASE + '\n```bash\n# comment\n```    \n\n~~~\n```\n# inner\n~~~\n')

    def test_unclosed_fence_runs_to_the_end(self):
        # As on GitHub, everything after an unclosed fence is code.
        self.assertProblems(
            BASE.replace('# Gamma\n', '```\n# Gamma\n'),
            ['README.md:6: TOC entry #gamma matches no heading'],
        )

    def test_shorter_fence_does_not_close_a_longer_one(self):
        self.assertClean(BASE + '\n````\n```\n## Delta\n````\n')

    def test_default_path_is_the_repository_readme(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'bin').mkdir()
            shutil.copy(SCRIPT, root / 'bin' / 'check-readme')
            (root / 'README.md').write_text(BASE + '\n## Delta\n', encoding='utf-8')
            (root / 'elsewhere').mkdir()
            self.assertEqual(
                execute([sys.executable, root / 'bin' / 'check-readme'], root / 'elsewhere'),
                (1, ["README.md:14: heading 'Delta' (#delta) has no TOC entry"], ''),
            )

    def test_heading_markup_fails(self):
        cases = [
            ('## Beta _Two_\n',
             "README.md:10: heading 'Beta _Two_' contains markup whose anchor is not modeled;"
             " check it by hand"),
            ('## Beta [Two](https://example.com)\n',
             "README.md:10: heading 'Beta [Two](https://example.com)' contains markup whose"
             " anchor is not modeled; check it by hand"),
        ]
        for heading, message in cases:
            with self.subTest(heading=heading):
                code, out, _ = run(BASE.replace('## Beta Two\n', heading))
                self.assertEqual(code, 1)
                self.assertIn(message, out)

    def test_github_annotations(self):
        self.assertProblems(
            BASE + '\n## Delta\n',
            ["::error file=README.md,line=14::heading 'Delta' (#delta) has no TOC entry"],
            github=True,
        )

    def test_annotation_escapes_percent(self):
        self.assertProblems(
            BASE + '\n## 100% Done\n',
            ["::error file=README.md,line=14::heading '100%25 Done' (#100-done) has no TOC entry"],
            github=True,
        )

    def test_annotation_escapes_file_property(self):
        self.assertProblems(
            BASE + '\n## Delta\n',
            ["::error file=a%2Cb.md,line=14::heading 'Delta' (#delta) has no TOC entry"],
            github=True,
            name='a,b.md',
        )

    def test_crlf_readme(self):
        self.assertClean(BASE, crlf=True)

    def test_byte_order_mark_is_not_part_of_line_1(self):
        self.assertClean('\ufeff' + BASE + '\n[(Back to top)](#guide)\n')

    def test_runs_without_docstrings(self):
        self.assertClean(BASE, flags=('-OO',))

    def test_script_is_executable(self):
        self.assertTrue(os.access(SCRIPT, os.X_OK))


class LinkTest(CheckTestCase):

    def test_in_page_link_to_missing_heading(self):
        self.assertProblems(
            BASE + '\n[(Back to top)](#table-of-content)\n',
            ['README.md:14: link to #table-of-content matches no heading'],
        )

    def test_back_to_top_resolves(self):
        self.assertClean(BASE + '\n[(Back to top)](#table-of-contents)\n')

    def test_repo_link_missing_file(self):
        self.assertProblems(
            BASE + '\nCopy [ps.sh](os/etc/profile.d/ps.sh).\n',
            ["README.md:14: link target 'os/etc/profile.d/ps.sh' does not exist"],
        )

    def test_repo_link_existing_file(self):
        self.assertClean(
            BASE + '\nCopy [ps.sh](os/etc/profile.d/ps.sh).\n',
            files=('os/etc/profile.d/ps.sh',),
        )

    def test_repo_link_query_title_escape_image(self):
        self.assertClean(
            BASE + '\n[b](files/bios.bin?raw=1) [n](notes/a%20b.md "Title")'
                   ' ![i](files/bios.bin)\n',
            files=('files/bios.bin', 'notes/a b.md'),
        )

    def test_root_relative_link_resolves_in_the_repository(self):
        self.assertClean(BASE + '\n[x](/os/x)\n', files=('os/x',))

    def test_root_relative_link_missing_file(self):
        self.assertProblems(
            BASE + '\n[x](/os/missing)\n',
            ["README.md:14: link target '/os/missing' does not exist"],
        )

    def test_link_outside_the_repository(self):
        self.assertProblems(
            BASE + '\n[o](../outside.md)\n',
            ["README.md:14: link target '../outside.md' points outside the repository"],
            files=('../outside.md',),
        )

    def test_repo_link_fragment_is_stripped(self):
        self.assertClean(BASE + '\n[n](notes/a.md#section)\n', files=('notes/a.md',))

    def test_branch_relative_link(self):
        self.assertProblems(
            BASE + '\n[20.04](tree/20.04)\n',
            ["README.md:14: relative branch link 'tree/20.04' 404s on GitHub;"
             ' use https://github.com/akalongman/ubuntu-configuration/tree/20.04'],
        )

    def test_branch_relative_blob_link(self):
        self.assertProblems(
            BASE + '\n[r](blob/24.04/README.md)\n',
            ["README.md:14: relative branch link 'blob/24.04/README.md' 404s on GitHub;"
             ' use https://github.com/akalongman/ubuntu-configuration/blob/24.04/README.md'],
        )

    def test_external_links_ignored(self):
        self.assertClean(
            BASE + '\n[x](https://example.invalid/missing) [h](http://example.invalid)'
                   ' [m](mailto:a@example.com)\n'
        )

    def test_links_in_fenced_code_ignored(self):
        self.assertClean(BASE + '\n```\n[x](os/missing)\n```\n')

    def test_links_in_indented_code_ignored(self):
        self.assertClean(BASE + '\nRun this:\n\n    sed -i "s/[x](missing)/y/" file\n')

    def test_indented_code_block_extent(self):
        # The block runs over blank lines and lines indented 4 spaces or a tab, and ends at
        # the first non-blank line indented less.
        self.assertProblems(
            BASE + '\nRun this:\n\n    [a](missing)\n\n\t[b](missing)\nSee [c](os/missing)\n',
            ["README.md:19: link target 'os/missing' does not exist"],
        )

    def test_indented_list_item_after_blank_is_not_code(self):
        self.assertProblems(
            BASE + '\n- item\n\n    - [x](os/missing)\n',
            ["README.md:16: link target 'os/missing' does not exist"],
        )

    def test_indented_line_under_prose_is_not_code(self):
        self.assertProblems(
            BASE + '\n**- Packages:**\n    - [x](os/missing)\n',
            ["README.md:15: link target 'os/missing' does not exist"],
        )

    def test_reference_definition_is_checked(self):
        self.assertProblems(
            BASE + '\n[ps]: os/missing "Title"\n',
            ["README.md:14: link target 'os/missing' does not exist"],
        )

    def test_html_href_and_src_are_checked(self):
        self.assertProblems(
            BASE + '\n<a href="os/missing">x</a>\n\n<img src=\'files/missing.png\'>\n',
            ["README.md:14: link target 'os/missing' does not exist",
             "README.md:16: link target 'files/missing.png' does not exist"],
        )

    def test_link_in_code_span_ignored(self):
        self.assertClean(BASE + '\nRun `[x](missing)` as is.\n')

    def test_link_between_code_spans_checked(self):
        for line in (
            'Run `a` then [x](os/missing) then `b`.',
            'Run ``a ` b`` then [x](os/missing) then `c`.',  # runs pair by length
            'A lone ` then [x](os/missing).',  # a run without a partner is literal
        ):
            with self.subTest(line=line):
                self.assertProblems(
                    BASE + '\n' + line + '\n',
                    ["README.md:14: link target 'os/missing' does not exist"],
                )

    def test_empty_in_page_link(self):
        self.assertProblems(
            BASE + '\n[top](#)\n',
            ["README.md:14: empty in-page link '#'; name a heading anchor"],
        )

    def test_any_uri_scheme_is_external(self):
        self.assertClean(
            BASE + '\n[f](ftp://example.invalid/x) [t](tel:+995322000000)'
                   ' [H](HTTPS://example.invalid/x)\n'
        )

    def test_link_in_toc_note_is_checked(self):
        self.assertProblems(
            BASE.replace('- [Alpha](#alpha)\n', '- [Alpha](#alpha) (see [cfg](os/missing))\n'),
            ["README.md:4: link target 'os/missing' does not exist"],
        )


if __name__ == '__main__':
    unittest.main()

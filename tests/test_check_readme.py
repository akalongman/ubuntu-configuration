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

    def test_heading_skips_a_level(self):
        # Its TOC entry's indentation is not checked, whichever form the TOC uses.
        entries = [(1, 'Alpha', 'alpha'), (2, 'Beta', 'beta'), (4, 'Delta', 'delta')]
        for indent in (12, 8):
            with self.subTest(indent=indent):
                readme = doc(entries).replace(' ' * 12 + '- [Delta]', ' ' * indent + '- [Delta]')
                self.assertProblems(readme, ["README.md:10: heading 'Delta' skips from H2 to H4"])

    def test_stale_toc_anchor(self):
        self.assertProblems(
            BASE.replace('## Beta Two\n', '## Beta Three\n'),
            ["README.md:5: TOC entry #beta-two does not match heading 'Beta Three'"
             ' (#beta-three, line 10)'],
        )

    def test_unequal_replace_keeps_unlinked_messages(self):
        self.assertProblems(
            BASE.replace('## Beta Two\n', '## Beta Three\n\n## Beta Four\n'),
            ['README.md:5: TOC entry #beta-two matches no heading',
             "README.md:10: heading 'Beta Three' (#beta-three) has no TOC entry",
             "README.md:12: heading 'Beta Four' (#beta-four) has no TOC entry"],
        )

    def test_stale_anchor_pairs_only_with_an_unlisted_heading(self):
        # #zeta faces Beta Two, but Beta Two is listed further down: two separate mistakes.
        readme = BASE.replace(
            '- [Alpha](#alpha)\n    - [Beta Two](#beta-two)\n- [Gamma](#gamma)\n',
            '- [Alpha](#alpha)\n    - [Zeta](#zeta)\n- [Gamma](#gamma)\n    - [B](#beta-two)\n',
        )
        self.assertProblems(
            readme,
            ['README.md:5: TOC entry #zeta matches no heading',
             'README.md:7: TOC entry #beta-two is out of order'],
        )

    def test_toc_entry_listed_twice(self):
        readme = BASE.replace('- [Gamma](#gamma)\n', '- [Gamma](#gamma)\n- [Again](#alpha)\n')
        self.assertProblems(
            readme, ['README.md:7: TOC entry #alpha is listed twice (first at line 4)']
        )

    def test_unparsable_toc_line(self):
        message = ("TOC line is not a '- [label](#anchor)' item;"
                   " use '- ' bullets and space indentation")
        cases = [
            ('- [Gamma](#gamma)\n', '* [Gamma](#gamma)\n', 6),
            ('    - [Beta Two](#beta-two)\n', '\t- [Beta Two](#beta-two)\n', 5),
        ]
        for old, new, line in cases:
            with self.subTest(line=new):
                self.assertProblems(BASE.replace(old, new), [f'README.md:{line}: {message}'])

    def test_unparsable_toc_line_stand_in_is_not_link_checked(self):
        # The TOC check reports the stand-in's stale anchor; the link scan does not repeat it.
        self.assertProblems(
            BASE.replace('- [Gamma](#gamma)\n', '* [Gamma](#gama)\n'),
            ["README.md:6: TOC line is not a '- [label](#anchor)' item;"
             " use '- ' bullets and space indentation",
             "README.md:6: TOC entry #gama does not match heading 'Gamma' (#gamma, line 12)"],
        )

    def test_unparsable_toc_line_without_a_link(self):
        # Nothing on the line names the heading, so the heading is reported too.
        self.assertProblems(
            BASE.replace('- [Gamma](#gamma)\n', '- Gamma\n'),
            ["README.md:6: TOC line is not a '- [label](#anchor)' item;"
             " use '- ' bullets and space indentation",
             "README.md:12: heading 'Gamma' (#gamma) has no TOC entry"],
        )

    def test_toc_section_non_list_lines_are_silent(self):
        self.assertClean(BASE.replace(
            '- [Gamma](#gamma)\n',
            '- [Gamma](#gamma)\n\n***\n\n[(Back to top)](#table-of-contents)\n',
        ))

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
        # Each TOC entry names the anchor the plain-text rule gives, so the TOC check passes
        # and the markup message is the only one.
        cases = [
            ('Beta _Two_', 'beta-_two_'),
            ('Beta [Two](https://example.com)', 'beta-twohttpsexamplecom'),
            ('Beta [Two][ref]', 'beta-tworef'),
            ('Beta &amp; Two', 'beta-amp-two'),
            ('Beta <kbd>Two</kbd>', 'beta-kbdtwokbd'),
        ]
        for text, slug in cases:
            with self.subTest(heading=text):
                readme = BASE.replace('(#beta-two)', f'(#{slug})')
                self.assertProblems(
                    readme.replace('## Beta Two\n', f'## {text}\n'),
                    [f"README.md:10: heading '{text}' contains markup whose anchor is not"
                     ' modeled; check it by hand'],
                )

    def test_setext_headings_pass_when_listed(self):
        readme = BASE.replace('## Beta Two\n', 'Beta Two\n--------\n')
        self.assertClean(readme.replace('# Gamma\n', 'Gamma\n=====\n'))

    def test_setext_h1_ends_the_toc_section(self):
        self.assertClean('# Guide\n\n# Table of Contents\n- [Alpha](#alpha)\n\nAlpha\n=====\n')

    def test_setext_heading_missing_from_toc(self):
        # A second `---` under the underline is a thematic break, not another heading.
        for underline in ('=====', '-', '---\n---'):
            with self.subTest(underline=underline):
                self.assertProblems(
                    BASE + f'\nDelta\n{underline}\n',
                    ["README.md:14: heading 'Delta' (#delta) has no TOC entry"],
                )

    def test_multi_line_setext_heading_is_reported(self):
        # GitHub's anchor drops the line break between the lines, and the TOC entry names
        # that anchor, so the span message is the only one.
        readme = BASE.replace(
            '- [Gamma](#gamma)\n', '- [Gamma](#gamma)\n    - [First](#first-linesecond-line)\n'
        )
        self.assertProblems(
            readme + '\nFirst line\nsecond line\n---\n',
            ['README.md:15: setext heading spans 2 lines; check its anchor by hand'],
        )

    def test_multi_line_setext_heading_text_joins_its_lines(self):
        # Messages show the stripped lines joined by one space, at the paragraph's first line.
        self.assertProblems(
            BASE + '\nFirst line\n  second line\n---\n',
            ['README.md:14: setext heading spans 2 lines; check its anchor by hand',
             "README.md:14: heading 'First line second line' (#first-linesecond-line)"
             ' has no TOC entry'],
        )

    def test_setext_text_starts_after_a_fence_heading_or_underline(self):
        # A closing fence, an ATX heading and an underline are not paragraph text, so each
        # heading here has one line.
        cases = [
            ('\n```\ncode\n```\nDelta\n---\n',
             ["README.md:17: heading 'Delta' (#delta) has no TOC entry"]),
            ('Delta\n---\n', ["README.md:13: heading 'Delta' (#delta) has no TOC entry"]),
            ('\nDelta\n---\nEpsilon\n---\n',
             ["README.md:14: heading 'Delta' (#delta) has no TOC entry",
              "README.md:16: heading 'Epsilon' (#epsilon) has no TOC entry"]),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertProblems(BASE + text, expected)

    def test_thematic_break_after_blank_line_is_not_a_heading(self):
        self.assertClean(BASE + '\nSome prose.\n\n---\n')

    def test_underline_under_list_item_or_quote_is_not_a_heading(self):
        for text in ('- item', '> quote'):
            with self.subTest(text=text):
                self.assertClean(BASE + f'\n{text}\n---\n')

    def test_underline_under_a_lone_html_tag_is_not_a_heading(self):
        # A line holding one HTML tag and nothing else opens an HTML block on GitHub.
        for text in ('<br>', '</details>', '   <div class="note" hidden>', '<br />  '):
            with self.subTest(text=text):
                self.assertClean(BASE + f'\n{text}\n---\n')

    def test_underline_under_inline_html_or_table_line_is_a_heading(self):
        # Inline HTML with text, and a table row whose delimiter row is missing, are
        # paragraph text, so GitHub renders them as an H2.
        cases = [
            ('| a | b |', ["README.md:14: heading '| a | b |' (#-a--b-) has no TOC entry"]),
            ('<kbd>Ctrl</kbd> + C',
             ["README.md:14: heading '<kbd>Ctrl</kbd> + C' contains markup whose anchor is not"
              ' modeled; check it by hand',
              "README.md:14: heading '<kbd>Ctrl</kbd> + C' (#kbdctrlkbd--c) has no TOC entry"]),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertProblems(BASE + f'\n{text}\n---\n', expected)

    def test_heading_in_list_or_quote_fails(self):
        for line in ('> ## Quoted', '> > # Deeper', '- ## Listed', '1) ### Numbered'):
            with self.subTest(line=line):
                self.assertProblems(
                    BASE + '\n' + line + '\n',
                    ['README.md:14: heading inside a list or quote is not modeled;'
                     ' check it by hand'],
                )

    def test_nested_heading_shape_in_indented_code_ignored(self):
        self.assertClean(BASE + '\nRun this:\n\n    - # not a heading\n')

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

    def test_indented_fence_keeps_the_list(self):
        # A fence indented under a list item stays in the item, so the 4-space line after it
        # and a blank line is a list paragraph, not code.
        for pad in ('  ', '    '):
            with self.subTest(indent=len(pad)):
                self.assertProblems(
                    BASE + f'\n- item\n\n{pad}```\n{pad}code\n{pad}```\n\n    [cfg](os/missing)\n',
                    ["README.md:20: link target 'os/missing' does not exist"],
                )

    def test_column_0_fence_ends_the_list(self):
        # The prose right after the fence follows no blank line, so only the fence ends the
        # list, and the 4-space block after the blank line is code.
        self.assertClean(BASE + '\n- item\n\n```\ncode\n```\nprose\n\n    [x](os/missing)\n')

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

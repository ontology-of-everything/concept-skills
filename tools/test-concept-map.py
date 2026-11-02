#!/usr/bin/env python3
"""Black-box contracts for the packaged Markdown concept-map CLI."""

from contextlib import contextmanager
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = (ROOT / 'skills/en/concept-design', ROOT / 'skills/zh-CN/concept-design-cn')
START, END = '<!-- concept-map:start -->', '<!-- concept-map:end -->'
IDENTITY = re.compile(r'\b([cis]_[0-9a-f]{12})\b')

CONCEPT = '''# concept {name} [T]
coverage: complete
## purpose
Remember items for a caller.
## state
items: set T, initially empty
## actions
finish [] => [item: T]
  requires true
  ensures returns one item; state is unchanged
check [item: T] => [valid: Bool]
  requires true
  ensures returns validity; state is unchanged
accept [item: T; owner: T] => []
  requires true
  ensures items contains item
## operational principle
after accept, finish can return the item
## queries
_owners [item: T] => [owner: T]
  returns owner bindings without completion
'''
APP = '''# app Demo
include Source [Id]
include Lookup [Id]
include Target [Id]

sync Follow
when { Source/finish: [] => [item: ?item] }
where { Lookup/_owners: [item: ?item] => [owner: ?owner] }
then { Target/accept: [item: ?item; owner: ?owner] }
'''


def put(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    return path


def seed(root, app=APP):
    for name in ('Source', 'Lookup', 'Target'):
        put(root, f'concepts/{name}/CONCEPT.md', CONCEPT.format(name=name))
    put(root, 'apps/main/SYNCS.md', app)


def identities(text, prefix):
    return {value for value in IDENTITY.findall(text) if value.startswith(prefix + '_')}


def graph(text):
    blocks = re.findall(r'```mermaid\s*\n(.*?)```', text, re.S)
    if not blocks:
        raise AssertionError('Markdown result has no Mermaid graph')
    return '\n'.join(blocks)


def edges(text):
    """Read observable graph endpoints, independent of label/layout formatting."""
    result = []
    for line in graph(text).splitlines():
        if '-->' not in line and '-.->' not in line:
            continue
        nodes = IDENTITY.findall(line)
        if len(nodes) >= 2:
            result.append((nodes[0], '-.->' if '-.->' in line else '-->', nodes[-1]))
    return result


def tree_snapshot(root):
    result = {}
    for directory, folders, files in os.walk(root, followlinks=False):
        for name in folders + files:
            path = Path(directory) / name
            if path.is_symlink():
                result[str(path.relative_to(root))] = ('link', os.readlink(path))
            elif path.is_file():
                result[str(path.relative_to(root))] = (
                    hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mtime_ns)
    return result


class MapContract(unittest.TestCase):
    @contextmanager
    def fixture(self, package):
        with tempfile.TemporaryDirectory(prefix='concept-map-') as directory:
            root = Path(directory) / 'My Project'
            root.mkdir()
            yield root, package / 'scripts/concept_map.py'

    def invoke(self, script, root, *arguments):
        result = subprocess.run([sys.executable, str(script), str(root), *map(str, arguments)],
                                text=True, capture_output=True)
        self.assertNotIn('Traceback', result.stderr, result.stderr)
        return result

    def expect(self, result, code):
        self.assertEqual(result.returncode, code, result.stdout + '\n' + result.stderr)
        return result.stdout

    def test_stdout_relations_provenance_and_read_only(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                before = tree_snapshot(root)
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(tree_snapshot(root), before)
                self.assertFalse((root / 'ARCHITECTURE.md').exists())
                self.assertFalse(list(root.rglob('*.json')), 'map must not emit JSON artifacts')
                self.assertEqual(len(identities(output, 'c')), 3)
                self.assertEqual(len(identities(output, 'i')), 3)
                self.assertEqual(len(identities(output, 's')), 1)
                relations = edges(output)
                self.assertEqual(sum(a.startswith('i_') and arrow == '-->' and b.startswith('s_')
                                     for a, arrow, b in relations), 1)
                self.assertEqual(sum(a.startswith('i_') and arrow == '-.->' and b.startswith('s_')
                                     for a, arrow, b in relations), 1)
                self.assertEqual(sum(a.startswith('s_') and arrow == '-->' and b.startswith('i_')
                                     for a, arrow, b in relations), 1)
                for path, line in [('apps/main/SYNCS.md', n) for n in (2, 3, 4, 6)] + [('concepts/Source/CONCEPT.md', 1)]:
                    self.assertRegex(output, re.escape(path) + r'(?:[^\n]*?)(?::|#L)' + str(line) + r'\b')
                self.assertRegex(output, r'\bId\b', 'instance type bindings remain visible')
                self.assertIn('AND', output)
                for word in ('Source/finish', 'Lookup/_owners', 'Target/accept'):
                    self.assertIn(word, output)

    def test_conjunctive_triggers_and_repeated_invocations(self):
        app = APP.replace('when { Source/finish: [] => [item: ?item] }', '''when {
  Source/finish: [] => [item: ?item]
  Source/check: [item: ?item] => [valid: true]
}''').replace('then { Target/accept: [item: ?item; owner: ?owner] }', '''then {
  Target/accept: [item: ?item; owner: ?owner]
  Target/accept: [item: ?item; owner: ?owner]
}''')
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root, app)
                output = self.expect(self.invoke(script, root), 0)
                relations = edges(output)
                completed = [(a, b) for a, arrow, b in relations if a.startswith('i_') and
                             arrow == '-->' and b.startswith('s_')]
                invoked = [(a, b) for a, arrow, b in relations if a.startswith('s_') and
                           arrow == '-->' and b.startswith('i_')]
                self.assertEqual(len(completed), 2, output)
                self.assertEqual(len(invoked), 2, 'identical calls remain two source occurrences')
                self.assertEqual(invoked[0], invoked[1])
                self.assertEqual(len({b for _, b in completed}), 1, 'AND conditions share one rule')
                self.assertIn('valid: true', output)

    def test_cases_are_visible(self):
        app = APP + APP[APP.index('sync Follow'):].replace('sync Follow', 'sync Refused').replace(
            '=> [item: ?item]', '=> [error: ?error]')
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root, app)
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(len(identities(output, 's')), 2)
                self.assertIn('error: ?error', output)
                self.assertIn('item: ?item', output)

    def test_literals_comments_and_fences_do_not_create_relations(self):
        fake = '''
// sync GhostComment
/*
sync GhostBlock
when { Ghost/act: [] => [] }
then { Ghost/next: [] }
*/
<!--
include Ghost [Id]
sync GhostHtml
-->
```text
# app GhostFence
include Ghost [Id]
sync GhostFence
when { Ghost/act: [] => [] }
then { Ghost/next: [] }
```
'''
        app = APP.replace('item: ?item; owner: ?owner]',
                          'item: "Ghost/act: [] => [] { /* //"; owner: ?owner]') + fake
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root, app)
                source = root / 'concepts/Source/CONCEPT.md'
                source.write_text('<!--\n# concept FalseComment\n-->\n' +
                                  '```text\n# concept FalseFence\n```\n' + source.read_text())
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(len(identities(output, 'c')), 3)
                self.assertEqual(len(identities(output, 'i')), 3)
                self.assertEqual(len(identities(output, 's')), 1)
                self.assertEqual(len(edges(output)), 3)

    def test_public_state_reads_are_dashed_in_compact_and_multiline_forms(self):
        for package in PACKAGES:
            for read in ('Lookup: { ?item owner: ?owner }', 'Lookup: {\n ?item owner: ?owner\n}'):
                with self.subTest(package=package, read=read), self.fixture(package) as (root, script):
                    seed(root, APP.replace('Lookup/_owners: [item: ?item] => [owner: ?owner]', read))
                    output = self.expect(self.invoke(script, root), 0)
                    relations = edges(output)
                    self.assertEqual(sum(arrow == '-.->' for _, arrow, _ in relations), 1)
                    self.assertEqual(sum(a.startswith('i_') and arrow == '-->' and b.startswith('s_')
                                         for a, arrow, b in relations), 1)
                    self.assertIn('owner: ?owner', output)

    def test_opaque_where_strings_remain_partial(self):
        query = 'Lookup/_owners: [item: ?item] => [owner: ?owner]'
        for package in PACKAGES:
            for where in ('"' + query + '"', query + ' "trailing text"'):
                with self.subTest(package=package, where=where), self.fixture(package) as (root, script):
                    seed(root, APP.replace(query, where))
                    before = tree_snapshot(root)
                    output = self.expect(self.invoke(script, root), 3)
                    self.assertIn('partial', output.lower())
                    self.assertEqual(tree_snapshot(root), before)
                    if where.startswith('"'):
                        self.assertFalse(any(arrow == '-.->' for _, arrow, _ in edges(output)),
                                         'literal text must not fabricate a read edge')

    def test_known_invalid_query_fields_do_not_write(self):
        query = 'Lookup/_owners: [item: ?item] => [owner: ?owner]'
        invalid = ('Lookup/_owners: [?item] => [owner: ?owner]',
                   'Lookup/_owners: [item: ?item] => [?owner]',
                   'Lookup/_owners: [item:] => [owner: ?owner]',
                   'Lookup/_owners: [item: ?item] => [owner:]')
        for package in PACKAGES:
            for where in invalid:
                with self.subTest(package=package, where=where), self.fixture(package) as (root, script):
                    seed(root, APP.replace(query, where))
                    output = put(root, 'ARCHITECTURE.md', START + '\nOld map\n' + END + '\n')
                    before = tree_snapshot(root)
                    self.expect(self.invoke(script, root, '--output', output), 1)
                    self.assertEqual(tree_snapshot(root), before)

    def test_same_application_spans_files_without_duplicating_instances(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                put(root, 'apps/other/SYNCS.md', APP.replace('sync Follow', 'sync Another'))
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(len(identities(output, 'c')), 3)
                self.assertEqual(len(identities(output, 'i')), 3)
                self.assertEqual(len(identities(output, 's')), 2)
                put(root, 'apps/third/SYNCS.md', APP.replace('# app Demo', '# app Other'))
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(len(identities(output, 'c')), 3)
                self.assertEqual(len(identities(output, 'i')), 6, 'apps own separate instances')
                self.assertEqual(len(identities(output, 's')), 3, 'same rule name in another app is distinct')

    def test_duplicate_names_and_bindings_are_errors_without_writes(self):
        changes = (
            ('duplicate-rule', 'copies/SYNCS.md', APP),
            ('conflicting-instance-binding', 'copies/SYNCS.md',
             APP.replace('include Source [Id]', 'include Source [OtherId]').replace('sync Follow', 'sync Other')),
        )
        for package in PACKAGES:
            for case, path, text in changes:
                with self.subTest(package=package, case=case), self.fixture(package) as (root, script):
                    seed(root)
                    put(root, path, text)
                    output = put(root, 'ARCHITECTURE.md', 'Keep this document.\n')
                    before = tree_snapshot(root)
                    self.expect(self.invoke(script, root, '--output', output), 1)
                    self.assertEqual(tree_snapshot(root), before)

    def test_homonymous_definitions_stay_distinct_and_references_are_ambiguous(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                first = put(root, 'one/CONCEPT.md', CONCEPT.format(name='Source'))
                second = put(root, 'two/CONCEPT.md', CONCEPT.format(name='Source'))
                output = self.expect(self.invoke(script, root), 0)
                self.assertEqual(len(identities(output, 'c')), 2)
                self.assertIn('one/CONCEPT.md', output)
                self.assertIn('two/CONCEPT.md', output)
                put(root, 'app/SYNCS.md', '# app Demo\ninclude Source [Id]\n' +
                    'sync One\nwhen { Source/finish: [] => [item: ?item] }\n' +
                    'then { Source/accept: [item: ?item; owner: ?item] }\n')
                output = self.expect(self.invoke(script, root), 3)
                self.assertEqual(len(identities(output, 'c')), 2, 'ambiguity must not merge definitions')
                self.assertIn('ambiguous', output.lower())

    def test_identity_survives_reordering_and_unrelated_additions(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                initial = self.expect(self.invoke(script, root), 0)
                put(root, 'apps/main/SYNCS.md', APP.replace(
                    'include Source [Id]\ninclude Lookup [Id]\ninclude Target [Id]',
                    'include Target [Id]\ninclude Source [Id]\ninclude Lookup [Id]'))
                reordered = self.expect(self.invoke(script, root), 0)
                for prefix in ('c', 'i', 's'):
                    self.assertEqual(identities(initial, prefix), identities(reordered, prefix))
                put(root, 'unrelated/CONCEPT.md', CONCEPT.format(name='Unrelated'))
                expanded = self.expect(self.invoke(script, root), 0)
                self.assertTrue(identities(initial, 'c') < identities(expanded, 'c'))
                for prefix in ('i', 's'):
                    self.assertEqual(identities(initial, prefix), identities(expanded, prefix))

    def test_unresolved_and_unknown_are_partial_not_invented_external_contracts(self):
        variants = (
            ('unresolved-include', APP.replace('include Lookup [Id]', 'include Missing [Id]').replace('Lookup/', 'Missing/')),
            ('undeclared-participant', APP.replace('Target/accept:', 'Missing/accept:')),
            ('unknown-where', APP.replace('Lookup/_owners: [item: ?item] => [owner: ?owner]', 'opaque operation')),
        )
        for package in PACKAGES:
            for case, app in variants:
                with self.subTest(package=package, case=case), self.fixture(package) as (root, script):
                    seed(root, app)
                    before = tree_snapshot(root)
                    output = self.expect(self.invoke(script, root), 3)
                    self.assertEqual(tree_snapshot(root), before)
                    self.assertIn('partial', output.lower())
                    if case != 'unknown-where':
                        self.assertIn('Missing', output)
                        self.assertEqual(len(identities(output, 'c')), 3,
                                         'missing definitions must not become invented concepts')

    def test_scope_keeps_direct_boundary_instances_but_not_other_rules(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                put(root, 'apps/outside/SYNCS.md', APP.replace('sync Follow', 'sync UnrelatedRule'))
                put(root, 'apps/main/local/CONCEPT.md', CONCEPT.format(name='LocalUnused'))
                output = self.expect(self.invoke(script, root, '--scope', 'apps/main'), 0)
                self.assertEqual(len(identities(output, 's')), 1)
                self.assertEqual(len(identities(output, 'i')), 3)
                self.assertIn('LocalUnused', output)
                self.assertNotIn('UnrelatedRule', output)
                self.assertIn('outside_scope', output)
                self.assertNotRegex(output, r'\b\d+(?:\.\d+)?\s*%', 'no inferred coverage percentage')

    def test_default_exclusions_custom_exclusions_and_symlinks(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                for folder in ('.git', 'node_modules', '.venv', 'generated', 'drafts'):
                    put(root, folder + '/CONCEPT.md', CONCEPT.format(name='Source'))
                outside = root.parent / 'outside'
                put(outside, 'CONCEPT.md', CONCEPT.format(name='Source'))
                (root / 'linked-directory').symlink_to(outside, target_is_directory=True)
                (root / 'linked').mkdir()
                (root / 'linked/CONCEPT.md').symlink_to(outside / 'CONCEPT.md')
                (root / 'broken').symlink_to(root.parent / 'missing', target_is_directory=True)
                output = self.expect(self.invoke(script, root, '--exclude', 'generated/**', '--exclude', 'drafts/**'), 0)
                self.assertEqual(len(identities(output, 'c')), 3)
                self.assertEqual(len(identities(output, 's')), 1)

    def test_output_region_preserves_manual_notes_and_skips_unchanged_writes(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                output = root / 'ARCHITECTURE.md'
                self.expect(self.invoke(script, root, '--output', output), 0)
                text = output.read_text()
                self.assertEqual(text.count(START), 1)
                self.assertEqual(text.count(END), 1)
                generated = text[text.index(START):text.index(END) + len(END)]
                prefix, suffix = '# Human notes\nExact prefix.\n\n', '\n\nExact suffix.\n'
                output.write_text(prefix + generated + suffix)
                self.expect(self.invoke(script, root, '--output', output), 0)
                self.assertTrue(output.read_text().startswith(prefix))
                self.assertTrue(output.read_text().endswith(suffix))
                os.utime(output, ns=(1_000_000_000, 1_000_000_000))
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output), 0)
                self.assertEqual(tree_snapshot(root), before, 'identical generation must not rewrite mtime')

    def test_nested_output_source_links_resolve_from_the_written_document(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                source = root / 'concepts/Source/CONCEPT.md'
                destination = root / '资料 自有/CONCEPT.md'
                destination.parent.mkdir()
                source.rename(destination)
                output = root / '说明 文档/ARCHITECTURE.md'
                output.parent.mkdir()
                self.expect(self.invoke(script, root, '--output', output), 0)
                found = set()
                for link in re.findall(r'\]\(([^)]+)\)', output.read_text()):
                    parsed = urlsplit(link)
                    if parsed.scheme or not parsed.path:
                        continue
                    target = (output.parent / unquote(parsed.path)).resolve()
                    self.assertTrue(target.is_file(), f'broken local source link: {link}')
                    found.add(target)
                expected = {path.resolve() for name in ('CONCEPT.md', 'SYNCS.md') for path in root.rglob(name)}
                self.assertEqual(found, expected, 'every indexed specification remains reachable')

    def test_invalid_output_encoding_is_an_io_error_without_writes(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                output = root / 'ARCHITECTURE.md'
                output.write_bytes(b'\xff\xfe')
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output), 2)
                self.assertEqual(tree_snapshot(root), before)

    def test_invalid_markers_do_not_overwrite_existing_documents(self):
        invalid = ('Human file without markers.\n', START + '\nmissing end\n',
                   END + '\n' + START + '\n', START + '\n' + START + '\n' + END + '\n',
                   START + '\n' + END + '\n' + START + '\n' + END + '\n')
        for package in PACKAGES:
            for index, content in enumerate(invalid):
                with self.subTest(package=package, case=index), self.fixture(package) as (root, script):
                    seed(root)
                    output = put(root, 'ARCHITECTURE.md', content)
                    before = tree_snapshot(root)
                    self.expect(self.invoke(script, root, '--output', output), 1)
                    self.assertEqual(tree_snapshot(root), before)

    def test_check_is_read_only_and_reports_difference(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                output = root / 'ARCHITECTURE.md'
                self.expect(self.invoke(script, root, '--output', output, '--check'), 1)
                self.assertFalse(output.exists())
                self.expect(self.invoke(script, root, '--output', output), 0)
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output, '--check'), 0)
                self.assertEqual(tree_snapshot(root), before)
                put(root, 'unrelated/CONCEPT.md', CONCEPT.format(name='Another'))
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output, '--check'), 1)
                self.assertEqual(tree_snapshot(root), before)

    def test_check_partial_consistency_and_difference_have_distinct_exits(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root, APP.replace('include Lookup [Id]', 'include Missing [Id]').replace('Lookup/', 'Missing/'))
                output = root / 'ARCHITECTURE.md'
                self.expect(self.invoke(script, root, '--output', output), 3)
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output, '--check'), 3)
                self.assertEqual(tree_snapshot(root), before)
                put(root, 'more/CONCEPT.md', CONCEPT.format(name='Another'))
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output, '--check'), 1)
                self.assertEqual(tree_snapshot(root), before)

    def test_no_specs_do_not_replace_a_previous_map_or_human_document(self):
        for package in PACKAGES:
            for text in ('# Notes\n' + START + '\nOld map\n' + END + '\n', '# Human notes without markers\n'):
                with self.subTest(package=package, text=text), self.fixture(package) as (root, script):
                    output = put(root, 'ARCHITECTURE.md', text)
                    before = tree_snapshot(root)
                    self.expect(self.invoke(script, root, '--output', output), 3)
                    self.assertEqual(tree_snapshot(root), before)

    def test_error_priorities_and_output_protection(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root, APP.replace('when { Source/finish: [] => [item: ?item] }', 'when {}'))
                put(root, 'legacy/CONCEPT.md', 'concept Legacy [T]\npurpose old notation\n')
                output = put(root, 'ARCHITECTURE.md', START + '\nold map\n' + END + '\n')
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output), 1)
                self.assertEqual(tree_snapshot(root), before)
                (root / 'broken').mkdir()
                (root / 'broken/CONCEPT.md').write_bytes(b'\xff\xfe')
                before = tree_snapshot(root)
                self.expect(self.invoke(script, root, '--output', output), 2)
                self.assertEqual(tree_snapshot(root), before)

    def test_usage_and_io_errors_do_not_write(self):
        for package in PACKAGES:
            with self.subTest(package=package), self.fixture(package) as (root, script):
                seed(root)
                for args in (('--scope', '../escape'), ('--scope', str(root)), ('--output', str(root))):
                    with self.subTest(args=args):
                        before = tree_snapshot(root)
                        self.expect(self.invoke(script, root, *args), 2)
                        self.assertEqual(tree_snapshot(root), before)
                self.expect(self.invoke(script, root.parent / 'missing'), 2)
                no_root = subprocess.run([sys.executable, str(script)], text=True, capture_output=True)
                self.assertEqual(no_root.returncode, 2)
                help_result = subprocess.run([sys.executable, str(script), '--help'], text=True, capture_output=True)
                self.assertEqual(help_result.returncode, 0)
                for flag in ('--output', '--scope', '--exclude', '--check'):
                    self.assertIn(flag, help_result.stdout)

    def test_language_editions_have_identical_observable_output(self):
        with self.fixture(PACKAGES[0]) as (root, en_script):
            seed(root)
            cn_script = PACKAGES[1] / 'scripts/concept_map.py'
            before = tree_snapshot(root)
            en = self.invoke(en_script, root)
            cn = self.invoke(cn_script, root)
            self.expect(en, 0)
            self.expect(cn, 0)
            self.assertEqual((en.returncode, en.stdout, en.stderr), (cn.returncode, cn.stdout, cn.stderr))
            self.assertEqual(tree_snapshot(root), before)


if __name__ == '__main__':
    unittest.main(verbosity=2)

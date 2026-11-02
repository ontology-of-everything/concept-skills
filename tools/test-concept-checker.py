#!/usr/bin/env python3
"""Black-box regressions for the packaged read-only CONCEPT/SYNCS checker."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills/en/concept-design/scripts/concept_lint.py"

CONCEPT = '''# concept Tagging [Item]
coverage: complete

## purpose
Find grouped items.
## state
items: set Item, initially empty
## actions
add [item: Item] => []
  requires true
  ensures items contains item
## operational principle
after add then the item belongs to items
'''
APP = '''# app Demo
include Source [Id]
include Target [Id]
sync Follow
when { Source/finish: [] => [item: ?item] }
where { Source: { ?item owner: ?owner } }
then { Target/accept: [item: ?item; owner: ?owner] }
'''
CHECKED, SKIPPED, ERROR = 'format_checked', 'not_checked', 'format_error'


def cases():
    result = [
        ('concept', [CONCEPT], 0, CHECKED),
        ('app', [APP], 0, CHECKED),
        ('optional-where', [APP.replace('where { Source: { ?item owner: ?owner } }\n', '')], 0, CHECKED),
        ('same-line-blocks', ['# app Demo\nsync Follow\nwhen { Source/finish: [] => [] } then { Target/accept: [] }\n'], 0, CHECKED),
        ('quoted-purpose', [CONCEPT.replace('Find grouped items.', '"Find grouped items."')], 0, CHECKED),
        ('apostrophe-in-prose', [CONCEPT.replace('Find grouped items.', "Find an owner's grouped items.")], 0, CHECKED),
        ('unicode-prose', [CONCEPT.replace('Find grouped items.', '查找带标签的项目。')], 0, CHECKED),
        ('fenced-incomplete-note', [CONCEPT+'\n```text\n/* \" { ( ]\n# concept Fake\n```\n'], 0, CHECKED),
        ('missing-when', [APP.replace('when { Source/finish: [] => [item: ?item] }\n', '')], 1, ERROR),
        ('missing-then', [APP.split('then {')[0]], 1, ERROR),
        ('empty-when', [APP.replace('when { Source/finish: [] => [item: ?item] }', 'when {}')], 1, ERROR),
        ('empty-then', [APP.replace('then { Target/accept: [item: ?item; owner: ?owner] }', 'then {}')], 1, ERROR),
        ('comment-only-when', [APP.replace('when { Source/finish: [] => [item: ?item] }', 'when {\n// no pattern\n/* nothing */\n}')], 1, ERROR),
        ('comment-only-then', [APP.replace('then { Target/accept: [item: ?item; owner: ?owner] }', 'then { /* nothing */ }')], 1, ERROR),
        ('missing-open-brace', [APP.replace('when { Source/finish: [] => [item: ?item] }', 'when Source/finish: [] => [item: ?item]')], 1, ERROR),
        ('duplicate-rule', [APP+'sync Follow'+APP.split('sync Follow')[1]], 1, ERROR),
        ('duplicate-where', [APP.replace('then {', 'where {}\nthen {')], 1, ERROR),
        ('reordered-blocks', [APP.replace('when { Source/finish: [] => [item: ?item] }\n', '')+'when { Source/finish: [] => [item: ?item] }\n'], 1, ERROR),
        ('mismatched-bracket', [APP.replace('owner: ?owner] }', 'owner: ?owner) }')], 1, ERROR),
        ('unclosed-rule', [APP[:-2]], 1, ERROR),
        ('old-principle', [CONCEPT.replace('## operational principle', '## principle')], 3, SKIPPED),
        ('old-signature', [CONCEPT.replace('add [item: Item] => []', 'add (item: Item) : ()')], 3, SKIPPED),
        ('old-bare-concept', ['concept Demo [T]\npurpose test\n'], 3, SKIPPED),
        ('old-sync', ['# app Demo\nsync Follow\nwhen Source.finish (x)\nthen Target.accept (x)\n'], 3, SKIPPED),
        ('missing-coverage', [CONCEPT.replace('coverage: complete\n', '')], 3, SKIPPED),
        ('missing-coverage-and-section', [CONCEPT.replace('coverage: complete\n', '').replace('## state\n', '')], 1, ERROR),
        ('missing-coverage-and-empty', [CONCEPT.replace('coverage: complete\n', '').replace('Find grouped items.\n', '')], 1, ERROR),
        ('unknown-document', ['not a recognized specification\n'], 3, SKIPPED),
        ('unknown-app', ['# app Demo\nThis uses another rule language.\n'], 3, SKIPPED),
        ('unclosed-fence', [CONCEPT+'\n```text\n# concept FalseDeclaration\n'], 3, SKIPPED),
        ('unclosed-comment', [CONCEPT+'\n/* unfinished annotation { ( \n'], 3, SKIPPED),
        ('masked-later-sections', ['# concept Demo\ncoverage: partial\n## purpose\nA useful purpose.\n/* unfinished'], 3, SKIPPED),
        ('known-empty-before-unknown', [CONCEPT.replace('Find grouped items.\n', '')+'\n/* unfinished'], 1, ERROR),
        ('known-empty-rule-before-unknown', [APP.replace('when { Source/finish: [] => [item: ?item] }', 'when {}')+'\n/* unfinished'], 1, ERROR),
        ('unclosed-string', [APP.replace('item: ?item]', 'item: "unfinished ]')], 3, SKIPPED),
        ('invalid-coverage', [CONCEPT.replace('coverage: complete', 'coverage: maybe')], 1, ERROR),
        ('late-coverage', [CONCEPT.replace('coverage: complete\n', '').replace('## state', 'coverage: complete\n## state')], 1, ERROR),
        ('missing-section', [CONCEPT.replace('## state\n', '')], 1, ERROR),
        ('duplicate-section', [CONCEPT+'\n## purpose\nAnother purpose.\n'], 1, ERROR),
        ('split-heading', [CONCEPT.replace('## purpose', '##\npurpose')], 1, ERROR),
        ('multiple-inputs', [CONCEPT, APP], 0, CHECKED),
        ('mixed-not-checked', [CONCEPT, 'unknown\n'], 3, SKIPPED),
        ('mixed-error-and-not-checked', [CONCEPT.replace('## state\n', ''), 'unknown\n'], 1, ERROR),
    ]
    body_map = {
        'purpose': 'Find grouped items.\n',
        'state': 'items: set Item, initially empty\n',
        'actions': 'add [item: Item] => []\n  requires true\n  ensures items contains item\n',
        'op': 'after add then the item belongs to items\n',
    }
    for name, body in body_map.items():
        result.append(('empty-'+name, [CONCEPT.replace(body, '')], 1, ERROR))
        result.append(('comment-only-'+name, [CONCEPT.replace(body, '<!-- no content -->\n// no content\n/* no content */\n')], 1, ERROR))
    for name, wrapper in [
        ('string', '"\n# concept Fake\n## purpose\ncoverage: partial\nsync Ghost\nwhen {}\n"'),
        ('block-comment', '/*\n# concept Fake\n## purpose\ncoverage: partial\nsync Ghost\nwhen {}\n*/'),
        ('html-comment', '<!--\n# concept Fake\n## purpose\ncoverage: partial\nsync Ghost\nwhen {}\n-->'),
    ]:
        result.append((name+'-in-concept', [CONCEPT.replace('Find grouped items.', wrapper+'\nFind grouped items.')], 0, CHECKED))
        value = wrapper if name == 'string' else wrapper + '\n?item'
        result.append((name+'-in-app', [APP.replace('item: ?item]', 'item: '+value+']')], 0, CHECKED))
    for marker in ['```', '~~~~']:
        note='\n'+marker+'text\n'+CONCEPT+'\n'+APP+'\n'+marker+'\n'
        result.append(('fenced-'+marker[0]+'-concept', [CONCEPT+note], 0, CHECKED))
        result.append(('fenced-'+marker[0]+'-app', [APP+note], 0, CHECKED))
    result.append(('quoted-delimiters', [APP.replace('item: ?item]', 'item: "{ ] ) /* // \\\" quoted" ]')], 0, CHECKED))
    result.append(('comment-delimiters', [APP.replace('then {', '// ] ) }\n/* compare x > y ( ] } */\nthen {')], 0, CHECKED))
    calculated = APP.replace('where { Source: { ?item owner: ?owner } }',
                             'where { bind (Math.abs(-1) as ?owner) }')
    result.extend([
        ('where-computation', [calculated], 0, CHECKED),
        ('empty-when-with-computation', [calculated.replace(
            'when { Source/finish: [] => [item: ?item] }', 'when {}')], 1, ERROR),
        ('empty-purpose-with-old-signature', [CONCEPT.replace('Find grouped items.', '').replace(
            'add [item: Item] => []', 'add (item: Item) : ()')], 1, ERROR),
        ('empty-purpose-with-old-heading', [CONCEPT.replace('Find grouped items.', '').replace(
            '## operational principle', '## principle')], 1, ERROR),
        ('when-needs-completion', [APP.replace('[] => [item: ?item]', '[]')], 1, ERROR),
        ('completion-needs-record', [APP.replace('=> [item: ?item]', '=> ?item')], 1, ERROR),
        ('then-forbids-output', [APP.replace('owner: ?owner] }', 'owner: ?owner] => [] }')], 1, ERROR),
        ('unknown-when-content', [APP.replace('Source/finish: [] => [item: ?item]', 'some other language')], 3, SKIPPED),
        ('unknown-then-content', [APP.replace('Target/accept: [item: ?item; owner: ?owner]', 'some other language')], 3, SKIPPED),
        ('braced-legacy-call', [APP.replace('Source/finish: [] => [item: ?item]', 'Source.finish() : (item)')], 3, SKIPPED),
        ('literal-is-not-action', [APP.replace('Source/finish: [] => [item: ?item]', '"Source/finish: [] => []"')], 3, SKIPPED),
        ('unknown-rule-tail', [APP+'otherwise retry\n'], 3, SKIPPED),
        ('unknown-rule-body', ['# app Demo\nsync Unknown\nother notation\n'], 3, SKIPPED),
        ('input-needs-record', [APP.replace('Target/accept: [item: ?item; owner: ?owner]', 'Target/accept: ?item')], 1, ERROR),
        ('input-needs-names', [APP.replace('[item: ?item; owner: ?owner]', '[?item; ?owner]')], 1, ERROR),
        ('output-needs-names', [APP.replace('=> [item: ?item]', '=> [?item]')], 1, ERROR),
        ('duplicate-input-field', [APP.replace('owner: ?owner]', 'item: ?owner]')], 1, ERROR),
        ('duplicate-output-field', [APP.replace('=> [item: ?item]', '=> [item: ?item; item: ?other]')], 1, ERROR),
        ('empty-named-field', [APP.replace('item: ?item; owner:', 'item: ?item;; owner:')], 1, ERROR),
        ('missing-field-value', [APP.replace('owner: ?owner]', 'owner:]')], 1, ERROR),
        ('trailing-field-separator', [APP.replace('owner: ?owner]', 'owner: ?owner;]')], 0, CHECKED),
        ('semicolon-in-literal', [APP.replace('owner: ?owner]', 'owner: "a;b"]')], 0, CHECKED),
        ('nested-record-values', [APP.replace('owner: ?owner]', 'owner: [item: "a;b"; owner: ?owner]]')], 0, CHECKED),
        ('multiline-call', [APP.replace('Source/finish: [] => [item: ?item]', 'Source/finish:\n[]\n=>\n[item: ?item]')], 0, CHECKED),
        ('multiple-calls', [APP.replace('then {', 'then { Target/prepare: [] ')], 0, CHECKED),
        ('cross-file-rule-duplicate', [APP, APP], 1, ERROR),
        ('different-apps-same-rule', [APP, APP.replace('# app Demo', '# app Other')], 0, CHECKED),
        ('same-app-different-rules', [APP, APP.replace('sync Follow', 'sync Another')], 0, CHECKED),
        ('literal-before-input', [APP.replace('Source/finish: []', 'Source/finish: "extra" []')], 3, SKIPPED),
        ('literal-before-arrow', [APP.replace('[] =>', '[] "extra" =>')], 3, SKIPPED),
        ('literal-before-output', [APP.replace('=> [item:', '=> "extra" [item:')], 3, SKIPPED),
        ('literal-before-field', [APP.replace('[item: ?item]', '["extra" item: ?item]')], 3, SKIPPED),
        ('literal-before-field-colon', [APP.replace('item: ?item]', 'item "extra": ?item]')], 3, SKIPPED),
        ('literal-before-action-colon', [APP.replace('Source/finish:', 'Source/finish "extra":')], 3, SKIPPED),
        ('literal-before-clause-brace', [APP.replace('when {', 'when "extra" {')], 3, SKIPPED),
        ('missing-field-separator', [APP.replace('item: ?item; owner:', 'item: ?item owner:')], 3, SKIPPED),
        ('literal-in-app-declaration', [APP.replace('# app Demo', '# app "extra" Demo')], 3, SKIPPED),
        ('literal-in-rule-declaration', [APP.replace('sync Follow', 'sync "extra" Follow')], 3, SKIPPED),
        ('literal-in-section-declaration', [CONCEPT.replace('## state', '## "extra" state')], 3, SKIPPED),
        ('literal-in-coverage', [CONCEPT.replace('coverage: complete', 'coverage: complete "extra"')], 3, SKIPPED),
    ])
    return result


def invoke(paths):
    result = subprocess.run([sys.executable, str(CHECKER), *map(str, paths), "--json"],
                            capture_output=True, text=True)
    return result, json.loads(result.stdout) if result.stdout else {}


def regress(directory):
    failures, count = [], 0
    for index, (name, texts, expected_exit, expected_status) in enumerate(cases()):
        paths = []
        for part, text in enumerate(texts):
            path = directory / f"{index}-{part}.md"
            path.write_text(text)
            paths.append(path)
        before = {p: hashlib.sha256(p.read_bytes()).digest() for p in paths}
        result, report = invoke(paths)
        passed = ((result.returncode, report.get("status")) == (expected_exit, expected_status)
                  and report.get("scope") == "format only"
                  and all("issues" in f and "unchecked" in f and "warnings" not in f for f in report["files"])
                  and before == {p: hashlib.sha256(p.read_bytes()).digest() for p in paths})
        if not passed:
            failures.append({"case": name, "expected": [expected_exit, expected_status],
                             "exit": result.returncode, "report": report})
        count += 1
    unreadable = directory / "bad-encoding.md"
    unreadable.write_bytes(b"\xff\xfe")
    for name, paths in (("missing", [directory / "missing.md"]), ("directory", [directory]),
                        ("encoding", [unreadable]), ("usage", [])):
        result, report = invoke(paths)
        if result.returncode != 2:
            failures.append({"case": name, "exit": result.returncode, "report": report})
        count += 1
    invalid = directory / "invalid.md"
    invalid.write_text(CONCEPT.replace("## state\n", ""))
    result, report = invoke([invalid, directory / "missing.md"])
    if result.returncode != 2 or report.get("status") != "read_error":
        failures.append({"case": "read-error-priority", "report": report})
    count += 1
    shared = directory / 'shared.md'
    shared.write_text(APP)
    alias = directory / 'alias.md'
    alias.symlink_to(shared)
    result, report = invoke([shared, alias, shared])
    if result.returncode != 0 or len(report.get('files', [])) != 1:
        failures.append({'case': 'same-input-alias', 'report': report})
    count += 1
    bad_when = directory / 'bad-when.md'
    bad_when.write_text(APP.replace('Source/finish: [] => [item: ?item]', 'Source/finish: []'))
    result, report = invoke([bad_when])
    issues = report.get('files', [{}])[0].get('issues', [])
    if not any(item['code'] == 'when-completion' and item['line'] == 5 for item in issues):
        failures.append({'case': 'completion-line-number', 'report': report})
    count += 1
    result = subprocess.run([sys.executable, str(CHECKER), "--help"], capture_output=True, text=True)
    if result.returncode or not all(word in result.stdout for word in ("--json", CHECKED, SKIPPED, ERROR)):
        failures.append({"case": "help", "output": result.stdout + result.stderr})
    return count + 1, failures


def main():
    with tempfile.TemporaryDirectory(prefix="concept-checker-") as directory:
        count, failures = regress(Path(directory))
    if failures:
        print(json.dumps(failures, ensure_ascii=False, indent=2))
        return 1
    print(f"OK: {count} checker regressions, including input hashes and exit/status contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ValidatorTests(unittest.TestCase):
    def run_case(self, value, raw=False):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'input.json'
            source.write_text(value if raw else json.dumps(value), encoding='utf-8')
            out = Path(tmp) / 'reports'
            p = subprocess.run([sys.executable, str(ROOT / 'validate.py'), str(source), '--output-dir', str(out)], capture_output=True, text=True)
            self.assertTrue((out / 'report.json').exists(), p.stderr)
            return p.returncode, json.loads((out / 'report.json').read_text()), (out / 'report.html').read_text()

    def codes(self, report):
        return {i['code'] for r in report['files'] for i in r['issues']}

    def graph(self):
        return {'@context': 'https://schema.org', '@graph': [
            {'@type': 'Person', '@id': 'https://example.org/#person', 'name': 'Alex Rowan', 'url': 'https://example.org/alex'},
            {'@type': 'Organization', '@id': 'https://example.org/#org', 'name': 'Cedar Notes', 'url': 'https://example.org/'},
            {'@type': 'Article', '@id': 'https://example.org/notes/one#article', 'headline': 'A note', 'url': 'https://example.org/notes/one', 'author': {'@id': 'https://example.org/#person'}, 'publisher': {'@id': 'https://example.org/#org'}, 'datePublished': '2026-10-01'}]}

    def test_identity_graph(self):
        code, report, _ = self.run_case(self.graph())
        self.assertEqual(code, 0)
        self.assertEqual(report['summary'], {'errors': 0, 'warnings': 0})

    def test_context(self):
        for context in (None, 'http://schema.org', {'@vocab': 'https://schema.org/'}):
            data = self.graph()
            data['@context'] = context
            code, report, _ = self.run_case(data)
            self.assertEqual(code, 1)
            self.assertIn('context', self.codes(report))

    def test_invalid_types(self):
        for val in (42, {}, [], ['Person', 42], 'javascript:Person'):
            data = self.graph(); data['@graph'][0]['@type'] = val
            self.assertIn('type-format', self.codes(self.run_case(data)[1]))

    def test_url_properties(self):
        for value in ('javascript:alert(1)', 'https://', 'https://example.org/a b', 'https://user:pass@example.org', 42):
            data = self.graph(); data['@graph'][0]['url'] = value
            self.assertIn('url', self.codes(self.run_case(data)[1]))

    def test_duplicate_ids(self):
        data = self.graph(); data['@graph'].append(data['@graph'][0].copy())
        self.assertIn('duplicate-id', self.codes(self.run_case(data)[1]))

    def test_dangling_local_external_allowed(self):
        data = self.graph(); data['@graph'][2]['author']['@id'] = 'https://example.org/#absent'
        self.assertIn('dangling-reference', self.codes(self.run_case(data)[1]))
        data['@graph'][2]['author']['@id'] = 'https://external.example.org/#author'
        self.assertNotIn('dangling-reference', self.codes(self.run_case(data)[1]))

    def test_relationship_target_types(self):
        data = self.graph(); data['@graph'][2]['author']['@id'] = data['@graph'][2]['@id']
        self.assertIn('relationship-type', self.codes(self.run_case(data)[1]))

    def test_recommendations_are_warnings(self):
        code, report, _ = self.run_case({'@context': 'https://schema.org', '@type': 'Person'})
        self.assertEqual(code, 0)
        self.assertIn('recommended-field', self.codes(report))

    def test_json_errors_and_duplicate_keys(self):
        for text, expected in [('{', 'json-syntax'), ('{"@context":"https://schema.org","@type":"Person","name":"a","name":"b"}', 'duplicate-key'), ('{"x":NaN}', 'json-syntax')]:
            code, report, _ = self.run_case(text, raw=True)
            self.assertEqual(code, 1)
            self.assertIn(expected, self.codes(report))

    def test_html_escape(self):
        data = self.graph(); data['@graph'][0]['url'] = '<script>alert(1)</script>'
        _, _, html = self.run_case(data)
        self.assertNotIn('<script>', html)
        self.assertIn('&lt;script&gt;', html)

    def test_collision_resolve_hardlink_symlink(self):
        for mode in ('direct', 'resolve', 'hardlink', 'symlink'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as tmp:
                base = Path(tmp); out = base / 'reports'; out.mkdir()
                source = base / 'input.json'; source.write_text(json.dumps(self.graph()))
                target = out / 'report.json'
                if mode == 'direct':
                    source = target; source.write_text(json.dumps(self.graph()))
                elif mode == 'resolve':
                    source = out / '..' / 'reports' / 'report.json'; source.write_text(json.dumps(self.graph()))
                elif mode == 'hardlink': os.link(str(source), str(target))
                else: target.symlink_to(source)
                before = source.read_bytes()
                p = subprocess.run([sys.executable, str(ROOT / 'validate.py'), str(source), '--output-dir', str(out)], capture_output=True, text=True)
                self.assertEqual(p.returncode, 2)
                self.assertEqual(source.read_bytes(), before)
                self.assertIn('collision', p.stderr.lower())

if __name__ == '__main__': unittest.main()

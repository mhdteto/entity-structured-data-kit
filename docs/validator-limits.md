# Validator limits

[README](../README.md) · [Models](modeling-guide.md) · [Checklist](publication-checklist.md)

This is an **educational subset structural linter**, not a full JSON-LD processor, schema.org validator or Google eligibility test. Its errors mean “outside this supported subset or structurally suspicious,” not necessarily “illegal schema.org.” Warnings are kit suggestions or scope notices. No issue list is exhaustive.

## Supported structure

One JSON object with exactly `"@context": "https://schema.org"`, as a standalone entity or containing a nonempty `@graph` array of objects. Context dictionaries/arrays, HTTP contexts, trailing-slash contexts, aliases, remote custom contexts, named graphs, top-level arrays and general expansion are outside scope. Nested changed contexts are reported.

Malformed JSON, duplicate keys at any depth, NaN/Infinity and duplicate string IDs among graph definitions are errors. General JSON-LD can merge repeated definitions; this kit rejects them to catch accidental duplication. IDs must be HTTP(S) URLs or simple `#fragment` strings; other valid IRI forms are outside this subset.

`@type` can be an alphanumeric type name, an HTTPS schema.org type URL, or a nonempty list of those strings. Unknown names receive unsupported-type warnings, not a vocabulary-membership verdict. Unknown properties, inheritance/subclasses, general property domains/ranges, inverse relationships, and text/date/language formats are not validated.

## Selected URL policy

String values for `url`, `sameAs`, `image`, `mainEntityOfPage`, `contentUrl` and `logo` must be absolute HTTP(S) URLs with a hostname and without credentials, whitespace, controls or backslashes. Lists are checked item by item. Objects are recursively inspected; objects without `@id`, `url` or `contentUrl` receive a warning.

This is a small policy check, not a complete URL standard implementation, image check or safety guarantee. Passing URLs can be untrusted or unreachable. No URL is fetched.

## Local reference policy

The index contains only definitions immediately inside this document's `@graph`, or the standalone root entity. A reference-only object is exactly `{"@id": "…"}`.

- Exact ID matches resolve locally.
- A `#fragment` is considered local.
- An absolute ID with a fragment is considered local if the URL before `#` equals the URL before `#` of any declared ID. An absent full ID then produces a dangling-reference error.
- Other absolute references are permitted as external and **remain unverified**. They may be unreachable or incorrect.

No base-URL resolution, slash normalization, relative paths, HTTP equivalence or cross-file resolution occurs. Do not mix `#person` with `https://example.org/#person`: this tool does not equate them. A missing bare document URL is not reliably identifiable as a dangling graph ID and is not flagged. Include definitions or review external references yourself.

## Relationship model and recommendations

For inline typed targets or locally resolved targets, `author`/`publisher` are modeled as Person/Organization; `worksFor` as Organization; ProfilePage `mainEntity` as Person/Organization. Other types produce a warning because broader schema.org ranges and subclasses are not inferred. Untyped external references cannot have their target type checked. Non-object relationship representations receive a shape warning, not a claim that every such representation is illegal.

| Type | Kit recommended fields |
|---|---|
| Person | `@id`, `name`, `url` |
| Organization | `@id`, `name`, `url` |
| ProfilePage | `@id`, `url`, `mainEntity` |
| Article | `@id`, `headline`, `url`, `author`, `publisher`, `datePublished` |

Absent/null/empty-string/empty-list recommendations are warnings. These are not schema.org required fields or a complete set of provider feature requirements. A nonempty value is not automatically fact-checked or fully type-checked.

## Operational boundaries

No networking, remote contexts, account access, page rendering, fact/evidence checking, cross-page reconciliation or ranking measurement. HTML escapes file/finding text and uses no scripts or remote resources. Input paths appear in reports as supplied: absolute/private paths should be reviewed before sharing. No timestamps are generated.

Resolved-path and same-file checks detect input/output collisions before either write. Another process changing links after the check is outside the guarantee; use a trusted workspace. Writes replace reports and are not transactional. An output failure may leave one updated report; stderr and exit 2 identify failure. Run on bounded local files, not as a hostile-input service.

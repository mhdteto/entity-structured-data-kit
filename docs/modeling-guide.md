# Modeling guide

[README](../README.md) · [Limits](validator-limits.md) · [Checklist](publication-checklist.md)

## Give each thing its own identity

Use one stable absolute `@id` per entity, such as `https://example.org/#alex-rowan`, and reuse it across pages. `url` identifies the public page people visit. The person differs from the ProfilePage describing that person: the page's separate ID ends in `#page`, and its `mainEntity` points to the person ID.

An Article is another thing. Its `author` points to the writer; its `publisher` points to the organization responsible for publication. The same organization can publish the profile page. Publication responsibility does not establish employment, credentials or endorsement. The examples assert none of those. `mainEntityOfPage` connects the article to its public page URL. An `@graph` groups related definitions.

An organization profile points its `mainEntity` to the organization ID. A page merely mentioning a company is not automatically a profile about it. Choose the type from the page's actual primary purpose. This kit's Person/Organization expectation for ProfilePage targets is a narrow teaching model, not schema.org's entire mainEntity range.

## Adapt the graph

1. Inventory visible, supported facts and the actual author/publisher.
2. Choose stable identity IDs and canonical public page URLs. Replace all occurrences of the fictional domain consistently.
3. Select the smallest example reflecting the page. Repeated definitions across pages must agree; this tool checks one file at a time.
4. Replace names, descriptions, dates and URLs from real content. Remove unsupported fields. Never invent reviews, awards, offices, credentials, clients or results to satisfy a recommendation.
5. Lint syntax/structure, check vocabulary separately, compare markup with visible facts, then assess provider-specific eligibility.

To embed, use a `<script type="application/ld+json">` element on the appropriate page. The CLI reads JSON, not HTML. Your publishing system must embed untrusted text safely; neutralize literal `<` characters in JSON string values as `\u003c` so strings cannot close the script element. This report's HTML escaping is not an embedding helper.

For translations of the same person, retain the same entity ID and use truthful page URLs/languages. Language alternates belong in the website's separate publishing setup. Country/currency fields are not inherently needed for these models.

## Four distinct questions

| Layer | Establishes | Does not establish |
|---|---|---|
| JSON syntax | Parser can read the document | Vocabulary meaning or truth |
| Types and relationships | A meaningful entity model | Visible, evidenced facts |
| Visible supported facts | Human review of copy/evidence | Search eligibility or display |
| Provider feature rules | A particular feature's conditions | Guaranteed display, ranking or AI citation |

The local tool covers only a subset of the first two layers. Passing cannot verify a fictional claim.

## Official references

Accessed **2026-11-01**. The four schema.org pages displayed their development-version notice when opened; no vocabulary snapshot is bundled or pinned.

- [Schema.org Person](https://schema.org/Person): person model and available properties.
- [Schema.org Organization](https://schema.org/Organization): organization model.
- [Schema.org ProfilePage](https://schema.org/ProfilePage): profile page as WebPage/CreativeWork subtype.
- [Schema.org Article](https://schema.org/Article): article and inherited CreativeWork properties.
- [Google general structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies): visible relevant content, quality and technical requirements; correct markup does not guarantee rich results.

Those five documentation pages were opened directly. The [Schema Markup Validator](https://validator.schema.org/) and [Google Rich Results Test](https://search.google.com/test/rich-results) are separate next-step tools; no official validation verdict is claimed here. General guidelines do not replace a particular Google feature's current documentation.

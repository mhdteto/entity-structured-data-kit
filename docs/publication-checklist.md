# Publication checklist

[README](../README.md) · [Models](modeling-guide.md) · [Limits](validator-limits.md)

1. **Establish visible facts.** Check actual page copy, byline, publisher, dates and URLs. Keep evidence for material claims. Remove fictional placeholders, invented results, credentials, awards, offices and reviews.
2. **Choose the model.** Separate entity and page IDs. Confirm authorship, publication responsibility and primary subject. Keep identity definitions consistent across pages and translations.
3. **Run local lint.** `python3 validate.py page.json --output-dir reports`. Review warnings and external references manually. Exit 0 is a subset-lint result; unknown fields and date/text semantics still need review.
4. **Check vocabulary and rendering.** Review current schema.org type/property definitions and use its separate validator. Embed JSON safely; inspect actual CMS output and ensure it describes visible supported content.
5. **Check provider-specific rules.** Read current feature documentation alongside Google's general guidelines, and use the Rich Results Test for supported features. A schema.org type is not automatically a Google feature. Tests do not guarantee ranking, display or AI citations.
6. **Deploy and inspect.** Confirm canonical URLs, public access, crawling/indexing permissions and production copy. Recheck differences between reviewed JSON and rendered output. This tool does not deploy or submit pages.
7. **Maintain.** Correct stale facts, conflicting IDs and page changes. Track factual edits in your editorial process; separate evidence checks from vocabulary checks and search performance measurements.

[Official sources](modeling-guide.md#official-references) accessed 2026-11-01. Revisit current documentation before substantive releases.

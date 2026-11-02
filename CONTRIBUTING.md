# Contributing

Discuss subset changes first. Keep the CLI offline and dependency-free, reports deterministic, and errors/warnings tied to documented scope. Add regression tests before parser, identity, URL or output changes. Test file collisions and HTML escaping. Never add network access implicitly or private identity data to fixtures.

Run `python3 -m unittest discover -s tests -v` and regenerate samples with `python3 validate.py --all examples --output-dir reports`. CI checks Python 3.10 and 3.13 and compares reports byte for byte. Use fictional reserved domains. Recommendations must remain explicit kit choices, not invented schema.org requirements.

Code/tests/configuration contributions are MIT; documentation/examples/artwork are CC BY 4.0. Do not include third-party content without appropriate rights.

## Choose a contribution route

- [Bug or documentation error](https://github.com/mhdteto/entity-structured-data-kit/issues/new?template=bug_report.yml): include a release tag or commit and a minimal public/fictional reproducer.
- [Feature request](https://github.com/mhdteto/entity-structured-data-kit/issues/new?template=feature_request.yml): state the task, example and proposed behavior.
- [Source or methodology proposal](https://github.com/mhdteto/entity-structured-data-kit/issues/new?template=source_proposal.yml): provide the specific claim, publisher, dates, market, relationship and limits.

Run the documented validation and preserve the distinction between observed, supplied, inferred and unknown. See the [connected fictional workflow](https://github.com/mhdteto/authority-architecture-system/tree/main/examples/fictional-workflow) for an example.

# Contributing

Discuss subset changes first. Keep the CLI offline and dependency-free, reports deterministic, and errors/warnings tied to documented scope. Add regression tests before parser, identity, URL or output changes. Test file collisions and HTML escaping. Never add network access implicitly or private identity data to fixtures.

Run `python3 -m unittest discover -s tests -v` and regenerate samples with `python3 validate.py --all examples --output-dir reports`. CI checks Python 3.10 and 3.13 and compares reports byte for byte. Use fictional reserved domains. Recommendations must remain explicit kit choices, not invented schema.org requirements.

Code/tests/configuration contributions are MIT; documentation/examples/artwork are CC BY 4.0. Do not include third-party content without appropriate rights.

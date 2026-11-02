# Connected fictional example

**Entirely fictional teaching data:** Alex Rowan, Cedar Notes, publishers, HTTP responses, reviews, engines and answers are invented. Reserved example domains are placeholders. No client case or live AI measurement is presented.

Run from the repository root:

```sh
python3 validate.py examples/connected-workflow/inputs/entity-graph.json --output-dir examples/connected-workflow/report
```

Inputs: [entity-graph.json](inputs/entity-graph.json)

## Expected output

0 errors and 0 warnings in the educational structural subset. The fictional visible-copy brief is that Alex Rowan is Research Director at Cedar Notes and authored its reading-journal article. Disputed forum and office claims are omitted. The linter does not establish factual truth, visible-page parity, full schema.org validity or Google eligibility.

Inspect [the generated HTML](report/report.html) and [JSON](report/report.json). The command replaces the report directory’s output files; keep your own inputs elsewhere.

## Where this fits

[Follow the complete five-tool workflow](https://github.com/mhdteto/authority-architecture-system/tree/main/examples/fictional-workflow) · [Operating method](https://github.com/mhdteto/authority-architecture-system) · [Next: ai-citation-tracker](https://github.com/mhdteto/ai-citation-tracker)

These original synthetic inputs and reports use CC BY 4.0; the tool retains its existing code license. Verify reproduction with:

```sh
python3 tools/verify_connected_example.py
```

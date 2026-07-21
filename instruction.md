# Recover the Northgate containment rollup

Badge-access containment for the Northgate site is being driven by a rollup that shipped mid-incident, and the responder queue it produces cannot be trusted. Two things are needed from you: the rollup at `/app/workflow/export_access.py` has to be put back into a state that matches what the access-review board actually decided, and a small audit tool has to exist at `/app/access_audit.py` so the next responder can re-derive the same conclusions without you.

That tool takes two subcommands:

* `diagnose --dossier PATH --report PATH` — writes a defect report. This command holds no state between runs. Calling it twice, calling it before any repair, or calling it after one, all produce the same complete report; it never assumes an earlier invocation happened.
* `repair --output-dir PATH` — restores the rollup, runs it, and leaves five files behind: `summary.json`, `zone_matrix.json`, `contained.jsonl` (compact JSON lines), `diagnosis.json` and `repair_audit.json`. Default output directory is `/app/output`.

Six deployment defects are known and every one of them has to appear in the report: `class_normalization`, `class_scope_filter`, `dedupe_swipe`, `queue_ordering`, `revoked_filter` and `wrong_entry_field`.

## Evidence

Your evidence is the board's dossier at `/app/incident/access_review_dossier.md` together with the untouched build kept at `/app/workflow/.export_access.original`. That snapshot is read-only on purpose: the repair audit reports a SHA-256 taken from those exact bytes, which is what makes the audit reproducible after the live workflow has already been replaced. Leave it exactly as you found it. Which defective constructs have to disappear from the restored rollup is recorded in the spec.

Both evidence fields are compared literally. A `dossier_quote` has to be one line of the dossier reproduced character for character, with nothing changed but the whitespace at either end; a `pipeline_evidence` value is the same thing taken from the frozen snapshot. Summarizing, re-wrapping or tidying either one is treated as wrong.

## Where the rules live

`/app/docs/output_contract.md` walks through the commands, the artifacts and the processing stages. Schemas are pinned separately in `/app/docs/report_spec.json` — key sets, the defect record shape, `input_stats`, digest payloads and the exact byte layout behind each checksum. Work from it directly instead of inferring structure from the sample data, because an artifact missing a single key counts as wrong however good the arithmetic behind it is.

Behaviour is a different matter and is not in either document. Badge-class normalization, which row survives a repeated swipe, how swipes merge into occupancies, how control windows are scoped and which layer wins when two of them overlap, the occupancy ledger, and the admission, priority and ordering rules were all argued out by the access-review board and recorded in its PAC-ticketed notes. Most of the dossier around those notes is routine site chatter. Positions changed as the review went on: several February triage proposals were reversed outright, and some March working notes were revised again during the May close-out. Follow each rule to its final dated decision — where an earlier note and a later one disagree the later one governs, and that holds even when the earlier note reads like the more natural engineering choice.

## Shapes worth settling first

Four format details invalidate every downstream comparison if you get them wrong, so fix them before writing any arithmetic. `zone_matrix.json` is an object keyed by zone name, not an array. `class_counts` lists `privileged`, `contractor`, `staff`, `visitor` in that order and emits `0` for any class with no canonical rows — and it counts every canonical row, revoked badges included. `priority_counts` behaves the same way over `critical`, `high`, `standard`. Within a queue row, `swipe_ids` is an ascending array of strings, while the rows of `contained.jsonl` themselves follow the board's queue order, which is deliberately not entry-time order.

The restored rollup has to keep working on a different badge stream supplied through `--input`, give byte-identical results when run twice, and take nothing from `/tests` or `/solution`.

Finish by running:

`python3 /app/access_audit.py repair --output-dir /app/output`

and leave the result in `/app/output` for the responder handoff.

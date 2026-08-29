# Claims-Completion Evidence

This directory preserves the 2026-08-29 evidence summarized in Section 9.

- `PREDECLARED_PROTOCOL.md` freezes the evidence tracks and acceptance criteria.
- `stress-design.json` and `stress-confirmation.json` preserve the independent
  seeded heterogeneous-residual, group-comparison, and changepoint runs.
- `selective-stress-dataset.json`, `selective-stress-report.json`, and
  `selective-vs-update-all-report.json` preserve the bounded-frontier controls
  and paired selective comparison.
- `chronological-session-protocol.json` and the two aggregate confirmation reports
  preserve privacy-reduced chronological results. Raw private session text and
  case-level chronological data are intentionally excluded.
- `predictive-snap-invariance-go-test.jsonl` records the integration test showing
  that graph publication and rollback do not yet alter scored recall output.
- `RESULTS.md` is the human-readable decision ledger.

The synthetic artifacts establish only behavior under their declared generators.
The chronological block contains two independent trajectories and is therefore
inconclusive under its frozen minimum. The snap test establishes current
implementation wiring, not a general impossibility result for predictive graph
revision.

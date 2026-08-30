# Rank Adaptation Evidence

> **Superseded organic evidence:** The organic replay outputs in this directory
> used full transcript text in semantic retrieval. They are retained as
> historical false-start provenance and are not current EventFrame-corpus
> evidence. See `../eventframe-corpus-v1/` for the corrected contract-12
> aggregates. Synthetic mechanism results remain applicable only where the
> corrected contract-12 rerun explicitly reproduced them.

This directory preserves the small aggregate reports used by the whitepaper's Bayesian elastic-ranking and Anti-Pigeon shock-revision discussion. Raw session exports, local databases, embedding caches, and generated replay datasets are intentionally excluded.

The evidence has five parts:

- `elastic-real/`: fixed-delta versus elastic-delta retrospective replay.
- `antipigeon-revision/`: Anti-Pigeon revision wiring and the first calibration-rescue attempt.
- `calibration-rescue/`: a fresh same-cutoff rerun that falsified a stationary calibration claim across retrieval regimes.
- `modulated-real/`: confidence-modulated elastic ranking against the preceding full-upgrade configuration and raw baseline.
- `modulated-synthetic/`: constructed promotion, demotion, retention, envelope, churn, and latency cases.

The real-data artifacts are retrospective regression evidence. They are not untouched confirmation, independent replication, or proof that the same gains transfer to another corpus. In particular, the real replay did not exercise Anti-Pigeon `split` or `split_reset`, because its records had no valid sharing certificates. The shock transition is therefore mechanism-tested but not empirically validated on a naturally shared group.

See the individual `RESULTS.md` and `protocol.json` files for denominators, comparisons, and limitations.

# Runtime Concurrency Rescue Evidence

This directory preserves aggregate, privacy-safe performance artifacts from the
2026-08-30 EventFrame runtime concurrency and persistence rescue. No source
conversation, event text, user identifier, database, machine serial number, or
private endpoint is included.

The fixture used an Apple M4 Mac mini with 10 CPU cores and 16 GB of memory. A
fresh embedded EventFrame database was seeded with 200 deterministic synthetic
events. Sixteen workers then issued a deterministic mixed workload for 30
seconds: approximately 90% recall and 10% capture, with `recall_k=50`,
`pack_k=10`, 256-dimensional local feature-hash embeddings, SQ8 traversal,
contextual scoring, hierarchical posterior support, residual application, a
durable Bayesian journal, and a SQLite-backed rank-delta cache.

- `failed-group-commit.json` records the rejected batching design. Long
  overlapping write transactions caused 64 recall timeouts and failed health.
- `serialized-repaired-baseline.json` records the clean baseline after that
  batching design was removed.
- `final-rescue.json` records the retained implementation: shared read locks,
  striped immutable journal commits, bounded residual reads, per-connection
  SQLite WAL controls, suppression of zero-reliability rank-delta writes, and
  bounded full-recall retries after a stale snapshot.

These are descriptive capacity measurements, not preregistered validation of a
universal latency claim. The final run supports practical median, p95, and
throughput on the named host while continuing to falsify a strict sub-100 ms
p99 claim for this write-heavy fixture.

# Authenticated Outcome Evidence

Runtime source: [eventframed d5cda75](https://github.com/JuanHuaXu/eventframed/commit/d5cda75).

The four authenticated-evidence files are verbatim copies of the public runtime
documents at that revision. They contain synthetic mechanism descriptions and
aggregate timing only, not private text, event identities, keys, or embeddings.
The raw benchmark is the saved three-run campaign, not a new paper-only run.
The copied runtime documents retain their source Apache-2.0 terms; the source
license and attribution notice are preserved as `SOURCE_LICENSE` and
`SOURCE_NOTICE`. The paper's own MIT license is unchanged.

`timings.json` is generated from `authenticated-evidence-benchmark.txt` by
`ruby scripts/summarize_authenticated_benchmarks.rb` from the paper repository
root. The summarizer checks completed package runs, metric pairs, 500 operations
per run, three repetitions, and records the input SHA-256 digest. Concurrent
ns/op is inverse throughput; p99-ns and max-ns are individual-call timings.

This evidence supports local mechanisms and conditional internal timing, not
calibration, truthful independent evidence, improved answer quality, downstream
poisoning resistance, or a production latency guarantee. It does not supersede
the earlier 16-worker tail-latency failure. See the paper's Claim 2e.

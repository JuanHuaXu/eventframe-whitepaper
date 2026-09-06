# Fixed-share grid evidence

Copied verbatim from public runtime revision
[76576dc](https://github.com/JuanHuaXu/eventframed/commit/76576dc).
Generator: cmd/grid-belief-experiment/main.go at that revision. The protocol
was written before executing either split; there was no parameter search.
It was not externally preregistered. Design base 2026090601 and confirmation
base 2026090602 each contain 512 trajectories, with all per-trajectory metrics.
Normal/Bonferroni uncertainty is approximate fixed-sample coverage, not a
sequential confidence guarantee. The composition fixture is not an agent test.

Both score regressions and Beta control results are retained. Benchmark logs
contain all modes and runs, including the unsigned legacy control. SHA256SUMS
binds the copied artifacts. Source files remain Apache-2.0 with SOURCE_LICENSE
and SOURCE_NOTICE; the whitepaper's own license is unchanged. Only synthetic
outcome streams and public implementation documentation are included.

# Grid belief math and evidence audit, 2026-09-06

Confirmed gap: two fixed usefulness hypotheses constrain the raw predictive
range, regardless of authentication quality. No contradiction is asserted with
the wider final calibrated law. Evidence coverage, source truth, and saturation
latency remain open empirical gaps, not fixed by adding more hypotheses.

The finite reset-HMM equations use one latent model for likelihood and prediction.
Posterior q is after n committed observations; prior a is before observation
n+1. Predictive p uses a, not q, and serving does not mutate either. Updating
uses the same a, not a second transition. Bernoulli parameters are strictly
inside (0,1), the denominator is positive, and all normalized vectors lie in
the 21-simplex. Predictive bounds include the reset contribution. Unit-weight
model semantics are distinguished from fractional generalized updates and from
unknown external-law calibration. All new symbols are indexed.

Composition substitutes the grid useful probability into the pre-residual map;
it does not multiply a second correction or bypass residual/certificate gates.
Model family is policy-versioned. Code tests verify actual score wiring,
nonmutating reads, both-store replay/restart and split-reset transitions.
The two-hypothesis default and existing unsigned compatibility mode are unchanged.

Evidence is copied from public runtime revision 76576dc with checksums and
Apache source attribution. Both 512-trajectory splits are retained. Paper tests
recompute every interval from trajectory means and every confirmation table row;
no fixture metric is transcribed without a check. Intervals are approximate
fixed-sample normal/Bonferroni, not exact sequential coverage. Frozen protocol was
written before execution but not externally preregistered. No tuned rescue is
claimed. Raw belief improves in six scenarios and regresses in two; composed
score improves in five and regresses in three. Beta wins all stationary cases.

New claim 2f separates validated range-bias correction from falsified universal
improvement and untested signed real-data benefit. Timing includes lock/storage
waits, excludes signing/setup, and reports throughput separately from p99.
Three descriptive runs do not rescue the earlier 16-worker deadline failure.

Two remaining high-value research directions: validate source-dependence and
selection certificates on a prospective signed stream; compare prequential
stationary/adaptive mixtures using the complete composed proper score with varied
baseline/calibration regimes. These are recommendations, not published features.

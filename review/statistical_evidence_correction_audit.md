# Statistical Evidence Correction Audit

Date: 2026-08-28

## Classification

- E1 was stale against the repository artifacts. The v4 group design and confirmation seed bases are 984451656 and 69867970; the changepoint seed bases are 982451653 and 67867967.
- E2's missing-data diagnosis was stale: the v2, v3, and v4 JSON reports contain changepoint scenarios, and v4 contains its CUSUM policy. A narrower gap was confirmed: no numeric false-alarm acceptance boundary was preserved for the v2/v3 iterations.
- E3 was confirmed. Fixed-sample Wilson intervals were absent from the headline group and changepoint proportions.
- E4 was confirmed. The paper did not define unmatched-alarm matching or report a denominator.
- E5(a)--(c) were confirmed: mean delay lacked its detected-change denominator, the deterministic share control lacked a paper-repository artifact, and the results digest called the running-mean warm-up unbiased.

## Corrections

- Added two-sided 95% Wilson score intervals and labeled them fixed-sample descriptive intervals rather than sequential confidence sequences.
- Defined one-to-one inclusive-window trigger matching, unmatched alarms, per-trajectory burden, trigger fractions, and detected-change-only mean delay.
- Replaced the unsupported v2/v3 target-failure claim with the observed stable alarm counts and disclosed the absent predeclared numeric boundary.
- Corrected the warm-up description to a 20-observation ordinary running mean.
- Preserved the passing `go test -json` record for `TestBayesianGroupComparisonProposesWithoutChangingAuthority` as machine-readable integration-control evidence.

No raw experiment JSON was edited.

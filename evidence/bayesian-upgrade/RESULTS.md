# Bayesian grouping and changepoint upgrade, 2026-08-28

This is synthetic implementation evidence, not a real OpenClaw replay. The
production comparison and changepoint code was run on fixed design seeds and
then on an untouched confirmation seed. Failed v2 and v3 attempts remain in this
directory rather than being overwritten.

## Frozen v4 policy

- Beta-Bernoulli group comparison: split prior 0.5, decision probability 0.95,
  minimum support 8 per member, and at most 64 members.
- Changepoints: hazard 0.05, exact threshold 0.30, run-length cap 32, EWMA rates
  0.25/0.025, two-sided CUSUM slack 0.10 and threshold 8, 20-sample unbiased
  warm-up, and 20-sample reset cooldown.
- Abrupt and recurring detections use a 20-observation window. Gradual drift has
  a stable prefix and a separately declared 60-observation window.
- Changepoint confirmation seed base: 67,867,967. Group-comparison confirmation seed base: 69,867,970. Both were run after the v4 policy was frozen.

## Confirmation results

### Shared-versus-split comparison

| Scenario, 100 samples/member | Share | Split | Uncertain | Wrong |
| --- | ---: | ---: | ---: | ---: |
| Same rates, 0.8 / 0.8 | 0.0% | 0.0% | 100.0% | 0.0% |
| Moderate split, 0.65 / 0.35 | 0.0% | 87.5% | 12.5% | 0.0% |
| Strong split, 0.9 / 0.1 | 0.0% | 100.0% | 0.0% | 0.0% |

The comparison is deliberately asymmetric in practice: divergent groups become
visible much sooner than compatible noisy groups become safe to merge. At this
sample size it proposed no false shares, but it also did not affirm ordinary
compatible groups. A separate deterministic integration fixture with 50
all-useful outcomes per member does produce `share`, proving that the branch is
reachable. Every proposal remains non-authoritative until an external
Anti-Pigeon certificate passes.

### Changepoints

| Scenario | Detected | Miss rate | False alarms | Mean delay |
| --- | ---: | ---: | ---: | ---: |
| Stable 0.8 | n/a | n/a | 1 | n/a |
| Abrupt, noiseless | 64 / 64 | 0.0% | 0 | 0.0 |
| Abrupt, 0.9 to 0.1 | 56 / 64 | 12.5% | 17 | 12.3 |
| Gradual after stable prefix | 60 / 64 | 6.25% | 10 | 44.6 |
| Recurring, noiseless | 128 / 128 | 0.0% | 0 | 0.0 |
| Recurring, 0.9 / 0.1 | 99 / 128 | 22.66% | 21 | 13.8 |

Compared with the original detector, which missed 96.88% of noisy abrupt, all
gradual, and 93.75% of noisy recurring changes, v4 is a substantial correction.
It is not a proof of production reliability. One stable false alarm, repeated
unmatched alarms in changing streams, recurring misses, and long gradual delay
remain explicit limitations.

Raw reports:

- `2026-08-28-additional-claims-v4-design.json`
- `2026-08-28-additional-claims-v4-confirmation.json`
- rejected confirmations: `2026-08-28-additional-claims-v2-confirmation.json`
  and `2026-08-28-additional-claims-v3-confirmation.json`

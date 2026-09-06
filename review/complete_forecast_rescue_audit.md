# Complete-forecast rescue audit

This follows the grid failure report rather than relabeling that report as a
successful rescue. Fixed-share weights now combine complete forecasts, including
direct predictive experts, so the new law is not confined to the old fixed-blend
envelope. That is an explicit mathematical and implementation contract change.

All expert probabilities are clipped to an open Bernoulli interval; priors and
transition weights are normalized. Likelihood normalization remains positive.
Mixture prediction precedes outcome observation and has no mutable read effect.
Delayed evidence uses stored predictions, not post-outcome expert recomputation.
The published model experiment uses immediate feedback and no detector resets;
runtime reset/delay/persistence checks are distinct mechanism evidence.

The selector initially chooses among calibrated baseline, calibrated grid blend,
raw grid and Beta. It does not recalibrate the mixture again. The runtime rejects
active residual application and contextual/hierarchical composition in this mode,
so tested proper loss corresponds to the final scored law. Rank/answer benefit
and residual coexistence are not inferred. No authentication or Anti-Pigeon
authority is expanded. Epoch and policy checks are repeated inside the outcome
transaction; policy stamps also invalidate already stored performance weights.

Protocol and all controls precede the fresh design/confirmation execution. No
parameters were searched. Approximate normal intervals use independent trajectory
means; the simultaneous family has 128 comparisons. The .003 mean-harm ceiling
is not zero harm: two correct-baseline controls regress by about .00013-.00015.
The three target repairs have positive simultaneous gain bounds. Full raw data,
source revision, checksums, and negative results are retained. No real signed
data experiment or production test was performed.

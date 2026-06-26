# Review: 04 Residual Prediction

## Extracted Definitions

- Baseline predictor \(B\).
- Residual composition \(\oplus_{\mathcal{A}}\).
- Operator-like representation \(q\).
- Residual cache \(\mathcal{C}_R\).

## Extracted Claims

- Residual correction can approximate repeated baseline errors.
- CFS is inspiration, not physical equivalence.
- Residual reuse requires thresholded context similarity.

## Math Review

- Severity: high.
- Issue: \(r_t^{obs} \approx q(e_{t+1}) - q(b_t)\) assumes subtraction in \(\mathcal{Q}\), while the spec only says operator-like representation.
- Suggested fix: Define observed residual through a representation-space residual estimator \(\Delta_{\mathcal{Q}}\) rather than raw subtraction.

## Red-Team Review

- Main objection: CFS-inspired language may look decorative unless the composition operator is presented as a constraint pattern.
- Minimum change needed: State that the residual estimator is model-dependent.

## Patch Decision

- Patched observed residual equation to use \(\Delta_{\mathcal{Q}}\) instead of raw subtraction.

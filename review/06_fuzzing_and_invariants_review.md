# Review: 06 Fuzzing and Invariants

## Extracted Definitions

- Fuzzing operator \(\mathcal{F}_{i,\epsilon}\).
- Change score \(\Delta_g\).
- Clamped score \(S_g\).
- Counterfactual event frame.
- Confluence/divergence boundary.

## Extracted Claims

- Property fuzzing can identify candidate invariants.
- Fuzzing can help detect confluence and divergence.
- Thresholds determine stable, unstable, and boundary regions.

## Math Review

- Severity: high.
- Issue: The equation uses \(F_\theta(e)\) even though the predictor is defined over contexts \(C_t \in \mathcal{E}^k\).
- Suggested fix: Define a context-level fuzzing operator \(\mathcal{F}_{i,\epsilon}^{(r)}(C_t)\) and compute \(F_\theta(C_t)\) versus \(F_\theta(\mathcal{F}_{i,\epsilon}^{(r)}(C_t))\).

## Red-Team Review

- Main objection: Without context-level notation, the method looks inconsistent with the prediction model.
- Minimum change needed: Patch notation and prose.

## Patch Decision

- Patched section and `spec/notation.md` to use context-level fuzzing \(\mathcal{F}_{i,\epsilon}^{(r)}(C_t)\).

# Review: 03 Mathematical Framework

## Extracted Definitions

- \(\Gamma_{\Delta_\tau}\): substrate-to-event coarse-graining.
- \(Q_{\Delta_\tau}\): time quantization.
- \(G_t = (V_t, R_t)\): event graph.
- \(F_\theta\): transition model.
- \(\mathcal{L}_{time}^H\): temporal loss.
- \(D_j(I)\): representative-frame divergence score.

## Extracted Claims

- Temporal loss is canonical.
- Event histories may be graphs.
- Representative frames make group boundary tests operational.
- Sparse intervention-effective distinctions justify compression.

## Math Review

- Severity: low.
- Issue: Generic \(\mathcal{E}\) shorthand is defined, so later use is acceptable.
- Suggested fix: No immediate patch required.

## Red-Team Review

- Main objection: \(P(Y \mid do(I), \bar{e}_j)\) assumes intervention semantics not yet fully grounded.
- Minimum change needed: Treat as a proposed diagnostic rather than a proven causal calculus.

## Patch Decision

- No immediate patch required; revisit during final math normalization.

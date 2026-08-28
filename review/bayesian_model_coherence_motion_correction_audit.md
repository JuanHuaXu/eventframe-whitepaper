# Bayesian Model-Coherence and Motion-Certificate Audit

Date: 2026-08-28

Scope: reviewer findings R1--R3 concerning coherence between Bayesian evidence and prediction models, point-template residual stability, and posterior-approximation error. This is a mathematical integration audit, not empirical validation.

## Severity Result

- P1 open: none.
- P2 open: none after the model-coherence correction.
- P3 open: empirical calibration, approximation-bound coverage, and latency remain implementation questions by design.

## Finding Classification

1. **R1, confirmed:** the likelihood and predictive kernel were separately declared, so the term posterior predictive did not enforce one probabilistic model. The ordinary contract now requires one family \(\{\mathbb P_{K,\theta}\}\) whose evidence marginal induces \(L_K\) and whose next-outcome conditional induces \(\mathsf P_{H,K}\). A modular pair must declare a linking restriction and pass untouched forward proper-score and calibration validation before receiving the weaker modular belief-conditioned label.
2. **R2, confirmed:** the fixed-reference motion certificate protected only the scored law. The point template could therefore move while a cached point residual remained anchored to an obsolete template. Motion checks are now component-sensitive: mode \(Q\) requires law stability, mode \(E\) requires template stability, mode \(EQ\) requires both, and the zero record requires neither.
3. **R3, confirmed:** the prior wording did not explicitly allocate posterior-approximation error. Both certified motion bounds now include approximation error propagated through the outcome kernel and mixture fusion, and through \(B_H^{\mathrm{bel}}\) for the template path, in addition to statistical uncertainty.

## Atomic Invariants

**Model coherence.** An ordinary posterior-predictive output has the chain

\[
\mathbb P_{K,\theta}
\longrightarrow L_K
\longrightarrow q_{K,t}^{\mathrm{eff}}
\longrightarrow \mathsf P_{H,K}
\longrightarrow \mathsf Q_t^0
\longrightarrow \mathsf Q_t^R.
\]

If \(L_K\) and \(\mathsf P_{H,K}\) are not induced by one family, the ordinary claim is unavailable even when each object is separately normalized.

**Component-sensitive reuse.** For residual mode \(m_i\), acceptance requires

\[
\begin{array}{c|c}
m_i & \text{required certified margins}\\
\hline
\varnothing & \text{none}\\
E & \mu_i^{\mathrm{tmpl}}\ge0\\
Q & \mu_i^{\mathrm{bel}}\ge0\\
EQ & \mu_i^{\mathrm{bel}}\ge0\text{ and }\mu_i^{\mathrm{tmpl}}\ge0.
\end{array}
\]

**Approximation coverage.** A materialized margin is valid only if its analytic or simultaneous upper bound includes posterior-approximation error propagated to the object being protected. A plug-in posterior distance, law distance, or template distance is not a certificate.

## Falsifiers

1. A valid evidence likelihood paired with an unrelated valid outcome kernel must fail the ordinary posterior-predictive contract.
2. Moving the template beyond tolerance while holding the law fixed must reject point-bearing records but need not reject a law-only record.
3. Moving the law beyond tolerance while holding the template fixed must reject law-bearing records but need not reject a point-only record.
4. Under controlled posterior approximation, the stated simultaneous law/template coverage must be measured; failure invalidates the certificate procedure, not merely one cache entry.

## Hot-Path Boundary

The fast path reads materialized law and template margins and checks only those applicable to the record mode. Constructing confidence bounds, estimating propagated approximation error, and running untouched model-coherence validation remain publication or slow-path work. The additional point-component check is constant work per selected cache record.

## Residual Risk

The corrected contracts prevent arbitrary likelihood/kernel pairing from being labeled posterior predictive and prevent a point residual from surviving unbounded template drift. They do not prove that any concrete model is calibrated, that approximation bounds cover, or that residuals improve outcomes; Experiment 4 now makes those claims falsifiable.

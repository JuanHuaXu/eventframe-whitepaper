# Bayesian Scored-Pipeline Correction Audit

Supplemented on 2026-08-28 by `bayesian_model_coherence_motion_correction_audit.md`, which tightens the model-coherence contract and extends residual motion certification from the law alone to mode-applicable law and template components.

Date: 2026-08-28

Scope: reviewer findings P1.1--P2.4 and adjacent P3 notation issues introduced by the selective Bayesian upgrade. This audit is limited to mathematical formulation and cross-section integration; it is not empirical validation.

## Severity Result

- P1 open: none after the corrections below.
- P2 open: none after the corrections below.
- P3 open: empirical calibration, latency, and coverage behavior remain implementation questions by design.

## Finding Classification

1. **P1.1, confirmed:** the posterior was not an input to the scored law. The correction defines a posterior-predictive kernel and finite mixture, producing \(\mathsf Q_t^0\), and binds the final scored object to the posterior-aware residual output \(\mathsf Q_t^R\).
2. **P1.2, confirmed:** \(D_B\), the compared laws, and simultaneous coverage were undefined. The correction replaces \(D_B\) with normalized Jensen--Shannon divergence \(D_{\mathrm{omit}}\), defines complete local and shadow-expanded scored laws, and names a design-weighted simultaneous confidence sequence.
3. **P2.1, confirmed:** the introduction and runtime chapter disagreed about whether the posterior existed before residual selection. Both now use one canonical order: nominate, activate, update, form the posterior-predictive base, select a compatible residual, compose, gate, and score.
4. **P2.2, confirmed:** residual certificates could silently survive an in-place posterior change. Each entry now binds to a fixed posterior-predictive reference and version. The supplementary model-coherence audit extends this to a law-motion margin for law-bearing records and a template-motion margin for point-bearing records. Out-of-tolerance motion uses the same dependency-closure bump and stale-marking operators as snapping and changepoints.
5. **P2.3, confirmed:** the selection likelihood modeled threshold activation without making frontier nomination total. Nomination and evidence-readiness indicators now extend activation by zero over the finite candidate universe; the selection probability covers the complete process.
6. **P2.4, confirmed:** the fast-path formula omitted selection-probability cost. \(T_{\mathrm{act}}\) and \(T_{\mathrm{sel}}\) are now explicit, and history-independent cost requires bounded exact evaluation or a predeclared bounded approximation.
7. **P3, confirmed in part:** evidence-less graph children are nomination-only; the Bayesian ladder is one aligned object; audit-capacity and Bayesian runtime notation no longer overload the fallback-baseline symbol; all new load-bearing operators are indexed.
8. **Recommendation only:** broader cosmetic renaming of every superscript \(B\) was not required for correctness and was not applied. Existing, typed uses remain distinguishable in the symbol register.

## Atomic Invariants

**Scored-law wiring.** For any prediction origin with valid belief buckets,

\[
(q_{K,t}^{\mathrm{eff}})_K
\longmapsto \mathsf Q_t^0
\longmapsto \mathfrak F_R(\mathsf Q_t^0,b_t^0,C_t;S_{t^-})
=\mathsf Q_t^R
=\mathsf Q_{\Theta_\Gamma}.
\]

Deleting the Bayesian layer leaves the scored law unchanged only in a declared degenerate case: no valid belief bucket, a posterior-predictive map equal to the fallback, or predictive kernels whose posterior mixtures coincide.

**Residual validity.** A law-bearing residual calibrated at reference \(\mathsf Q_i^{0,\mathrm{ref}}\) is reusable only when its posterior-predictive version matches and

\[
\overline D_{i,t}^{\mathrm{bel}}\le\epsilon_i^{\mathrm{bel}}.
\]

A point-bearing record additionally requires the template margin defined in the supplementary model-coherence audit; a joint record requires both. A plug-in distance without analytic or simultaneous uncertainty coverage cannot satisfy either certificate.

**Selective evidence.** \(J_t^{\mathrm{act}}=1\) implies nomination, evidence readiness, and threshold admission. A declared future graph child with no available frame can therefore consume nomination capacity but cannot enter the likelihood.

**Omission claim.** \(U_t^{\mathrm{omit}}\) covers only the declared audit population unless exhaustive coverage or a verified envelope extends it. Empty effective audit support yields no certificate, not zero disagreement.

## Hot-Path Boundary

The direct Bayesian cost now contains candidate construction, activation evaluation, complete selection-probability evaluation, bounded posterior work, and materialized certificate checks. Posterior-motion confidence construction and shadow-expanded omission audits remain outside the direct prediction path. A sub-100-ms claim still requires implementation-specific bounds and measurements for every displayed term.

## Residual Risk

The paper remains a specification. Correct wiring does not establish calibration, useful correction, simultaneous-coverage performance, or latency. Experiment 4 now includes posterior-predictive deletion, component-motion invalidation, and omission-certificate falsifiers.

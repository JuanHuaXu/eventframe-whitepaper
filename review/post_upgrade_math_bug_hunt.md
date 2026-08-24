# Post-Upgrade Mathematical Bug Hunt

Date: 2026-08-24

Scope: all displayed mathematics and cross-section contracts in `src/`, with emphasis on the compatibility, staged-refinement, priority, and hardware upgrade.

Disposition: all confirmed P1 and P2 findings below were corrected in the source, normative notation register, assembled Markdown, and rebuilt PDF. No unresolved P1 or P2 finding remained after the final symbol-resolution and edge-case pass.

## Severity Convention

- P1: invalidates a core formula, safety criterion, or claimed lifecycle invariant.
- P2: can produce an undefined, misleading, or unsafe result for a realistic edge case.
- P3: clarity or completeness issue that does not invalidate the current result.

## Confirmed P1 Findings

1. **Forecast/point type mismatch and normalization conflict.** `A_post` accepted a point event while containing `L_pred`, which requires a probability law. The text also normalized every action component to `[0,1]` while the displayed logarithmic score is unbounded. The residual point operator was not connected to the probability law scored by the proper rule.
2. **Anti-Pigeon diameter was not indexed by contexts.** `D_K` ranged over event frames but evaluated distributions conditioned on associated contexts that were not uniquely determined by those frames. The audit set was frame-valued while the audited object was context-conditional.
3. **Audit coverage did not certify future coverage.** A cover in an undeclared representation metric does not bound unobserved future-distribution divergence without a verified continuity or Lipschitz condition.
4. **Ontology promotion lacked a harm constraint.** Requiring a minimum number of improved contexts permits promotion despite arbitrarily many or arbitrarily severe regressions elsewhere.
5. **Zero was not an identity for residual composition.** With lossy encoders and admissibility projections, the old event and packet formulas could alter their baselines even when \(r=0\), so a cache miss or no-op packet correction was not guaranteed to return the baseline.
6. **The governing optimizer was ill-typed and assumed attainment.** The paper equated one parameter value with an `argmin` set and did not account for an empty feasible family or an unattained infimum.
7. **The governing design tuple did not determine its own output or constraints.** It omitted the residual Markov kernel, key maps, gates, context metric, comparison maps, thresholds, and confidence procedures used by \(\mathcal O_\Theta\) and \(D_K(\Theta)\).

## Confirmed P2 Findings

1. The log-score no-event branch referenced an undefined waiting-time variable instead of the probability mass of the declared null outcome.
2. The sparsity ratio was undefined for an empty candidate set.
3. Exact-cache miss and a valid zero residual were indistinguishable; the displayed equations did not define the advertised exact-to-general fallback.
4. Compatibility margin was undefined for a cache key with no dependent edges, and epoch invalidation was not tied to every change in a dependent defect bound or map.
5. The Beta posterior mean was called calibrated without an empirical calibration result or complete Beta-Bernoulli assumptions.
6. Packet encoder, decoder, projection, and clipping domains were not fully typed; the candidate reweighting rule used event action for potentially non-event candidates.
7. Fuzzing sampled a partial operator without stating that the validation distribution is supported on its domain, and used an untyped predictor symbol.
8. The abstraction state space collided with the marked-outcome notation.
9. Compatibility maxima were undefined on an edgeless graph and did not require simultaneous confidence coverage across selected edges.
10. Local reconciliation ignored boundary edges, could have an empty argmin without existence conditions, and lacked an explicit safe spectral step-size condition.
11. Stage 4 could rerun earlier stages without charging repeated work to the resource budget.
12. Priority-weighted relative gain was undefined when baseline weighted loss was zero; stage-promotion confidence did not state paired or multiple-comparison handling.
13. The causal distance was an effect magnitude relative to a reference law, not a signed or uniquely identified causal effect.
14. Conditional-law suprema ranged over arbitrary contexts, including zero-probability contexts where a regular conditional law is defined only up to version choice.
15. The mixed continuous/discrete logarithmic score omitted its dominating reference measure and fixed time units, making the event density and cross-run score comparison underspecified.
16. The exact-cache indicator referenced tuple fields even when the partial cache key was outside the cache domain.
17. The particle reweighting denominator could be zero because non-emptiness and positive total initial weight were unstated; cache margins also used non-simultaneous edge bounds.
18. The coverage theorem substituted a noisy estimator for the true audit diameter and claimed a false sample-wise ordering \(\widehat D_K\le D_K\).
19. Exact-cache confidence could be updated from the final fallback bundle, allowing a general-cache residual to receive credit or blame for a different exact-key candidate.
20. Priority was pre-outcome but not explicitly frozen across candidate systems, permitting a candidate-dependent priority rule to game its own weighted objective; weight integrability was also unstated.
21. The upgrade-promotion bound mixed uncertain predictive gain with hardware cost without covering resource-estimation uncertainty, and divided by an undeclared positive latency budget.
22. The governing Anti-Pigeon constraint included buckets with empty admissible context families, for which the displayed future-diameter supremum was undefined.
23. Evaluation domains, thresholds, weights, and confidence rules were mixed into the candidate design contract, allowing a candidate in principle to weaken the test used to judge itself.

## Non-Patch Classifications

- **Recommendation only:** prove online regret or convergence under drift. The paper already labels this open.
- **Recommendation only:** claim full sheaf structure. The paper correctly limits itself to a sheaf-compatible scaffold.
- **Stale:** the earlier unsupported `operatorname` GitHub-math issue is absent from the current source.

## Patch Invariants

1. Every proper score receives a probability law; every point diagnostic receives a point decision.
2. Bounded composite utility is distinct from the untransformed proper score and is not called proper after nonlinear normalization.
3. Every residual used to claim proper-score improvement induces a declared probability kernel, not only a point shift.
4. Anti-Pigeon audits range over contexts and certify unseen contexts only under an explicit coverage-to-future continuity bound.
5. Promotion requires paired held-out gain and an explicit harm bound.
6. Every cache certificate has defined empty-set behavior and is invalidated by all dependency changes.
7. Every staged invocation, including reruns, consumes the hardware-indexed budget.
8. Conditional-law suprema range only over a declared admissible/support domain, and partial maps are never evaluated before domain membership is established.

## Falsifiers

- A remaining call to `A_post` with only a point event falsifies invariant 1.
- A claim that normalized log loss remains strictly proper falsifies invariant 2.
- A certified Anti-Pigeon upper bound without a continuity assumption or exhaustive domain falsifies invariant 4.
- A promotion rule based only on the count of improvements falsifies invariant 5.
- A stage rerun not represented in cumulative cost falsifies invariant 7.

## Verification

- Display-math delimiters balance in the assembled Markdown.
- No stale point-only action calls, frame-valued audit sets, false audit-estimator ordering, old optimizer equality, or unsupported `operatorname` macro remain.
- Two XeLaTeX passes complete without errors, undefined references, underfull boxes, or overfull boxes.
- All 41 PDF pages were rendered with Poppler; full-document contact sheets and the repaired formula pages were visually inspected.

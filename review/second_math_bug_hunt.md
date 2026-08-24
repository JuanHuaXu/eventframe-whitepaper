# Second Mathematical Bug Hunt

Date: 2026-08-24

Scope: independent adversarial pass over the governing objective, residual lifecycle, Anti-Pigeon certification, causal notation, staged runtime accounting, and evaluation protocol. This pass starts from counterexamples rather than the first audit's symbol checklist.

## Patch Gate

- Symptom: several formulas remain satisfiable by systems that do not preserve real future behavior, or compare quantities with incompatible types or data domains.
- Root-cause candidates tested: stale notation only; missing edge-case domains; candidate self-certification; lifecycle mismatch; evaluation reuse. The last three survive cross-section checks.
- Chosen hypothesis: the upgrade added locally valid equations without fully separating candidate-controlled objects, world/reference quantities, and independent confirmation data.
- Falsifier: a declared external target law for Anti-Pigeon, an operational factorization through the abstraction, disjoint design/confirmation samples, and one unambiguous type for every symbol would disprove the central findings. Those contracts are absent.
- Hot-path cost: the proposed cache fix adds constant-size metadata checks; the other proposed repairs affect slow-path validation or paper semantics, not fast-path asymptotic lookup.
- Confidence: high for the confirmed findings below; no implementation exists, so empirical performance claims remain outside this audit.

## Confirmed P1 Findings

1. **Anti-Pigeon is self-certified by the candidate predictor.** The governing constraint and coverage theorem use \(P_\Theta(Y\mid C)\). A candidate that emits the same forecast for every context has \(D_K(\Theta)=0\), even when the real conditional futures differ. This invalidates Anti-Pigeon as a guard against hidden real-world divergence. Proposed repair: define a fixed target/reference law \(P_\star(Y\mid C)\), use its estimators and confidence bounds for admissibility, and retain model-forecast diameter as a separate diagnostic.

2. **The abstraction need not be operationally used.** The predictor, exact key, and general key consume detailed \(C\), while \(\pi\) is optimized separately. Setting \(\pi\) constant can make abstraction tests and representation cost look favorable while \(\mathsf Q_\theta\), \(B\), \(\alpha\), and \(\kappa\) continue using all detailed context. Proposed repair: require compressed-path maps to factor through a declared operational abstraction key, including any retained side information, and charge all side information to representation cost.

3. **The empirical governing objective selects and evaluates on the same distribution.** \(P_{\mathrm{eval}}\) appears inside the infimum, while the text calls a fixed validation set an empirical realization of that objective. Optimizing candidates on that set invalidates later claims from the same set. Proposed repair: separate a design/objective distribution or sample from an untouched confirmation distribution, and freeze the candidate before confirmation.

4. **Distributional residual correction bypasses the clipping bound.** Point composition applies \(\mathrm{clip}_{\delta_E}(r)\), but the scored law uses \(\mathfrak K_E(r)\) directly. Thus an arbitrarily large cached residual is bounded for the point output but unbounded for the probability law and proper score. Proposed repair: define one effective residual \(\bar r=\mathrm{clip}_{\delta_E}(r)\) and use it in both point and law correction.

5. **The governing and promotion rules do not protect the primary proper score.** They optimize or promote using the nonlinear bounded action \(\mathcal A_{\mathrm{post}}\), which is explicitly not proper after transformation. A candidate may improve that composite while worsening the untransformed proper forecast score. Proposed repair: add an independently evaluated proper-score non-inferiority constraint, with a stricter improvement criterion when forecast improvement is claimed.

6. **\(d_Y\) has incompatible types.** Section 4 defines \(d_Y:\mathcal V_{Y,\mathrm{adm}}\to\mathcal Y_{\mathrm{pkt}}\) as a packet decoder. Sections 3 and 6 use the same symbol as a distance between probability laws. Proposed repair: retain \(d_Y\) for the decoder and rename the law distance \(D_Y^{\mathrm{law}}\) everywhere.

7. **Optimizing \(\Gamma_{\Delta_\tau}\) is incompatible with an expectation over fixed contexts.** \(\Gamma_{\Delta_\tau}\) is inside \(\Theta\), but \(P_{\mathrm{eval}}\) is written over \((C,Z)\). Different coarse-grainings create different context spaces and can change event labels, so the candidates are not functions on one declared sample space. Proposed repair: state the governing objective at fixed \(\Gamma\), or compare coarse-grainings on a common raw-history sample with a target defined independently of each candidate.

8. **Mutable runtime state is not indexed "as of" prediction time.** \(\mathcal C_A\), \(\mathcal C_R\), confidence trial sets, epochs, audit sets, abstraction maps, and thresholds are written as timeless objects. In a retrospective run, nothing in the formulas prevents prediction at time \(t\) from reading residuals or confidence learned from outcomes after \(t\). Proposed repair: evaluate with a left-limit state \(S_{t^-}\); every retrieved item must have an availability timestamp no later than prediction time, and every historical prediction must be replayed from a snapshot containing only then-available state.

9. **"Held out" does not impose temporal separation.** The experimental protocol does not require rolling-origin or forward-chaining evaluation. Randomly splitting overlapping event windows can put later outcomes, duplicate trajectory fragments, or post-change regimes into model selection before earlier test predictions. Proposed repair: require trajectory-grouped rolling-origin splits with an embargo at least as long as the maximum context, outcome horizon, and label delay; reserve a final untouched time block for confirmation.

## Confirmed P2 Findings

1. **General-cache metadata is recorded but not enforced.** \(s_i\) contains age, support, provenance, and loss, yet \(r_t^*\) is accepted using only nearest-key distance. It also lacks the exact cache's epoch and compatibility checks. Proposed repair: define a general-cache acceptance indicator with explicit metadata, epoch, margin, and miss semantics.

2. **The early general-cache gate references the final output bundle.** \(\mathcal R_{\mathrm{pre}}(\mathcal O_t^R\mid C_t)\) appears before exact-to-general selection and before \(\mathcal O_t^R\) is defined. Proposed repair: gate the general candidate \(\mathcal O_t(r_t^*)\) there, and gate the final selected bundle once after selection.

3. **Auxiliary field loss is undefined for no-event outcomes.** \(\mathcal L_i\) dereferences \(e_{t+1}\) even when \(Z_{t+1}=\varnothing\). Proposed repair: condition field loss on a concrete event or define an explicit missing/no-event penalty.

4. **The bounded score transform can erase impossible forecasts.** Only monotonicity is required; a constant transform is allowed and \(g_{\mathrm{pred}}(+\infty)=1\) is not required. Proposed repair: require order preservation on the declared finite score range, maximum loss at \(+\infty\), and the proper-score guard from P1-5.

5. **The representation penalty has no declared domain.** \(\lambda_{\mathrm{rep}}\) is absent from the frozen evaluation contract and is not required to be non-negative. Proposed repair: freeze \(\lambda_{\mathrm{rep}}\ge0\) and the definition/normalization of \(\mathcal C_{\mathrm{rep}}\).

6. **Predicted cost is treated as a resource-budget guarantee.** Stage admission uses \(\widehat C_t\le\mathcal B\), but no error bound or actual hard stop prevents underprediction from exceeding the budget. Proposed repair: use a conservative cost UCB or distinguish predicted admission from an enforced measured budget with overrun handling.

7. **Slow-path cost multiplication assumes uniform invocation cost.** \(M_fT_{\mathrm{predict}}\) and \(M_cT_{\mathrm{causal}}\) are incorrect when invocation costs vary by perturbation or intervention. Proposed repair: sum per-invocation costs, retaining multiplication only as a stated equal-cost special case.

8. **Stage evaluation does not match the upgraded recurrence.** The runtime permits repeated and reordered stages \(r_n\), while the experiment reports only adjacent one-pass stages \(j-1\) and \(j\). Proposed repair: evaluate complete policies or invocation sequences and attribute marginal gains only under a preregistered sequence/ablation design.

9. **Regime-conditioned divergence can condition off support.** \(P_\Theta(Y\mid C_i,\zeta_a)\) and \(P_\Theta(Y\mid C_i,\zeta_b)\) are compared without requiring \(C_i\) to have support in both regimes. Proposed repair: restrict comparisons to declared common support or use an explicit transport/overlap assumption.

10. **Overlapping contexts are counted as independent evidence.** The Beta cache model assumes conditionally independent Bernoulli trials, while adjacent windows from one trajectory share most frames and may repeat one underlying event. Ordinary confidence intervals over such cases can be severely overconfident. Proposed repair: define the independent unit, use trajectory/episode clusters or blocked uncertainty estimates, and report effective rather than raw support.

11. **Outcome availability is not formalized.** A no-event label is known only after horizon \(H\), and other targets may arrive after an additional delay. Merely requiring \(u<t\) would still permit premature updates. Proposed repair: define an availability time \(a_u\) and allow trial \(u\) into state \(S_{t^-}\) only when \(a_u<t\).

12. **Preprocessing and priority can be future-trained while remaining prediction-time functions.** A priority value may use only current inputs at inference yet still come from a model fitted on future labels; the same applies to \(\Gamma\), event extraction, metrics, thresholds, and continuity constants. Proposed repair: fit every learned preprocessing and policy object inside each training window, record its fit cutoff, and freeze it through the corresponding validation/test block.

13. **Repeated monitoring lacks a sequential-testing contract.** Cache confidence, split/merge decisions, and stage promotion may be checked after every new outcome. Fixed-sample UCB/LCB coverage does not survive optional stopping automatically. Proposed repair: use confidence sequences, alpha spending, or preregistered review times and include all repeated looks in multiplicity control.

## Recommendation Only

- Prove regret or online convergence under drift; the paper already labels this open.
- Require a one-sided lower confidence bound for fuzzing stability rather than merely saying "confidence interval." This improves protocol precision but does not invalidate the current conceptual definition.
- Declare \(\delta_{\mathrm{pkt}}>0\) and finite-state potential domains explicitly. These are narrow domain clarifications rather than current core failures.

## Proposed Patch Invariants

1. A candidate never supplies the world/reference law, evaluation sample, threshold, weight, or cost certificate used to judge itself.
2. Any claimed abstraction changes the information actually available to prediction and retrieval, with retained side information declared and charged.
3. Point and distributional residual paths use the same clipped effective residual and the same validity state.
4. A system-action improvement cannot authorize a forecast change that fails independent proper-score non-inferiority.
5. Every cache path validates freshness, support, provenance, compatibility, and miss state before use.
6. Every comparison is defined on common support and every reported budget distinguishes prediction from enforcement.
7. A prediction at time \(t\) is a function only of raw observations and derived state whose availability timestamps are strictly earlier than that prediction.
8. Model selection, threshold tuning, and adaptive review never reuse the untouched temporal confirmation block.

## Status

User approval was received on 2026-08-24. All nine confirmed P1 findings and all thirteen confirmed P2 findings have been corrected in the paper and normative notation. The recommendation-only clarifications for one-sided fuzzing confidence and \(\delta_{\mathrm{pkt}}>0\) were also incorporated.

Verification completed after the patch:

- The paper was rebuilt from `src/` into `build/paper.md`; display equations use GitHub `$$` blocks, with no `\operatorname` macro or stale `P_{\mathrm{eval}}`, candidate-law Anti-Pigeon, causal `d_Y`, uniform slow-path multiplication, or adjacent-stage gain notation.
- The PDF compiled twice under XeLaTeX with no warnings, overfull boxes, underfull boxes, undefined controls, or errors.
- All 44 final PDF pages were rendered and visually inspected, including the governing objective, residual gates, Anti-Pigeon certificate, runtime diagram, policy comparison, symbol index, and references. No clipping, overlap, blank page, broken formula, or broken diagram was observed.
- The paper remains a proposed framework without implementation results; these repairs establish internal mathematical and evaluation-protocol consistency, not empirical validation.

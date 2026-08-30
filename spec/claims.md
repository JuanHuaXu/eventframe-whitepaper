# Claims Register

## Current Experiment Results

The result labels are local to the declared fixture. **Validated in fixture** means the frozen proposition met its stated test; **Falsified in fixture** means it failed; **Inconclusive** means the declared evidence requirement was not met; **Not tested** means no reported experiment addresses it. None of these local outcomes is automatically universal.

| Claim | Tested proposition | Result | Evidence and boundary |
| --- | --- | --- | --- |
| 2b | Frontier-all improves candidate-level probability quality over no Bayesian update. | Validated in fixture | Priority-weighted Brier improved by 9.29% in the frozen bounded-frontier experiment. |
| 2b | The tested 5%-activation selective policy retains the frontier-all quality gain. | Falsified in fixture | It improved priority-weighted Brier by 0.16%, versus 9.29% for frontier-all; paired stress Brier was 0.02891 worse than update-all. |
| 2b | Frontier-all cheap updates plus selective deep work retain frontier-all forecast output. | Validated in synthetic mechanism fixture | Brier, priority-weighted Brier, and recall at 10 exactly matched frontier-all. |
| 2b | The tested Bayesian policies repair post-shift recall at 10. | Falsified in fixture | Every policy measured 0.3000 after the shift. |
| 2 | Stable recurring residual bias is correctable. | Validated in fixture | Brier loss fell by 29.81% in the repeated-bias fixture. |
| 2 | Residual reuse adds gain in the original frontier generator. | Falsified in fixture | The measured incremental gain was zero. |
| 2 | Heterogeneous residual reuse meets gain and false-reuse safety criteria. | Falsified in fixture | Mean gain was 0.01931, 95% bootstrap [0.00614, 0.03280], but harmful reuse was 41.34%, 95% Wilson [38.90%, 43.82%], above the 5% ceiling. |
| 2 | An abstaining residual expert meets positive-gain and cumulative trajectory-harm criteria. | Validated in synthetic confirmation fixture | Mean gain was 0.01378, 95% bootstrap [0.00904, 0.01863], and worst-trajectory excess 0.00909 stayed below the 0.02 budget; 256/861 applied cases were still individually harmful. |
| 6 | A correct split improves an invalid broad bucket. | Validated, mechanism only | Oracle splitting improved Brier by 29.41%; certificate coverage was not tested. |
| 2b, 6 | The comparator nominates divergent groups. | Validated in fixture | Independent confirmation split 64/64 strong and 58/64 moderate groups without a false share. |
| 2b, 6 | The comparator positively recognizes compatible noisy groups at tested support. | Falsified in fixture | All compatible noisy groups remained uncertain. |
| 2b, 6 | The practical-equivalence comparator recognizes compatible and divergent groups. | Validated in synthetic confirmation fixture | It recommended share for 61/64 compatible groups and split for 60/64 moderate and 64/64 strong divergent groups, with zero wrong terminal decisions. |
| 2b, 6 | The comparator preserves Anti-Pigeon authority. | Validated in integration fixture | It did not mutate posterior keys or certificates. |
| 2b, 6 | Validated contradictory member evidence can revoke active sharing without certifying a replacement merge. | Validated, mechanism only | Synthetic integration exercised atomic split and split-reset transitions; the real-session replay did not install sharing certificates. |
| 2b, 6 | Discounted pooled updates retain full-strength member divergence evidence. | Validated, mechanism only | Integration controls preserved direct member counts while reducing pooled effective support. |
| 2b, 2c | The corrected EventFrame-corpus pipeline improves retrieval and Brier over no update on the reserved Codex split. | Supported in retrospective confirmation-split replay | Across 138 cases in three trajectories, Brier improved 0.26117 to 0.24121, Recall@10 0.36192 to 0.46087, and packed recall 0.27585 to 0.37200; cluster intervals were positive. Shuffled feedback reduced both retrieval metrics. |
| 2c | Rank-boundary modulation improves retrieval over the preceding full upgrade under the corrected representation. | Not retested | The former organic result is superseded because raw transcript text participated in its semantic corpus. |
| 2c | Rank-boundary modulation preserves bidirectional correction and its hard envelope. | Validated in synthetic mechanism confirmation | 200/200 promotions, 200/200 demotions, 90/90 useful controls retained, zero churn, and zero of 50 wide-margin crossings. |
| 2b, 2c | The corrected EventFrame-corpus pipeline improves both Brier and ECE. | Mixed; not validated | Brier improved by 0.01996, 95% trajectory-cluster interval [0.00978, 0.04238], while ECE worsened 0.14072 to 0.17976. The old cross-regime calibration result is superseded with the full-text runs. |
| 2b | The original changepoint detector handles noisy and gradual drift. | Falsified in fixture | Miss rates reached 96.88%, 100%, and 93.75%. |
| 2b | The revised monitor generalizes across frozen synthetic confirmations. | Mixed; not robustly validated | Earlier v6 confirmation passed all cases; a later untouched run missed the gradual alarm ceiling by 0.003125 alarms per trajectory. |
| 2b | Omitted-influence bounds attain coverage on the declared finite synthetic population. | Validated in synthetic fixture only | 256/256 bounds covered; Wilson 95% lower 0.9852. Mean UCB 0.21999 versus true mean 0.00526 was too loose for typical certification. |
| 8b | Accepted snaps improve scored forecasts in the current runtime. | Falsified in integration fixture | Graph and dependent versions changed, but scores, rank deltas, templates, and forecast laws did not. |
| 8b | Graph publication affects nominated-candidate features and rank deltas and rollback removes them. | Validated, mechanism only | Integration controls passed; untouched forecast benefit remains untested. |
| 1 | Structured frames improve the reserved chronological block. | Inconclusive | Only two independent trajectories and no interpretability ratings were available. |
| 1 | The matched-ablation evaluator enforces equality and evidence-minimum contracts. | Validated, mechanism only | It rejects mismatches and refuses readiness below three trajectories or without blinded ratings. |
| 8c | Priority weighting reduces high-priority misses. | Inconclusive | Baseline and EventFrame both had a 7.5% high-priority miss rate in the two-trajectory block. |
| 8c | The priority deployment gate prevents aggregate gain from hiding excess critical misses. | Validated, mechanism only | A positive-aggregate-gain control with additional high-priority misses was rejected. |
| 7, 7a | Corrected EventFrame-corpus recall remains below 100 ms local sequential p99. | Validated, narrow benchmark | At 1,000 local SQ8 events, p99 ranged 9.988--11.014 ms; concurrency, remote transport, and external embeddings were excluded. |
| 7, 7a | Corrected EventFrame-corpus recall remains below 100 ms p99 under the tested 16-worker mixed workload. | Falsified in runtime fixture | Earlier embedded and remote runs measured 218.75 and 219.85 ms p99. The final rescued embedded runtime measured 378.831 ms p99 with zero request errors; the strict tail proposition remains false on the tested hosts. |
| 7, 7a | The rescued embedded runtime provides practical single-host mixed-load capacity with sub-100 ms recall p50 and p95 on the named fixture. | Supported descriptively; not preregistered | A 10-core, 16 GB Apple M4 Mac mini sustained 200.77 operations/s with zero errors, 42.314 ms recall p50, and 63.848 ms recall p95 under approximately 90%-recall/10%-capture traffic. Recall p99 remained 378.831 ms. |
| 2b, 7 | Explicit useful outcomes update the exact posterior and survive restart. | Validated, mechanism only | Ten exact-journal outcomes moved Beta(1,1) to Beta(11,1), probability 0.916667; the posterior and +0.067814 rank delta survived restart. |
| 2c, 7 | Learned rank correction improves answer output through isolated OpenClaw. | Inconclusive | Boundary tests produced no nonzero rank deltas; the five-case organic smoke test had identical candidate order in both arms. |
| Other empirical claims | All propositions not listed above. | Not tested | Their protocols remain proposed future work. |

Each major claim in the paper should be tracked here and revised conservatively.

## Claim 0: Adaptive event abstraction is the governing principle

At a fixed resolution, EventFrame uses an external target-law constrained population objective as an oracle benchmark. Operational selection minimizes empirical normalized priority-weighted post-observation action plus non-negative declared representation cost over a finite candidate family whose Anti-Pigeon and proper-score constraints have predeclared certificates. Oracle feasibility and empirical certifiability are distinct. The design- and confirmation-generating laws are distinct from their realized chronological samples; priority, preprocessing, target, and weights are frozen before confirmation outcomes. Prediction-time gating uses a separate pre-observation risk and as-of state.

Status: organizing mathematical claim; requires implementation evidence, ablation tests, and future convergence analysis.

## Claim 1: Structured events are useful predictive units

Event frames provide compressed fields for who, what, when, where, why, and how, making prediction and error analysis more interpretable than unstructured sequence records alone.

Status: conceptual claim; requires experiments.

## Claim 1a: Event frames are compressed representations, not fundamental ontology

The modeled substrate may contain more detail than a usable event representation. EventFrame treats event frames as task-relative coarse-grained records. Planck scales and entropy bounds provide only a limiting thought experiment for physical substrates and do not prove this modeling hypothesis. Simulated and software substrates require independent justification.

Status: modeling assumption and conceptual claim; should be framed conservatively and linked to entropy-bound and coarse-graining motivations rather than presented as a proven physical result.

## Claim 1b: Temporal precision controls frame granularity

EventFrame may instantiate as many candidate frames as the chosen temporal resolution requires. The precision of the when field controls whether frames are represented at seconds, milliseconds, microseconds, or another declared scale.

Status: representational design claim; requires measurement assumptions and computational-cost reporting.

## Claim 2: Residual caches can reduce prediction cost

When similar contexts or action signatures produce similar transition errors, certified as-of residual caches can approximate corrections without recomputing the full transition. An abstaining residual expert also requires positive-gain and cumulative-harm evidence; failed gates produce shadow evaluation rather than application. A point residual is defined only for an event inside its originating horizon; a separately declared law estimator is defined on both marked and no-event outcomes. A typed record carries independently interpreted point-template and forecast-law components. The full-outcome kernel explicitly governs probability flow into and out of the no-event atom, and the final mark and time are derived coherently from the corrected law. Proper-score improvement requires the law correction and all metadata gates to pass; a joint claim additionally requires complete-bundle validation. Cumulative harm control is not per-application safety.

Status: plausible systems claim; requires cache hit-rate, confidence, validity, and accuracy evaluation. Residual composition should be framed as Causal Fermion Systems-inspired structure, not as a claim that the physical theory directly applies.

## Claim 2a: Runtime prediction packets specialize residual composition

A runtime may use a separately typed packet composition rule to predict \(\widehat{\mathbf y}_{t+1}\) over memory nodes, graph edges, retrieval lane, compaction risk, response mode, and optional control branch.

Status: operational architecture claim; requires usefulness scoring, residual-confidence calibration, particle-set update tests, and ablation against a baseline packet selector.

## Claim 2b: A bounded Bayesian frontier can preserve local work

Vector retrieval, sheaf-inspired compatibility expansion, and as-of causal or predictive adjacency may nominate a bounded belief-update frontier. The reference policy cheaply updates every evidence-ready nominated member; activation selects bounded deep work rather than suppressing that update. Neither policy updates the corpus outside the frontier. A current Anti-Pigeon certificate controls whether admitted events may share a posterior. A bounded practical-equivalence comparison may nominate share, split, or uncertain and a bounded borrowing weight, but cannot authorize sharing or mutate posterior keys. Ordinary posterior-predictive semantics require one declared joint evidence-and-outcome model whose displayed marginals induce the likelihood and outcome kernel; separately modeled components remain modular forecasts. The valid effective posterior family is mapped to the base law that the residual kernel subsequently corrects and the proper score evaluates. A near-constant update claim requires explicit caps on retrieval width, graph degree, candidate universe, frontier size, group size, hypothesis or sufficient-statistic dimension, retained changepoint state, update iterations, and complete nomination-probability evaluation. Informative nomination is included in the likelihood and satisfies a certified positive support condition, or the result is labeled an admission-conditioned working posterior. Independent design-weighted audits use a simultaneous bound on normalized Jensen--Shannon disagreement only for their exact query-journal and declared finite omitted population. Law-bearing residual reuse requires a certified law-motion bound; point-bearing reuse requires a certified template-motion bound; both include propagated approximation error. Synthetic confirmation supports frontier-all/deep-work separation, practical-equivalence recommendations, and finite-population audit coverage without establishing full-stream calibration, useful audit tightness, or real-world performance.

Status: architectural and mathematical proposal with synthetic mechanism and local runtime evidence. Frontier-all remains the cheap-update reference; the tested selective-update policy lost material probability quality, while selective deep-work separation retained frontier-all output. A finite-population omitted-influence estimator attained synthetic coverage but produced loose bounds. Controlled full-stream calibration, independent changepoint replication, real audit coverage, and deep-specialist ablations remain required.

## Claim 2c: Bayesian elastic rank correction can adapt bounded packing

After the external retrieval contract returns a bounded frontier, EventFrame may add a hard-capped rank delta produced by an accepted Bayesian, residual, or versioned graph path. Packing-boundary certainty modulates plasticity, while a separate correction-reliability gate authorizes application. Rank certainty is a score-margin diagnostic, not a posterior probability or proper-scored law. Anti-Pigeon shock revocation invalidates unsafe shared state and dependent residuals but neither creates a correction nor certifies replacement sharing.

Status: mathematical and systems mechanism with synthetic confirmation and retrospective real-session regression evidence. It requires prospective untouched evaluation, direct task-success labels, stability across retrieval regimes, and separate probability-calibration validation.

## Claim 3: Episodic memory and residual cache serve different roles

Episodic memory recalls prior cases. Residual cache recalls reusable corrections. The former stores examples; the latter stores transition adjustments.

Status: definitional and architectural claim.

## Claim 4: Property fuzzing can expose invariants

Validity-constrained perturbation can identify conditional model invariants. It measures predictor sensitivity, not real-world causal effect unless an explicit causal model and identification strategy are supplied.

Status: methodological claim; requires controlled experiments and explicit temporal-error thresholds.

## Claim 5: Lumpability provides a formal route to abstraction

If coarse event projections preserve predictive transition behavior, then detailed event states can be compressed into abstract states for the chosen target.

Status: mathematical claim adapted from state aggregation ideas; needs careful formulation and citations to Markov chain lumpability, state aggregation, and approximate abstraction literature.

## Claim 5a: Event streams can conjoin or diverge over time

Event trajectories need not remain linear independent chains. Multiple streams can become representable as a single aggregate event, while small distinctions can also amplify into divergent downstream predictions.

Status: modeling claim; requires formal treatment as event confluence, branching, and sensitivity analysis.

## Claim 5b: Each event frame group should retain a representative frame

Every group should retain at least one concrete frame for traceability and a coverage-aware context audit set for divergence and convergence tests. One representative alone cannot establish group stability, and non-exhaustive coverage certifies unseen contexts only under a verified continuity bound.

Status: design invariant; requires experiments on boundary detection and cache or abstraction stability.

## Claim 6: Anti-Pigeon prevents invalid abstraction

Abstraction should be earned against the external target law on untouched chronological confirmation data. Candidate-model agreement and Bayesian practical-equivalence evidence are diagnostic proposals but cannot self-certify a bucket. Conditional on valid target-law estimation, audit coverage, simultaneous uncertainty coverage, and any declared continuity bound, a group whose certified context-conditional external future-diameter exceeds threshold should split or be marked divergence-sensitive. This is an empirical certificate, not a theorem that those premises hold. Regime comparisons require common support or an explicit transport model and do not establish causality without identified intervention evidence.

Status: formal design criterion with an empirical certificate; requires experiments on target-law estimation, simultaneous coverage, future-divergence thresholds, regime shifts, split stability, stale-cache decay, false merges, and false-positive refinement.

## Claim 6a: Predictively effective event distinctions may be sparse

Relative to a finite declared candidate set, EventFrame hypothesizes that distinctions whose held-out ablation materially worsens proper risk form a small fraction in compressible domains. A separate causal ratio may be reported only when intervention effects are randomized or otherwise identified. Neither ratio is inferred from the cardinality of a continuous substrate.

Status: modeling hypothesis; predictive and causal ratios require separate falsifiable tests and must not be conflated.

## Claim 7: Fast-path / slow-path separation is computationally useful

Low-latency prediction can be served by memory and residual approximation, while slower computation refines caches and tests invariants.

Status: systems claim; requires latency/quality experiments.

## Claim 7a: Expected fast-path lookup is history-independent under bounded local keys

If key construction, context update, local graph degree, action-key size, and action-residual cache are bounded, expected exact-key lookup is independent of total event-history length. Fallback retrieval and cache maintenance are reported separately.

Status: design property; requires implementation validation and adversarial tests for unbounded key growth or fallback retrieval.

## Claim 8: Heterogeneous abstractions can be tested through explicit compatibility maps

Event groups, resolutions, sensors, local models, or agents may be compared by mapping their predictive laws into declared edge spaces. Edge defects complement within-bucket future-diameter and must preserve unreconciled disagreement for audit.

Status: architectural and mathematical proposal; requires map-validity tests, confidence calibration, and comparison against bucket-only Anti-Pigeon. It is currently a sheaf-inspired compatibility scaffold; it becomes sheaf-theoretic only when the required map laws hold and causal only when SCM semantics are supplied.

## Claim 8a: Full refinement can be integrated without redefining the fast path

A cumulative architecture may retain certified residual reuse while adding compatibility audit, local reconciliation, bounded predictive sheaf snapping, spectral refinement under linear assumptions, and regime-mixture refinement. Hardware improvements may increase the selected depth without changing stage semantics.

Status: systems design claim; requires implementation, stage-by-stage ablation, cost prediction, queue-stability tests, and validation on multiple hardware profiles.

## Claim 8b: Predictive sheaf snapping can revise local abstraction structure without redefining the fast path

A finite, bounded family of local compatibility-graph edits may be selected on chronological design data and accepted only after untouched confirmation. Fixed comparison obligations prevent deletion from masquerading as compatibility. Publication is an atomic graph-key-epoch transition with targeted cache invalidation and rollback. Compatibility improvement alone never promotes a causal edge.

Status: architectural and mathematical proposal; requires implementation, controls against unrestricted graph search and no-snap operation, false-snap and rollback measurement, chronological confirmation, and causal-label audits.

## Claim 8c: Upgrade value must be priority-weighted and utility-normalized

A small average correction can be valuable when it credibly reduces predeclared high-priority failure. Prediction loss, latency, compute, and memory must be converted to a declared common utility scale; priority-weighted results must be reported beside unweighted and stratified results.

Status: evaluation-design claim; requires preregistered priority and utility functions, uncertainty intervals, and manipulation or subgroup-harm audits.

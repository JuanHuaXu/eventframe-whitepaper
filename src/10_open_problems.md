# 10. Open Problems

EventFrame is a framework, not a completed theory. Several open problems must be resolved before it can support strong claims.

The first open problem is the status of substrate-to-frame compression. EventFrame hypothesizes that predictively effective distinctions have a small held-out ablation ratio in compressible domains. A separate causal sparsity ratio is meaningful only where interventions are identified. Physical information bounds provide a limiting analogy only for physical substrates; they do not justify compression in simulated or software systems. A future theory would need to state when a coarse-graining \(\Gamma\) preserves exactly the distinctions needed for prediction and, where applicable, intervention.

The second open problem is formal guarantees. The paper now specifies a finite-dimensional operator space, clipping, admissible projection, and decoder, but does not prove that learned encoders preserve semantic fields or that non-convex admissible projections are stable. The CFS connection remains structural inspiration, not physical equivalence.

The third open problem is online convergence. Finite-state strict descent terminates on a fixed evaluation distribution, and per-evidence-epoch publication budgets can cap immediate thrashing, but real runtimes jointly change posteriors, residuals, epochs, graphs, candidates, and data distributions. No common state metric or Lyapunov function currently covers all of those transitions. Regret, tracking error, cross-epoch oscillation, invalidation cascades, and churn bounds under drift remain open.

The fourth open problem is event scoring. Proper marked-event scores handle identity, time, uncertainty, and censoring, but practical systems still need calibrated component distances over actors, locations, mechanisms, and auxiliary state.

The fifth open problem is grounding. EventFrame assumes that event fields can be extracted or inferred. In many domains, this is difficult. The "why" and "how" fields may be ambiguous, contested, or unavailable. Confidence metadata can record uncertainty, but it does not solve extraction. A robust system must distinguish observed fields from inferred fields and must avoid treating speculation as fact.

The sixth open problem is drift. Residual caches depend on the assumption that similar contexts continue to produce similar transition errors. When the environment changes, old residuals may become harmful. Cache metadata, decay, and slow-path review can reduce this risk, but drift detection remains a core challenge.

The seventh open problem is cache pollution. If the system stores too many residuals, it may memorize noise. If it stores too few, it misses useful corrections. The right update rule may depend on domain, context length, confidence, and the cost of false correction.

The eighth open problem is residual confidence under drift. Residuals are statistical corrections, not causal hypotheses. A stronger theory would specify decay schedules, effective sample size, false-correction costs, and change detection.

The ninth open problem is robust invariant extraction. Fuzzing can identify candidate invariants, but perturbation validity is hard. A counterfactual event may be syntactically valid but semantically impossible. Thresholds may be too permissive or too strict. Invariants may be local, conditional, or unstable under distribution shift.

The tenth open problem is abstraction quality. Approximate predictive lumpability is attractive, but exact lumpability is usually too strong. The framework needs practical criteria for deciding when an abstraction is good enough for one target but unsafe for another. An abstraction that preserves timing may destroy causal explanation.

The eleventh open problem is confluence and divergence detection. A system needs criteria for deciding when event streams have truly become prediction-equivalent and when small distinctions are about to amplify. Bad confluence loses necessary distinctions; bad divergence preserves noise as if it were signal.

The twelfth open problem is audit-set construction. One traceability frame is necessary but insufficient. Future work should compare coresets, boundary examples, reservoir sampling, coverage metrics, and adversarial audits.

The thirteenth open problem is temporal resolution selection. Finer time precision can create more candidate frames and expose divergence boundaries, but it can also increase noise, cache pressure, and false distinctions. The framework needs principled methods for choosing \(\Delta_\tau\), possibly adapting it across domains or event groups.

The fourteenth open problem is multimodal scaling. Event frames may be built from text, sensor streams, images, logs, graphs, or simulations. A unified event representation must allow these sources to contribute without pretending that all fields have the same reliability or comparison rule.

The fifteenth open problem is evaluation design. Synthetic worlds are useful because ground truth is known, but real domains are messier. A credible research program should move from synthetic tests to controlled real-world benchmarks while preserving the ability to inspect fields, residuals, and invariants.

The sixteenth open problem is causal identification. Model graph perturbations measure sensitivity. Future work must specify structural equations, intervention targets, identification assumptions, and transport conditions before promoting predictive dependencies to causal edges.

The seventeenth open problem is empirical evidence. The bibliography and mathematical distinctions are now explicit, but implementation, ablation, and controlled real-world validation remain absent.

The eighteenth open problem is compatibility-map validity. Pairwise comparison maps may be learned incorrectly, may fail to compose, or may erase exactly the distinctions that Anti-Pigeon is intended to protect. A graph of forecasts is not automatically a sheaf, and low edge defect under bad maps is not evidence of global coherence.

The nineteenth open problem is predictive sheaf-snap search. Candidate families must be expressive enough to repair local incompatibility but bounded enough to avoid combinatorial search, repeated-test overfitting, and graph churn. Theory is needed for neighborhood selection, edit penalties, rollback, and cache-hit recovery under drift.

The twentieth open problem is priority calibration. Priority weighting can protect rare consequential cases, but a misspecified or manipulable priority function can hide ordinary harms or overfit a favored subgroup. Priority must be assigned before outcomes and evaluated beside unweighted and stratified results.

The twenty-first open problem is hardware-aware scheduling. The staged architecture permits deeper refinement as hardware improves, but stage-cost prediction, queue stability, energy use, worst-case deadlines, and post-snap cache recovery remain implementation-dependent. Faster hardware does not relax statistical, causal, or safety prerequisites.

The twenty-second open problem is selective posterior calibration. Activation depends on relevance, novelty, topology, and source structure, so the admitted stream is generally not an ignorable sample. Selection-conditioned likelihoods, inverse-probability methods, doubly robust audits, and conservative working-posterior semantics should be compared under misspecification.

The twenty-third open problem is posterior granularity. Anti-Pigeon supplies an external divergence gate for sharing, but optimal split and merge policies under sparse evidence, multiple horizons, source dependence, and drift remain unknown. Over-sharing creates confident category errors; over-splitting wastes evidence and memory.

The twenty-fourth open problem is bounded changepoint inference. Exact Bayesian online changepoint support grows with stream length. Truncation, pruning, and finite-state approximations require error bounds that remain meaningful under selective activation and delayed labels.

The twenty-fifth open problem is omitted influence. A bounded local frontier can miss weak individual signals whose joint effect is material. Independent inactive-event audits estimate this risk only on sampled candidates; coverage guarantees under adversarial or highly correlated omissions remain open.

These open problems define the boundary of the current paper. The framework is useful if it makes prediction, memory, and abstraction more explicit and testable. It should not be presented as a final cognitive architecture, universal predictor, or complete mathematical theory. The conclusion summarizes the role EventFrame can play as a conservative event-centric substrate.

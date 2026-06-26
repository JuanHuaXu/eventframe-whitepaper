# 10. Open Problems

EventFrame is a framework, not a completed theory. Several open problems must be resolved before it can support strong claims.

The first open problem is the status of substrate-to-frame compression. EventFrame assumes that useful event frames are sparse relative to the microscopic substrate and concentrated around intervention-effective distinctions. This is motivated by physical information-bound intuitions, but the paper does not prove it. A future theory would need to state when a coarse-graining \(\Gamma\) preserves exactly the distinctions needed for prediction and intervention.

The second open problem is formal guarantees. The residual composition operator is constrained and Causal Fermion Systems-inspired, but the current formulation does not prove convergence, optimality, or physical equivalence. A future theory would need to specify the representation space \(\mathcal{Q}\), admissibility projection \(\Pi_{\mathcal{Q}}\), decoder \(q^{-1}_{\mathrm{approx}}\), and action-like criterion in enough detail to prove useful properties.

The third open problem is event distance. Temporal loss is the canonical objective, but practical systems also need diagnostic distances over actors, actions, locations, mechanisms, and auxiliary state. These distances may be symbolic, geometric, probabilistic, graph-based, or learned. A poor distance can make similar events appear different or different events appear similar.

The fourth open problem is grounding. EventFrame assumes that event fields can be extracted or inferred. In many domains, this is difficult. The "why" and "how" fields may be ambiguous, contested, or unavailable. Confidence metadata can record uncertainty, but it does not solve extraction. A robust system must distinguish observed fields from inferred fields and must avoid treating speculation as fact.

The fifth open problem is drift. Residual caches depend on the assumption that similar contexts continue to produce similar transition errors. When the environment changes, old residuals may become harmful. Cache metadata, decay, and slow-path review can reduce this risk, but drift detection remains a core challenge.

The sixth open problem is cache pollution. If the system stores too many residuals, it may memorize noise. If it stores too few, it misses useful corrections. The right update rule may depend on domain, context length, confidence, and the cost of false correction.

The seventh open problem is residual confidence theory. The current action-residual update treats residuals as cached causal hypotheses whose confidence is revised by later observations. A stronger theory would specify convergence conditions, decay schedules, false-positive costs, and when a residual should trigger graph intervention rather than eviction.

The eighth open problem is robust invariant extraction. Fuzzing can identify candidate invariants, but perturbation validity is hard. A counterfactual event may be syntactically valid but semantically impossible. Thresholds may be too permissive or too strict. Invariants may be local, conditional, or unstable under distribution shift.

The ninth open problem is abstraction quality. Approximate predictive lumpability is attractive, but exact lumpability is usually too strong. The framework needs practical criteria for deciding when an abstraction is good enough for one target but unsafe for another. An abstraction that preserves timing may destroy causal explanation.

The tenth open problem is confluence and divergence detection. A system needs criteria for deciding when event streams have truly become prediction-equivalent and when small distinctions are about to amplify. Bad confluence loses necessary distinctions; bad divergence preserves noise as if it were signal.

The eleventh open problem is representative selection. Keeping one representative per group is necessary for boundary tests, but choosing a bad representative may hide internal divergence or exaggerate differences between groups. Future work should compare medoids, boundary examples, highest-confidence examples, and adversarial representatives.

The twelfth open problem is temporal resolution selection. Finer time precision can create more candidate frames and expose divergence boundaries, but it can also increase noise, cache pressure, and false distinctions. The framework needs principled methods for choosing \(\Delta_\tau\), possibly adapting it across domains or event groups.

The thirteenth open problem is multimodal scaling. Event frames may be built from text, sensor streams, images, logs, graphs, or simulations. A unified event representation must allow these sources to contribute without pretending that all fields have the same reliability or comparison rule.

The fourteenth open problem is evaluation design. Synthetic worlds are useful because ground truth is known, but real domains are messier. A credible research program should move from synthetic tests to controlled real-world benchmarks while preserving the ability to inspect fields, residuals, and invariants.

The fifteenth open problem is counterfactual graph learning. The current paper sketches graph interventions as slow-path tests for high residual action, but it does not provide a full learning algorithm, regret bound, or graph-backpropagation method. Future work should specify how candidate graph interventions are selected, budgeted, validated, and promoted into residual keys or ontology changes.

The sixteenth open problem is publication-quality references. The current reference section is a placeholder register. A publication draft should replace it with full bibliographic entries for Causal Fermion Systems, lumpability, state aggregation, temporal point processes, causal abstraction, counterfactual learning, and information-bound motivations.

These open problems define the boundary of the current paper. The framework is useful if it makes prediction, memory, and abstraction more explicit and testable. It should not be presented as a final cognitive architecture, universal predictor, or complete mathematical theory. The conclusion summarizes the role EventFrame can play as a conservative event-centric substrate.

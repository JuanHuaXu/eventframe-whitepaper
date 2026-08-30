# 1. Introduction

Prediction systems often operate over sequences whose internal structure is only implicit. A model may receive tokens, vectors, logs, traces, or state observations and learn statistical regularities among them. This can be effective, but it makes some questions difficult to ask directly: which compressed distinction mattered, what changed, when did it happen, where did it occur, why might it matter, and how did it transform the state of the world?

EventFrame begins from a compression premise: a modeled substrate may contain more detail than a prediction system can retain. Event frames are task-relative coarse-grained representations, not assertions about fundamental spacetime. For physical substrates, Planck scales and information bounds motivate a limiting thought experiment [7--9]; they do not prove the compression premise. Simulated and software substrates require independent task- and resource-based justification.

The framework represents experience as event frames selected for predictive and intervention relevance. An event frame is a typed record of an occurrence or transition after compression. It includes the 5W1H fields of who, what, when, where, why, and how, plus auxiliary state and confidence metadata. The goal is not to claim that every domain naturally exposes these fields perfectly. The goal is to create a disciplined representation in which uncertainty, missing fields, competing explanations, and compression choices can still be recorded explicitly.

The core contribution is adaptive event abstraction. At fixed resolution, an external-law population objective defines the constrained oracle benchmark; the operational rule selects from a finite family using certified empirical constraints, post-observation action, and representation cost. It distinguishes model-sensitivity evidence from causal intervention evidence.

At prediction time, EventFrame forecasts both what may happen and when it may happen, including the possibility that no relevant event occurs within the chosen horizon. Forecast probability is evaluated separately from operational usefulness: a system should not be able to purchase a convenient answer by becoming a worse probabilistic forecaster.

The framework separates three jobs that are often blurred together. Episodic retrieval finds prior cases. Bayesian belief memory summarizes accumulated outcome evidence. Residual memory stores reusable corrections to a baseline forecast. These components cooperate, but none is allowed to certify its own abstractions or silently convert predictive association into causal evidence.

Section 2 gives the complete lifecycle in ordinary language before introducing notation. Sections 3--9 then define the representation, mathematics, prediction rule, memory system, abstraction safeguards, and runtime model. The claims register follows those definitions, and the experimental section reports what the current implementation evidence supports, falsifies, or leaves unresolved.

The contributions of this paper are therefore:

1. A compressed event-frame ontology for prediction-oriented representation.
2. A governing optimization principle for adaptive event abstraction.
3. A residual prediction model with constrained composition and action-residual fast-path caching.
4. A bounded Bayesian update frontier with a frontier-all cheap-update reference policy, selective deep review, Anti-Pigeon posterior-sharing control, fail-closed shock revocation, a practical-equivalence split/share diagnostic with bounded borrowing, selection-aware semantics, bounded cumulative changepoint invalidation, and independent audit sampling.
5. A combined episodic, residual, and bounded belief-memory architecture.
6. A validity-constrained sensitivity method for conditional invariants and ontology review.
7. A lumpability-based approach to abstraction.
8. A bounded predictive sheaf-snapping rule for validated local compatibility-graph revision.
9. A fast-path and slow-path reference runtime model with reliability-gated elastic rank correction at the packing boundary.
10. Experiment designs for testing the framework's claims.

These are proposed as a research framework with initial synthetic and local runtime evidence, not as validated real-world results or a fixed implementation. Event-centric latent retrieval itself has prior art [10]. Streaming and sequential Bayesian methods provide prior work for incremental posterior approximation and changepoint monitoring [14--18], while Pattern Markov Chains and shift-aware sequential prediction provide narrower event-forecasting precedents [19,20]. D'Acunto, Di Lorenzo, and Barbarossa's *Networks of Causal Abstractions: A Sheaf-theoretic Framework* provides prior work on coordinating heterogeneous causal abstractions through network sheaves, restriction maps, connection Laplacians, global sections, and mixture causal models [13]. EventFrame's claimed contribution is the typed residual-error and evidence-controlled event-abstraction loop, including bounded frontier updates, optional selective activation, Anti-Pigeon posterior granularity, cache certificates, bounded predictive sheaf snapping, and priority- and hardware-aware staged integration. It does not claim to invent streaming Bayes, particle filtering, online changepoint detection, or event-pattern forecasting. The snapping term is EventFrame terminology for validated local predictive-structure revision, not a theorem or standard operation inherited from sheaf theory. The next section explains how these pieces work together without mathematics.

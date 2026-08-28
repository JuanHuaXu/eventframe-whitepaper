# 1. Introduction

Prediction systems often operate over sequences whose internal structure is only implicit. A model may receive tokens, vectors, logs, traces, or state observations and learn statistical regularities among them. This can be effective, but it makes some questions difficult to ask directly: which compressed distinction mattered, what changed, when did it happen, where did it occur, why might it matter, and how did it transform the state of the world?

EventFrame begins from a compression premise: a modeled substrate may contain more detail than a prediction system can retain. Event frames are task-relative coarse-grained representations, not assertions about fundamental spacetime. For physical substrates, Planck scales and information bounds motivate a limiting thought experiment [7--9]; they do not prove the compression premise. Simulated and software substrates require independent task- and resource-based justification.

The framework represents experience as event frames selected for predictive and intervention relevance. An event frame is a typed record of an occurrence or transition after compression. It includes the 5W1H fields of who, what, when, where, why, and how, plus auxiliary state and confidence metadata. The goal is not to claim that every domain naturally exposes these fields perfectly. The goal is to create a disciplined representation in which uncertainty, missing fields, competing explanations, and compression choices can still be recorded explicitly.

The core contribution is adaptive event abstraction. At fixed resolution, an external-law population objective defines the constrained oracle benchmark; the operational rule selects from a finite family using certified empirical constraints, post-observation action, and representation cost. It distinguishes model-sensitivity evidence from causal intervention evidence.

Given \(C_t=e_{t-k+1:t}\), the system predicts a distribution over event identity, event time, and no event within horizon \(H\). A proper forecast score is the primary probabilistic-fidelity metric because timing-only loss can reward the wrong event at the right time. The complete system design minimizes a separate composite objective under a proper-score guard. Event-aware timing remains an interpretable diagnostic.

The reference prediction procedure has seven steps:

1. Form a context \(C_t\) from the last \(k\) event frames.
2. Construct the bounded Bayesian candidate frontier, require evidence readiness and certified positive support for the recorded total nomination-and-activation rule, and share a cached posterior only under a current Anti-Pigeon certificate; otherwise use working-posterior semantics, preserve separate posteriors, or defer.
3. Map the valid effective posterior family to the posterior-predictive base law \(\mathsf Q_t^0(\cdot\mid C_t)\) and aligned template \(b_t^0\), using \(\mathsf Q_B\) and \(B\) only when no valid belief bucket is available.
4. From candidate-specific state \(S_{\Theta,t^-}\), select an exact-key or general residual record \(\mathbf r_t^{\mathrm{use}}\) only when its distance, confidence, effective support, age, epoch, forecast-horizon equality, compatibility margin, component provenance, posterior-predictive version, and mode-applicable certified law and template motion checks pass.
5. Clip the separately typed point and law residual components, apply the law kernel after \(\mathsf Q_t^0\), derive a mark/time-coherent no-event-capable summary from the corrected law, and apply the pre-observation risk gate to the complete output bundle.
6. Observe the next marked event or no-event outcome and evaluate proper predictive loss.
7. Use a slower refinement process to audit selective updates, detect changepoints, recalibrate beliefs, update residuals, test invariants, revise abstractions, or revise the event ontology.

This procedure explains why the framework includes both memory and residual prediction. Episodic memory stores prior cases. A residual cache stores reusable corrections to a baseline transition. The distinction matters because recalling a similar event and applying a similar error correction are not the same operation. The first supports case-based reasoning; the second supports low-latency approximation when similar contexts produce similar transition errors.

The slow path uses validity-constrained perturbations to test model sensitivity, coverage-aware bucket audits to find hidden divergence, and approximate predictive lumpability to test compression. Causal analysis is a separate optional path requiring structural equations and identification assumptions.

The contributions of this paper are therefore:

1. A compressed event-frame ontology for prediction-oriented representation.
2. A governing optimization principle for adaptive event abstraction.
3. A residual prediction model with constrained composition and action-residual fast-path caching.
4. A selective Bayesian update frontier with Anti-Pigeon posterior-sharing control, selection-aware semantics, changepoint invalidation, and independent audit sampling.
5. A combined episodic, residual, and bounded belief-memory architecture.
6. A validity-constrained sensitivity method for conditional invariants and ontology review.
7. A lumpability-based approach to abstraction.
8. A bounded predictive sheaf-snapping rule for validated local compatibility-graph revision.
9. A fast-path and slow-path reference runtime model.
10. Experiment designs for testing the framework's claims.

These are proposed as a research framework, not as validated results or a fixed implementation. Event-centric latent retrieval itself has prior art [10]. Streaming and sequential Bayesian methods provide prior work for incremental posterior approximation and changepoint monitoring [14--18], while Pattern Markov Chains and shift-aware sequential prediction provide narrower event-forecasting precedents [19,20]. D'Acunto, Di Lorenzo, and Barbarossa's *Networks of Causal Abstractions: A Sheaf-theoretic Framework* provides prior work on coordinating heterogeneous causal abstractions through network sheaves, restriction maps, connection Laplacians, global sections, and mixture causal models [13]. EventFrame's claimed contribution is the typed residual-error and evidence-controlled event-abstraction loop, including selective Bayesian activation, Anti-Pigeon posterior granularity, cache certificates, bounded predictive sheaf snapping, and priority- and hardware-aware staged integration. It does not claim to invent streaming Bayes, particle filtering, online changepoint detection, or event-pattern forecasting. The snapping term is EventFrame terminology for validated local predictive-structure revision, not a theorem or standard operation inherited from sheaf theory. The next section defines the event ontology.

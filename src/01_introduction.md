# 1. Introduction

Prediction systems often operate over sequences whose internal structure is only implicit. A model may receive tokens, vectors, logs, traces, or state observations and learn statistical regularities among them. This can be effective, but it makes some questions difficult to ask directly: which compressed distinction mattered, what changed, when did it happen, where did it occur, why might it matter, and how did it transform the state of the world?

EventFrame begins from a compression premise: a modeled substrate may contain more detail than a prediction system can retain. Event frames are task-relative coarse-grained representations, not assertions about fundamental spacetime. For physical substrates, Planck scales and information bounds motivate a limiting thought experiment [7--9]; they do not prove the compression premise. Simulated and software substrates require independent task- and resource-based justification.

The framework represents experience as event frames selected for predictive and intervention relevance. An event frame is a typed record of an occurrence or transition after compression. It includes the 5W1H fields of who, what, when, where, why, and how, plus auxiliary state and confidence metadata. The goal is not to claim that every domain naturally exposes these fields perfectly. The goal is to create a disciplined representation in which uncertainty, missing fields, competing explanations, and compression choices can still be recorded explicitly.

The core contribution is adaptive event abstraction. At fixed resolution, an external-law population objective defines the constrained oracle benchmark; the operational rule selects from a finite family using certified empirical constraints, post-observation action, and representation cost. It distinguishes model-sensitivity evidence from causal intervention evidence.

Given \(C_t=e_{t-k+1:t}\), the system predicts a distribution over event identity, event time, and no event within horizon \(H\). A proper forecast score is the primary probabilistic-fidelity metric because timing-only loss can reward the wrong event at the right time. The complete system design minimizes a separate composite objective under a proper-score guard. Event-aware timing remains an interpretable diagnostic.

The reference prediction procedure has six steps:

1. Form a context \(C_t\) from the last \(k\) event frames.
2. Compute a baseline forecast law \(\mathsf Q_B(\cdot\mid C_t)\) and conditional event template \(b_t=B(C_t)\).
3. From state \(S_{t^-}\), select an exact-key or general residual \(r_t^{\mathrm{use}}\) only when its distance, confidence, effective-support, age, epoch, forecast-horizon equality, compatibility-margin, and provenance checks pass.
4. Clip one horizon-valid residual, use it for both the conditional event-template correction and the declared full-outcome residual kernel, derive the no-event-capable point summary from the corrected law, and apply the pre-observation risk gate to the coherent output bundle.
5. Observe the next marked event or no-event outcome and evaluate proper predictive loss.
6. Use a slower refinement process to update residuals, test invariants, revise abstractions, or revise the event ontology.

This procedure explains why the framework includes both memory and residual prediction. Episodic memory stores prior cases. A residual cache stores reusable corrections to a baseline transition. The distinction matters because recalling a similar event and applying a similar error correction are not the same operation. The first supports case-based reasoning; the second supports low-latency approximation when similar contexts produce similar transition errors.

The slow path uses validity-constrained perturbations to test model sensitivity, coverage-aware bucket audits to find hidden divergence, and approximate predictive lumpability to test compression. Causal analysis is a separate optional path requiring structural equations and identification assumptions.

The contributions of this paper are therefore:

1. A compressed event-frame ontology for prediction-oriented representation.
2. A governing optimization principle for adaptive event abstraction.
3. A residual prediction model with constrained composition and action-residual fast-path caching.
4. A combined episodic and residual memory architecture.
5. A validity-constrained sensitivity method for conditional invariants and ontology review.
6. A lumpability-based approach to abstraction.
7. A bounded predictive sheaf-snapping rule for validated local compatibility-graph revision.
8. A fast-path and slow-path reference runtime model.
9. Experiment designs for testing the framework's claims.

These are proposed as a research framework, not as validated results or a fixed implementation. Event-centric latent retrieval itself has prior art [10]. D'Acunto, Di Lorenzo, and Barbarossa's *Networks of Causal Abstractions: A Sheaf-theoretic Framework* provides prior work on coordinating heterogeneous causal abstractions through network sheaves, restriction maps, connection Laplacians, global sections, and mixture causal models [13]. EventFrame's claimed contribution is the typed residual-error and evidence-controlled event-abstraction loop, including its predictive Anti-Pigeon criterion, cache certificates, bounded predictive sheaf snapping, and priority- and hardware-aware staged integration. The snapping term is EventFrame terminology for validated local predictive-structure revision, not a theorem or standard operation inherited from sheaf theory. The next section defines the event ontology.

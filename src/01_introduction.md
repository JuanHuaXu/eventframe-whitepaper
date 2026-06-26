# 1. Introduction

Prediction systems often operate over sequences whose internal structure is only implicit. A model may receive tokens, vectors, logs, traces, or state observations and learn statistical regularities among them. This can be effective, but it makes some questions difficult to ask directly: which compressed distinction mattered, what changed, when did it happen, where did it occur, why might it matter, and how did it transform the state of the world?

EventFrame begins from a compression premise. The underlying substrate may be physically or computationally thick: at the physical limit, one can imagine distinctions at scales comparable to Planck length and Planck time. A useful prediction system cannot assign a separate durable event frame to every microscopic distinction. Entropy-bound and horizon-style arguments motivate the conservative view that representable distinctions must be compressed. EventFrame therefore treats the event frame as a coarse-grained representation, not as the fundamental thing itself.

The framework represents experience as event frames selected for predictive and intervention relevance. An event frame is a typed record of an occurrence or transition after compression. It includes the 5W1H fields of who, what, when, where, why, and how, plus auxiliary state and confidence metadata. The goal is not to claim that every domain naturally exposes these fields perfectly. The goal is to create a disciplined representation in which uncertainty, missing fields, competing explanations, and compression choices can still be recorded explicitly.

Conceptually, EventFrame treats prediction as a question about the next structured event. Given a recent context \(C_t = e_{t-k+1:t}\), the system estimates \(\hat{e}_{t+1}\). The canonical loss is temporal: the prediction is evaluated by how far the predicted event time is from the observed event time within a chosen horizon \(H\). This keeps the first version of the framework focused. Other field-level errors can be measured, but the central operational question is whether the framework improves time-to-event prediction while retaining interpretable structure.

The reference prediction procedure has six steps:

1. Form a context \(C_t\) from the last \(k\) event frames.
2. Compute a baseline prediction \(b_t = B(C_t)\).
3. Retrieve a residual correction \(r_t^*\) from a residual cache if the current context matches a prior error pattern.
4. Compose the prediction as \(\hat{e}_{t+1} = b_t \oplus_{\mathcal{A}} r_t^*\).
5. Observe \(e_{t+1}\) and evaluate temporal loss.
6. Use a slower refinement process to update residuals, test invariants, or revise abstractions.

This procedure explains why the framework includes both memory and residual prediction. Episodic memory stores prior cases. A residual cache stores reusable corrections to a baseline transition. The distinction matters because recalling a similar event and applying a similar error correction are not the same operation. The first supports case-based reasoning; the second supports low-latency approximation when similar contexts produce similar transition errors.

EventFrame also proposes a slow path for analysis beyond immediate prediction. Property fuzzing perturbs event fields to test whether predicted outcomes remain stable. Stable properties can become candidate invariants. Event confluence asks whether multiple streams can be represented as one aggregate event without losing target-relevant prediction. Event divergence asks whether a small distinction amplifies into materially different downstream branches. Approximate predictive lumpability then asks whether detailed event frames can be projected into coarser abstract states without losing target-relevant transition behavior. The Anti-Pigeon principle is the corresponding design rule: do not collapse events into broad categories merely because they look similar; require evidence that the collapsed category preserves prediction and does not hide divergence-effective distinctions.

The contributions of this paper are therefore:

1. A compressed event-frame ontology for prediction-oriented representation.
2. A mathematical event-space formulation with temporal prediction loss.
3. A residual prediction model with constrained composition.
4. A distinction between episodic memory and residual cache memory.
5. A property fuzzing method for invariant discovery.
6. A lumpability-based approach to abstraction.
7. A fast-path and slow-path reference runtime model.
8. Experiment designs for testing the framework's claims.

These are proposed as a research framework, not as a finished theory or a fixed implementation. Several claims require empirical validation, especially the utility of residual caches, the stability of invariants discovered by fuzzing, and the quality of learned abstractions. The next section defines the event ontology used by the rest of the paper.

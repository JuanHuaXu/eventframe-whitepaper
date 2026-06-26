# Glossary

## Event

A structured representation of a change, occurrence, action, observation, or state transition.

## Event Frame

A compressed structured event record containing fields such as who, what, when, where, why, and how, plus optional state vectors, confidence, causal links, and residuals.

## Microscopic Substrate

The dense underlying physical, simulated, biological, robotic, software, or computational description from which event frames are coarse-grained. The framework requires only that substrate detail may be much denser than the representable event space.

## Coarse-Graining

The mapping from a dense substrate history to a lower-dimensional event frame or event trajectory.

## Intervention-Effective Event

A compressed event distinction whose alteration would be expected to change the prediction target or downstream state beyond a declared threshold.

## Event Sparsity Hypothesis

The hypothesis that intervention-effective event distinctions are sparse relative to the density of the microscopic substrate.

## Temporal Resolution

The chosen precision of the event time field. A model may choose coarse resolution such as seconds or finer resolution such as microseconds, subject to measurement quality and computational budget.

## Candidate Event Frame

An event frame instantiated or considered at a chosen temporal resolution before it is known whether the frame is intervention-effective or worth retaining.

## 5W1H Ontology

An event-frame schema organized around: who, what, when, where, why, and how. In EventFrame, these are not fundamental physical categories; they are typed fields used for compressed prediction and comparison.

## Event State

A representation of the system before, during, or after an event. May include symbolic fields, vector fields, graph links, and latent variables.

## Event Transition

A mapping from one event state to a later event state.

## Event Confluence

A many-to-one process in which multiple event streams or event frames become representable as a single larger event, aggregate, or macro-event.

## Event Divergence

A one-to-many process in which a small event distinction, perturbation, or intervention leads to multiple downstream event branches or materially different predictions.

## Event Stream

A temporally ordered event trajectory or subtrajectory that can merge with other streams or branch into multiple downstream streams.

## Event Frame Group

A set of event frames treated as equivalent or jointly represented under a chosen abstraction, confluence, cache key, or projection.

## Representative Event Frame

At least one retained event frame for an event frame group. It is used as an anchor for measuring when intervention causes divergence or when multiple events have become safe to merge.

## Prediction

The estimation of a future event frame, event state, or transition from current and prior event context.

## Prediction Context

The finite event history used as input to a prediction step, usually written as \(C_t = e_{t-k+1:t}\) for a context of length \(k\).

## Baseline Predictor

A model, rule, or procedure that produces an initial event prediction before residual correction.

## Prediction Horizon

The time scale \(H\) used to normalize temporal prediction loss and decide when timing errors should be treated as saturated.

## Residual Prediction

A prediction strategy that estimates the difference between a baseline transition and the actual observed transition.

## Residual Composition

The operation that applies a residual correction to a baseline event prediction. In EventFrame, residual composition is treated as a structured, causal-action-inspired update rather than ordinary vector addition.

## Temporal Loss

A bounded measure of prediction error based on the time field of an event frame. It measures how far the predicted event time is from the observed event time within a chosen prediction horizon.

## Threshold Clamp

A bounded decision rule that maps an error magnitude to a fixed interval, usually \([0, 1]\), so that invariance and cache-reuse tests are not dominated by outliers.

## Residual Cache

A memory structure storing reusable transition corrections. It is used when similar contexts produce similar residuals.

## Residual Lookup

The process of retrieving a cached residual correction whose key is sufficiently similar to the current prediction context.

## Action-Residual Cache

A low-latency residual cache keyed by a compact action signature. It stores a residual correction with confidence, support count, and age metadata so the fast path can reuse correction patterns when validity checks pass.

## KV Episodic Cache

A key-value memory structure storing prior event episodes. Keys represent retrieval conditions; values represent event frames, trajectories, or summaries.

## Property Fuzzing

A method for perturbing selected event properties to test whether predictions remain stable or change systematically.

## Invariant

A property or relation that remains stable under a defined class of event perturbations.

## Lumpability

A condition under which many detailed states can be aggregated into a coarser state without losing relevant predictive behavior.

## Anti-Pigeon Principle

A split-side abstraction criterion. If one event-frame group predicts multiple materially different futures, the abstraction is invalid for that target and must be split, refined, or marked divergence-sensitive.

## Fast Path

A low-latency prediction route using cached residuals, episodic retrieval, or learned approximations.

## Slow Path

A higher-cost route using deeper computation, search, simulation, external tools, or background refinement.

## Background Refinement

Asynchronous or deferred computation used to improve future predictions, update caches, or test invariants after an initial response.

## Ontology Self-Organization

The slow-path process of revising, splitting, duplicating, or marking 5W1H field assignments when intervention and fuzzing evidence shows that the initial event ontology is incomplete or misleading.

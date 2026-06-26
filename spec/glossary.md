# Glossary

## Event

A structured representation of a change, occurrence, action, observation, or state transition.

## Event Frame

A compressed structured event record containing fields such as who, what, when, where, why, and how, plus optional state vectors, confidence, causal links, and residuals.

## Microscopic Substrate

The dense underlying physical or computational description from which event frames are coarse-grained. In the physical motivation, this substrate is considered at scales comparable to Planck time and Planck length, but EventFrame does not require a settled theory of quantum gravity.

## Coarse-Graining

The mapping from a dense substrate history to a lower-dimensional event frame or event trajectory.

## Intervention-Effective Event

A compressed event distinction whose alteration would be expected to change the prediction target or downstream state beyond a declared threshold.

## Event Sparsity Hypothesis

The hypothesis that intervention-effective event distinctions are sparse relative to the density of the microscopic substrate.

## 5W1H Ontology

An event-frame schema organized around: who, what, when, where, why, and how. In EventFrame, these are not fundamental physical categories; they are typed fields used for compressed prediction and comparison.

## Event State

A representation of the system before, during, or after an event. May include symbolic fields, vector fields, graph links, and latent variables.

## Event Transition

A mapping from one event state to a later event state.

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

## KV Episodic Cache

A key-value memory structure storing prior event episodes. Keys represent retrieval conditions; values represent event frames, trajectories, or summaries.

## Property Fuzzing

A method for perturbing selected event properties to test whether predictions remain stable or change systematically.

## Invariant

A property or relation that remains stable under a defined class of event perturbations.

## Lumpability

A condition under which many detailed states can be aggregated into a coarser state without losing relevant predictive behavior.

## Anti-Pigeon Principle

A design principle that discourages collapsing events into overly broad categories before predictive distinctions have been tested.

## Fast Path

A low-latency prediction route using cached residuals, episodic retrieval, or learned approximations.

## Slow Path

A higher-cost route using deeper computation, search, simulation, external tools, or background refinement.

## Background Refinement

Asynchronous or deferred computation used to improve future predictions, update caches, or test invariants after an initial response.

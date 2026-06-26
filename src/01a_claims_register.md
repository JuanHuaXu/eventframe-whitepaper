# Claims Register

This section states the paper's major claims as falsifiable targets. The claims are not treated as established results. Each one names what would need to be measured, proved, or falsified by later experiments.

Claim 0. Adaptive event abstraction is the governing principle of EventFrame: a useful implementation should minimize expected surrogate event action plus representation cost while preventing abstraction buckets from hiding future-distinct events.

Claim 1. Structured event frames are useful predictive units if, for a declared task, they improve interpretability or temporal prediction relative to unstructured sequence records without hiding field-level error.

Claim 1a. Event frames are compressed representations, not fundamental ontology, if they can be modeled as coarse-grained records selected from a denser substrate by predictive and intervention relevance.

Claim 1b. Temporal precision controls frame granularity if changing the declared time resolution \(\Delta_\tau\) changes the candidate-frame set, cache pressure, and detectable divergence boundaries in measurable ways.

Claim 2. Residual caches reduce prediction cost or error when similar contexts or action signatures produce similar baseline errors and retrieved residuals improve temporal loss often enough to justify lookup and maintenance.

Claim 3. Episodic memory and residual cache memory serve different roles because prior-case recall and prior-error correction can be independently useful or harmful under the same prediction context.

Claim 4. Property fuzzing exposes candidate invariants and ontology corrections when controlled perturbations of event fields reveal which assigned 5W1H roles are stable, misleading, or target-relevant across validation contexts.

Claim 5. Approximate predictive lumpability provides a route to abstraction when projected event states preserve target-relevant transition behavior within a declared divergence threshold.

Claim 5a. Event streams can conjoin or diverge over time when multiple streams become prediction-equivalent under a merge threshold or when small distinctions amplify into target-distinct downstream futures.

Claim 5b. Each event-frame group should retain a representative frame if later intervention, divergence, and convergence tests need a concrete anchor for the group.

Claim 6. Anti-Pigeon prevents invalid abstraction when an event bucket whose members predict materially different futures is split, refined, or marked divergence-sensitive instead of being retained as one abstraction.

Claim 6a. Intervention-effective event distinctions are sparse if useful prediction and intervention distinctions occupy a small subset of the microscopic or candidate-frame distinctions considered by the model.

Claim 7. Fast-path and slow-path separation is computationally useful if low-latency prediction can reuse cached residuals while slower background work improves future predictions without blocking the current one.

Claim 7a. Expected fast-path lookup is history-independent when the 5W1H field arity, local graph degree, action-key size, and action-residual cache are bounded.

# Claims Register

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

When similar contexts or action signatures produce similar transition errors, certified as-of residual caches can approximate corrections without recomputing the full transition. A point residual is defined only for an event inside its originating horizon; a separately declared law estimator is defined on both marked and no-event outcomes. A typed record carries independently interpreted point-template and forecast-law components. The full-outcome kernel explicitly governs probability flow into and out of the no-event atom, and the final mark and time are derived coherently from the corrected law. Proper-score improvement requires the law correction and all metadata gates to pass; a joint claim additionally requires complete-bundle validation.

Status: plausible systems claim; requires cache hit-rate, confidence, validity, and accuracy evaluation. Residual composition should be framed as Causal Fermion Systems-inspired structure, not as a claim that the physical theory directly applies.

## Claim 2a: Runtime prediction packets specialize residual composition

A runtime may use a separately typed packet composition rule to predict \(\widehat{\mathbf y}_{t+1}\) over memory nodes, graph edges, retrieval lane, compaction risk, response mode, and optional control branch.

Status: operational architecture claim; requires usefulness scoring, residual-confidence calibration, particle-set update tests, and ablation against a baseline packet selector.

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

Abstraction should be earned against the external target law on untouched chronological confirmation data. Candidate-model agreement is diagnostic but cannot self-certify a bucket. If a group's context-conditional external future-diameter exceeds threshold, it should split or be marked divergence-sensitive. Regime comparisons require common support or an explicit transport model and do not establish causality without identified intervention evidence.

Status: formal design criterion; requires experiments on future-divergence thresholds, causal-regime shifts, split stability, stale-cache decay, and false-positive refinement.

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

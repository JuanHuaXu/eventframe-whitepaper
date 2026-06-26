# Claims Register

Each major claim in the paper should be tracked here and revised conservatively.

## Claim 0: Adaptive event abstraction is the governing principle

EventFrame should learn the lowest-action, lowest-unnecessary-complexity event representation that does not hide future-distinct events inside the same abstraction bucket.

Status: organizing mathematical claim; requires implementation evidence, ablation tests, and future convergence analysis.

## Claim 1: Structured events are useful predictive units

Event frames provide compressed fields for who, what, when, where, why, and how, making prediction and error analysis more interpretable than unstructured sequence records alone.

Status: conceptual claim; requires experiments.

## Claim 1a: Event frames are compressed representations, not fundamental ontology

The fundamental substrate may be much denser than any usable event representation. EventFrame treats event frames as coarse-grained records selected for predictive and intervention relevance.

Status: modeling assumption and conceptual claim; should be framed conservatively and linked to entropy-bound and coarse-graining motivations rather than presented as a proven physical result.

## Claim 1b: Temporal precision controls frame granularity

EventFrame may instantiate as many candidate frames as the chosen temporal resolution requires. The precision of the when field controls whether frames are represented at seconds, milliseconds, microseconds, or another declared scale.

Status: representational design claim; requires measurement assumptions and computational-cost reporting.

## Claim 2: Residual caches can reduce prediction cost

When similar contexts or action signatures produce similar transition errors, cached residuals can approximate corrections without recomputing the full transition.

Status: plausible systems claim; requires cache hit-rate, confidence, validity, and accuracy evaluation. Residual composition should be framed as Causal Fermion Systems-inspired structure, not as a claim that the physical theory directly applies.

## Claim 3: Episodic memory and residual cache serve different roles

Episodic memory recalls prior cases. Residual cache recalls reusable corrections. The former stores examples; the latter stores transition adjustments.

Status: definitional and architectural claim.

## Claim 4: Property fuzzing can expose invariants

Perturbing individual event properties and observing stable prediction outputs can identify candidate invariants.

Status: methodological claim; requires controlled experiments and explicit temporal-error thresholds.

## Claim 5: Lumpability provides a formal route to abstraction

If coarse event projections preserve predictive transition behavior, then detailed event states can be compressed into abstract states for the chosen target.

Status: mathematical claim adapted from state aggregation ideas; needs careful formulation and citations to Markov chain lumpability, state aggregation, and approximate abstraction literature.

## Claim 5a: Event streams can conjoin or diverge over time

Event trajectories need not remain linear independent chains. Multiple streams can become representable as a single aggregate event, while small distinctions can also amplify into divergent downstream predictions.

Status: modeling claim; requires formal treatment as event confluence, branching, and sensitivity analysis.

## Claim 5b: Each event frame group should retain a representative frame

Every abstraction group, confluence group, or event-frame cluster should retain at least one representative frame so that future intervention, divergence, and convergence tests have a concrete anchor.

Status: design invariant; requires experiments on boundary detection and cache or abstraction stability.

## Claim 6: Anti-Pigeon prevents invalid abstraction

Abstraction should be earned by invariance or lumpability evidence, not assumed from superficial similarity. If an event-frame group contains members whose predicted future behavior diverges beyond a declared threshold, the group is invalid for that target and should be split, refined, or marked divergence-sensitive.

Status: formal design criterion; requires experiments on future-divergence thresholds, split stability, and false-positive refinement.

## Claim 6a: Intervention-effective event distinctions are sparse

If every microscopic distinction required a unique event frame, the representation would be computationally and physically implausible. EventFrame therefore assumes that useful event distinctions are sparse and concentrated where interventions or predictions change outcomes.

Status: physics-inspired modeling hypothesis; requires careful argument and should be tied to falsifiable compression and intervention tests.

## Claim 7: Fast-path / slow-path separation is computationally useful

Low-latency prediction can be served by memory and residual approximation, while slower computation refines caches and tests invariants.

Status: systems claim; requires latency/quality experiments.

## Claim 7a: Expected fast-path lookup is history-independent under bounded local keys

If the 5W1H field arity, local graph degree, action-key size, and action-residual cache are bounded, expected action-residual lookup depends on local abstraction size rather than total event-history length.

Status: design property; requires implementation validation and adversarial tests for unbounded key growth or fallback retrieval.

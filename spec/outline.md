# White Paper Outline

# EventFrame: A Mathematical Framework for Event-Centric Prediction

## Abstract

Briefly introduce event-centric prediction, structured event frames, residual prediction, memory, fuzzing, invariants, lumpability, and evaluation plan.

## 1. Introduction

- Motivation
- Limits of purely unstructured sequence prediction
- Why events are useful units
- Contributions
- Scope and non-goals

## 2. Event Ontology

- Event frames as compressed, non-fundamental representations
- Microscopic substrate and coarse-graining
- Event definition
- 5W1H fields
- Typed event frames
- Intervention-effective event distinctions
- Event states and transitions
- Event confluence and divergence
- Causal, temporal, and spatial links

## 3. Mathematical Framework

- Substrate-to-event coarse-graining
- Event space
- Event trajectories
- Event graphs, stream merge, and branching
- Transition functions
- Temporal prediction loss
- Intervention-effective sparsity
- Optional event-frame diagnostic distances
- Confidence and uncertainty

## 4. Residual Prediction

- Baseline transition model
- Residual correction model
- Composition operator
- Residual reuse
- Failure modes

## 5. Memory Model

- Episodic memory
- KV episodic cache
- Residual cache
- Similarity lookup
- Consolidation
- Cache pollution

## 6. Fuzzing and Invariants

- Property fuzzing
- Counterfactual event frames
- Invariance testing
- Boundary discovery
- Confluence and divergence detection
- Experimental protocols

## 7. Lumpability and Abstraction

- Projection from events to abstract states
- Merge operators and branching safeguards
- Predictive lumpability
- Abstraction quality
- Anti-Pigeon principle
- Avoiding premature category collapse

## 8. Complexity and Runtime Model

- Fast path
- Slow path
- Background refinement
- Complexity sketch
- O(1) cache lookup as an approximate fast path
- When expensive computation is still required

## 9. Experimental Evaluation

- Synthetic event worlds
- Compression and intervention tests
- Controlled perturbation tests
- Cache hit-rate tests
- Long-horizon prediction
- Invariant stability tests
- Confluence and divergence tests
- Ablation studies

## 10. Open Problems

- Substrate-to-frame compression guarantees
- Formal guarantees
- Event distance metrics
- Grounding symbolic fields
- Drift and cache pollution
- Robust invariant extraction
- Confluence and divergence detection
- Scaling to multimodal data

## 11. Conclusion

Summarize EventFrame as a framework, not a product or agent, and state next research steps.

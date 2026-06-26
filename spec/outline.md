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

- Event definition
- 5W1H fields
- Typed event frames
- Event states and transitions
- Causal, temporal, and spatial links

## 3. Mathematical Framework

- Event space
- Event trajectories
- Transition functions
- Temporal prediction loss
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
- Experimental protocols

## 7. Lumpability and Abstraction

- Projection from events to abstract states
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
- Controlled perturbation tests
- Cache hit-rate tests
- Long-horizon prediction
- Invariant stability tests
- Ablation studies

## 10. Open Problems

- Formal guarantees
- Event distance metrics
- Grounding symbolic fields
- Drift and cache pollution
- Robust invariant extraction
- Scaling to multimodal data

## 11. Conclusion

Summarize EventFrame as a framework, not a product or agent, and state next research steps.

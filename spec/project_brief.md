# Project Brief: EventFrame Whitepaper

## One-sentence summary

The EventFrame Whitepaper presents EventFrame as a framework for representing, predicting, fuzzing, and abstracting events using structured event frames, residual prediction, episodic memory, and invariant extraction.

## Problem

Current predictive systems often operate over tokens, vectors, or unstructured histories. This makes it difficult to reason explicitly about what happened, who acted, where it occurred, why it mattered, how it changed state, and what is likely to happen next. EventFrame proposes structured event frames as compressed predictive representations rather than as fundamental ontology.

## Core Idea

Treat the underlying physical or computational substrate as far denser than any usable event representation. Event frames are coarse-grained records of regions where distinctions matter for prediction or intervention. Fast prediction can use cached residuals, episodic lookup, and bounded cached Bayesian updates over these compressed frames. A bounded frontier limits updates to vector-retrieved, sheaf-inspired, and as-of graph neighbors. The reference policy cheaply updates every evidence-ready frontier member; a threshold selects expensive deep work. Anti-Pigeon controls which events may share a posterior, discounts pooled evidence while preserving member evidence, and can revoke stale sharing after independently valid split evidence. A separate Bayesian elastic rank delta uses packing-boundary certainty and independently established correction reliability to modulate bounded promotion or demotion after retrieval and before packing. Slower computation audits declared omitted populations, runs proposal-only practical-equivalence comparison, detects regime changes with bounded run-length and cumulative state, refines uncertain predictions, discovers invariants by fuzzing event properties, and consolidates memory.

## Contribution Claims

EventFrame contributes:

1. A compressed 5W1H event-frame ontology for prediction-oriented representation.
2. A mathematical event-space formulation that distinguishes microscopic substrate from coarse event frames.
3. A residual prediction model for approximating event transitions.
4. A distinction between episodic key-value memory and residual cache memory.
5. A property fuzzing method for invariant discovery.
6. A lumpability framework for abstraction and state compression.
7. An Anti-Pigeon principle for resisting premature collapse into overly broad categories.
8. A reference runtime model separating fast-path prediction from slow-path refinement.
9. Experiment designs for evaluating prediction accuracy, cache utility, invariant stability, and abstraction quality.
10. A bounded Bayesian update contract with frontier-all and optional selective admission, Anti-Pigeon posterior granularity and shock revocation, proposal-only group comparison, independent audits, and staged changepoint or particle refinement.
11. A hard-capped elastic retrieval correction whose strength decreases with packing-boundary certainty and vanishes without an independently accepted correction path.

## Non-goals

The EventFrame Whitepaper is not:

- A specific chatbot.
- A specific autonomous agent.
- A replacement for all machine learning methods.
- A claim of human-level cognition.
- A fully proven mathematical theory in its first formulation.
- A fixed implementation or product architecture.
- A claim that 5W1H event frames are fundamental physical entities.

## Target Reader

The reader should be assumed to know general machine learning, state-space modeling, caching, and basic mathematical notation, but not any private project names, prior chats, or implementation history.

## Style

The paper should be precise, self-contained, conservative in claims, and explicit about assumptions. Avoid grandiose language. Prefer definitions, equations, algorithms, and falsifiable experiments.

## Expository Contract

The paper must provide both conceptual explanation and operational mathematics.
For each core construct, the reader should be able to answer:

1. Why is this construct introduced?
2. What does it mean intuitively?
3. How is it computed or used during prediction?
4. What assumptions make the computation valid?
5. What failure modes should be expected?

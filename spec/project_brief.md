# Project Brief: EventFrame Whitepaper

## One-sentence summary

The EventFrame Whitepaper presents EventFrame as a framework for representing, predicting, fuzzing, and abstracting events using structured event frames, residual prediction, episodic memory, and invariant extraction.

## Problem

Current predictive systems often operate over tokens, vectors, or unstructured histories. This makes it difficult to reason explicitly about what happened, who acted, where it occurred, why it mattered, how it changed state, and what is likely to happen next. EventFrame proposes an event-centered substrate in which prediction is performed over structured events rather than raw sequence elements alone.

## Core Idea

Represent experience as event frames with structured fields, then learn or compute transitions between event states. Fast prediction can use cached residuals and episodic lookup. Slower computation can refine uncertain predictions, discover invariants by fuzzing event properties, and consolidate memory.

## Contribution Claims

EventFrame contributes:

1. A 5W1H event ontology for prediction-oriented event representation.
2. A mathematical event-space formulation.
3. A residual prediction model for approximating event transitions.
4. A distinction between episodic key-value memory and residual cache memory.
5. A property fuzzing method for invariant discovery.
6. A lumpability framework for abstraction and state compression.
7. An Anti-Pigeon principle for resisting premature collapse into overly broad categories.
8. A reference runtime model separating fast-path prediction from slow-path refinement.
9. Experiment designs for evaluating prediction accuracy, cache utility, invariant stability, and abstraction quality.

## Non-goals

The EventFrame Whitepaper is not:

- A specific chatbot.
- A specific autonomous agent.
- A replacement for all machine learning methods.
- A claim of human-level cognition.
- A fully proven mathematical theory in its first formulation.
- A fixed implementation or product architecture.

## Target Reader

The reader should be assumed to know general machine learning, state-space modeling, caching, and basic mathematical notation, but not any private project names, prior chats, or implementation history.

## Style

The paper should be precise, self-contained, conservative in claims, and explicit about assumptions. Avoid grandiose language. Prefer definitions, equations, algorithms, and falsifiable experiments.

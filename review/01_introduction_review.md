# Review: 01 Introduction

## Extracted Definitions

- Event frame: typed compressed record after coarse-graining.
- Reference prediction procedure: context, baseline, residual, composition, loss, slow-path update.
- Event confluence/divergence: merge and branch tests for event streams.

## Extracted Claims

- Structured event frames improve interpretability.
- Residual caches and episodic memory have distinct roles.
- Abstraction should preserve prediction and not hide divergence-effective distinctions.

## Math Review

- Severity: low.
- Issue: Procedure is operational and references notation defined later.
- Suggested fix: No immediate patch required.

## Red-Team Review

- Main objection: Entropy-bound and horizon-style motivation can be challenged.
- Minimum change needed: Keep it as motivation, not proof.
- Citation need: Physical-information references are placeholders in `spec/references.md`.

## Patch Decision

- No patch required for this section in Phase 3.

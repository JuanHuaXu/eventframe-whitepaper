# Writing Rules

## Hard constraints

1. Do not mention any private project, chatbot, agent name, or prior conversation.
2. Do not present speculative ideas as proven results.
3. Every equation must define variables and interpretation.
4. Every major claim must map to `spec/claims.md` or be added there.
5. Prefer conservative academic phrasing.
6. Distinguish framework, algorithm, and implementation.
7. Use examples only when they clarify a definition.
8. Avoid marketing language.
9. Keep notation consistent with `spec/notation.md` unless revising that file deliberately.
10. If a term is introduced, add it to `spec/glossary.md`.
11. If a claim depends on external literature, add or update a placeholder in `spec/references.md`.
12. Every core construct must include both conceptual explanation and operational use.

## Equation template

For each equation include:

- Equation
- Variables
- Interpretation
- Operational use
- Assumptions
- Failure mode or limitation

## Section template

Each section should include:

- Purpose
- Conceptual role
- Definitions if needed
- Main formulation
- How the formulation is used in prediction
- Example if useful
- Limitations
- Transition to next section

## Review checklist

For each drafted section, check:

- Is it self-contained?
- Does it depend on unstated history?
- Are terms defined before use?
- Are equations meaningful or decorative?
- Are claims too broad?
- Are experiments proposed where claims need evidence?

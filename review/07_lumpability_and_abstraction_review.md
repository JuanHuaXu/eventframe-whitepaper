# Review: 07 Lumpability and Abstraction

## Extracted Definitions

- Projection \(\pi\).
- Approximate predictive lumpability.
- Representative preservation invariant.
- Anti-Pigeon principle.

## Extracted Claims

- Abstraction is useful only when it preserves prediction.
- Merge distinctions that are prediction-equivalent.
- Preserve divergence-effective distinctions.

## Math Review

- Severity: medium.
- Issue: Lumpability uses one-step conditioning on \(e_t\); context-level conditioning may be needed for \(k>1\).
- Suggested fix: Add a note that the displayed equation is a one-step simplification and context-level variants use \(C_t\).

## Red-Team Review

- Main objection: Claim 5 requires citations and careful phrasing.
- Minimum change needed: Keep "approximate" and citation placeholder.

## Patch Decision

- Patched a context-level note for \(k>1\) prediction contexts.

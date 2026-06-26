# Final Red-Team Review

## Scope

This review covers the assembled Markdown paper in `build/paper.md` after section-level review and source synchronization.

## Finding Classification

- Confirmed: The paper needs an assembled artifact with normalized heading hierarchy, claim mapping, and bibliography placeholders. Action taken in `build/paper.md`.
- Confirmed: The phrase "predictive wrong" in the abstraction section was grammatically incorrect. Action taken in `src/07_lumpability_and_abstraction.md` and regenerated into `build/paper.md`.
- Confirmed: The abstract's Causal Fermion Systems caveat was readable but slightly awkward. Action taken in `src/00_abstract.md` and regenerated into `build/paper.md`.
- Recommendation only: The bibliography is still a placeholder register, not publication-grade citation metadata. This is acceptable for the current phase because the master prompt requires placeholders and conservative claims, not final references.
- Recommendation only: The residual composition operator remains a framework pattern rather than a theorem. The paper handles this conservatively by stating that the representation space, projection, decoder, and action-like criterion must be specified before stronger guarantees can be claimed.
- Recommendation only: The Planck-scale and entropy-bound motivation remains conceptual. The paper caveats it as motivation for compression, not as a proof of the event-frame ontology.
- Needs investigation: Experimental datasets and benchmark protocols are not yet instantiated. The experimental section is falsifiable in structure, but the next phase should choose concrete domains, datasets, thresholds, and baselines.
- Needs investigation: Representative frame selection is specified as an invariant, but selection heuristics are not yet formalized. This should become a method section or experimental ablation before external release.

## Patch Decision

Patch only the confirmed local text issues and assemble the paper with claim and reference normalization. Do not broaden claims, add fake citations, or generate a PDF until the Markdown draft remains internally consistent after checklist completion.

# Predictive Sheaf Snapping Mathematical Bug Hunt

Scope: mathematical formulation and end-to-end state semantics only. Prose style and language fitting are excluded.

## Confirmed P1 Findings - Fixed

1. Candidate compatibility was written as a function of the candidate structure alone even though edge defect also depends on candidate-induced predictive laws. The score now evaluates both \(\Theta_\Gamma[\Xi']\) and \(\Xi'\).
2. Deleting difficult edges could lower the maximum defect, including to zero for an empty graph. A frozen comparison-obligation set and unresolved-obligation gate now prevent deletion from erasing required comparisons.
3. Publication previously named graph and epoch changes only in prose. The accepted and rejected branches now define one atomic transition over compatibility structure, abstraction map, local epochs, and dependent memory state.
4. Confirmation gates were not represented as one post-selection decision. A joint indicator now requires net priority gain, proper-score non-inferiority, Anti-Pigeon validity, affected-edge compatibility, and bounded unresolved burden on disjoint chronological confirmation data.

## Confirmed P2 Findings - Fixed

1. Snap-score terms had no stated common scale. Every term must now be normalized to a declared utility scale or converted by its coefficient.
2. The affected set covered named buckets and edges but not the reverse dependency closure. The closure now includes dependent laws, maps, keys, certificates, cache entries, buckets, and edges.
3. Maxima over empty affected sets were undefined. The snap rule now declares \(\max\varnothing=0\).
4. The no-snap candidate could theoretically trigger a publication version change. The candidate family contains the current state and the publication margin satisfies \(\delta_{\mathrm{snap}}>0\), so zero-gain no-op publication fails.
5. The runtime bound omitted candidate generation and obligation validation. Both costs are now explicit, and published-graph auditing is separated from incremental candidate comparison to avoid omission or double counting.
6. Confirmation risk was written as population risk over a finite block. It is now an empirical confirmation-risk difference with a predeclared confidence bound.

## End-to-End Cases Checked

1. No-op selected: acceptance is zero and published state is unchanged.
2. Candidate rejected: graph, abstraction map, epochs, and memories are unchanged.
3. Candidate accepted: the complete tuple publishes atomically and affected memory entries become unusable until recertified.
4. Difficult edge removed: its frozen comparison obligation remains discharged by a valid path or contributes unresolved burden.
5. Empty affected bucket or edge projection: its maximum contributes zero without making the gain and obligation gates vacuous.
6. Confirmation outcomes: they may evaluate but never refit the selected candidate.
7. Repeated reviews: they require fresh chronological blocks or a sequentially valid procedure.
8. Causal nomination: predictive compatibility may generate an SCM-edit hypothesis but cannot orient or publish a causal edge.

## Residual Status

No unresolved P1 or P2 mathematical defect was found in the predictive-snap formulation after these corrections. Empirical calibration, finite-sample power, runtime constants, queue stability, and causal identifiability remain implementation or experimental obligations rather than established results.

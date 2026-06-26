# Discussion: Innovation and Scientific Refinement

EventFrame treats innovation conservatively. An innovation is not merely a novel label, cluster, or prediction. It is the discovery of a new causal distinction that repeatedly survives intervention. In the framework's terms, a candidate innovation begins as a residual, anomaly, fuzzing result, or graph-intervention result. It becomes meaningful only if later observations keep validating the distinction.

This connects the runtime to a broader scientific pattern. Science alternates between compression and refinement. Lumpability compresses: it asks when detailed distinctions can be removed because future behavior remains equivalent for the target. Anti-Pigeon refines: it asks when an apparently unified abstraction hides incompatible futures and must split. Counterfactual graph learning supplies a mechanism for testing which side is currently warranted.

The alternation can be written operationally:

1. Predict with the current event ontology and abstraction.
2. Measure residual action \(\mathcal{A}_{event}\).
3. If the action remains low, preserve the current abstraction.
4. If the action remains high, run fuzzing or graph intervention.
5. If distinctions do not affect the target, compress through lumpability.
6. If distinctions repeatedly affect the target, refine through Anti-Pigeon or ontology revision.

In this sense, EventFrame does not assume that its ontology is correct at the start. The ontology is a working compression that earns stability through intervention. A field assignment, cache key, event group, or causal edge becomes more credible when it reduces future residual action under repeated tests. It becomes less credible when counterfactual interventions reveal hidden structure.

This discussion also limits the claim. EventFrame does not provide a complete theory of scientific discovery. It provides a runtime vocabulary for one recurring pattern: prediction creates residuals, residuals suggest interventions, interventions test distinctions, and validated distinctions either compress or refine the event representation.

The natural convergence conjecture is local rather than global. Under a stationary environment, bounded action keys, bounded local graph degree, finite candidate abstraction moves, and positive validation thresholds, repeated intervention-driven refinement should converge toward a locally stable predictive abstraction. Local stability means that no available merge reduces representation cost without violating Anti-Pigeon, and no available split or ontology migration reduces \(\mathcal{A}_{event}\) by the required validation margin. This is a conjecture, not a theorem in the current paper, but it identifies the proof obligation for future work.

The next section lists open problems that remain before this pattern can support stronger guarantees.

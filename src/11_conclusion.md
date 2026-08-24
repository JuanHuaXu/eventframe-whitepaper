# 11. Conclusion

EventFrame proposes typed, task-relative event frames for prediction without treating them as fundamental entities. A coarse-graining \(\Gamma_{\Delta_\tau}\) maps detailed histories into event frames at a declared resolution. The predictor returns a distribution over marked event times and a no-event outcome, evaluated by a proper score; bounded event-aware timing error remains diagnostic.

At fixed temporal resolution, the governing objective minimizes expected priority-weighted post-observation action plus non-negative representation cost. Feasibility requires that prediction and retrieval operationally factor through the declared abstraction, that each bucket pass an external target-law future-diameter bound, and that the untransformed proper score remain non-inferior. Candidate selection and untouched chronological confirmation are separate. A distinct pre-observation risk gates fast-path use from \(S_{t^-}\) because realized loss is unavailable until its recorded availability time.

Baseline and residual point composition is type-resolved:

\[
\hat e_{t+1}=b_t\oplus_E r_t^{\mathrm{use}}.
\]

The operator encodes events into a finite-dimensional self-adjoint operator space, norm-clips the residual, projects into a declared admissible set, and decodes with a named decoder. A separately declared residual Markov kernel transforms the baseline probability law when proper-score improvement is claimed; the point operator alone does not define that law. Runtime packets use an independent packet encoder, residual space, admissible set, and operator \(\oplus_Y\). The construction takes limited structural inspiration from Causal Fermion Systems but is not a CFS action or physical theory.

Episodic memory stores prior cases; residual memory stores prior statistical corrections. Residuals are not causal hypotheses without separate intervention evidence. The fast path performs bounded lookup, typed composition, and pre-risk checks. The slow path evaluates realized scores, updates confidence, runs model-sensitivity audits, and tests abstractions. Causal-edge updates require an explicit structural causal model and identification strategy.

Approximate predictive lumpability compares detailed contexts that map to the same operational abstraction key. Anti-Pigeon rejects buckets whose externally estimated target-law future-diameter exceeds threshold; a candidate model's own forecast agreement is diagnostic and cannot certify itself. Every bucket retains a concrete traceability frame, but divergence testing uses a coverage-aware context audit set because one representative cannot characterize a heterogeneous group. Observed regime divergence is evaluated on common support and supports predictive adaptation, not causal attribution by itself.

The target architecture also admits a staged abstraction compatibility network. It begins with certified residual reuse, then adds edge audits, local reconciliation, bounded predictive sheaf snapping, spectral refinement under declared linear assumptions, and predictive regime mixtures. A snap selects from a finite local edit family, preserves externally fixed comparison obligations, requires later untouched confirmation, and publishes an atomic graph-key-epoch version with targeted cache invalidation and rollback. It reorganizes predictive compatibility and does not establish causality. Hardware improvements may permit a greater refinement depth, but do not change the mathematical interfaces or waive evidence gates. Rare high-priority corrections are evaluated with predeclared priority-weighted risk alongside unweighted and stratified results.

A finite-state abstraction search terminates under a strict-decrease rule on a fixed potential and fixed evaluation distribution. This result does not imply convergence in an online drifting environment. Implementation, staged ablation, compatibility-map validation, audit-coverage studies, and controlled real-world validation remain necessary before the framework's utility claims can be accepted.

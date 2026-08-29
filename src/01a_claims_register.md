# Claims Register

This section states the paper's major claims as falsifiable targets. The claims are not treated as established results. Each one names what would need to be measured, proved, or falsified by later experiments.

The current experiment ledger labels a proposition Validated in fixture when its frozen test met the declared target, Falsified in fixture when it failed, and Not tested when no reported experiment addresses it. These labels are local to the stated generator, hardware, metric, and evaluation window. A fixture-level validation is not universal proof, and a fixture-level falsification rejects the tested proposition or configuration rather than every possible implementation of the broader claim.

| Claim | Tested proposition | Result | Evidence and boundary |
| --- | --- | --- | --- |
| 2b | Frontier-all improves candidate-level probability quality over no Bayesian update. | Validated in fixture | Priority-weighted Brier loss improved by 9.29% in the frozen 20-candidate synthetic frontier. |
| 2b | The tested 5%-activation selective policy retains the quality gain of frontier-all. | Falsified in fixture | Selective admission improved priority-weighted Brier by only 0.16%, versus 9.29% for frontier-all. |
| 2b | The tested Bayesian policies repair post-shift ranking at recall at 10. | Falsified in fixture | Every tested policy had post-shift recall at 10 of 0.3000. |
| 2 | A reusable residual improves probability quality under a stable recurring bias. | Validated in fixture | The repeated-bias fixture reduced Brier loss by 29.81% over 40 untouched outcomes. |
| 2 | Residual reuse adds predictive gain in the original frontier experiment. | Falsified in fixture | The selective-plus-residual policy produced no incremental gain over selective admission alone. |
| 6 | Correctly separating a deliberately invalid broad group improves probability quality. | Validated, mechanism only | An oracle two-bucket split reduced Brier loss by 29.41%; oracle labels mean the Anti-Pigeon certificate procedure itself was not tested. |
| 2b, 6 | The bounded comparator nominates behaviorally divergent groups. | Validated in fixture | Strong split: 100%, 95% Wilson [94.34%, 100%]; moderate split: 87.5%, [77.23%, 93.53%]. No false share was observed in either divergent scenario; each scenario's upper endpoint is 5.66%. |
| 2b, 6 | The bounded comparator positively recognizes ordinary compatible noisy groups at the tested support. | Falsified in fixture | All 64 compatible 0.8/0.8 groups remained uncertain at 100 outcomes per member. |
| 2b, 6 | Bayesian comparison preserves Anti-Pigeon authority. | Validated in integration fixture | The comparison reached share and split branches without changing a posterior key or certificate. |
| 2b | The original run-length-zero detector reliably handles noisy abrupt, gradual, and recurring drift. | Falsified in fixture | Miss rates were 96.88%, 100%, and 93.75%, respectively. |
| 2b | The revised v4 monitor materially improves drift recovery under its declared windows. | Validated in fixture | Abrupt: 87.5%, 95% Wilson [77.23%, 93.53%]; recurring: 77.34%, [69.36%, 83.74%]; gradual: 93.75%, [85.00%, 97.54%]. |
| 2b | The revised v4 monitor is ready for production drift guarantees. | Falsified in fixture | One stable unmatched alarm; 0.2656, 0.3281, and 0.1563 unmatched alarms per trajectory in noisy abrupt, recurring, and gradual scenarios; recurring misses; and long gradual delay violate readiness. |
| 7, 7a | The frontier-all policy change remains below 100 ms local sequential p99 recall in the declared fixture. | Validated, narrow benchmark | Measured p99 was 9.043 ms at 1,000 stored events; transport, external embeddings, concurrency, cold start, and full service load were excluded. |
| 0, 1, 1b, 2a, 3--5b, 6a, 8--8c | All remaining empirical propositions. | Not tested | The paper specifies protocols, but reports no claim-validating experiment for these propositions yet. Claim 1a is a scope statement rather than an empirical performance claim. |

Claim 0. At a fixed resolution, an external target-law constrained population objective defines an oracle benchmark. The operational rule selects from a finite family using certified Anti-Pigeon and proper-score constraints, empirical priority-weighted action, and representation cost. Oracle feasibility and empirical certifiability are distinct; generating laws are distinct from their realized design and untouched confirmation samples, and as-of runtime admission remains separate.

Claim 1. Structured event frames are useful predictive units if, for a declared task, they improve interpretability or temporal prediction relative to unstructured sequence records without hiding field-level error.

Claim 1a. Event frames are task-relative compressed representations rather than claims about fundamental ontology. Physical constants do not prove the compression hypothesis.

Claim 1b. Temporal precision controls frame granularity if changing the declared time resolution \(\Delta_\tau\) changes the candidate-frame set, cache pressure, and detectable divergence boundaries in measurable ways.

Claim 2. Residual caches reduce prediction cost or error when similar contexts or action signatures produce similar baseline errors and as-of, metadata-gated residual records improve forward-held-out loss often enough to justify lookup and maintenance. Point residuals are in-horizon only, while a separately declared law estimator covers marked and no-event outcomes. A typed cache record keeps point-template and law corrections semantically separate; the full kernel governs the no-event atom, and the final mark and time are coherent with the corrected law. Joint records require forward validation of the complete bundle.

Claim 2a. Runtime prediction packets are useful when a separately typed packet composition operator improves selection of memory nodes, graph edges, retrieval lane, compaction risk, response mode, or control branch on held-out packet loss.

Claim 2b. A bounded Bayesian frontier can preserve local update cost when vector width, graph degree, candidate universe, evidence-ready frontier size, hypothesis dimension, retained changepoint state, and complete admission-probability evaluation are explicitly capped. The reference frontier-all policy updates every evidence-ready nominated member; the optional selective policy adds a frozen activation threshold. Neither policy performs corpus-wide posterior updates. Anti-Pigeon certificates determine which admitted evidence may share a posterior. A bounded shared-versus-split marginal-evidence comparison may nominate \(\mathrm{share}\), \(\mathrm{split}\), or \(\mathrm{uncertain}\), but it cannot authorize sharing or mutate posterior keys. Ordinary posterior-predictive semantics require one declared joint model whose displayed evidence and outcome marginals induce the likelihood and next-outcome kernel; separately modeled components remain modular forecasts. The effective posterior family maps to the base forecast law, which is then corrected only by residual components whose law or template motion certificates remain valid, including propagated approximation error, and evaluated by the proper score. Informative nomination or activation must enter the likelihood and satisfy the certified positive admission-support condition, or the result is reported only as an admission-conditioned working posterior. Independent design-weighted non-admitted-event audits and simultaneous omitted-influence bounds test omitted influence only on their declared audit population. Initial synthetic evidence supports frontier-all over the tested 5%-activation policy for probability quality and demonstrates bounded grouping and drift mechanisms, but does not establish certificate coverage, full-stream calibration, or real-world performance.

Claim 3. Episodic memory and residual cache memory serve different roles because prior-case recall and prior-error correction can be independently useful or harmful under the same prediction context.

Claim 4. Validity-constrained property fuzzing exposes conditional model invariants and ontology review signals. It does not establish causal effects without an explicit SCM and identification strategy.

Claim 5. Approximate predictive lumpability provides a route to abstraction when projected event states preserve target-relevant transition behavior within a declared divergence threshold.

Claim 5a. Event streams can conjoin or diverge over time when multiple streams become prediction-equivalent under a merge threshold or when small distinctions amplify into target-distinct downstream futures.

Claim 5b. Each group retains at least one concrete traceability frame plus a coverage-aware context audit set; one representative alone is insufficient for group-level divergence claims, and unseen-context certification additionally requires exhaustive coverage or a verified continuity bound.

Claim 6. Conditional on valid target-law estimation, audit coverage, simultaneous uncertainty coverage, and any declared continuity bound, Anti-Pigeon rejects buckets whose certified context-conditional target-law diameter exceeds threshold. This is an empirical certificate, not a framework-level theorem that those premises hold. Model-forecast diameter and Bayesian shared-versus-split evidence are diagnostic proposals only; neither may certify its own bucket. Regime comparisons require common support or transport assumptions, and causal attribution requires separate intervention evidence.

Claim 6a. Predictively effective distinctions are sparse only when their held-out ablation ratio is small within a finite declared candidate set. A causal sparsity ratio is a separate quantity available only under identified interventions.

Claim 7. Fast-path and slow-path separation is computationally useful if low-latency prediction can reuse cached residuals while slower background work improves future predictions without blocking the current one.

Claim 7a. Expected exact-key lookup is history-independent only when context update, key construction, graph degree, key size, and cache size are bounded; fallback and maintenance costs remain explicit.

Claim 8. Heterogeneous abstractions can be tested through declared comparison maps and edge defects, complementing within-bucket Anti-Pigeon audits. The current construction is a sheaf-inspired compatibility scaffold; it becomes sheaf-theoretic only when the required map laws hold and causal only when SCM semantics are supplied.

Claim 8a. A full refinement architecture can retain certified residual reuse while adding compatibility audit, local reconciliation, bounded predictive sheaf snapping, spectral refinement under linear assumptions, and regime-mixture refinement. Hardware changes stage depth, not stage meaning.

Claim 8b. A predictive sheaf snap can improve a heterogeneous abstraction network when a finite local edit family is selected on chronological design data, fixed comparison obligations prevent deletion from masquerading as compatibility, the candidate is accepted only on later untouched evidence, and graph-key-epoch state is published atomically. Compatibility evidence alone does not promote causal edges.

Claim 8c. Upgrade value is evaluated by predeclared priority-weighted utility beside unweighted and stratified results; loss and resource percentages are not compared until converted to a common utility scale.

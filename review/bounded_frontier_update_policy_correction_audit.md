# Bounded Frontier Update Policy Correction Audit

Date: 2026-08-28

- **Symptom:** The paper treated threshold-selective Bayesian admission as the reference policy, while the reference implementation experiment found that updating all 20 evidence-ready frontier members retained most of the available probability improvement and the tested 5% policy did not.
- **Classification:** The reference-policy wording is stale. The bounded-frontier complexity claim remains valid. Broader quality, residual, and regime-adaptation claims remain unproved.
- **Competing explanations:** The result could arise from a weak activation rule, from a synthetic world in which useful evidence is diffuse across the frontier, or from an implementation defect. Frozen-policy tests, deterministic repeated reports, and the identical selective/residual ablation support the first two explanations but do not distinguish them generally.
- **Chosen correction:** Define frontier-all and selective policies over the same bounded nominated frontier, make frontier-all the reference default, and preserve selective admission as an optional measured tradeoff.
- **Patch invariant:** "Update all" always means all evidence-ready members of the bounded frontier, never every event in the corpus. Posterior work is bounded by frontier size; corpus dependence remains in retrieval and index maintenance.
- **Hot-path cost:** Bayesian work becomes linear in the bounded updated count. A local 1,000-event sequential benchmark measured 9.043 ms p99 after the default changed to frontier-all, compared with 9.026 ms before; this is not a concurrent service-level guarantee.
- **Falsifier:** A fresh, correctly implemented experiment in which a frozen selective policy preserves frontier-all forecast quality at materially lower measured cost would overturn the reference-policy preference. Unbounded frontier growth would overturn the stated runtime bound.
- **Evidence limits:** The experiment uses 20 candidates, 120 predictions, four synthetic trajectories, and an in-memory event store. It does not test the complete marked-time/no-event score, Anti-Pigeon coverage, real OpenClaw workloads, or corpus-scale posterior updates.
- **Confidence:** High that the formulation should distinguish frontier-all from corpus-all; moderate that frontier-all should remain the default beyond the current synthetic mechanism test.

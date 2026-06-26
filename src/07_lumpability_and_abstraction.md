# 7. Lumpability and Abstraction

Abstraction is useful only when it preserves what the prediction task needs. EventFrame uses approximate predictive lumpability as a formal route from detailed event frames to coarser states. The purpose is to compress detail when the compressed representation preserves transition behavior for the target of interest.

Let:

\[
\pi: \mathcal{E} \rightarrow \mathcal{Z}
\]

be a projection from detailed event frames to abstract states. The abstract state \(\pi(e_t)\) may remove fields, group values, or map a high-dimensional representation into a smaller symbolic or latent state. The projection is useful only if it preserves enough predictive structure.

A transition process is predictively lumpable for a target when:

\[
P(\pi(e_{t+1}) \mid e_t) \approx P(\pi(e_{t+1}) \mid \pi(e_t)).
\]

The left side conditions on the detailed event. The right side conditions only on the abstract state. This one-step expression is a simplified case. For context-length \(k\), the analogous test conditions on \(C_t\) and on the projected context \(\pi(C_t)\). If the two distributions are close, the abstraction preserves target-relevant transition behavior. The approximation should be measured by a declared divergence or distance and accepted only under a threshold.

Operationally, abstraction quality can be tested by comparing predictions before and after projection:

1. Choose a projection \(\pi\) and target property.
2. Estimate transition behavior using detailed contexts.
3. Estimate transition behavior using projected contexts.
4. Compare temporal loss and target distribution divergence.
5. Accept the abstraction only if predictive degradation remains below a declared threshold.

This connects directly to property fuzzing. If perturbing a field does not change the prediction target beyond threshold, that field may be a candidate for abstraction. If lumpability tests show that projected states preserve transition behavior, the abstraction has stronger evidence. Fuzzing gives local stability evidence; lumpability tests transition-level preservation.

Abstraction also has to respect event confluence and divergence. When streams merge, a projection or merge operator may intentionally replace several event histories with one aggregate event. When a small distinction branches into materially different futures, the same projection becomes unsafe. A good abstraction therefore has two duties: merge distinctions that have become prediction-equivalent, and preserve distinctions that are divergence-effective.

EventFrame therefore imposes a representative preservation invariant. Every event-frame group \(\mathcal{H}_j\) created by projection, clustering, confluence, or cache-key equivalence must keep at least one representative frame \(\bar{e}_j \in \mathcal{H}_j\). This representative lets the system measure boundary conditions later: intervene on the representative to test whether the group should diverge, or compare representatives from multiple groups to test whether they have converged enough to merge.

The Anti-Pigeon principle is the split-side criterion that prevents invalid abstraction. It says that events should not be grouped into broad categories merely because they share surface features. Grouping must be earned by invariance evidence, confluence evidence, lumpability evidence, or measured predictive adequacy. The principle is not a theorem. It is a discipline for avoiding abstractions that are convenient but predictively wrong.

Formally, let \(B \subseteq \mathcal{E}\) be an event bucket represented by one abstract state, cache key, or event-frame group. For each retained event \(e_i \in B\), let \(H_i\) denote the prediction history or representative context associated with that event. Let \(P_Y(\cdot \mid H_i)\) be the predicted future distribution for the target \(Y\). Define pairwise future divergence:

\[
D_{ij} =
D\left(P_Y(\cdot \mid H_i), P_Y(\cdot \mid H_j)\right),
\]

where \(D\) is a declared divergence or distance, such as total variation distance, KL divergence when well-defined, Wasserstein distance, or latent predictive distance. The bucket fails the Anti-Pigeon criterion whenever:

\[
\exists e_i,e_j \in B \quad \text{such that} \quad D_{ij} \ge \epsilon_{AP}.
\]

Equivalently, the bucket is valid for the target only when:

\[
\max_{e_i,e_j \in B} D_{ij} < \epsilon_{AP}.
\]

When this test fails, the system applies a split or refinement operator:

\[
\operatorname{Split}_{\epsilon_{AP}}(B) = \{B_1,\ldots,B_M\},
\]

such that each resulting non-empty bucket satisfies the same internal-divergence bound:

\[
\forall B_\ell,\quad \max_{e_i,e_j \in B_\ell} D_{ij} < \epsilon_{AP}.
\]

Every resulting bucket must retain at least one representative event frame. The representative requirement is what makes the split test repeatable: after refinement, the system can continue checking whether a bucket remains stable, should split again, or has converged enough to merge with another bucket.

This makes lumpability and Anti-Pigeon dual operations. Lumpability accepts a merge when future distributions remain close enough under a declared merge threshold. Anti-Pigeon rejects or splits a bucket when internal future divergence crosses a declared split threshold. In practice, the thresholds may differ, for example \(\eta_{\mu} < \epsilon_{AP}\), so the system does not oscillate between merge and split decisions near a noisy boundary.

Abstraction quality should be reported with both benefits and costs. Benefits may include lower memory use, faster lookup, better generalization, and simpler explanations. Costs may include lost distinctions, degraded temporal prediction, and hidden subgroup errors. A good abstraction for fast-path prediction may still be too coarse for causal explanation or invariant discovery.

The main mathematical limitation is that exact lumpability is often too strong for real event data. EventFrame therefore uses approximate predictive lumpability and must cite prior work on Markov chain lumpability, state aggregation, and approximate abstraction. The paper should not claim a new theorem unless a proof is added. The next section places these pieces into a reference runtime model.

# 3. Mathematical Framework

The mathematical framework turns compressed event frames into objects that can be predicted, evaluated, cached, and abstracted. The main purpose of the formalism is operational: given a context \(C_t\), produce a next-event estimate \(\hat{e}_{t+1}\), measure its temporal error, and decide whether memory or abstraction should be updated.

Let \(\Omega\) denote a dense substrate state space. For a finite region \(A_t\), let \(\omega_{A_t}\) denote the substrate history over that region. An event frame is produced by a coarse-graining map:

\[
e_t = \Gamma(\omega_{A_t}), \quad \Gamma: \Omega^{A_t} \rightarrow \mathcal{E}.
\]

The conceptual role of \(\Gamma\) is to select usable predictive distinctions from a substrate that is too dense to represent directly. The operational use is that every prediction, cache key, and invariant test operates on \(e_t\), while slow-path review may revise \(\Gamma\) if the compression discards distinctions that matter.

Let \(\mathcal{E}\) be the compressed event space defined by the product of typed fields. A linear trajectory is:

\[
E_{1:T} = (e_1, e_2, \ldots, e_T), \quad e_t \in \mathcal{E}.
\]

More generally, an event history is a directed acyclic event graph:

\[
G_t = (V_t, R_t),
\]

where \(V_t \subset \mathcal{E}\) is a set of event frames and \(R_t\) contains temporal, causal, or dependency edges. This graph view allows streams to merge and branch instead of forcing all event histories into a single chain.

For a context length \(k\), the prediction context is:

\[
C_t = e_{t-k+1:t} = (e_{t-k+1}, \ldots, e_t) \in \mathcal{E}^k.
\]

A transition model maps this context to a predicted event:

\[
F_\theta: \mathcal{E}^k \rightarrow \mathcal{E}.
\]

Here \(\theta\) may denote learned parameters, rules, retrieval settings, or a mixture of these. The direct formulation is:

\[
\hat{e}_{t+1} = F_\theta(C_t).
\]

The conceptual role of \(F_\theta\) is simple: it is the mechanism that converts recent structured history into a next event. The operational use is also direct: compute \(C_t\), apply \(F_\theta\), and receive \(\hat{e}_{t+1}\). Later sections decompose \(F_\theta\) into a baseline predictor plus residual correction, but the single-function view is useful for defining loss.

The canonical loss is temporal. For point-valued event times:

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{\left|\tau(\hat{e}_{t+1})-\tau(e_{t+1})\right|}{H}\right).
\]

The variable \(H > 0\) is a prediction horizon. The operator \(\tau(e)\) extracts the time field of an event. The loss is zero when the predicted and observed times match, grows linearly within the horizon, and saturates at one when the error reaches or exceeds \(H\). This clamping is deliberate: it prevents a small number of extreme misses from dominating all diagnostics.

For interval-valued times, replace absolute difference with an interval distance \(d_{\mathcal{T}}\):

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{d_{\mathcal{T}}(\tau(\hat{e}_{t+1}),\tau(e_{t+1}))}{H}\right).
\]

The interval distance may be midpoint distance, endpoint Hausdorff distance, or another declared metric. The assumption is that \(\mathcal{T}\) has enough structure to compare predicted and observed times. If the time field is missing or uncertain, the loss should be reported with that uncertainty rather than silently treated as exact.

Optional diagnostic distances may be defined over other event fields. For a field projection \(\rho_i: \mathcal{E} \rightarrow \mathcal{X}_i\), a diagnostic field loss may be written:

\[
\mathcal{L}_i(\theta) = d_i(\rho_i(\hat{e}_{t+1}), \rho_i(e_{t+1})).
\]

These losses answer secondary questions: did the predictor identify the right actor, action type, location, or mechanism? They are not the canonical objective in the current formulation, but they are important for error analysis and for discovering which fields matter in a domain.

The event sparsity hypothesis can be stated operationally. Let \(I_j\) be an intervention on a substrate or event-frame distinction, and let \(Y\) be a prediction target. A distinction is intervention-effective when:

\[
d_Y(P(Y \mid do(I_j)), P(Y)) > \eta_Y.
\]

EventFrame assumes that such distinctions are sparse relative to the microscopic substrate. This is not a proven physical theorem in the paper. It is a modeling hypothesis that justifies searching for compressed event frames rather than assigning a unique frame to every microscopic cell.

Confluence and divergence define when compression is safe or unsafe over time. Let \(S_1,\ldots,S_m\) be event streams or subgraphs. A merge operator:

\[
e^{merge}_t = \mu_{\delta}(S_1,\ldots,S_m)
\]

is accepted only when replacing the streams by \(e^{merge}_t\) changes the prediction target by at most a threshold. Conversely, a branching operator:

\[
\mathcal{B}_{\epsilon}: \mathcal{E} \rightarrow \mathcal{P}(\mathcal{G})
\]

identifies downstream event subgraphs reachable under a perturbation or intervention scale \(\epsilon\). If the target distribution changes by more than \(\eta_Y\), the original distinction is divergence-effective and should not be compressed away.

Representative preservation makes this test operational for groups. Let \(\mathcal{H}_j \subseteq \mathcal{E}\) be an event-frame group induced by an abstraction, cache key, or merge. EventFrame requires:

\[
\exists \bar{e}_j \in \mathcal{H}_j
\]

for every non-empty group. The retained frame \(\bar{e}_j\) is a measurement anchor. For an intervention \(I\), a group-level divergence score can be estimated as:

\[
D_j(I) =
d_Y(P(Y \mid do(I), \bar{e}_j), P(Y \mid \bar{e}_j)).
\]

If \(D_j(I)\) exceeds the target threshold, the group is not stable under that intervention and should be split, refined, or marked as sensitive. If two representative frames remain within a merge threshold, their groups may be candidates for confluence.

Confidence and provenance metadata enter the framework through \(c_t\). Operationally, \(c_t\) should affect whether a field is trusted for training, lookup, fuzzing, or invariant extraction. For example, if \(m_t\) is an inferred motive with low confidence, fuzzing that motive should not be treated the same as perturbing an observed timestamp. A conservative implementation can use \(c_t\) to weight losses, filter cache entries, or mark claims as uncertain.

The framework is limited by representation choices. A poor event encoding can make a useful transition appear noisy, while an overly rich encoding can make similar events appear unrelated. The rest of the paper therefore treats distance functions, cache keys, and abstraction maps as objects that must be specified and tested, not assumed. The next section decomposes the transition model into baseline prediction and residual correction.

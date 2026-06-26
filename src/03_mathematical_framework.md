# 3. Mathematical Framework

The mathematical framework turns event frames into objects that can be predicted, evaluated, cached, and abstracted. The main purpose of the formalism is operational: given a context \(C_t\), produce a next-event estimate \(\hat{e}_{t+1}\), measure its temporal error, and decide whether memory or abstraction should be updated.

Let \(\mathcal{E}\) be the event space defined by the product of typed fields. A trajectory is:

\[
E_{1:T} = (e_1, e_2, \ldots, e_T), \quad e_t \in \mathcal{E}.
\]

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

Confidence and provenance metadata enter the framework through \(c_t\). Operationally, \(c_t\) should affect whether a field is trusted for training, lookup, fuzzing, or invariant extraction. For example, if \(m_t\) is an inferred motive with low confidence, fuzzing that motive should not be treated the same as perturbing an observed timestamp. A conservative implementation can use \(c_t\) to weight losses, filter cache entries, or mark claims as uncertain.

The framework is limited by representation choices. A poor event encoding can make a useful transition appear noisy, while an overly rich encoding can make similar events appear unrelated. The rest of the paper therefore treats distance functions, cache keys, and abstraction maps as objects that must be specified and tested, not assumed. The next section decomposes the transition model into baseline prediction and residual correction.

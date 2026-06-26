# 4. Residual Prediction

Residual prediction separates a first-pass event estimate from a correction. The baseline predictor captures ordinary transition structure. The residual captures recurring ways in which the baseline tends to be wrong. This separation is useful when full recomputation is expensive or when similar contexts repeatedly produce similar errors.

Let \(B\) be a baseline predictor:

\[
B: \mathcal{E}^k \rightarrow \mathcal{E}.
\]

Given a context \(C_t\), the baseline prediction is:

\[
b_t = B(C_t).
\]

A residual model or residual cache supplies a correction \(r_t\). In ordinary vector spaces, one might add a residual directly. EventFrame avoids treating event frames as simple vectors. Instead, it writes prediction as structured composition:

\[
\hat{e}_{t+1} = b_t \oplus_{\mathcal{A}} r_t.
\]

The operator \(\oplus_{\mathcal{A}}\) applies a residual correction while preserving admissibility constraints. The subscript \(\mathcal{A}\) indicates that the corrected representation is regularized by a causal-action-inspired criterion. This is inspired by Causal Fermion Systems in the limited sense that meaningful configurations are evaluated through structured relationships and an action-like admissibility condition. EventFrame does not claim to be a physical causal fermion system.

The reference composition rule is:

\[
b \oplus_{\mathcal{A}} r =
q^{-1}_{\mathrm{approx}}\left(\Pi_{\mathcal{Q}}\left(q(b) + \operatorname{clamp}(r)\right)\right).
\]

Here \(q: \mathcal{E} \rightarrow \mathcal{Q}\) encodes an event into an operator-like representation space, \(r \in \mathcal{Q}\) is a residual correction, \(\operatorname{clamp}(r)\) bounds the residual magnitude, \(\Pi_{\mathcal{Q}}\) projects the corrected representation back into the admissible representation space, and \(q^{-1}_{\mathrm{approx}}\) decodes the representation back into an event frame. The operational use is: encode the baseline, apply a bounded correction, project to a valid representation, and decode to a predicted event.

The admissibility constraint can be made measurable through a surrogate event action. One conservative choice is:

\[
\mathcal{A}_{event}(\hat{e}_{t+1}) =
\lambda_r \mathcal{L}_{time}^{H}
+ \lambda_a D_{abs}
+ \lambda_c D_{edge}
+ \lambda_u U(\hat{e}_{t+1}),
\]

where \(D_{abs}\) measures abstraction or bucket inconsistency, \(D_{edge}\) measures causal-edge or graph-transition inconsistency, \(U(\hat{e}_{t+1})\) measures prediction uncertainty, and the \(\lambda\) terms are non-negative weights declared by the implementation. This is not a Causal Fermion Systems action. It is a runtime surrogate inspired by the idea that admissible configurations should minimize a structured action-like quantity. A corrected prediction is preferred only when it improves temporal loss without creating excessive abstraction, graph, or uncertainty penalties.

Residuals may be estimated after observation. If the baseline prediction is \(b_t\) and the observed event is \(e_{t+1}\), then the observed residual is the correction that would have moved \(b_t\) toward \(e_{t+1}\) under the chosen representation. Because \(\mathcal{Q}\) is only specified as an operator-like representation space, the residual should be estimated by a declared residual estimator:

\[
r_t^{obs} = \Delta_{\mathcal{Q}}(q(b_t), q(e_{t+1})).
\]

Here \(\Delta_{\mathcal{Q}}\) is model-dependent. In a vector representation it may reduce to subtraction, but in a structured or operator-like representation it may be an optimization, projection, alignment, or learned correction rule. The residual should therefore be treated as a reusable correction candidate, not as a guaranteed truth. Its value depends on the representation and the domain.

Residual reuse requires a lookup rule. A residual cache stores triples:

\[
\mathcal{C}_R = \{(\kappa_i, r_i, s_i)\}_{i=1}^{N},
\]

where \(\kappa_i\) is a context key, \(r_i\) is a residual, and \(s_i\) stores metadata such as age, confidence, and observed temporal loss. A key function \(\kappa: \mathcal{E}^{k} \rightarrow \mathcal{K}\) maps the current context to a retrieval key. The retrieved residual is:

\[
r_t^* =
\begin{cases}
r_j & \text{if } j = \arg\min_i d_{\mathcal{K}}(\kappa(C_t), \kappa_i)
\text{ and } d_{\mathcal{K}}(\kappa(C_t), \kappa_j) \le \epsilon_K,\\
0_{\mathcal{Q}} & \text{otherwise.}
\end{cases}
\]

This rule is the operational heart of fast-path residual prediction. If a sufficiently similar prior context exists, reuse its correction. If not, fall back to the baseline.

For implementations that require a lower-latency path, EventFrame can use an action-residual cache keyed by a compact action signature. Let:

\[
\alpha: \mathcal{E}^{k} \rightarrow \mathcal{K}_A
\]

map a context to an action key, such as a tuple of action type, temporal regime, relevant actor class, and abstraction bucket. The action-residual cache is a partial map:

\[
\mathcal{C}_A: \mathcal{K}_A \rightharpoonup (r_a, c_a, n_a, t_a),
\]

where \(r_a \in \mathcal{Q}\) is the cached action residual, \(c_a \in [0,1]\) is confidence, \(n_a\) is support count, and \(t_a\) is last update time. The fast-path action residual is:

\[
r_t^{A} =
\begin{cases}
r_a & \text{if } \alpha(C_t) \in \operatorname{dom}(\mathcal{C}_A)
\text{ and } c_a \ge \gamma_A
\text{ and } n_a \ge n_{\min}
\text{ and } age(t_a) \le A_{\max},\\
0_{\mathcal{Q}} & \text{otherwise.}
\end{cases}
\]

If \(\mathcal{C}_A\) is implemented as a bounded hash table or array over declared action keys, lookup is expected \(O(1)\). This is an implementation property, not a mathematical guarantee: collisions, eviction, unbounded key growth, or nearest-neighbor fallback can increase cost. The action-residual path should therefore report hit rate, confidence, support, age, and post-correction temporal loss.

Action-residual validity is updated only after observation. A simple confidence update can be:

\[
c_a^{new} =
(1-\beta)c_a + \beta \mathbf{1}
\left[
\mathcal{L}_{time}^{H}(b_t \oplus_{\mathcal{A}} r_a)
+ \delta_A
< \mathcal{L}_{time}^{H}(b_t)
\right],
\]

where \(\delta_A\) is the required improvement margin and \(\beta\) is an update rate. When confidence falls below \(\gamma_A\), when support is too small, or when the corrected prediction worsens loss, the slow path should trigger fuzzing, episodic review, or residual eviction rather than continuing to trust the cached action residual.

The main failure modes are cache pollution, overcorrection, stale residuals, and false similarity. Cache pollution occurs when low-quality residuals accumulate. Overcorrection occurs when a residual dominates the baseline. Stale residuals occur when the environment changes. False similarity occurs when the key function treats different contexts as equivalent. The clamping function, metadata \(s_i\), and threshold \(\epsilon_K\) are safeguards, but they do not remove the need for empirical evaluation. The next section distinguishes this residual cache from episodic memory.

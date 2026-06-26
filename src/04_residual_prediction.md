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

The main failure modes are cache pollution, overcorrection, stale residuals, and false similarity. Cache pollution occurs when low-quality residuals accumulate. Overcorrection occurs when a residual dominates the baseline. Stale residuals occur when the environment changes. False similarity occurs when the key function treats different contexts as equivalent. The clamping function, metadata \(s_i\), and threshold \(\epsilon_K\) are safeguards, but they do not remove the need for empirical evaluation. The next section distinguishes this residual cache from episodic memory.

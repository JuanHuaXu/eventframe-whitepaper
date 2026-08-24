# 4. Residual Prediction

Residual prediction separates a first-pass event estimate from a correction. The baseline captures ordinary transition structure; the residual records a recurring statistical prediction error. A residual is not a causal hypothesis unless separate intervention evidence identifies it as causal.

Let the baseline probability law and its structured point summary be:

\[
\mathsf Q_B:\mathcal E^k\rightarrow\mathcal P(\mathcal Z_H),
\qquad
B:\mathcal E^k\rightarrow\mathcal E,
\qquad b_t=B(C_t).
\]

To make structured correction type-correct, choose a finite-dimensional Hilbert space \(\mathscr H\) and let \(\mathbb H_d\) be the real vector space of self-adjoint operators on \(\mathscr H\), equipped with the Frobenius norm \(\|\cdot\|_F\). Define:

\[
q_E:\mathcal E\rightarrow\mathbb H_d,
\qquad
d_E:\mathcal Q_{E,\mathrm{adm}}\rightarrow\mathcal E,
\]

where \(\mathcal Q_{E,\mathrm{adm}}\subseteq\mathbb H_d\) is a non-empty closed admissible set and \(d_E\) is a decoder, not an inverse of the lossy encoder. For a radius \(\delta_E>0\), define norm clipping by:

\[
\mathrm{clip}_{\delta_E}(r)=
\begin{cases}
0, & r=0,\\
r\min\!\left(1,\dfrac{\delta_E}{\|r\|_F}\right), & r\neq0.
\end{cases}
\]

Let the admissibility projection be a deterministic selection:

\[
\Pi_E(v)\in\arg\min_{u\in\mathcal Q_{E,\mathrm{adm}}}\|u-v\|_F.
\]

A minimizer exists when the admissible set is closed in finite dimensions. It is unique when that set is convex; otherwise the implementation must declare a tie-breaking rule. Event residual composition is:

\[
b\oplus_E r=
\begin{cases}
b, & r=0,\\
d_E\!\left(\Pi_E\!\left(q_E(b)+\mathrm{clip}_{\delta_E}(r)\right)\right), & r\neq0,
\end{cases}
\qquad r\in\mathbb H_d.
\]

Thus zero is an exact identity even when the encoder is lossy or the baseline encoding is outside the admissible set.

This construction borrows only the use of self-adjoint operator representations and variational admissibility from Causal Fermion Systems [1,2]. It is not the CFS causal action, does not inherit CFS field equations, and makes no claim of physical equivalence.

Residuals are estimated after observation. When a concrete next event has been observed, a simple representation residual is:

\[
r_t^{\mathrm{obs}}=q_E(e_{t+1})-q_E(b_t).
\]

If the horizon ends with \(Z_{t+1}=\varnothing\) before a concrete next event is observed, this event-representation residual is not yet available. The no-event outcome may update distributional residual utility, but it must not be silently encoded as a concrete event. An implementation may replace subtraction with a learned alignment or constrained estimator, but its domain and objective must be declared. In all cases, the residual is a reusable correction candidate whose utility must be re-evaluated on later observations.

The general residual cache available immediately before prediction is:

\[
\mathcal C_{R,t^-}=\{(\kappa_i,r_i,c_i,n_i,t_i,v_i,m_i,s_i)\}_{i=1}^{N_t},
\qquad
\kappa:\mathcal E^k\rightarrow\mathcal K_R,
\qquad r_i\in\mathbb H_d,
\]

where \(c_i\) is residual confidence, \(n_i\) is effective support, \(t_i\) is the last certified update time, \(v_i\) is its abstraction epoch, \(m_i\) is its compatibility safety margin, and \(s_i\) is provenance including residual identity and eligible training interval. Only entries whose availability time is at most \(t\) may occur in \(\mathcal C_{R,t^-}\). For \(N_t>0\), let:

\[
j_t=\min\!\left(\arg\min_{1\le i\le N_t}
d_{\mathcal K_R}(\kappa(C_t),\kappa_i)\right),
\]

where the outer minimum is the declared deterministic tie-break. Define general-cache acceptance without dereferencing an empty cache:

\[
J_t^R=
\begin{cases}
\mathbf 1\!\left[
\begin{array}{l}
d_{\mathcal K_R}(\kappa(C_t),\kappa_{j_t})\le\epsilon_R,\quad
c_{j_t}\ge\gamma_R,\quad n_{j_t}\ge n_{\min}^R,\\
\mathrm{age}_t(t_{j_t})\le A_{\max}^R,\quad
v_{j_t}=v_t,\quad m_{j_t}\ge0,\quad s_{j_t}\text{ is valid}
\end{array}
\right],&N_t>0,\\
0,&N_t=0.
\end{cases}
\]

The retrieved residual is:

\[
r_t^*=
\begin{cases}
r_{j_t}, & J_t^R=1,\\
0_{\mathbb H_d}, & \text{otherwise.}
\end{cases}
\]

A valid zero residual is distinguishable from a miss because \(J_t^R\), not its value, records acceptance. Realized loss and cache updates wait for an available \(Z_{t+1}\); the final selector and pre-observation gate are defined only after the candidate bundle below exists.

For lower-latency exact-key reuse, let:

\[
\alpha:\mathcal E^k\rightarrow\mathcal K_A,
\]

and define the partial map:

\[
\mathcal C_{A,t^-}:
\mathcal K_A\rightharpoonup
\mathbb H_d\times[0,1]\times\mathbb N_0\times\mathcal T
\times\mathbb N_0\times\mathbb R.
\]

For \(k_t=\alpha(C_t)\), bind the cache entry only when it exists:

\[
 k_t\in\mathrm{dom}(\mathcal C_{A,t^-})
 \quad\Longrightarrow\quad
\mathcal C_{A,t^-}(k_t)=(r_{k_t},c_{k_t},n_{k_t},t_{k_t},v_{k_t},m_{k_t}),
\]

where \(n_{k_t}\) is effective support after accounting for clustered or overlapping trials, \(v_{k_t}\) is the cache entry's local abstraction epoch, \(v_t\) is the active as-of epoch for the same dependency region, and \(m_{k_t}\) is the compatibility safety margin materialized by the slow path. If \(E(k_t)\) is the declared set of compatibility edges on which the entry depends, for example:

\[
m_{k_t}=
\begin{cases}
\epsilon_{\mathrm{merge}}^{\mathrm{comp}}, & E(k_t)=\varnothing,\\
\epsilon_{\mathrm{merge}}^{\mathrm{comp}}
-\max_{e\in E(k_t)}\mathrm{UCB}_{\mathrm{sim}}[\delta_e], & E(k_t)\neq\varnothing.
\end{cases}
\]

The simultaneous confidence procedure covers every edge inspected for that cache certificate.

Define the exact-cache acceptance indicator without dereferencing a missing entry:

\[
J_t^A=
\begin{cases}
\mathbf 1\!\left[
c_{k_t}\ge\gamma_A,\ n_{k_t}\ge n_{\min},\
\mathrm{age}_t(t_{k_t})\le A_{\max},\ v_{k_t}=v_t,\ m_{k_t}\ge0
\right],&k_t\in\mathrm{dom}(\mathcal C_{A,t^-}),\\
0,&k_t\notin\mathrm{dom}(\mathcal C_{A,t^-}).
\end{cases}
\]

Then:

\[
r_t^A=
\begin{cases}
r_{k_t}, & J_t^A=1,\\
0_{\mathbb H_d}, & \text{otherwise.}
\end{cases}
\]

A valid zero residual is now distinguishable from a miss because \(J_t^A\), not the residual value, records acceptance. The exact-to-general selection is:

\[
r_t^{\mathrm{use}}=
\begin{cases}
r_t^A, & J_t^A=1,\\
r_t^*, & J_t^A=0\text{ and }J_t^R=1,\\
0_{\mathbb H_d},&\text{otherwise.}
\end{cases}
\]

To connect point correction to the probability law evaluated by the proper score, let \(\mathrm{Ker}(\mathcal Z_H)\) denote Markov kernels on \(\mathcal Z_H\), and declare a measurable map:

\[
\mathfrak K_E:\mathbb H_d\rightarrow\mathrm{Ker}(\mathcal Z_H),
\qquad
\mathfrak K_E(0)(z,A)=\mathbf 1_A(z).
\]

For every measurable \(A\subseteq\mathcal Z_H\) and candidate residual \(r\in\mathbb H_d\), first set \(\bar r=\mathrm{clip}_{\delta_E}(r)\) and define:

\[
\mathsf Q_t^{(r)}(A\mid C_t)=
\int_{\mathcal Z_H}\mathfrak K_E(\bar r)(z,A)
\,\mathsf Q_B(dz\mid C_t).
\]

Because \(\mathfrak K_E(r)\) is a Markov kernel, \(\mathsf Q_t^{(r)}\) is a probability law. Define the candidate bundle:

\[
\mathcal O_t(r)=
\left(\mathsf Q_t^{(r)}(\cdot\mid C_t),\ b_t\oplus_E\bar r\right).
\]

The same effective residual \(\bar r\) therefore controls both the probability law and the point correction. The baseline bundle is exactly \(\mathcal O_t^B=\mathcal O_t(0)=(\mathsf Q_B(\cdot\mid C_t),b_t)\). Form the selected candidate \(\mathcal O_t^{\mathrm{cand}}=\mathcal O_t(r_t^{\mathrm{use}})\), and accept it only from current information:

\[
J_t^{\mathrm{pre}}=
\mathbf 1\!\left[
\mathcal R_{\mathrm{pre}}(\mathcal O_t^{\mathrm{cand}}\mid C_t;S_{t^-})
\le\eta_{\mathrm{pre}}
\right].
\]

The final residual law and bundle are:

\[
\mathcal O_t^R=
\begin{cases}
\mathcal O_t^{\mathrm{cand}},&J_t^{\mathrm{pre}}=1,\\
\mathcal O_t^B,&J_t^{\mathrm{pre}}=0,
\end{cases}
\qquad
\mathsf Q_t^R=
\begin{cases}
\mathsf Q_t^{(r_t^{\mathrm{use}})},&J_t^{\mathrm{pre}}=1,\\
\mathsf Q_B,&J_t^{\mathrm{pre}}=0.
\end{cases}
\]

An implementation may try the next lower-precedence residual after a rejected candidate only when that fallback order and every gate were preregistered. No post-observation quantity may enter this decision.

If an implementation supplies only the point operator \(\oplus_E\) and no declared kernel \(\mathfrak K_E\), it may claim improvement only on point diagnostics, not on the proper forecast score.

A bounded hash table can provide expected \(O(1)\) lookup after the bounded key has been constructed. The epoch and margin are constant-size certificate checks; graph traversal and compatibility estimation remain off the hot path. Key construction, hashing, collision handling, synchronization, and eviction remain separate costs. The active epoch \(v_t\) must increase whenever a dependent comparison map, edge set, threshold, or simultaneous defect bound changes. Local epochs and a reverse dependency index permit affected entries to be invalidated without globally flushing unrelated abstractions.

After observation, evaluate the particular residual candidate stored for key \(k\), either on a deployed trial or in shadow mode. Set \(I_{t,k}=1\) when

\[
\mathcal A_{\mathrm{post}}(\mathcal O_t^B,Z_{t+1})
-\mathcal A_{\mathrm{post}}(\mathcal O_t(r_k),Z_{t+1})
\ge\delta_A,
\]

and set \(I_{t,k}=0\) otherwise, where \(\delta_A>0\). A fallback residual belonging to another key may not update this candidate's confidence. Under an explicitly stationary, conditionally independent Bernoulli model for evaluated trials assigned to key \(k\), with prior \(\mathrm{Beta}(a_0,b_0)\) and \(a_0,b_0>0\), the posterior mean is:

\[
c_{k,t^-}=\frac{a_0+\sum_{u\in\mathcal T_{k,t^-}^{\mathrm{cache}}}I_{u,k}}
{a_0+b_0+|\mathcal T_{k,t^-}^{\mathrm{cache}}|}.
\]

Here \(\mathcal T_{k,t^-}^{\mathrm{cache}}\) contains only trials for that exact candidate whose outcome availability time satisfies \(a(Z_{u+1})\le t\). The Beta update is justified only for conditionally independent episode-level units. Overlapping windows from the same trajectory must be clustered or replaced by a declared effective-support calculation; they may not be counted as independent trials. This posterior mean is not automatically calibrated; calibration is tested on forward-held-out trials. Repeated monitoring uses a confidence sequence, alpha-spending rule, or fixed preregistered review times rather than repeatedly applying a fixed-sample interval. For drift, the implementation may use explicitly time-decayed counts, but must report the decay schedule and effective sample size. Low confidence, insufficient support, excessive pre-risk, or worsened post-loss routes the case to slow-path review.

The runtime packet uses a separate typed composition operator. Let:

\[
X_t=\chi(C_t,\mathcal M_t,G_t,\sigma_t)\in\mathcal X_{\mathrm{ctx}},
\]

and define the packet space:

\[
\mathcal Y_{\mathrm{pkt}}
=\mathcal N_{\mathrm{mem}}
\times\mathcal E_{\mathrm{graph}}
\times\mathcal L_{\mathrm{lane}}
\times\mathcal C_{\mathrm{compact}}
\times\mathcal M_{\mathrm{mode}}
\times\mathcal U_{\mathrm{control}}.
\]

Choose a normed finite-dimensional packet representation \(\mathcal V_Y\), a non-empty closed admissible subset \(\mathcal V_{Y,\mathrm{adm}}\), and maps:

\[
q_Y:\mathcal Y_{\mathrm{pkt}}\rightarrow\mathcal V_Y,
\qquad
d_Y:\mathcal V_{Y,\mathrm{adm}}\rightarrow\mathcal Y_{\mathrm{pkt}},
\]

with a deterministic projection selection \(\Pi_Y(v)\in\arg\min_{u\in\mathcal V_{Y,\mathrm{adm}}}\|u-v\|_Y\) and clipping radius \(\delta_Y>0\). Define:

\[
y\oplus_Y r=
\begin{cases}
y,&r=0,\\
d_Y\!\left(\Pi_Y\!\left(q_Y(y)+\mathrm{clip}_{\delta_Y}(r)\right)\right),&r\neq0.
\end{cases}
\]

The baseline and residual now have compatible types:

\[
B_Y:\mathcal X_{\mathrm{ctx}}\rightarrow\mathcal Y_{\mathrm{pkt}},
\qquad
R_Y:\mathcal X_{\mathrm{ctx}}\rightarrow\mathcal V_Y,
\]

and the packet prediction is:

\[
\widehat{\mathbf y}_{t+1}=B_Y(X_t)\oplus_Y R_Y(X_t).
\]

Its components are top memory nodes, top graph edges, retrieval lane, compaction risk, response mode, and an optional control branch. Discrete components may be encoded as logits with validity masks; the decoder must specify tie-breaking and null actions.

After execution, let \(\mathbf y_{t+1}^{\star}\) be the audited packet target and let \(\mathcal L_{\mathrm{pkt}}(\widehat{\mathbf y},\mathbf y^{\star})\in[0,1]\) be a declared weighted component loss. Packet residual utility is the observed improvement:

\[
I_t^Y=\mathbf 1\!\left[
\mathcal L_{\mathrm{pkt}}(B_Y(X_t)\oplus_Y R_Y(X_t),\mathbf y_{t+1}^{\star})
+\delta_{\mathrm{pkt}}
\le
\mathcal L_{\mathrm{pkt}}(B_Y(X_t),\mathbf y_{t+1}^{\star})
\right].
\]

Require \(\delta_{\mathrm{pkt}}>0\), so mere ties do not count as evidence that a packet residual improved utility.

Confidence is updated from the corresponding success/failure counts, as above. If \(\mathcal P_t=\{(p_m,w_m)\}_{m=1}^{M}\) is a non-empty candidate set with \(w_m\ge0\), \(\sum_mw_m>0\), and \(\lambda_P\ge0\), let \(\ell_t^{(m)}\in[0,1]\) be the declared post-observation loss appropriate to candidate \(p_m\), such as packet loss for packet candidates or event action for event candidates. An explicitly heuristic exponential-weights update is:

\[
w_m^{\mathrm{new}}=
\frac{w_m\exp(-\lambda_P\ell_t^{(m)})}
{\sum_{j=1}^{M}w_j\exp(-\lambda_P\ell_t^{(j)})}.
\]

This is not a Bayesian particle filter unless \(\ell_t^{(m)}\) is a negative log-likelihood with the required probabilistic model. Pruning or resampling must monitor effective sample size to avoid premature collapse.

The main failure modes are cache pollution, overcorrection, stale residuals, false similarity, invalid decoding, and packet-component incompatibility. Every implementation must report cache support, age, pre-risk, realized improvement, fallback frequency, and decoder failures.

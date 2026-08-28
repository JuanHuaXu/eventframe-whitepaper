# 4. Residual Prediction

Residual prediction separates a first-pass event estimate from a correction. The fallback baseline captures ordinary transition structure; when valid Bayesian beliefs exist, their posterior predictive becomes the first-pass base. The residual records a recurring statistical error relative to that recorded base. A residual is not a causal hypothesis unless separate intervention evidence identifies it as causal.

Let the baseline probability law and its conditional structured event template be:

\[
\mathsf Q_B:\mathcal E^k\rightarrow\mathcal P(\mathcal Z_H),
\qquad
B:\mathcal E^k\rightarrow\mathcal E,
\qquad b_t=B(C_t).
\]

The baseline is a fallback, not the final scored input when valid Bayesian beliefs are available. After the selective update in Section 5, let \(\mathcal K_t^{\mathrm{bel}}\) be the finite set of posterior buckets valid for the current context, horizon, provenance, and epoch. For each \(K\in\mathcal K_t^{\mathrm{bel}}\), let \(q_{K,t}^{\mathrm{eff}}\) be its accepted updated posterior, or its current cached prior when no evidence was admitted. Let \((\mathcal X_K,\mathscr A_{\mathcal X_K})\) be the bucket evidence space and let \(\nu_K\) be a declared sigma-finite dominating measure on it. Ordinary posterior-predictive semantics require a single measurable joint kernel

\[
\mathbb P_{K,\theta}:
\mathfrak H_t\longrightarrow
\mathcal P(\mathcal X_K\times\mathcal Z_H),
\qquad
\mathbb P_{K,\theta}(d\xi,dz\mid\mathfrak h),
\quad \theta\in\Theta_K.
\]

The outcome kernel appearing in the scored forecast has type

\[
\mathsf P_{H,K}:\Theta_K\times\mathcal E^k
\longrightarrow\mathcal P(\mathcal Z_H).
\]

Its evidence and outcome marginals are

\[
\begin{aligned}
\mathbb P_{K,\theta}^{\Xi}(D\mid\mathfrak h)
&=\mathbb P_{K,\theta}(D\times\mathcal Z_H\mid\mathfrak h),\\
\mathbb P_{K,\theta}^{Z}(A\mid\mathfrak h)
&=\mathbb P_{K,\theta}(\mathcal X_K\times A\mid\mathfrak h),
\end{aligned}
\]

for \(D\in\mathscr A_{\mathcal X_K}\) and \(A\in\mathscr A_H\). The likelihood and forecast kernel are linked by the required identities

\[
L_K(\xi\mid\theta,\mathfrak h)
=\frac{d\mathbb P_{K,\theta}^{\Xi}(\cdot\mid\mathfrak h)}{d\nu_K}(\xi),
\qquad
\mathbb P_{K,\theta}^{Z}(A\mid\mathfrak h)
=\mathsf P_{H,K}(A\mid\theta,c_k(\mathfrak h)).
\]

Here \(\mathbb P_{K,\theta}^{\Xi}(\cdot\mid\mathfrak h)\ll\nu_K\) for every declared \((\theta,\mathfrak h)\). Because \(\mathsf P_{H,K}\) below does not separately consume \(\xi\), the ordinary contract additionally requires the conditional factorization

\[
\mathbb P_{K,\theta}(d\xi,dz\mid\mathfrak h)
=L_K(\xi\mid\theta,\mathfrak h)\,\nu_K(d\xi)\,
\mathsf P_{H,K}(dz\mid\theta,c_k(\mathfrak h)).
\]

This states that evidence and next outcome are conditionally independent given \((\theta,c_k(\mathfrak h))\) under the declared history restriction. If that factorization fails, the predictive kernel must retain \(\xi\) or the additional history and the posterior-predictive integral below must use that conditional kernel. Selection conditioning in Section 5 is derived from the evidence factor and the complete nomination-and-activation event. A likelihood and forecast kernel not induced by one such joint family may still define a modular belief-conditioned forecast, but no proper-score or calibration test turns it into an ordinary posterior predictive; it is excluded from that semantic claim and reported separately.

Use frozen as-of fusion weights \(\lambda_{K,t}^{\mathrm{bel}}\ge0\) satisfying \(\sum_{K\in\mathcal K_t^{\mathrm{bel}}}\lambda_{K,t}^{\mathrm{bel}}=1\) when the set is non-empty. The posterior-predictive base law is

\[
\mathsf Q_t^0(A\mid C_t)=
\begin{cases}
\displaystyle
\sum_{K\in\mathcal K_t^{\mathrm{bel}}}
\lambda_{K,t}^{\mathrm{bel}}
\int_{\Theta_K}\mathsf P_{H,K}(A\mid\theta,C_t)
q_{K,t}^{\mathrm{eff}}(d\theta),
&\mathcal K_t^{\mathrm{bel}}\neq\varnothing,\\[2mm]
\mathsf Q_B(A\mid C_t),
&\mathcal K_t^{\mathrm{bel}}=\varnothing.
\end{cases}
\]

Thus \(\mathsf Q_t^0\in\mathcal P(\mathcal Z_H)\). The weights, bucket-eligibility rule, kernels, and any approximation are frozen in \(\Xi_B\). A plug-in implementation is permitted only when \(\Xi_B\) replaces the integral by a declared measurable posterior decision rule and labels it as plug-in prediction.

For auxiliary structured fields, declare a measurable posterior-aware template map \(B_H^{\mathrm{bel}}\). Set

\[
b_t^0=
\begin{cases}
B_H^{\mathrm{bel}}\!\left(C_t,
(q_{K,t}^{\mathrm{eff}})_{K\in\mathcal K_t^{\mathrm{bel}}},
(\lambda_{K,t}^{\mathrm{bel}})_{K\in\mathcal K_t^{\mathrm{bel}}}\right),
&\mathcal K_t^{\mathrm{bel}}\neq\varnothing,\\
B(C_t),&\mathcal K_t^{\mathrm{bel}}=\varnothing.
\end{cases}
\]

The canonical order is fixed: construct the frontier, admit evidence, update or retrieve posteriors, form \((\mathsf Q_t^0,b_t^0)\), select only residuals certified for that base, apply the residual kernel, and then score the resulting law.

To make structured correction type-correct, choose a finite-dimensional Hilbert space \(\mathscr H\). Let \(\mathbb H_d^E\) and \(\mathbb H_d^Q\) be separately tagged copies of the real vector space of self-adjoint operators on \(\mathscr H\), each equipped with the Frobenius norm \(\|\cdot\|_F\). The superscripts distinguish point-template semantics from forecast-law semantics even when an implementation uses the same matrix representation. Define:

\[
q_E:\mathcal E\rightarrow\mathbb H_d^E,
\qquad
d_E:\mathcal Q_{E,\mathrm{adm}}\rightarrow\mathcal E,
\]

where \(\mathcal Q_{E,\mathrm{adm}}\subseteq\mathbb H_d^E\) is a non-empty closed admissible set and \(d_E\) is a decoder, not an inverse of the lossy encoder. For a radius \(\delta_E>0\), define point-residual norm clipping by:

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
\qquad r\in\mathbb H_d^E.
\]

Thus zero is an exact identity even when the encoder is lossy or the baseline encoding is outside the admissible set.

This construction takes limited inspiration from the use of self-adjoint operator representations in Causal Fermion Systems [1,2]. The clipping radius, admissible set, projection, decoder, and residual objective are EventFrame definitions; they are not CFS terminology or consequences of the CFS causal action principle. The construction does not inherit CFS field equations and makes no claim of physical equivalence.

Residuals are estimated after observation and are indexed by the forecast horizon that generated their label. For the forecast issued at \(t\), a simple point-representation residual exists only when the concrete next event lies inside that same horizon:

\[
r_{t,H}^{E,\mathrm{obs}}=
q_E(e_{t+1})-q_E(b_t^0),
\qquad
0<\tau(e_{t+1})-\tau(e_t)\le H.
\]

If \(Z_{t+1}=\varnothing\), then \(r_{t,H}^{E,\mathrm{obs}}\) is undefined for that forecast origin. A concrete event observed after \(H\) may label a later forecast origin, but it must not retroactively become the point residual of the expired \(H\)-horizon forecast. To learn a law correction from either branch, declare a measurable horizon-specific distributional residual estimator with a separately tagged codomain

\[
\rho_H^Q:\mathcal P(\mathcal Z_H)\times\mathcal Z_H\rightarrow\mathbb H_d^Q,
\qquad
r_{t,H}^{Q,\mathrm{obs}}=
\rho_H^Q\!\left(\mathsf Q_t^0(\cdot\mid C_t),Z_{t+1}\right).
\]

Its objective may be a proper-score gradient, a constrained law update, or another predeclared rule, but it must be defined at \(Z_{t+1}=\varnothing\), fitted without future leakage, and evaluated on later outcomes. Define the residual mode set \(\mathcal M_R=\{\varnothing,E,Q,EQ\}\) and a typed residual record

\[
\mathbf r=(r^E,r^Q,m)
\in\mathbb H_d^E\times\mathbb H_d^Q\times\mathcal M_R.
\]

Write \(\mathcal V_R=\mathbb H_d^E\times\mathbb H_d^Q\times\mathcal M_R\) and \(\mathbf 0_R=(0_E,0_Q,\varnothing)\).

The mode says which components are semantically present; an absent component is stored as zero, but zero remains a valid present correction when its mode includes that component. A point-only record \(m=E\) may support point diagnostics but cannot change the forecast law. A law-only record \(m=Q\) may change the law and proper score while leaving non-mark, non-time template fields at baseline. A joint record \(m=EQ\) contains separately estimated components and must pass joint forward validation of the resulting bundle; it does not assert \(r^E=r^Q\) or infer one component's semantics from the other. A no-event observation must not be silently encoded as a concrete point residual. Every cache entry records its mode, estimator identities, horizon, and censoring convention; reuse across horizons requires a separately validated transport rule. In all cases, a stored record is a reusable correction candidate whose utility must be re-evaluated on later observations.

The general residual cache available immediately before prediction is:

\[
\mathcal C_{R,t^-}=
\{(\kappa_i,\mathbf r_i,c_i,n_i,t_i,v_i,\mu_i,H_i,
\upsilon_i^{\mathrm{bel}},\mu_i^{\mathrm{bel}},
\mu_i^{\mathrm{tmpl}},s_i)\}_{i=1}^{N_t},
\qquad
\kappa:\mathcal E^k\rightarrow\mathcal K_R,
\qquad \mathbf r_i\in\mathcal V_R,
\]

where \(c_i\) is residual confidence, \(n_i\) is effective support, \(t_i\) is the last certified update time, \(v_i\) is its abstraction epoch, \(\mu_i\) is its compatibility safety margin, \(H_i\) is its forecast horizon, \(\upsilon_i^{\mathrm{bel}}\) is the posterior-predictive certificate version against which it was calibrated, \(\mu_i^{\mathrm{bel}}\) is its materialized base-law motion margin, and \(\mu_i^{\mathrm{tmpl}}\) is its base-template motion margin. The provenance \(s_i\) includes component modes, estimator identities, censoring convention, eligible training interval, posterior-predictive law and template reference identities, and permitted motion radii. Only entries whose availability time is at most \(t\) may occur in \(\mathcal C_{R,t^-}\). For \(N_t>0\), let:

For each residual entry, freeze a bounded law metric \(D_{\mathrm{res}}\), a posterior-predictive reference law \(\mathsf Q_i^{0,\mathrm{ref}}\), and a permitted radius \(\epsilon_i^{\mathrm{bel}}\). For point-bearing modes also freeze a bounded template metric \(D_{\mathrm{tmpl}}\), reference template \(b_i^{0,\mathrm{ref}}\), and radius \(\epsilon_i^{\mathrm{tmpl}}\). Let \(\overline D_{i,t}^{\mathrm{bel}}\) and \(\overline D_{i,t}^{\mathrm{tmpl}}\) be analytic or simultaneously valid upper bounds for the respective motions, and materialize

\[
\mu_i^{\mathrm{bel}}=
\epsilon_i^{\mathrm{bel}}-\overline D_{i,t}^{\mathrm{bel}},
\qquad
\mu_i^{\mathrm{tmpl}}=
\epsilon_i^{\mathrm{tmpl}}-\overline D_{i,t}^{\mathrm{tmpl}},
\]

where the bounded quantities cover

\[
D_{\mathrm{res}}(\mathsf Q_t^0,\mathsf Q_i^{0,\mathrm{ref}}),
\qquad
D_{\mathrm{tmpl}}(b_t^0,b_i^{0,\mathrm{ref}}).
\]

Each bound includes the declared posterior-approximation error propagated through \(\mathsf P_{H,K}\), fusion, and, for the point path, \(B_H^{\mathrm{bel}}\), in addition to statistical uncertainty. A plug-in distance or approximation estimate without uncertainty coverage is not a residual-survival certificate. Ordinary posterior updates remain inside version \(\upsilon_t^{\mathrm{bel}}\) only while every applicable fixed-reference margin remains valid. Otherwise the dependency-closure transition in Section 7 bumps the local version and marks affected residual entries stale before the new posterior becomes readable.

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
v_{j_t}=v_t,\quad H_{j_t}=H,\quad \mu_{j_t}\ge0,\\
\upsilon_{j_t}^{\mathrm{bel}}=\upsilon_t^{\mathrm{bel}},\quad
\bigl(m_{j_t}\notin\{Q,EQ\}\text{ or }\mu_{j_t}^{\mathrm{bel}}\ge0\bigr),\\
\bigl(m_{j_t}\notin\{E,EQ\}\text{ or }\mu_{j_t}^{\mathrm{tmpl}}\ge0\bigr),\quad
s_{j_t}\text{ is valid}
\end{array}
\right],&N_t>0,\\
0,&N_t=0.
\end{cases}
\]

The retrieved residual is:

\[
\mathbf r_t^*=
\begin{cases}
\mathbf r_{j_t}, & J_t^R=1,\\
\mathbf 0_R, & \text{otherwise.}
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
\mathcal V_R\times[0,1]\times\mathbb N_0\times\mathcal T
\times\mathbb N_0\times\mathbb R\times\mathbb R_{>0}
\times\mathbb N_0\times\mathbb R\times\mathbb R
\times\mathcal S_{\mathrm{prov}}.
\]

For \(k_t=\alpha(C_t)\), bind the cache entry only when it exists:

\[
 k_t\in\mathrm{dom}(\mathcal C_{A,t^-})
\quad\Longrightarrow\quad
\mathcal C_{A,t^-}(k_t)=
(\mathbf r_{k_t},c_{k_t},n_{k_t},t_{k_t},v_{k_t},\mu_{k_t},H_{k_t},
\upsilon_{k_t}^{\mathrm{bel}},\mu_{k_t}^{\mathrm{bel}},
\mu_{k_t}^{\mathrm{tmpl}},s_{k_t}),
\]

where \(n_{k_t}\) is effective support after accounting for clustered or overlapping trials, \(v_{k_t}\) is the cache entry's local abstraction epoch, \(v_t\) is the active as-of epoch for the same dependency region, \(\mu_{k_t}\) is the compatibility safety margin materialized by the slow path, \(H_{k_t}\) is the horizon under which the residual was estimated, \(\upsilon_{k_t}^{\mathrm{bel}}\) is its posterior-predictive certificate version, and \(\mu_{k_t}^{\mathrm{bel}},\mu_{k_t}^{\mathrm{tmpl}}\) are its materialized law and template motion margins. The provenance \(s_{k_t}\) records component modes, estimator identities, censoring convention, eligible training interval, posterior-predictive law and template reference identities, and permitted motion radii. If \(E(k_t)\) is the declared set of compatibility edges on which the entry depends, for example:

\[
\mu_{k_t}=
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
\begin{gathered}
c_{k_t}\ge\gamma_A,\quad n_{k_t}\ge n_{\min},\quad
\mathrm{age}_t(t_{k_t})\le A_{\max},\\
v_{k_t}=v_t,\quad H_{k_t}=H,\quad \mu_{k_t}\ge0,\\
\upsilon_{k_t}^{\mathrm{bel}}=\upsilon_t^{\mathrm{bel}},\quad
\bigl(m_{k_t}\notin\{Q,EQ\}\text{ or }\mu_{k_t}^{\mathrm{bel}}\ge0\bigr),\\
\bigl(m_{k_t}\notin\{E,EQ\}\text{ or }\mu_{k_t}^{\mathrm{tmpl}}\ge0\bigr),\quad
s_{k_t}\text{ is valid}
\end{gathered}
\right],&k_t\in\mathrm{dom}(\mathcal C_{A,t^-}),\\
0,&k_t\notin\mathrm{dom}(\mathcal C_{A,t^-}).
\end{cases}
\]

Then:

\[
\mathbf r_t^A=
\begin{cases}
\mathbf r_{k_t}, & J_t^A=1,\\
\mathbf 0_R, & \text{otherwise.}
\end{cases}
\]

A valid zero residual is now distinguishable from a miss because \(J_t^A\), not the residual value, records acceptance. The exact-to-general selection is:

\[
\mathbf r_t^{\mathrm{use}}=
\begin{cases}
\mathbf r_t^A, & J_t^A=1,\\
\mathbf r_t^*, & J_t^A=0\text{ and }J_t^R=1,\\
\mathbf 0_R,&\text{otherwise.}
\end{cases}
\]

To connect a law residual to the probability law evaluated by the proper score, choose \(\delta_Q>0\), define \(\mathrm{clip}_{\delta_Q}\) on \(\mathbb H_d^Q\) by the same norm-clipping rule as above, and let \(\mathrm{Ker}(\mathcal Z_H)\) denote Markov kernels on the measurable space \((\mathcal Z_H,\mathscr A_H)\). Declare:

\[
\mathfrak K_H^Q:\mathbb H_d^Q\rightarrow\mathrm{Ker}(\mathcal Z_H),
\qquad
\mathfrak K_H^Q(0_Q)(z,A)=\mathbf 1_A(z).
\]

For every \(A\in\mathscr A_H\), the evaluation map \((r^Q,z)\mapsto\mathfrak K_H^Q(r^Q)(z,A)\) must be jointly measurable on \(\mathbb H_d^Q\times\mathcal Z_H\); for fixed \(r^Q\), it must be a Markov kernel. These conditions supply the measurable structure actually used below without requiring an unspecified sigma-algebra on a function space. The declaration covers every \(z\in\mathcal Z_H\), including \(\varnothing\), for every effective residual. The implementation must explicitly specify both \(\mathfrak K_H^Q(\bar r^Q)(\varnothing,\{\varnothing\})\) and \(\mathfrak K_H^Q(\bar r^Q)(z,\{\varnothing\})\) for \(z\in\mathcal Z_H^+\); preservation of the no-event atom is not a default assumption.

For \(\mathbf r=(r^E,r^Q,m)\), define the effective components

\[
\bar r^E=
\begin{cases}
\mathrm{clip}_{\delta_E}(r^E),&m\in\{E,EQ\},\\
0_E,&m\in\{\varnothing,Q\},
\end{cases}
\qquad
\bar r^Q=
\begin{cases}
\mathrm{clip}_{\delta_Q}(r^Q),&m\in\{Q,EQ\},\\
0_Q,&m\in\{\varnothing,E\}.
\end{cases}
\]

For every \(A\in\mathscr A_H\), define:

\[
\mathsf Q_t^{(\mathbf r)}(A\mid C_t)=
\int_{\mathcal Z_H}\mathfrak K_H^Q(\bar r^Q)(z,A)
\,\mathsf Q_t^0(dz\mid C_t).
\]

Because \(\mathfrak K_H^Q(r^Q)\) is a Markov kernel, \(\mathsf Q_t^{(\mathbf r)}\) is a probability law. Its no-event mass is explicitly:

\[
\begin{aligned}
\mathsf Q_t^{(\mathbf r)}(\{\varnothing\}\mid C_t)
={}&\mathfrak K_H^Q(\bar r^Q)(\varnothing,\{\varnothing\})
\mathsf Q_t^0(\{\varnothing\}\mid C_t)\\
&+\int_{\mathcal Z_H^+}
\mathfrak K_H^Q(\bar r^Q)(z,\{\varnothing\})
\,\mathsf Q_t^0(dz\mid C_t).
\end{aligned}
\]

Thus a nonzero residual may change the no-event probability by moving mass in either direction. Let \(\mathrm{lift}_H:\mathcal E\times\mathcal Z_H^+\to\mathcal E\) be a declared measurable map that aligns a structured event template with the mark and time selected by \(d_H\). Define the no-event-capable structured point summary:

\[
\hat e_t^H(\mathbf r)=
\begin{cases}
\varnothing,
&d_H(\mathsf Q_t^{(\mathbf r)})=\varnothing,\\
\mathrm{lift}_H\!\left(b_t^0\oplus_E\bar r^E,d_H(\mathsf Q_t^{(\mathbf r)})\right),
&d_H(\mathsf Q_t^{(\mathbf r)})\in\mathcal Z_H^+.
\end{cases}
\]

\[
\mathcal O_t(\mathbf r)=
\left(\mathsf Q_t^{(\mathbf r)}(\cdot\mid C_t),\hat e_t^H(\mathbf r)\right)
\in\mathcal P(\mathcal Z_H)\times\mathcal E_\varnothing.
\]

The residual record pairs two independently typed semantics. The law component controls the proper forecast, while the point component controls auxiliary structured fields. The fixed \(d_H\) and \(\mathrm{lift}_H\) keep the final mark and time coherent with the corrected law, but they do not prove that auxiliary fields improved; a joint record must pass forward validation of the complete output bundle. The no-residual bundle is exactly \(\mathcal O_t^0=\mathcal O_t(\mathbf 0_R)=(\mathsf Q_t^0(\cdot\mid C_t),\hat e_t^H(\mathbf 0_R))\). It equals the original baseline bundle only when \(\mathcal K_t^{\mathrm{bel}}=\varnothing\). Form the selected candidate \(\mathcal O_t^{\mathrm{cand}}=\mathcal O_t(\mathbf r_t^{\mathrm{use}})\), and accept it only from current information:

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
\mathcal O_t^0,&J_t^{\mathrm{pre}}=0,
\end{cases}
\qquad
\mathsf Q_t^R=
\begin{cases}
\mathsf Q_t^{(\mathbf r_t^{\mathrm{use}})},&J_t^{\mathrm{pre}}=1,\\
\mathsf Q_t^0,&J_t^{\mathrm{pre}}=0.
\end{cases}
\]

Define the deterministic scored residual-policy map \(\mathfrak F_R\) by

\[
\mathfrak F_R(\mathsf Q_t^0,b_t^0,C_t;S_{t^-})=\mathsf Q_t^R.
\]

It includes posterior-aware cache selection, the full-outcome residual kernel, and the pre-observation fallback. This map is reused by the omitted-influence audit in Section 5; therefore that audit compares complete scored laws rather than detached posterior states.

An implementation may try the next lower-precedence residual after a rejected candidate only when that fallback order and every gate were preregistered. No post-observation quantity may enter this decision.

If an implementation supplies only the point operator \(\oplus_E\) and no declared law component and kernel \(\mathfrak K_H^Q\), it may claim improvement only on point diagnostics, not on the proper forecast score. Conversely, a law-only record may support a proper-score claim but does not claim correction of auxiliary template fields.

Worked toy instantiation. The following finite example is arithmetic scaffolding, not an experimental result. Let \(H=1\) second and order the outcome space as

\[
\mathcal Z_H=\{z_a,z_b,\varnothing\},
\qquad
z_a=(\mathrm{move},0.2),
\qquad
z_b=(\mathrm{stop},0.8).
\]

For one context \(C_t\), suppose \(\mathcal K_t^{\mathrm{bel}}=\varnothing\), so the posterior-predictive fallback is the row vector \(\mathsf Q_t^0=\mathbf q_B=(0.50,0.20,0.30)\) and \(b_t^0=B(C_t)\).

Take \(\mathscr H=\mathbb R^3\), represent both tagged residual components by diagonal self-adjoint matrices, and use the certified joint cache record

\[
r_0^E=r_0^Q=\mathrm{diag}(0.10,-0.05,-0.05),
\qquad
\mathbf r_0=(r_0^E,r_0^Q,EQ),
\qquad
\delta_E=\delta_Q=0.20.
\]

The equality of the two matrices is a convenience of this toy, not a semantic identification. Their Frobenius norm is \(\sqrt{0.015}<0.20\), so clipping leaves both unchanged. For completeness, one distributional estimator on this finite space is

\[
\rho_H^Q(\mathbf q,z)
=\mathrm{diag}(\mathbf 1_z-\mathbf q),
\]

where \(\mathbf 1_z\) is the one-hot vector for any \(z\in\mathcal Z_H\), including \(\varnothing\). A separately declared point estimator supplies \(r_0^E\). A cache may store projected or averaged outputs such as \(\mathbf r_0\), together with component-specific estimator identities, horizon, and provenance; the example does not claim that one observation produced either component.

Define

\[
\lambda(r^Q)=
\min\!\left(1,
\max\!\left(0,
\frac{\langle r^Q,r_0^Q\rangle_F}{\|r_0^Q\|_F^2}
\right)\right)
\]

and let the full-outcome kernel, in the displayed outcome order, be the row-stochastic matrix

\[
K(r^Q)=
\begin{pmatrix}
1&0&0\\
\lambda(r^Q)/4&1-\lambda(r^Q)/4&0\\
\lambda(r^Q)/6&0&1-\lambda(r^Q)/6
\end{pmatrix}.
\]

Set \(\mathfrak K_H^Q(r^Q)(z_i,\{z_j\})=K(r^Q)_{ij}\). Every row sums to one, all entries are non-negative, and \(K(0_Q)=I\). At \(r_0^Q\), the corrected law is

\[
\mathbf q_R=\mathbf q_BK(r_0^Q)
=(0.60,0.15,0.25).
\]

The law correction therefore moves \(0.05\) probability from \(z_b\) and \(0.05\) from \(\varnothing\) to \(z_a\); the no-event branch is operational rather than pinned. Let \(d_H\) select a mode under zero-one loss with the displayed order as tie-break. Let \(b_t^0=e_a\in\mathcal E\), whose mark and anchor correspond to \(z_a\), and set \(q_E(e_a)=\mathrm{diag}(1,0,0)\). Let \(\mathcal Q_{E,\mathrm{adm}}\) be the diagonal probability simplex, let \(\Pi_E\) be Euclidean projection onto it, and let \(d_E\) decode its largest coordinate into the corresponding marked template with the same tie-break. Then \(e_a\oplus_Er_0^E=e_a\). With \(\mathrm{lift}_H\) replacing the template's mark and temporal anchor by the marked decision, the coherent summary is

\[
d_H(\mathbf q_R)=z_a,
\qquad
\hat e_t^H(\mathbf r_0)=\mathrm{lift}_H(e_a,z_a)=e_a.
\]

If \(z_a\) is observed, logarithmic loss changes from \(-\log(0.50)\approx0.693\) to \(-\log(0.60)\approx0.511\). If \(\varnothing\) is observed, it worsens from \(-\log(0.30)\approx1.204\) to \(-\log(0.25)\approx1.386\). This paired calculation shows why a residual needs forward evidence and cannot be certified from one favorable case.

Suppose the exact joint cache entry records \(H_{k_t}=1\), \(\upsilon_{k_t}^{\mathrm{bel}}=\upsilon_t^{\mathrm{bel}}\), \(\mu_{k_t}^{\mathrm{bel}}\ge0\), \(\mu_{k_t}^{\mathrm{tmpl}}\ge0\), all other metadata gates pass, and the requested horizon is \(H=1\). Then \(J_t^A=1\) and \(\mathbf r_t^{\mathrm{use}}=\mathbf r_0\). The same entry requested at \(H=0.5\) has \(J_t^A=0\) solely because \(H_{k_t}\ne H\), so the expired-horizon correction is not reused.

Finally, let the finite design family built on \(\mathcal S_{\mathrm{obj}}\) be \(\{\Theta_0,\Theta_1\}\), where \(\Theta_0\) is baseline-only and \(\Theta_1\) includes the certified residual. Take \(\epsilon_{AP}=0.05\), \(D_K^{\mathrm{cert},\star}(\Theta_0)=0.03\), \(D_K^{\mathrm{cert},\star}(\Theta_1)=0.04\), \(\epsilon_{\mathrm{prop}}=0.02\), and suppose the grouped design-sample calculations are

\[
\begin{aligned}
\left(
\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{obj}}}(\Theta_0),
\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{obj}}}(\Theta_1)
\right)&=(0.80,0.72),\\
\left(
\widehat{\mathcal R}_{\mathrm{pri}}^{\mathcal S_{\mathrm{obj}}}(\Theta_0),
\widehat{\mathcal R}_{\mathrm{pri}}^{\mathcal S_{\mathrm{obj}}}(\Theta_1)
\right)&=(0.30,0.24),\\
\left(
\mathcal C_{\mathrm{rep}}(\Theta_0),
\mathcal C_{\mathrm{rep}}(\Theta_1)
\right)&=(0,0.01).
\end{aligned}
\]

with \(\mathrm{UCB}[0.72-0.80]=-0.02\le\epsilon_{\mathrm{prop}}\) and \(\lambda_{\mathrm{rep}}=1\). Both designs remain feasible, while their empirical composite values are \(0.30\) and \(0.25\), so the deterministic operational rule selects \(\widehat\Theta_\Gamma=\Theta_1\). An untouched \(\mathcal S_{\mathrm{conf}}\) may then confirm or reject the frozen claim, but it cannot alter the candidate family or the selected residual. These stipulated values demonstrate how to execute the contracts; they are not measurements of EventFrame performance.

A bounded hash table can provide expected \(O(1)\) lookup after the bounded key has been constructed. The epoch and margins are constant-size certificate checks; graph traversal, component-motion certification, and compatibility estimation remain off the hot path. Key construction, hashing, collision handling, synchronization, and eviction remain separate costs. The active epoch \(v_t\) or posterior-predictive version \(\upsilon_t^{\mathrm{bel}}\) must increase whenever its dependent graph contract or any certified law or template motion region changes. Local versions and a reverse dependency index permit affected entries to be invalidated without globally flushing unrelated abstractions. A predictive sheaf snap or out-of-tolerance posterior update is built against shadow state and published atomically with its affected keys and epoch map. A reader uses one immutable graph-posterior-key-epoch snapshot for the entire prediction. Entries invalidated by publication fall back to the current posterior-predictive no-residual law or another currently certified cache path until recertified; rollback republishes the previous complete structure with a new monotone publication version rather than reusing an old identifier.

After observation, evaluate the particular residual candidate stored for key \(k\), either on a deployed trial or in shadow mode. Set \(I_{t,k}=1\) when

\[
\mathcal A_{\mathrm{post}}(\mathcal O_t^0,Z_{t+1})
-\mathcal A_{\mathrm{post}}(\mathcal O_t(\mathbf r_k),Z_{t+1})
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

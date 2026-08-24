# 3. Mathematical Framework

The mathematical framework turns compressed event frames into objects that can be predicted, evaluated, cached, and abstracted. Given a context \(C_t\), the predictor must produce a next-event distribution before the next observation exists. Only after the observation arrives may the runtime compute realized prediction loss and update memory or abstraction.

Let \(\Omega\) denote a dense substrate state space. For a finite region \(A_t\), let \(\omega_{A_t} \in \Omega^{A_t}\) denote the substrate history over that region. At temporal resolution \(\Delta_\tau\), an event frame is produced by:

\[
e_t = \Gamma_{\Delta_\tau}(\omega_{A_t}), \qquad
\Gamma_{\Delta_\tau}: \Omega^{A_t} \rightarrow \mathcal{E}_{\Delta_\tau}.
\]

The coarse-graining \(\Gamma_{\Delta_\tau}\) is task-relative and lossy. It selects distinctions available to prediction, memory, and review; it does not establish a fundamental discretization of spacetime. The Planck scales and physical information bounds motivate caution about microscopic descriptions but do not prove the EventFrame sparsity hypothesis [7--9].

A trajectory at fixed resolution is:

\[
E_{1:T}=(e_1,\ldots,e_T), \qquad e_t\in\mathcal E_{\Delta_\tau},
\]

and a time quantizer is:

\[
Q_{\Delta_\tau}:\mathbb R\rightarrow\mathcal T_{\Delta_\tau}.
\]

Second-level or microsecond-level precision is permitted only when the measurement process supports it. Finer resolution creates more candidate frames and can expose boundaries, but also increases noise and cache pressure.

For a context length \(k\), define:

\[
C_t=e_{t-k+1:t}\in\mathcal E^k.
\]

Let \(\mathfrak C_{\mathrm{adm}}\subseteq\mathcal E^k\) be the declared admissible context domain on which the chosen version of each conditional forecast law is defined. Population suprema below range over this domain or over the support of a named evaluation law, not over arbitrary zero-probability contexts.

Let \(a(x)\) be the time at which observation, label, cache record, or derived object \(x\) becomes available to the runtime. Let \(\mathscr F_t^{\mathrm{pred}}\) be the information available when the prediction at index \(t\) is issued, including \(C_t\) but excluding \(Z_{t+1}\). Mutable runtime state is the left-limit snapshot \(S_{t^-}\), constructed only from objects with \(a(x)\le t\). Every prediction, priority, cache lookup, abstraction decision, and pre-risk value used at time \(t\) must be measurable with respect to \(\mathscr F_t^{\mathrm{pred}}\). For a no-event outcome, \(a(Z_{t+1})\) is no earlier than expiration of horizon \(H\); delayed labels use their actual later availability time.

Let \(\nu(e)\) be the event mark or occurrence type and \(\tau(e)\) its time. Over a prediction horizon \(H>0\), the next outcome is:

\[
Z_{t+1}=
\begin{cases}
(\nu(e_{t+1}),\tau(e_{t+1})-\tau(e_t)), & \text{if an event occurs within }H,\\
\varnothing, & \text{otherwise.}
\end{cases}
\]

A probabilistic predictor returns a distribution rather than only a point:

\[
\mathsf Q_\theta(\cdot\mid C_t)\in\mathcal P(\mathcal Z_H),
\]

where \(\mathcal Z_H\) contains marked event times in \((0,H]\) and the no-event outcome \(\varnothing\). Let \(\hat e_\theta(C_t)\in\mathcal E\) be a separately declared point decision or structured point summary. The typed predictor output is the bundle:

\[
\mathcal O_\theta(C_t)=
\left(\mathsf Q_\theta(\cdot\mid C_t),\hat e_\theta(C_t)\right)
\in\mathcal P(\mathcal Z_H)\times\mathcal E.
\]

The primary prediction objective is a declared strictly proper scoring rule applied to the probability-law component:

\[
\mathcal L_{\mathrm{pred}}(\theta;t)
=S_{\mathrm{prop}}\!\left(\mathsf Q_\theta(\cdot\mid C_t),Z_{t+1}\right).
\]

Fix a dominating reference measure \(\mu_H\) on the marked-time branch, including declared units for time, and let \(q_\theta=d\mathsf Q_\theta^{\mathrm{event}}/d\mu_H\) be the event subdensity. Its integral equals \(1-\mathsf Q_\theta(\{\varnothing\}\mid C_t)\). Relative to this fixed reference measure, the logarithmic score is one implementation:

\[
\mathcal L_{\log}(\theta;t)=
\begin{cases}
-\log q_\theta(\nu_{t+1},\Delta t_{t+1}\mid C_t), & Z_{t+1}\neq\varnothing,\\
-\log \mathsf Q_\theta(\{\varnothing\}\mid C_t), & Z_{t+1}=\varnothing.
\end{cases}
\]

Changing \(\mu_H\) or the time units changes density values by an additive score constant, so forecast comparisons must hold them fixed. This score covers event identity, timing, uncertainty, and right-censoring; calibration remains an empirical property to test. Proper scoring rules prevent a predictor from improving its expected score by reporting a distribution other than the one it believes [6].

For human-readable diagnostics, let \(\hat Z_{t+1}\) be a point summary of the distribution. A bounded event-aware timing diagnostic is:

\[
\mathcal L_{\mathrm{event}}^H(\hat Z,Z)=
\begin{cases}
0, & \hat Z=Z=\varnothing,\\
1, & \text{exactly one is }\varnothing\text{ or their marks differ},\\
\min\!\left(1,\dfrac{|\widehat{\Delta t}-\Delta t|}{H}\right),
& \text{their non-null marks agree.}
\end{cases}
\]

Unlike the original timing-only diagnostic, this expression cannot assign zero loss to the wrong event type merely because its timestamp is correct. It remains a diagnostic; model fitting and forecast comparison should use \(\mathcal L_{\mathrm{pred}}\).

For any other field, use a distinct projection \(\psi_i:\mathcal E\rightarrow\mathcal X_i\) and declared distance. The ordinary field loss is conditional on a concrete observed event:

\[
\mathcal L_i(\hat e_{t+1},Z_{t+1})
=d_i(\psi_i(\hat e_{t+1}),\psi_i(e_{t+1})),
\qquad Z_{t+1}\neq\varnothing.
\]

When \(Z_{t+1}=\varnothing\), this field loss is not evaluated unless a separate missing-aware loss with an explicit no-event symbol has been declared.

EventFrame uses separate pre-observation and post-observation quantities. For a candidate output bundle \(\widetilde{\mathcal O}=(\widetilde{\mathsf Q},\tilde e)\), a pre-observation admissibility risk may use only information available at prediction time:

\[
\mathcal R_{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t)
=\lambda_a^{\mathrm{pre}}D_{\mathrm{abs}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_c^{\mathrm{pre}}D_{\mathrm{edge}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_u^{\mathrm{pre}}U^{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t).
\]

The three components lie in \([0,1]\), the weights are non-negative, and \(\lambda_a^{\mathrm{pre}}+\lambda_c^{\mathrm{pre}}+\lambda_u^{\mathrm{pre}}=1\).

The proper loss need not be bounded; the logarithmic score above is not. To combine it with bounded system diagnostics, choose and preregister an order-preserving map \(g_{\mathrm{pred}}:\overline{\mathbb R}\to[0,1]\) on the declared finite score range, with \(g_{\mathrm{pred}}(+\infty)=1\), and define:

\[
\overline{\mathcal L}_{\mathrm{pred}}(\widetilde{\mathsf Q},Z)
=g_{\mathrm{pred}}\!\left(S_{\mathrm{prop}}(\widetilde{\mathsf Q},Z)\right).
\]

Constant or order-reversing transforms are inadmissible. Unless \(g_{\mathrm{pred}}\) is a positive affine transformation on the score's range, \(\overline{\mathcal L}_{\mathrm{pred}}\) is not asserted to remain proper. Model fitting and forecast comparison continue to report the untransformed proper score. After \(Z_{t+1}\) is observed, the bounded realized event action is:

\[
\begin{aligned}
\mathcal A_{\mathrm{post}}(\widetilde{\mathcal O},Z_{t+1})
={}&\lambda_p^{\mathrm{post}}\overline{\mathcal L}_{\mathrm{pred}}(\widetilde{\mathsf Q},Z_{t+1})
+\lambda_a^{\mathrm{post}}D_{\mathrm{abs}}^{\mathrm{post}}(\widetilde{\mathcal O},Z_{t+1})\\
&+\lambda_c^{\mathrm{post}}D_{\mathrm{edge}}^{\mathrm{post}}(\widetilde{\mathcal O},Z_{t+1})
+\lambda_u^{\mathrm{post}}U^{\mathrm{post}}(\widetilde{\mathcal O},Z_{t+1}).
\end{aligned}
\]

Every post-observation component lies in \([0,1]\), the four post weights are non-negative and sum to one, and therefore \(\mathcal A_{\mathrm{post}}\in[0,1]\).

The fast path may gate a correction using \(\mathcal R_{\mathrm{pre}}\); it may never use \(\mathcal A_{\mathrm{post}}\) before the observation exists.

The governing principle can now be stated without overloading \(\Omega\). It is evaluated at a fixed resolution \(\Gamma_{\Delta_\tau}\); comparisons across resolutions are a separate outer experiment on common raw histories. Group the event-residual implementation contract as:

\[
\Xi_R=(q_E,d_E,\Pi_E,\delta_E,\mathfrak K_E,
\alpha,\kappa,\epsilon_R,\text{cache gates}),
\]

and the candidate abstraction structure as \(\Xi_A\), containing its compatibility graph and comparison maps. Separately freeze an evaluation contract:

\[
\begin{aligned}
\Lambda_{\mathrm{eval}}=
({}&P_{\mathrm{obj}},P_{\mathrm{conf}},P_\star,
\mathfrak C_{\mathrm{adm}},d_C,
\text{targets and divergences},\text{thresholds},
\\
&\text{score weights},p^{\mathrm{pri}},w_{\mathrm{pri}},
\lambda_{\mathrm{rep}},\mathcal C_{\mathrm{rep}},
\text{confidence and map-validity procedures}).
\end{aligned}
\]

Here \(P_{\mathrm{obj}}\) is the design sample used to select a candidate, \(P_{\mathrm{conf}}\) is an untouched confirmation sample or future block, and \(P_\star(Y\mid C)\) is the external target conditional law that the predictor attempts to approximate. This contract is fixed independently of the candidates being compared; a candidate cannot shrink the context domain, relax its thresholds, choose its own weights, redefine the target, or validate its own comparison maps. Require \(\lambda_{\mathrm{rep}}\ge0\) and \(\mathcal C_{\mathrm{rep}}\ge0\). At the fixed resolution, let:

\[
\Theta_\Gamma=(\mathsf Q_\theta,B,\pi,
\mathcal C_A,\mathcal C_R,\mathcal C_E,\Xi_R,\Xi_A)
\]

denote the complete event-prediction design evaluated under \(\Lambda_{\mathrm{eval}}\). Let \(\mathcal O_{\Theta_\Gamma}(C;S_{t^-})\) denote its final typed output bundle from the state available immediately before prediction time. Let \(\mathfrak K_\pi\) be the buckets induced by \(\pi\), and let \(\mathfrak K_\pi^+=\{K\in\mathfrak K_\pi:\mathfrak C_K\neq\varnothing\}\) be the active buckets with admissible contexts. For an active bucket \(K\), define its external future-diameter \(D_K^\star(\pi)\) as in Section 7 under the fixed target law, divergence, and context domain. Runtime-packet contracts are evaluated by their separate packet loss and are added to \(\Theta_\Gamma\) only in an implementation that jointly optimizes packet selection.

Compression must be operational, not merely decorative. Define retained information by

\[
h_\pi(C)=\bigl(\pi^{(k)}(C),s_\pi(C)\bigr),
\]

where \(s_\pi\) is declared side information. There must exist measurable maps \(\widetilde{\mathsf Q}_\theta,\widetilde B,\widetilde\alpha,\widetilde\kappa\) such that \(\mathsf Q_\theta=\widetilde{\mathsf Q}_\theta\circ h_\pi\), \(B=\widetilde B\circ h_\pi\), \(\alpha=\widetilde\alpha\circ h_\pi\), and \(\kappa=\widetilde\kappa\circ h_\pi\). The storage and acquisition cost of \(s_\pi\) is charged to \(\mathcal C_{\mathrm{rep}}\). Without this factorization, \(\pi\) may remain an interpretive annotation, but the system must not claim operational compression through \(\pi\).

Let \(p^{\mathrm{pri}}(C;S_{t^-})\in[0,1]\) be priority assigned from information available at prediction time and let \(w_{\mathrm{pri}}(p)>0\) be a declared importance function with finite, positive mean. The priority model, its preprocessing, and the weight function are fitted only on data available before the evaluated block and are frozen independently of the candidates. The unweighted objective is recovered by setting \(w_{\mathrm{pri}}\equiv1\). For \(D\in\{P_{\mathrm{obj}},P_{\mathrm{conf}}\}\), define:

\[
\mathcal R_{\mathrm{pri}}^{D}(\Theta_\Gamma)=
\frac{
\mathbb E_{(C,Z)\sim D}
\left[w_{\mathrm{pri}}(p^{\mathrm{pri}}(C;S_{t^-}))
\mathcal A_{\mathrm{post}}(\mathcal O_{\Theta_\Gamma}(C;S_{t^-}),Z)\right]}
{\mathbb E_{C\sim D}
\left[w_{\mathrm{pri}}(p^{\mathrm{pri}}(C;S_{t^-}))\right]}.
\]

Let \(S_{\mathrm{prop}}\) be a predeclared strictly proper scoring rule on the predictive-law component, and define the unweighted proper risk

\[
\mathcal R_{\mathrm{prop}}^{D}(\Theta_\Gamma)
=\mathbb E_{(C,Z)\sim D}
\left[S_{\mathrm{prop}}(\mathsf Q_{\Theta_\Gamma}(\cdot\mid C;S_{t^-}),Z)\right].
\]

All displayed expectations must be finite. The proper risk prevents improvements in a bounded composite score from being purchased by a worse probabilistic forecast.

Define the feasible design family:

\[
\mathfrak F_{AP}^{\Gamma}=
\lbrace\Theta_\Gamma:
\begin{array}{l}
D_K^\star(\pi)\le\epsilon_{AP}
\text{ for every }K\in\mathfrak K_\pi^+,\\
\text{the operational factorization through }h_\pi\text{ holds},\\
\mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)
\le \mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_{\Gamma,0})
+\epsilon_{\mathrm{prop}}
\end{array}
\rbrace.
\]

Here \(\Theta_{\Gamma,0}\) is a frozen reference predictor and \(\epsilon_{\mathrm{prop}}\ge0\) is declared in advance. In finite samples, each inequality is enforced with the predeclared one-sided confidence procedure rather than by a point estimate alone.

The governing value is:

\[
\boxed{
\mathcal J_\Gamma^*=
\inf_{\Theta_\Gamma\in\mathfrak F_{AP}^{\Gamma}}
\left[\mathcal R_{\mathrm{pri}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)
+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}(\Theta_\Gamma)\right]
}.
\]

If the feasible set is non-empty and the infimum is attained, an optimizer satisfies:

\[
\Theta_\Gamma^*\in\arg\min_{\Theta_\Gamma\in\mathfrak F_{AP}^{\Gamma}}
\left[\mathcal R_{\mathrm{pri}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)
+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}(\Theta_\Gamma)\right].
\]

Otherwise, for a declared \(\varepsilon_{\mathrm{opt}}>0\), report a feasible \(\Theta_{\Gamma,\varepsilon}\) whose objective is at most \(\mathcal J_\Gamma^*+\varepsilon_{\mathrm{opt}}\), if such a candidate has been constructed.

Selection and tuning use only \(P_{\mathrm{obj}}\). After the candidate, preprocessing, thresholds, priority rule, and analysis are frozen, final claims are evaluated once on \(P_{\mathrm{conf}}\). Both samples use rolling-origin or forward-chaining construction, grouped by independent trajectory or entity where applicable, with an embargo long enough to cover context overlap, forecast horizon, and label delay. Weighted results are accompanied by unweighted and priority-stratified results. The feasible-set constraint discourages compression that hides target-distinct futures; it does not guarantee non-emptiness, attainment, identifiability, or computational tractability. Cross-resolution comparisons use the same raw histories and fixed target law; a candidate resolution may not redefine the outcome it is judged against.

An event history may be represented by a time-unrolled directed graph:

\[
G_t=(V_t,R_t),
\]

where \(V_t\subset\mathcal E\) and edges in \(R_t\) are typed as temporal, predictive-dependency, or causal. The graph is acyclic only after time-unrolling; feedback in the physical system is represented through edges across successive times. Predictive-dependency edges must not be interpreted as causal edges without a structural causal model.

For causal language, EventFrame requires an explicit structural causal model \(\mathfrak M=(U,V,F,P_U)\). An intervention such as \(do(V_j=v')\) replaces the structural equation for \(V_j\); only then is

\[
\Delta_Y^{\mathrm{causal}}(v';P_{\mathrm{ref}})=
D_Y^{\mathrm{law}}\!\left(P_{\mathfrak M}(Y\mid do(V_j=v')),P_{\mathrm{ref}}(Y)\right)
\]

a causal effect magnitude relative to a declared reference law \(P_{\mathrm{ref}}\), such as the natural-course law \(P_{\mathfrak M}(Y)\) or another intervention law [5]. It is not a signed effect, and its interpretation depends on the chosen distance and reference. Without \(\mathfrak M\), changing an input frame or graph is a model perturbation and measures predictor sensitivity, not causation.

The event sparsity hypothesis is therefore stated relative to a finite, non-empty declared candidate set \(\mathcal D_t\), not by comparing cardinalities with a continuous substrate. If \(\mathcal I_{\mathrm{eff}}(Y,\eta_Y)\subseteq\mathcal D_t\) contains candidate distinctions whose identified or randomized intervention effect magnitude exceeds \(\eta_Y\), then the empirical sparsity ratio is:

\[
s_{\mathrm{eff}}=
\frac{|\mathcal I_{\mathrm{eff}}(Y,\eta_Y)|}{|\mathcal D_t|}.
\]

EventFrame hypothesizes \(s_{\mathrm{eff}}\ll1\) in domains where compression is useful. This is a falsifiable modeling hypothesis, not a physical theorem.

Confluence and divergence concern target-relative predictive behavior. A merge \(\mu_\delta(S_1,\ldots,S_m)\) is accepted only when its held-out predictive degradation and bucket future-diameter remain below declared thresholds. A perturbation operator \(\mathcal B_\epsilon\) may generate candidate downstream graphs, but a distribution over those candidates must be specified before writing probabilities conditioned on its output.

Every non-empty event bucket \(K\) retains at least one concrete frame \(\bar e_K\in K\) for traceability. Future-divergence detection audits contexts, because the same frame may occur after different histories. With \(\mathrm{anc}(C)\) denoting the terminal frame of context \(C\), let \(\mathfrak C_K=\{C\in\mathfrak C_{\mathrm{adm}}:\mathrm{anc}(C)\in K\}\). For an active bucket, maintain a non-empty \(\mathcal R_C(K)\subseteq\mathfrak C_K\) satisfying a declared context-coverage rule, for example:

\[
\sup_{C\in\mathfrak C_K}\min_{R\in\mathcal R_C(K)}d_C(C,R)\le\delta_K.
\]

The audit set may combine contexts for a medoid, boundary examples, high-uncertainty examples, and a reservoir sample. Tests over \(\mathcal R_C(K)\) are statistical estimates, not proofs about unobserved contexts. A certified future-diameter bound additionally requires exhaustive coverage or the verified continuity condition in Section 7. Confidence, coverage, and false-negative risk must be reported.

Confidence and provenance metadata \(c_t\) determine whether fields may be used for training, lookup, sensitivity testing, or causal analysis. Observed fields, inferred fields, and synthetic perturbations remain distinct throughout the lifecycle.

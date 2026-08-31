# 7. Sensitivity Testing and Invariants

Property fuzzing tests model sensitivity: perturb a selected event field, rerun prediction, and measure the change in a declared output. It does not by itself establish how the real world would respond to an intervention.

Let \(\phi_i\) be an event property. A validity-constrained fuzzing operator is:

\[
\mathcal F_{i,\epsilon}:\mathcal E\rightharpoonup\mathcal E,
\]

where the partial arrow records that some perturbations are invalid. At context position or subset \(r\):

\[
\mathcal F_{i,\epsilon}^{(r)}:\mathcal E^k\rightharpoonup\mathcal E^k.
\]

Let \(\mathcal O_\theta(C)=(\mathsf Q_\theta(\cdot\mid C),\hat e_\theta^H(C))\) be the typed predictor output, including its coherent no-event-capable point summary. For a declared output functional \(g\) on that bundle and distance \(d_g\), model sensitivity is:

\[
\Delta_g^{\mathrm{model}}=
d_g\!\left(
g(\mathcal O_\theta(C_t)),
g(\mathcal O_\theta(\mathcal F_{i,\epsilon}^{(r)}(C_t)))
\right).
\]

The validation law \(\mathcal V_i\) must be supported only on triples \((C_t,\epsilon,r)\) for which the partial perturbation is defined. The field is empirically stable over that declared valid family when:

\[
\Pr_{(C_t,\epsilon,r)\sim\mathcal V_i}
\left(\Delta_g^{\mathrm{model}}\le\eta_g\right)
\ge1-\alpha_g,
\]

with a one-sided lower confidence bound for this probability at least \(1-\alpha_g\). A point estimate or a two-sided interval that crosses the threshold does not establish stability. The reporting score

\[
S_g=\min\!\left(1,\frac{\Delta_g^{\mathrm{model}}}{\eta_g}\right)
\]

requires \(\eta_g>0\). Thresholds are selected from measurement resolution, operational decision tolerance, and held-out calibration; fixed fractions such as \(0.05H\) are examples only and must not be presented as universal constants.

For 5W1H review, let \(\psi_j^{\mathrm{role}}(e)\) denote the component assigned to role \(j\in\{W,A,T,L,M,H\}\). The average sensitivity of field \(\phi_i\) to target property \(g\) is:

\[
I_{i\rightarrow g}^{\mathrm{model}}=
\mathbb E_{(C_t,\epsilon,r)\sim\mathcal V_i}
\left[\Delta_g^{\mathrm{model}}\right].
\]

This quantity may nominate a field for retain, migrate, duplicate, split, or uncertain status. It says that the current predictor uses the field; it does not prove that the field is a cause, that the assigned semantic explanation is true, or that changing the field in the world would change the target.

An operational protocol is:

1. Select contexts, target property, field, perturbation family, and validity constraints.
2. Separate observed contexts from synthetic perturbations.
3. Run original and perturbed predictions.
4. Estimate sensitivity, uncertainty, and boundary regions on held-out contexts.
5. Check whether the result survives alternative plausible perturbation families.
6. Use the result as a review signal, not an automatic ontology rewrite.

Synthetic frames are never inserted into episodic memory as observations. They may be stored in a separate audit log with their generating operator and validity assumptions.

## Background fuzz incubation

Fuzzing is not part of the immediate prediction computation. A conforming implementation may nominate work after a successful response when the packing-boundary certainty \(c_t^{\mathrm{pack}}\) is no greater than a frozen trigger \(\tau_{\mathrm{fuzz}}\), the already retrieved audit frontier contains at least two and at most \(B_{\mathrm{fuzz}}\) evidence-bearing events, and the declared perturbation family is non-empty. Write the resulting indicator as \(J_t^{\mathrm{fuzz}}\). This is a scheduling rule, not evidence that the nominated case contains an invariant.

Nomination must be bounded and nonblocking. It reuses the as-of query vector, snapshot, and capped candidate set already produced by recall, stores no synthetic frame as an observation, and may be discarded when a bounded queue is full. Equivalent candidate sets are deduplicated under a frozen cooldown. A worker executes the job later under a timeout and only when serving work is idle; a changed snapshot makes the job stale and causes rejection rather than silent reinterpretation. The worker emits an audit proposal only. Publication still requires the held-out validity, Anti-Pigeon, version, and evidence procedures defined elsewhere in this paper.

Because \(J_t^{\mathrm{fuzz}}\) selects low-certainty successful recalls, conclusions from this queue describe the trigger-selected stream. They do not estimate corpus-wide invariant prevalence unless an independent randomized or exhaustive audit supplies known inclusion support and an appropriate simultaneous uncertainty procedure. Queue depth, delay, drops, deduplication, stale rejection, failures, and externally reviewed proposal yield must be reported beside any benefit claim.

## Predictive chain translation

A single-field sensitivity test does not establish domain translation. Translation requires the perturbation to remain aligned along a complete time-ordered chain. Let domains \(A\) and \(B\) each supply a baseline trajectory and a revealed trajectory of equal finite length \(m_{\mathrm{ch}}\):

\[
E_A^{(b)}=(e_{A,0}^{(b)},\ldots,e_{A,m_{\mathrm{ch}}-1}^{(b)}),
\qquad
E_B^{(b)}=(e_{B,0}^{(b)},\ldots,e_{B,m_{\mathrm{ch}}-1}^{(b)}),
\qquad b\in\{0,1\}.
\]

The superscript \(b=0\) denotes the baseline chain and \(b=1\) the chain after the revealing upstream distinction. At every stage \(j\), let \(\phi_{A,j}\) and \(\phi_{B,j}\) be the declared 5W1H coordinate projections and freeze a partial correspondence \(T_j\) satisfying, on the supplied pair,

\[
T_j\!\left(\phi_{A,j}(e_{A,j}^{(b)})\right)
=\phi_{B,j}(e_{B,j}^{(b)}),
\qquad b\in\{0,1\}.
\]

Raw equality is not required: \(T_j\) may encode a unit conversion, vocabulary map, or other externally justified correspondence. Its generating procedure and validity evidence are part of the audit contract.

Let \(J_j^{\mathrm{loc}}=1\) only when the observed before and after values match the frozen correspondence and every non-target 5W1H coordinate remains unchanged in both domains. Let \(J_j^{\mathrm{map}}=1\) only when the mapped coordinate changes in both domains. The strict propagation and terminal-erasure indicators are

\[
\begin{aligned}
J_{\mathrm{prop}}&=\prod_{j=0}^{m_{\mathrm{ch}}-1}J_j^{\mathrm{map}},
&J_{\mathrm{erase}}&=\mathbf 1\{J_{m_{\mathrm{ch}}-1}^{\mathrm{map}}=0\},\\
J_{\mathrm{pred}}&=\mathbf 1\!\left\{
\prod_jJ_j^{\mathrm{loc}}=1
\ \land\ (J_{\mathrm{prop}}=1\ \lor\ J_{\mathrm{erase}}=1)
\right\}.
\end{aligned}
\]

Stage zero must have \(J_0^{\mathrm{map}}=1\). Later stages may change in both domains or remain unchanged in both. A change in an undeclared coordinate sets \(J_j^{\mathrm{loc}}=0\), even if the terminal values happen to agree. Thus endpoint agreement cannot hide a broken intermediate square.

For the current executable diagnostic, evaluate the predictive law only when \(J_{\mathrm{pred}}=1\). Then let \(p_A^{(b)},p_B^{(b)}\in\Delta^{m_{\mathrm{ch}}-1}\) be normalized nomination laws over the aligned stages under the declared query and define signed predictor effects and domain-wise movement by

\[
\delta_{A,j}=p_{A,j}^{(1)}-p_{A,j}^{(0)},
\qquad
\delta_{B,j}=p_{B,j}^{(1)}-p_{B,j}^{(0)},
\]

\[
M_A=\frac12\sum_{j=0}^{m_{\mathrm{ch}}-1}|\delta_{A,j}|,
\qquad
M_B=\frac12\sum_{j=0}^{m_{\mathrm{ch}}-1}|\delta_{B,j}|,
\qquad
D_{\mathrm{tr}}=\frac12\sum_{j=0}^{m_{\mathrm{ch}}-1}|\delta_{A,j}-\delta_{B,j}|.
\]

With frozen tolerances \(\eta_{\mathrm{inv}},\eta_{\mathrm{tr}}>0\), the runtime classification is

\[
\mathcal C_{\mathrm{chain}}=
\begin{cases}
\mathrm{invariant},&
\prod_jJ_j^{\mathrm{loc}}=1, J_{\mathrm{erase}}=1,
\ \max(M_A,M_B)\le\eta_{\mathrm{inv}},\\
\mathrm{translation},&
\prod_jJ_j^{\mathrm{loc}}=1, J_{\mathrm{prop}}=1,
\ D_{\mathrm{tr}}\le\eta_{\mathrm{tr}},
\ |\delta_{A,m_{\mathrm{ch}}-1}-\delta_{B,m_{\mathrm{ch}}-1}|\le\eta_{\mathrm{tr}},\\
\mathrm{divergence},&\text{otherwise.}
\end{cases}
\]

When \(J_{\mathrm{pred}}=0\), structural checks already force the third branch, so \(M_A\), \(M_B\), \(D_{\mathrm{tr}}\), and terminal effect agreement are not evaluated. A wire-format zero in those fields is a placeholder accompanied by a false `prediction-evaluated` flag, not a measured zero.

Exact score reuse does not change this classifier. Let \(\kappa\) be the ordered cache identity with components \(q\), \(\upsilon_{\mathrm{emb}}\), \(\upsilon_{\mathrm{5W1H}}\), \(S_{t^-}\), \(u\), and \(e\): respectively the canonical query, embedding-model version, semantic-representation version, complete captured snapshot, tenant, and event identity, which is immutable within that snapshot. A hit is admissible only under exact equality of \(\kappa\), in which case the cached raw nomination score satisfies \(s_{\mathrm{cache}}(\kappa)=s_{\mathrm{fresh}}(\kappa)\). Any model, representation, snapshot, tenant, identity, or generated-frame digest mismatch recomputes the score. Thus eviction or a cache miss changes cost but not the normalized law.

For bounded chain length, the local execution cost is \(T_{\mathrm{chain}}=T_{\mathrm{struct}}+J_{\mathrm{pred}}T_{\mathrm{law}}\). Structural validation and a warm exact-score hit are each \(O(m_{\mathrm{ch}})\); a cold dense-vector audit is \(O(m_{\mathrm{ch}}d)\) for embedding dimension \(d\). Store access, remote embedding, cache maintenance, and concurrency are measured separately.

The first branch means that the declared upstream distinction is erased at the terminal stage and is a candidate for higher-order abstraction. The second means that the mapped distinction propagates with bounded predictive-effect defect while other coordinates stay fixed. The third preserves the chains separately for Anti-Pigeon review. These labels are proposal-only. A declared map cannot certify itself, authorize a posterior merge, or publish a sheaf snap.

This finite observed-path test checks commuting squares only on the supplied trajectories. It does not prove equality of unknown transition kernels. If explicit transition maps \(K_{A,j}\) and \(K_{B,j}\) are available, the stronger requirement is

\[
T_{j+1}\circ K_{A,j}\approx K_{B,j}\circ T_j
\]

under a declared edge-space metric and simultaneous uncertainty procedure. Without an identified SCM and intervention evidence, the result is called predictive chain translation. Only identified intervention operators, stated transport assumptions, and valid causal evidence permit the stronger phrase causal chain translation.

Graph perturbation follows the same rule. Let \(G_t=(V_t,R_t)\) be a time-unrolled predictive graph and let:

\[
G_t'=\mathcal I_{v,\epsilon}^{\mathrm{model}}(G_t).
\]

The resulting predictor sensitivity is:

\[
\Delta_Y^{\mathrm{model}}=
D_Y^{\mathrm{law}}\!\left(\mathsf Q_\theta^Y(\cdot\mid G_t'),\mathsf Q_\theta^Y(\cdot\mid G_t)\right),
\]

where \(\mathsf Q_\theta^Y\) is the declared predictive marginal for target \(Y\). This may update predictive-dependency confidence, residual keys, or abstraction review priorities. It must not update causal-edge confidence merely because the predictor changed.

When an explicit structural causal model \(\mathfrak M=(U,V,F,P_U)\) exists and an intervention target is well-defined, a separate causal analysis may compute:

\[
\Delta_Y^{\mathrm{causal}}=
D_Y^{\mathrm{law}}\!\left(
P_{\mathfrak M}(Y\mid do(V_j=v')),
P_{\mathrm{ref}}(Y)
\right).
\]

The reference law \(P_{\mathrm{ref}}\) must be declared, and this distance is an effect magnitude rather than a signed effect. Identification assumptions, manipulated variables, confounder controls, and transport assumptions must be stated. Randomized or otherwise identified intervention evidence may update causal-edge confidence; input fuzzing alone may not [5].

The slow path begins only after a realized post-observation loss is available:

1. Observe \(\mathcal A_{\mathrm{post}}>\eta_{\mathrm{post}}\) or repeated packet failure.
2. Select candidate fields, nodes, or edges from residual and uncertainty evidence.
3. Run validity-constrained model perturbations.
4. If an SCM and identification strategy exist, run the corresponding causal analysis separately.
5. Update cache keys, predictive edges, or abstraction markers only after repeated held-out improvement.

For a candidate ontology change from state \(s\) to \(s'\), use an independent paired forward-validation set \(\mathcal V_{\mathrm{rev}}=\{(C_t,Z_{t+1})\}_{t=1}^{n}\). Replay each case from \(S_{t^-}\), include it only when \(a(Z_{t+1})\) is inside the validation availability window, and group inference by independent trajectory or entity. Define per-case composite improvement:

\[
\Delta_t^{s\rightarrow s'}=
\mathcal A_{\mathrm{post}}(\mathcal O^s(C_t),Z_{t+1})
-\mathcal A_{\mathrm{post}}(\mathcal O^{s'}(C_t),Z_{t+1}).
\]

and the paired proper-score degradation:

\[
G_{t,\mathrm{prop}}^{s\rightarrow s'}=
S_{\mathrm{prop}}(\mathsf Q^{s'}(\cdot\mid C_t;S_{t^-}),Z_{t+1})
-S_{\mathrm{prop}}(\mathsf Q^{s}(\cdot\mid C_t;S_{t^-}),Z_{t+1}).
\]

Promotion requires all of the following preregistered conditions:

\[
n\ge n_{\min}^{\mathrm{rev}},
\qquad
\mathrm{LCB}_{\mathrm{paired}}\!\left[\frac{1}{n}\sum_{t=1}^{n}\Delta_t^{s\rightarrow s'}\right]
\ge\delta_{\mathrm{rev}}>0,
\]

\[
\mathrm{UCB}\!\left[
\frac{1}{n}\sum_{t=1}^{n}
\mathbf 1\{\Delta_t^{s\rightarrow s'}<-\delta_{\mathrm{harm}}\}
\right]
\le\beta_{\mathrm{harm}}.
\]

It additionally requires proper-score non-inferiority:

\[
\mathrm{UCB}_{\mathrm{paired}}\!\left[
\frac{1}{n}\sum_{t=1}^{n}G_{t,\mathrm{prop}}^{s\rightarrow s'}
\right]
\le\epsilon_{\mathrm{prop}}^{\mathrm{rev}},
\qquad \epsilon_{\mathrm{prop}}^{\mathrm{rev}}\ge0.
\]

Here \(\delta_{\mathrm{harm}}\ge0\) and \(\beta_{\mathrm{harm}}\in[0,1]\) are fixed before evaluation.

Thus average composite improvement cannot hide either an uncontrolled rate of material regressions or degraded probabilistic calibration. The confidence construction must account for every adaptively compared candidate state. If promotion is monitored repeatedly, use a confidence sequence, alpha spending, or preregistered review times. All learned preprocessing, perturbation selection, and priority rules are fitted before the validation cutoff. The evaluation contexts must not be the same or temporally overlapping examples used to propose the change. Before validation, the field remains provisional. Previous assignments and provenance are retained so the change can be audited or reversed.

An EventFrame invariant is therefore conditional: stable under this valid perturbation family, for this predictor and target, in this data regime, within this threshold and confidence level. Failure modes include invalid perturbations, off-manifold inputs, hidden confounding, adaptive reuse of the validation set, and thresholds below measurement noise.

The next section uses these conditional diagnostics to decide when event distinctions may be compressed, must remain separate, or require a bounded compatibility-graph revision.

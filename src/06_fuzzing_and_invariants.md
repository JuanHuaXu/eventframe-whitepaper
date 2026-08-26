# 6. Fuzzing and Invariants

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

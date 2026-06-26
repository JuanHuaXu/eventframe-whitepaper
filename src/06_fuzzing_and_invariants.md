# 6. Fuzzing and Invariants

Property fuzzing tests whether predictions depend on specific event fields. The method perturbs a selected property, reruns prediction, and measures whether a target property of the output changes beyond a declared threshold. If a prediction remains stable under a controlled family of perturbations, the stable property becomes a candidate invariant.

Let \(\phi_i\) be an event property, such as actor, action type, time, location, or a component of auxiliary state. A single-event fuzzing operator is:

\[
\mathcal{F}_{i,\epsilon}(e) = e',
\]

where \(e'\) differs from \(e\) primarily in property \(\phi_i\) by perturbation magnitude \(\epsilon\). For prediction, the corresponding context-level operator is:

\[
\mathcal{F}_{i,\epsilon}^{(r)}: \mathcal{E}^k \rightarrow \mathcal{E}^k,
\]

where \(r\) identifies the event position or subset of \(C_t\) being perturbed.

The conceptual role of fuzzing is to separate apparent relevance from predictive relevance. A field may look semantically important but not affect the prediction target for a specific task. Another field may look incidental but sharply change the predicted event time. Fuzzing gives a controlled way to test these dependencies.

Fuzzing also supports 5W1H ontology self-organization. The initial assignment of information to who, what, when, where, why, and how may be wrong, incomplete, or too coarse. Let \(\rho_j(e)\) denote the component of an event assigned to role \(j \in \{W,A,T,L,M,H\}\), corresponding to actor, action, time, location, motive, and mechanism. For a field \(\phi_i\), define its target influence on output property \(g\) as:

\[
I_{i \rightarrow g} =
\mathbb{E}_{C_t,\epsilon,r}
\left[
d_g(g(F_\theta(C_t)), g(F_\theta(\mathcal{F}_{i,\epsilon}^{(r)}(C_t))))
\right].
\]

If a field assigned to one role consistently influences a target associated with another role, the ontology should not pretend the original assignment is final. The slow path may mark the field for migration, duplication, or splitting. For example, a value recorded as "where" may function as part of "how" if perturbing it changes the mechanism of the event rather than only spatial localization. A value recorded as "why" may need to split into confidence-tagged motive hypotheses if different interventions produce incompatible futures.

Let \(g\) be a property of the prediction output, and let \(d_g\) be a distance over that property. The change induced by fuzzing is:

\[
\Delta_g =
d_g(g(F_\theta(C_t)), g(F_\theta(\mathcal{F}_{i,\epsilon}^{(r)}(C_t)))).
\]

A property is treated as stable under the fuzzing family if:

\[
\Delta_g \le \eta_g,
\]

where \(\eta_g\) is a declared threshold. For reporting, use a clamped score:

\[
S_g = \min\left(1, \frac{\Delta_g}{\eta_g}\right).
\]

The value \(S_g = 0\) means no observed change, while \(S_g = 1\) means the perturbation reaches or exceeds the threshold. For temporal prediction, the threshold can be tied to the horizon \(H\). A strict test may use \(\eta_\tau = 0.05H\), while an exploratory test may use \(\eta_\tau = 0.10H\).

An operational fuzzing protocol is:

1. Select a context \(C_t\), prediction target \(g\), field \(\phi_i\), and context position or subset \(r\).
2. Define the perturbation family and valid magnitudes \(\epsilon\).
3. Run the original prediction.
4. Run predictions on perturbed contexts.
5. Compute \(\Delta_g\) and \(S_g\).
6. Record stable, unstable, and boundary regions.

The same protocol can detect confluence and divergence. If perturbing two event streams does not change the target beyond threshold, the streams may be candidates for confluence into a merged event. If a small perturbation produces multiple target-distinct downstream predictions, the event sits near a divergence boundary. This is the operational version of butterfly-effect-style sensitivity: small changes matter only when they amplify beyond the declared target threshold.

Counterfactual event frames are the perturbed frames produced by this protocol. They should be marked as synthetic and should not be inserted into episodic memory as observed events. They may, however, be used by the slow path to test invariants, improve key design, or identify abstraction boundaries.

Ontology updates should therefore be intervention-driven. A conservative update rule is:

\[
\operatorname{revise}(\phi_i) =
\begin{cases}
\operatorname{retain}(\phi_i) & \text{if all relevant } I_{i \rightarrow g} \text{ remain below threshold},\\
\operatorname{migrate}(\phi_i, j \rightarrow j') & \text{if influence is stable for role } j',\\
\operatorname{split}(\phi_i) & \text{if one field carries multiple target-distinct influences},\\
\operatorname{mark\ uncertain}(\phi_i) & \text{if perturbation evidence is unstable.}
\end{cases}
\]

This is not an automatic ontology rewrite. It is a slow-path review signal. The implementation should preserve provenance, confidence, and the previous assignment so that field migration can be audited or reversed.

An invariant is not a universal truth unless the fuzzing family and domain justify that claim. In EventFrame, invariants are usually conditional: stable under these perturbations, in this data regime, for this prediction target, within this threshold. That conservative framing matters because an invariant useful for temporal prediction may fail for actor prediction or causal explanation.

Failure modes include invalid perturbations, unrealistic counterfactuals, threshold gaming, and hidden confounding. If perturbing one field implicitly changes another, the test may not isolate the intended property. If the perturbation creates impossible events, stability may be meaningless. If thresholds are too loose, everything looks invariant and all streams appear to merge; if too strict, no abstraction or confluence is possible. The next section uses invariance evidence to decide when detailed events can be safely compressed.

# Notation

This notation is provisional and should be refined during drafting.

## Event Frames

Let an event frame be:

\[
e_t = (w_t, a_t, \tau_t, \ell_t, m_t, h_t, x_t, c_t)
\]

where:

- \(w_t\): who / participating agents or entities
- \(a_t\): what / action or occurrence type
- \(\tau_t\): when / temporal index or interval
- \(\ell_t\): where / location or spatial context
- \(m_t\): why / motive, objective, causal explanation, or inferred driver
- \(h_t\): how / mechanism, method, or process
- \(x_t\): auxiliary state vector or structured state
- \(c_t\): confidence, provenance, or uncertainty metadata

Each field should be treated as typed. A more explicit product-space notation is:

\[
\mathcal{E} =
\mathcal{W} \times \mathcal{A} \times \mathcal{T} \times
\mathcal{L} \times \mathcal{M} \times \mathcal{H} \times
\mathcal{X} \times \mathcal{C}
\]

where the component spaces correspond to who, what, when, where, why, how,
auxiliary state, and confidence/provenance metadata. The exact internal
representation of each component is implementation-dependent, but each
component must have a declared comparison rule before it is used in a loss,
cache key, or invariant test.

## Event Space

Let \(\mathcal{E}\) denote the space of possible event frames.

A trajectory is:

\[
E_{1:T} = (e_1, e_2, \ldots, e_T)
\]

## Transition Function

A transition model is:

\[
F_\theta: \mathcal{E}^k \rightarrow \mathcal{E}
\]

where \(k\) is the context length and \(\theta\) are model parameters or rules.

## Residual Formulation

Let \(B\) be a baseline predictor. A residual formulation should be written with
an explicit composition operator rather than ordinary vector addition:

\[
\hat{e}_{t+1} = B(e_{t-k:t}) \oplus R(e_{t-k:t})
\]

where \(\oplus\) composes a baseline event prediction with a residual event correction.

For the paper draft, use a Causal Fermion Systems-inspired composition rule
rather than ordinary vector addition. Let:

\[
q: \mathcal{E} \rightarrow \mathcal{Q}
\]

encode an event frame as an operator-like structured representation, where
\(\mathcal{Q}\) is an event representation space chosen for the model. Let
\(b = B(e_{t-k:t})\) be the baseline event prediction and let \(r\) be a
residual correction in the same representation space. Define:

\[
b \oplus_{\mathcal{A}} r =
q^{-1}_{\mathrm{approx}}\left(\Pi_{\mathcal{Q}}\left(q(b) + \operatorname{clamp}(r)\right)\right)
\]

where:

- \(\Pi_{\mathcal{Q}}\) projects the corrected representation back into the admissible event representation space.
- \(q^{-1}_{\mathrm{approx}}\) is an approximate decoder from representations to event frames.
- \(\operatorname{clamp}(r)\) bounds the residual magnitude so that cache reuse cannot dominate the baseline prediction.
- The subscript \(\mathcal{A}\) indicates that admissibility is regularized by a causal-action-inspired constraint.

Interpretation: residual composition is a constrained structured correction. It
borrows the idea that meaningful configurations should be evaluated through
operator relationships and an action-like admissibility criterion, but it does
not assume that EventFrame is a physical Causal Fermion System.

## Prediction Loss

The primary prediction loss is temporal. For point-valued event times:

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{\left|\tau(F_\theta(e_{t-k:t}))-\tau(e_{t+1})\right|}{H}\right)
\]

where \(H > 0\) is the prediction horizon used to normalize and clamp the loss.
The value is \(0\) for exact temporal prediction and saturates at \(1\) for
errors greater than or equal to the horizon.

For interval-valued event times, replace absolute difference with an interval
distance \(d_{\mathcal{T}}\), such as midpoint distance or endpoint Hausdorff
distance:

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{d_{\mathcal{T}}(\tau(F_\theta(e_{t-k:t})),\tau(e_{t+1}))}{H}\right)
\]

Other field-level losses may be added as auxiliary diagnostics, but the current
formulation treats time-to-event error as the canonical loss unless a section
explicitly defines a broader objective.

## Fuzzing Operator

Let \(\phi_i\) be an event property. A fuzzing operator perturbs it:

\[
\mathcal{F}_{i,\epsilon}(e) = e'
\]

where \(e'\) differs from \(e\) primarily in property \(\phi_i\) by perturbation magnitude \(\epsilon\).

## Invariance Test

A property \(g\) is invariant under fuzzing family \(\mathcal{F}\) if:

\[
\Delta_g =
d_g(g(F_\theta(e)), g(F_\theta(\mathcal{F}_{i,\epsilon}(e)))) \le \eta_g
\]

for defined ranges of \(i\) and \(\epsilon\), where \(d_g\) is a property-level
distance and \(\eta_g\) is a declared threshold. Use a clamped score for
reporting:

\[
S_g = \min\left(1, \frac{\Delta_g}{\eta_g}\right)
\]

with \(S_g = 0\) indicating no observed change and \(S_g = 1\) indicating that
the perturbation reaches or exceeds the invariance threshold. The default
threshold for temporal properties should be derived from the prediction horizon,
for example \(\eta_\tau = 0.05H\) for strict tests and \(\eta_\tau = 0.10H\)
for exploratory tests.

## Lumpability

A projection \(\pi: \mathcal{E} \rightarrow \mathcal{Z}\) maps detailed events to abstract states. A transition process is predictively lumpable if:

\[
P(\pi(e_{t+1}) \mid e_t) \approx P(\pi(e_{t+1}) \mid \pi(e_t))
\]

for the prediction target of interest.

This should be presented as approximate predictive lumpability and cited against
the existing literature on Markov chain lumpability, state aggregation, and
abstraction. The paper should avoid claiming a new theorem unless a proof is
added.

# Notation

This notation is provisional and should be refined during drafting.

## Microscopic Substrate and Event Frames

EventFrame distinguishes a dense underlying substrate from the compressed event
frames used for prediction. Let \(\Omega\) denote a microscopic substrate state
space and let:

\[
\omega_{\alpha} \in \Omega
\]

denote a substrate state indexed by a microscopic spacetime cell \(\alpha\). In
the physical motivation, \(\alpha\) may be considered at scales comparable to
Planck length and Planck time. This is a motivation for density, not a claim
that EventFrame supplies a theory of quantum gravity.

Let a coarse-graining map be:

\[
\Gamma: \Omega^{A_t} \rightarrow \mathcal{E}
\]

where \(A_t\) is a finite spacetime region or computational region available to
the model at event index \(t\). The event frame is then:

\[
e_t = \Gamma(\omega_{A_t})
\]

where \(\omega_{A_t}\) denotes the substrate history over the region. The
operational role of \(\Gamma\) is compression: it selects distinctions that are
useful for prediction, intervention, review, or memory.

An event frame is not fundamental in this formulation. It is a compressed
representation of an underlying substrate.

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

## Intervention-Effective Events

Let \(I_j\) denote an intervention on a substrate region or on the event-frame
representation. Let \(Y\) be a prediction target, such as the next event time.
An event distinction is intervention-effective for \(Y\) if:

\[
d_Y(P(Y \mid do(I_j)), P(Y)) > \eta_Y
\]

where \(d_Y\) is a target-level distance and \(\eta_Y\) is a declared threshold.
The event sparsity hypothesis says that the set of such distinctions is small
relative to the number of microscopic substrate distinctions:

\[
|\mathcal{I}_{eff}(Y, \eta_Y)| \ll |\Omega^{A_t}|.
\]

Conceptually, this is why EventFrame searches for compressed event frames rather
than assigning a unique event frame to every microscopic cell. Operationally,
the hypothesis is tested by intervention experiments, property fuzzing, and
ablation: distinctions that do not change the target beyond threshold should not
be promoted to durable event-frame structure.

## Event Space

Let \(\mathcal{E}\) denote the space of possible event frames.

A trajectory is:

\[
E_{1:T} = (e_1, e_2, \ldots, e_T)
\]

More generally, an event history may be a directed acyclic event graph:

\[
G_t = (V_t, R_t)
\]

where \(V_t \subset \mathcal{E}\) is a set of event frames and \(R_t\) contains
temporal, causal, or dependency edges among them. A linear trajectory is the
special case in which each event has at most one immediate predecessor and one
immediate successor.

## Event Confluence and Divergence

Event confluence is a many-to-one compression over event streams. Let
\(S_1, \ldots, S_m\) be event streams or subgraphs. A confluence operator is:

\[
\mu_{\delta}: \mathcal{G}^m \rightarrow \mathcal{E}
\]

where \(\mathcal{G}\) is the space of event subgraphs and \(\delta\) is a
resolution or tolerance parameter. The aggregate event is:

\[
e^{merge}_t = \mu_{\delta}(S_1, \ldots, S_m).
\]

Conceptually, \(\mu_{\delta}\) says that separate event streams can become one
larger event when their distinctions no longer change the target beyond the
chosen resolution. Operationally, confluence is accepted only if replacing the
streams by \(e^{merge}_t\) does not degrade prediction beyond a declared
threshold.

Event divergence is the opposite pattern: a small distinction produces multiple
downstream branches. Let \(\mathcal{B}_{\epsilon}\) be a branching operator:

\[
\mathcal{B}_{\epsilon}: \mathcal{E} \rightarrow \mathcal{P}(\mathcal{G})
\]

where \(\epsilon\) is a perturbation or intervention scale and
\(\mathcal{P}(\mathcal{G})\) is a set of possible downstream event subgraphs.
A distinction is divergence-effective when:

\[
d_Y(P(Y \mid \mathcal{B}_{\epsilon}(e)), P(Y \mid e)) > \eta_Y.
\]

Conceptually, this captures butterfly-effect-style sensitivity: a distinction
that appears small at one scale may amplify into materially different future
event streams. Operationally, such distinctions should not be merged away by
coarse-graining or lumpability unless the target-level divergence remains below
threshold.

## Event Frame Groups and Representatives

Let an abstraction, cache key, or confluence process induce event-frame groups:

\[
\mathcal{H} = \{\mathcal{H}_1, \ldots, \mathcal{H}_n\}, \quad
\mathcal{H}_j \subseteq \mathcal{E}.
\]

Each non-empty group must retain at least one representative event frame:

\[
\forall \mathcal{H}_j \neq \varnothing,\quad
\exists \bar{e}_j \in \mathcal{H}_j.
\]

The representative \(\bar{e}_j\) is not necessarily the centroid, average, or
most likely event. It is a concrete retained frame used as a measurement anchor.
For a proposed intervention \(I\), the divergence score of group
\(\mathcal{H}_j\) can be estimated by:

\[
D_j(I) =
d_Y(P(Y \mid do(I), \bar{e}_j), P(Y \mid \bar{e}_j)).
\]

If \(D_j(I) > \eta_Y\), the group should be split, refined, or marked as
divergence-sensitive. If several groups have representative frames whose
target-level behavior remains within a merge threshold \(\eta_{\mu}\), they may
be candidates for confluence:

\[
d_Y(P(Y \mid \bar{e}_i), P(Y \mid \bar{e}_j)) \le \eta_{\mu}.
\]

Operationally, representative preservation prevents abstraction from becoming
empty bookkeeping. It keeps at least one concrete event frame available for
future tests of when interventions cause divergence and when multiple event
streams have converged enough to merge.

## Transition Function

A transition model is:

\[
F_\theta: \mathcal{E}^k \rightarrow \mathcal{E}
\]

where \(k\) is the context length and \(\theta\) are model parameters or rules.

The prediction context at time \(t\) is:

\[
C_t = e_{t-k+1:t} = (e_{t-k+1}, \ldots, e_t)
\]

where \(C_t\) contains the \(k\) most recent event frames used by the
predictor. Conceptually, \(C_t\) is the local event history from which the
system asks, "what event should occur next, and when?"

## Residual Formulation

Let \(B\) be a baseline predictor. A residual formulation should be written with
an explicit composition operator rather than ordinary vector addition:

\[
\hat{e}_{t+1} = B(C_t) \oplus R(C_t)
\]

where \(\oplus\) composes a baseline event prediction with a residual event correction.

For the paper draft, use a Causal Fermion Systems-inspired composition rule
rather than ordinary vector addition. Let:

\[
q: \mathcal{E} \rightarrow \mathcal{Q}
\]

encode an event frame as an operator-like structured representation, where
\(\mathcal{Q}\) is an event representation space chosen for the model. Let
\(b = B(C_t)\) be the baseline event prediction and let \(r\) be a
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

## Residual Lookup

Let a residual cache be a finite set:

\[
\mathcal{C}_R = \{(\kappa_i, r_i, s_i)\}_{i=1}^{N}
\]

where \(\kappa_i\) is a context key, \(r_i \in \mathcal{Q}\) is a residual
correction, and \(s_i\) stores cache metadata such as age, confidence, and
observed temporal error. Let:

\[
\kappa: \mathcal{E}^{k} \rightarrow \mathcal{K}
\]

map a prediction context to a cache key, and let \(d_{\mathcal{K}}\) be a
distance over keys. The retrieved residual is:

\[
r_t^* =
\begin{cases}
r_j & \text{if } j = \arg\min_i d_{\mathcal{K}}(\kappa(C_t), \kappa_i)
\text{ and } d_{\mathcal{K}}(\kappa(C_t), \kappa_j) \le \epsilon_K,\\
0_{\mathcal{Q}} & \text{otherwise.}
\end{cases}
\]

Conceptually, residual lookup asks whether the current event context resembles a
past context whose baseline prediction failed in a reusable way. The threshold
\(\epsilon_K\) prevents weak similarities from forcing a cached correction into
the current prediction.

## Prediction Loss

The primary prediction loss is temporal. For point-valued event times:

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{\left|\tau(\hat{e}_{t+1})-\tau(e_{t+1})\right|}{H}\right)
\]

where \(H > 0\) is the prediction horizon used to normalize and clamp the loss.
The value is \(0\) for exact temporal prediction and saturates at \(1\) for
errors greater than or equal to the horizon. If the predictor is written as a
single transition model, then \(\hat{e}_{t+1} = F_\theta(C_t)\). If the
reference residual procedure is used, then
\(\hat{e}_{t+1} = B(C_t) \oplus_{\mathcal{A}} r_t^*\).

For interval-valued event times, replace absolute difference with an interval
distance \(d_{\mathcal{T}}\), such as midpoint distance or endpoint Hausdorff
distance:

\[
\mathcal{L}_{time}^{H}(\theta) =
\min\left(1,\frac{d_{\mathcal{T}}(\tau(\hat{e}_{t+1}),\tau(e_{t+1}))}{H}\right)
\]

Other field-level losses may be added as auxiliary diagnostics, but the current
formulation treats time-to-event error as the canonical loss unless a section
explicitly defines a broader objective.

## Reference Prediction Step

A single EventFrame prediction step should be described as:

1. Form the prediction context \(C_t = e_{t-k+1:t}\).
2. Compute the baseline prediction \(b_t = B(C_t)\).
3. Retrieve a cached residual \(r_t^*\) from \(\mathcal{C}_R\), or use
   \(0_{\mathcal{Q}}\) if no cache entry passes the lookup threshold.
4. Compose the prediction:

\[
\hat{e}_{t+1} = b_t \oplus_{\mathcal{A}} r_t^*
\]

5. When the observed event \(e_{t+1}\) becomes available, evaluate
   \(\mathcal{L}_{time}^{H}\).
6. On the slow path, estimate the observed residual and decide whether to update
   the residual cache, revise thresholds, or trigger invariant tests.

This procedure is not a mandatory implementation. It is the minimal operational
model the paper should use when explaining how the formal objects participate in
prediction.

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

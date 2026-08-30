# 3. Event Representation and Ontology

EventFrame uses event frames as predictive units, not as fundamental ontology. The underlying substrate is assumed to contain more detail than the predictor can retain. That substrate may be physical, simulated, biological, robotic, or software-based. EventFrame treats a frame as a task-relative compressed representation. For physical substrates, Planck scales and physical information bounds motivate a limiting thought experiment about microscopic description; they do not prove a discrete substrate, a Planck-scale sampling lattice, or the EventFrame sparsity hypothesis. Simulated and software substrates require independent task- and resource-based compression arguments.

An event is therefore a structured representation of a change, occurrence, action, observation, or state transition after coarse-graining. An event frame records that compressed event in fields that can be compared, predicted, fuzzed, cached, and abstracted.

An event frame at index \(t\) is written:

\[
e_t = (w_t, a_t, \tau_t, \ell_t, m_t, h_t, x_t, c_t)
\]

where \(w_t\) denotes participating agents or entities, \(a_t\) denotes the action or occurrence type, \(\tau_t\) denotes the time index or interval, \(\ell_t\) denotes location or spatial context, \(m_t\) denotes motive, objective, causal explanation, or inferred driver, \(h_t\) denotes mechanism or process, \(x_t\) denotes auxiliary state, and \(c_t\) denotes confidence, provenance, or uncertainty metadata. When \(\tau_t\) is an interval, the complete interval remains part of the frame; scalar timing formulas use a separately declared temporal anchor, defaulting to interval onset.

The conceptual role of this ontology is compression. It prevents prediction from treating history as a single undifferentiated sequence, but it also prevents prediction from pretending that every microscopic distinction deserves its own event identity. The fields ask different compressed questions. The "what" field identifies an occurrence type. The "when" field supports temporal prediction loss. The "who" and "where" fields localize the event. The "why" and "how" fields record explanatory hypotheses and mechanisms. The auxiliary state field allows symbolic, vector, graph, or latent variables to travel with the event. The confidence field prevents uncertain extraction from pretending to be certain observation.

Let \(\Omega\) denote a fine-grained substrate state space and let \(\omega_{A_t}\) denote the substrate history over a finite region \(A_t\). The adjective fine-grained describes retained detail and imposes no topology on \(\Omega\). A coarse-graining map at temporal resolution \(\Delta_\tau\):

\[
\Gamma_{\Delta_\tau}: \Omega^{A_t} \rightarrow \mathcal{E}_{\Delta_\tau}
\]

produces an event frame:

\[
e_t = \Gamma_{\Delta_\tau}(\omega_{A_t}).
\]

This equation states the ontology clearly: the event frame is a lossy, task-oriented compression. The compression is useful only if it preserves distinctions that matter for prediction, intervention, memory, or review.

The temporal resolution \(\Delta_\tau\) controls how precise the "when" field is. A model may choose second-level frames, microsecond-level frames, or another declared scale. Finer resolution can instantiate more candidate frames, but it does not imply that every candidate frame is predictively effective, causally effective, or worth retaining forever. Predictive and causal sparsity are measured separately over a finite declared candidate set; neither is inferred from the size of the substrate.

Mathematically, the event space is treated as a typed product:

\[
\mathcal{E} =
\mathcal{W} \times \mathcal{A} \times \mathcal{T} \times
\mathcal{L} \times \mathcal{M} \times \mathcal{H} \times
\mathcal{X} \times \mathcal{C}.
\]

This equation is operational, not decorative. It says that before a field can be used in prediction, caching, fuzzing, or abstraction, the field must have a representation and a comparison rule. For example, \(\mathcal{T}\) may contain timestamps or intervals; \(\mathcal{L}\) may contain coordinates, graph nodes, or symbolic regions; \(\mathcal{C}\) may contain confidence scores and source provenance. EventFrame does not require one universal encoding for all domains, but it requires the encoding to be declared.

An event state is the system state before, during, or after an event. In some domains, \(x_t\) may include an explicit pre-state and post-state. In others, \(x_t\) may be a latent state vector inferred from observations. A transition occurs when one event context gives rise to a later event frame. The basic trajectory is:

\[
E_{1:T} = (e_1, e_2, \ldots, e_T).
\]

Operationally, a prediction step extracts a context from this trajectory:

\[
C_t = e_{t-k+1:t}.
\]

The context \(C_t\) is the recent event history available to the predictor. It gives the predictor local structure for forecasting the next event and its time. If the context is too short, important predictive or temporal dependencies may be missing. Causal dependence is a stronger claim and requires an explicit causal model or identified intervention evidence. The context length \(k\) is a modeling choice that should be evaluated experimentally.

The ontology also supports typed links. Temporal links order events, spatial links relate locations, and predictive-dependency links record forecast-relevant association. Causal links are reserved for relations supported by a declared structural causal model or an identified intervention. These link types must remain distinct in storage and evaluation.

Event histories are therefore not limited to linear chains. Multiple event streams can become representable as a single aggregate event over time. This is event confluence: separate streams merge into a larger stream or macro-event when their separate identities no longer affect the target beyond a declared threshold. The reverse can also occur. A small distinction can branch into multiple downstream event streams when a perturbation is amplified by the dynamics. This is event divergence, or butterfly-effect-style sensitivity. EventFrame must model both patterns because compression that is safe in a confluence region may be unsafe near a divergence point.

For traceability, EventFrame keeps at least one concrete frame for every event-frame group. One frame cannot characterize a heterogeneous group, so abstraction audits use a coverage-aware set containing boundary, uncertain, and sampled examples. Section 4 formalizes that audit set; Section 8 states the conditions under which conclusions drawn from it are valid.

The event sparsity hypothesis follows from this compression view. Relative to a finite declared candidate set, EventFrame hypothesizes that only a small fraction of distinctions materially worsen held-out proper risk when ablated. This predictive ratio is observationally testable under the fixed ablation protocol. A separate causal ratio requires randomized or otherwise identified interventions. Both must be measured in each domain rather than inferred from Planck constants or entropy bounds.

The main limitation of the ontology is extraction and compression quality. In real data, the "why" and "how" fields may be ambiguous, inferred, or unavailable. More fundamentally, the chosen coarse-graining \(\Gamma_{\Delta_\tau}\) may discard distinctions that later turn out to matter. EventFrame handles this by allowing missing values, confidence metadata, and revision under slow-path review rather than requiring false precision. A conservative implementation should distinguish observed fields from inferred fields and should propagate uncertainty into prediction and review. The next section defines the mathematical framework built on this compressed ontology.

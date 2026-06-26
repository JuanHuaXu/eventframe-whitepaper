# 2. Event Ontology

EventFrame uses event frames as the basic predictive unit, but not as the fundamental ontology. The underlying substrate is assumed to be much denser than the representation used by the predictor. That substrate may be physical, simulated, biological, robotic, or software-based. EventFrame does not attempt to model every low-level distinction. It treats an event frame as a compressed representation of a region where a distinction may matter for prediction or intervention.

An event is therefore a structured representation of a change, occurrence, action, observation, or state transition after coarse-graining. An event frame records that compressed event in fields that can be compared, predicted, fuzzed, cached, and abstracted.

An event frame at index \(t\) is written:

\[
e_t = (w_t, a_t, \tau_t, \ell_t, m_t, h_t, x_t, c_t)
\]

where \(w_t\) denotes participating agents or entities, \(a_t\) denotes the action or occurrence type, \(\tau_t\) denotes the time index or interval, \(\ell_t\) denotes location or spatial context, \(m_t\) denotes motive, objective, causal explanation, or inferred driver, \(h_t\) denotes mechanism or process, \(x_t\) denotes auxiliary state, and \(c_t\) denotes confidence, provenance, or uncertainty metadata.

The conceptual role of this ontology is compression. It prevents prediction from treating history as a single undifferentiated sequence, but it also prevents prediction from pretending that every microscopic distinction deserves its own event identity. The fields ask different compressed questions. The "what" field identifies an occurrence type. The "when" field supports temporal prediction loss. The "who" and "where" fields localize the event. The "why" and "how" fields record explanatory hypotheses and mechanisms. The auxiliary state field allows symbolic, vector, graph, or latent variables to travel with the event. The confidence field prevents uncertain extraction from pretending to be certain observation.

Let \(\Omega\) denote a dense substrate state space and let \(\omega_{A_t}\) denote the substrate history over a finite region \(A_t\). A coarse-graining map at temporal resolution \(\Delta_\tau\):

\[
\Gamma_{\Delta_\tau}: \Omega^{A_t} \rightarrow \mathcal{E}_{\Delta_\tau}
\]

produces an event frame:

\[
e_t = \Gamma_{\Delta_\tau}(\omega_{A_t}).
\]

This equation states the ontology clearly: the event frame is a lossy, task-oriented compression. The compression is useful only if it preserves distinctions that matter for prediction, intervention, memory, or review.

The temporal resolution \(\Delta_\tau\) controls how precise the "when" field is. A model may choose second-level frames, microsecond-level frames, or another declared scale. Finer resolution can instantiate more candidate frames, but it does not imply that every candidate frame is intervention-effective or should be retained forever. Sparsity means that useful distinctions are rare relative to the possible substrate and candidate-frame distinctions, not that the model is forbidden from creating many candidate frames when the task demands precision.

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

The context \(C_t\) is the recent event history available to the predictor. It gives the predictor enough local structure to ask what event should occur next and when. If the context is too short, important causal or temporal dependencies may be missing. If the context is too long, lookup and transition estimation may become noisy or expensive. The context length \(k\) is therefore a modeling choice that should be evaluated experimentally.

The ontology also supports links among events. Temporal links order events and represent intervals or delays. Spatial links relate event locations. Causal links express hypothesized dependencies, such as one event enabling, preventing, or modifying another. These links may be stored inside \(x_t\), represented as fields in \(c_t\), or modeled as edges in a separate event graph. The important constraint is that links remain available to the prediction and review process rather than being hidden in uninspectable history.

Event histories are therefore not limited to linear chains. Multiple event streams can become representable as a single aggregate event over time. This is event confluence: separate streams merge into a larger stream or macro-event when their separate identities no longer affect the target beyond a declared threshold. The reverse can also occur. A small distinction can branch into multiple downstream event streams when a perturbation is amplified by the dynamics. This is event divergence, or butterfly-effect-style sensitivity. EventFrame must model both patterns because compression that is safe in a confluence region may be unsafe near a divergence point.

For this reason, EventFrame keeps at least one representative event frame for every event-frame group. A group may be produced by abstraction, cache-key equivalence, lumpability, or confluence. The representative is a concrete retained frame, not merely a label. It gives the system something to intervene on, perturb, and compare when measuring whether a group should split because an intervention causes divergence, or whether several groups should merge because their downstream behavior has converged.

The event sparsity hypothesis follows from this compression view. If every microscopic substrate distinction required a unique event frame, the representation would be physically and computationally implausible. EventFrame instead assumes that intervention-effective event distinctions are sparse: only some compressed differences change the prediction target or downstream state beyond a threshold. Property fuzzing, ablation, and intervention tests are ways to discover which distinctions are worth preserving.

The main limitation of the ontology is extraction and compression quality. In real data, the "why" and "how" fields may be ambiguous, inferred, or unavailable. More fundamentally, the chosen coarse-graining \(\Gamma_{\Delta_\tau}\) may discard distinctions that later turn out to matter. EventFrame handles this by allowing missing values, confidence metadata, and revision under slow-path review rather than requiring false precision. A conservative implementation should distinguish observed fields from inferred fields and should propagate uncertainty into prediction and review. The next section defines the mathematical framework built on this compressed ontology.

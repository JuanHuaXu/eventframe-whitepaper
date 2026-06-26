# 2. Event Ontology

EventFrame uses event frames as the basic predictive unit. An event is a structured representation of a change, occurrence, action, observation, or state transition. An event frame records that event in fields that can be compared, predicted, fuzzed, cached, and abstracted.

An event frame at index \(t\) is written:

\[
e_t = (w_t, a_t, \tau_t, \ell_t, m_t, h_t, x_t, c_t)
\]

where \(w_t\) denotes participating agents or entities, \(a_t\) denotes the action or occurrence type, \(\tau_t\) denotes the time index or interval, \(\ell_t\) denotes location or spatial context, \(m_t\) denotes motive, objective, causal explanation, or inferred driver, \(h_t\) denotes mechanism or process, \(x_t\) denotes auxiliary state, and \(c_t\) denotes confidence, provenance, or uncertainty metadata.

The conceptual role of this ontology is to prevent event prediction from collapsing into a single undifferentiated sequence element. The fields ask different questions. The "what" field identifies an occurrence type. The "when" field supports temporal prediction loss. The "who" and "where" fields localize the event. The "why" and "how" fields record explanatory hypotheses and mechanisms. The auxiliary state field allows symbolic, vector, graph, or latent variables to travel with the event. The confidence field prevents uncertain extraction from pretending to be certain observation.

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

The main limitation of the ontology is extraction quality. In real data, the "why" and "how" fields may be ambiguous, inferred, or unavailable. EventFrame handles this by allowing missing values and confidence metadata rather than requiring false precision. A conservative implementation should distinguish observed fields from inferred fields and should propagate uncertainty into prediction and review. The next section defines the mathematical framework built on this ontology.

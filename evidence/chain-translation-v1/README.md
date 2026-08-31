# Chain Translation Mechanism Evidence

Aggregate, non-private outputs from the contract-16 public-grounded controls in
the `eventframed` repository. The fixture uses NIST's published Celsius/kelvin
relation and generated EventFrame wrappers. It contains no private transcript
text, production identifiers, or unpublished research data.

Both the design and confirmation outputs contain 24 deterministic controls:
eight supplied-map translations, eight terminal-erasure invariants, and eight
intermediate locality violations. All 24 received the expected label in each
split. These artifacts validate the classifier wiring for the supplied map;
they do not establish autonomous map discovery, transition-kernel equivalence,
or causal transport.

The optimized evaluator performs structural checks before prediction. The eight
locality violations in each split therefore report `prediction_evaluated=false`;
their zero-valued movement and defect fields are non-measurements. The sixteen
eligible controls in each split report `prediction_evaluated=true`. On Apple M4,
five benchmark runs for 32 stages at 256 dimensions measured 48.3--48.5
microseconds warm, 245.7--247.7 microseconds cold, and 34.1--34.2 microseconds
for structural divergence. The warm path allocated about 22.1 KB in 399
allocations. Store and remote-embedding latency are excluded.

Source implementation and complete generated inputs:
https://github.com/JuanHuaXu/eventframed/tree/main/testdata/chain-public-facts

Public factual source:
https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes

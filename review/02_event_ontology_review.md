# Review: 02 Event Ontology

## Extracted Definitions

- Microscopic substrate \(\Omega\).
- Coarse-graining \(\Gamma_{\Delta_\tau}\).
- Event frame \(e_t\).
- Temporal resolution \(\Delta_\tau\).
- Representative event frame.

## Extracted Claims

- Event frames are compressed representations.
- Temporal resolution controls candidate frame granularity.
- Event histories may merge or diverge.
- At least one representative frame should be retained per group.

## Math Review

- Severity: medium.
- Issue: The section later says slow-path review may revise \(\Gamma\), but the current notation parameterizes it as \(\Gamma_{\Delta_\tau}\).
- Suggested fix: Use \(\Gamma_{\Delta_\tau}\) consistently.

## Red-Team Review

- Main objection: The Planck-scale motivation could be read as stronger than intended.
- Minimum change needed: Maintain wording that this is motivation, not a quantum-gravity theory.

## Patch Decision

- Patched stale \(\Gamma\) mention to \(\Gamma_{\Delta_\tau}\).

# Repetition Gate Paper Synchronization Audit

Date: 2026-09-04. Runtime inspected: `74ccb92`; retrospective replay control:
`aca468a`. No runtime behavior, production service, or private transcript was
modified for this paper patch. No publication was requested in this turn.

## Formulation and Implementation Review

- Confirmed: packing uses exact keys or same-lineage Jaccard, whereas feedback
  uses exact keys and the first report representative only. The paper now keeps
  these distinct and preserves the ordinary frontier-update policy.
- Confirmed: the different Anti-Pigeon-key exemption is a key test, not proof of
  independent sources or mutual divergence. The first-representative feedback
  implementation can exempt multiple later entries in another bucket. No
  per-bucket or cross-journal uniqueness guarantee is claimed.
- Confirmed: a default-one greedy packet cannot contain a non-exempt correlated
  pair. The later accepted member would have failed its predecessor-count gate.
  Exhaustive checking of 1,100 symmetric relations on zero through five items
  found no counterexample. For larger caps the predecessor bound does not imply
  a final-degree bound; near-duplicate Jaccard is not transitive.
- Confirmed: packing changes packet output only, but feedback rejection can
  change future learned state and proper-scored laws. Complete selection
  conditioning is still required; descriptor grouping supplies no certificate.
- Remaining research/implementation requirements: authenticated and transitive
  lineage, cross-journal evidence accounting, semantic contradiction protection,
  independent nomination coverage, and a downstream poisoned-answer experiment.
  These are documented limits, not implemented improvements in this patch.

## Evidence Review

The whitelist-only aggregate export contains six source/block rows and 1,459
cases. The zero-case source block has no evaluated metrics. Brier, ECE,
priority-weighted Brier, and Recall@10 were checked for exact equality against
the parent in every populated variant. Codex design packed recall declines by
0.00043530534115637787; its reused 138-case block is unchanged. These are
descriptive regression observations, not new confirmation or attack efficacy.
Input aggregate checksums are retained without source identities or claim keys.

Focused runtime descriptor, packing, and service tests passed on this checkout.
They include ordinary-update preservation and selective-only rejection, but do
not establish security against malicious feedback issuers. No new end-to-end
latency or corpus replay was run during the paper synchronization.

## Publishing Bug Found During Visual QA

Status: confirmed. The ignored historical PDF builder replaced the live claim
table with a hard-coded snapshot and recognized only three other specific
tables. Its PDF omitted the new claim rows, retained stale old result labels,
and printed the new replay table as pipe-delimited prose. This was an assembly
bug, not an error in the Markdown data or a reason to rewrite experiment values.

The versioned `scripts/build_paper.py` preserves the existing assembly and TeX
layout but derives all tables from source rows. Four regression checks cover
every claim cell, the six replay rows, math pipes inside cells, and malformed
width rejection. The old ignored builder is superseded, not deleted. README
and source-assembly instructions point at the versioned builder.

The 211 original display-equation positions are preserved; only the fast-path
cost equation changes, adding explicit repetition work. All new mathematical
definitions are inline or in the numbered algorithm. GitHub output remains at
191 native display nodes and 20 semantic displays; union rendering was added to
the existing inline converter. The equation-position check protects the current
indexed display fallbacks; replacing that fragile indexing is separate work.

XeLaTeX builds passed after source synchronization. Visual QA covers the gate,
feedback rule, cost model, new claim rows, replay table, and symbol index. No
overfull boxes, missing characters, undefined controls, or final rerun warnings
were reported. This is a focused integration review of the added contract and
publishing path, not certification that every existing formula is error-free.

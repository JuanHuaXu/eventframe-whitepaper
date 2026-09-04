# EventFrame Whitepaper

**Author:** Juan Hua Xu
**ORCID:** <https://orcid.org/0009-0008-7305-5690>
**Research profile:** <https://github.com/JuanHuaXu>
**License:** MIT License. Copyright (c) 2026 Juan Hua Xu.

This repository is a portable source package for drafting the EventFrame Whitepaper: a self-contained white paper on EventFrame as a mathematical and computational framework for event-centric prediction.

The repository is intentionally independent of any specific agent, chatbot, product, or runtime implementation. Treat these files as the source of truth.

## Read the Paper

- [EventFrame Whitepaper (PDF)](EventFrame_Whitepaper.pdf)
- [EventFrame Whitepaper (GitHub-safe Markdown)](paper.md)

The canonical fully typeset Markdown assembly is [`build/paper.md`](build/paper.md). Run `ruby scripts/build_github_paper.rb` after rebuilding it; the script preserves all display equations, limits native inline math so GitHub does not exhaust its per-page renderer, and converts the remaining inline notation to semantic HTML with Unicode symbols and real sub/superscripts.

Synthetic reports and privacy-reduced aggregate chronological results cited by the paper are preserved under [`evidence/`](evidence/). They are mechanism and implementation evidence, not independent or controlled real-world validation. The corrected canonical-EventFrame corpus results are under [`evidence/eventframe-corpus-v1/`](evidence/eventframe-corpus-v1/), the claim-completion round is under [`evidence/claims-completion/`](evidence/claims-completion/), the rescue/replacement confirmation is under [`evidence/claim-rescue-v1/`](evidence/claim-rescue-v1/), and aggregate concurrency-rescue measurements are under [`evidence/runtime-rescue-v1/`](evidence/runtime-rescue-v1/). The older elastic-ranking and calibration reports under [`evidence/rank-adaptation-v1/`](evidence/rank-adaptation-v1/) are retained as historical false-start provenance because those organic runs used full transcript text in semantic retrieval; their synthetic mechanism controls remain informative where explicitly rerun under contract 12.

## Intended Output

Build the canonical assembly and TeX with `python3 scripts/build_paper.py`, check source-derived tables with `python3 scripts/test_paper_tables.py`, and generate GitHub Markdown with `ruby scripts/build_github_paper.rb`. Compile `tmp/pdfs/eventframe_whitepaper.tex` with XeLaTeX twice before replacing the distributed PDF. Do not use the historical ignored PDF builder, whose hard-coded tables could lag the Markdown source.

The repeated-memory gate and its limits are described in Section 6. Aggregate-only retrospective regression evidence and test boundaries are recorded in [`evidence/repetition-gate-v1/`](evidence/repetition-gate-v1/); these are not a downstream poisoning-resistance benchmark.

A publishable concept-and-math white paper covering:

1. Motivation and scope
2. Event ontology
3. Event-space mathematics
4. Prediction objective
5. Residual prediction
6. Episodic memory and residual cache
7. Property fuzzing and invariant extraction
8. Lumpability and abstraction
9. Anti-Pigeon principle
10. Complexity analysis
11. Reference runtime model
12. Experiments and open problems

## Core Rule

Do not assume access to any prior conversation or private project history. Everything needed must be reconstructed from files in this repository.

## License

This research paper and its accompanying source materials are available under the MIT License. See `LICENSE`.

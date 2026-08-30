# EventFrame Whitepaper

**Author:** Juan Hua Xu
**ORCID:** <https://orcid.org/0009-0008-7305-5690>
**Research profile:** <https://github.com/JuanHuaXu>
**License:** MIT License. Copyright (c) 2026 Juan Hua Xu.

This repository is a portable source package for drafting the EventFrame Whitepaper: a self-contained white paper on EventFrame as a mathematical and computational framework for event-centric prediction.

The repository is intentionally independent of any specific agent, chatbot, product, or runtime implementation. Treat these files as the source of truth.

## Read the Paper

- [EventFrame Whitepaper (PDF)](EventFrame_Whitepaper.pdf)
- [EventFrame Whitepaper (Markdown)](paper.md)

Synthetic reports and privacy-reduced aggregate chronological results cited by the paper are preserved under [`evidence/`](evidence/). They are mechanism and implementation evidence, not independent or controlled real-world validation. The claim-completion round is under [`evidence/claims-completion/`](evidence/claims-completion/), the rescue/replacement confirmation is under [`evidence/claim-rescue-v1/`](evidence/claim-rescue-v1/), and the elastic-ranking, Anti-Pigeon revision, and calibration-rescue reports are under [`evidence/rank-adaptation-v1/`](evidence/rank-adaptation-v1/).

## Intended Output

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

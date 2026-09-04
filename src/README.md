# Source Sections

The paper is assembled in reader order by the versioned `scripts/build_paper.py`:

1. Abstract and introduction.
2. Plain-language lifecycle.
3. Formal representation, mathematics, prediction, memory, abstraction, and runtime.
4. Claims register and experimental evidence.
5. Discussion, limitations, conclusion, acknowledgments, references, and symbol appendix.

Keep one Markdown file per source section. Filenames retain some historical numbering; the headings and builder order are authoritative. Run `python3 scripts/build_paper.py`, then `ruby scripts/build_github_paper.rb` to produce the GitHub-facing `paper.md`. PDF tables are derived from the Markdown rows, not frozen copies. The historical ignored builder under `tmp/pdfs/` is superseded.

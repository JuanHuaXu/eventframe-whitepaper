from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "build" / "paper.md"
OUTPUT = ROOT / "tmp" / "pdfs" / "eventframe_whitepaper.tex"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

SOURCE_FILES = [
    "00_abstract.md",
    "01_introduction.md",
    "02_conceptual_overview.md",
    "02_event_ontology.md",
    "03_mathematical_framework.md",
    "04_residual_prediction.md",
    "05_memory_model.md",
    "06_fuzzing_and_invariants.md",
    "07_lumpability_and_abstraction.md",
    "08_complexity_and_runtime_model.md",
    "01a_claims_register.md",
    "09_experimental_evaluation.md",
    "09a_discussion.md",
    "10_open_problems.md",
    "11_conclusion.md",
    "13_acknowledgments.md",
]

APPENDIX_FILES = ["12_symbol_index.md"]


def assemble_markdown() -> None:
    header = """# EventFrame Whitepaper: A Mathematical Framework for Event-Centric Prediction

**Author:** Juan Hua Xu

**ORCID:** <https://orcid.org/0009-0008-7305-5690>

**Research profile:** <https://github.com/JuanHuaXu>

**License:** MIT License. Copyright (c) 2026 Juan Hua Xu.

_Public working paper. Initial implementation evidence is reported in Section 11; full real-world validation remains outstanding._
"""
    parts = [header.rstrip()]
    for filename in SOURCE_FILES:
        chapter = (ROOT / "src" / filename).read_text(encoding="utf-8")
        chapter = re.sub(
            r"(?m)^(#{2,5}) ",
            lambda match: "#" + match.group(1) + " ",
            chapter,
        )
        chapter = re.sub(r"^# ", "## ", chapter, count=1)
        chapter = re.sub(r"(?m)^\\\[$", "$$", chapter)
        chapter = re.sub(r"(?m)^\\\]$", "$$", chapter)
        chapter = chapter.replace(r"\(", "$").replace(r"\)", "$")
        parts.append(chapter.rstrip())
    references = (ROOT / "spec" / "references.md").read_text(encoding="utf-8")
    references = re.sub(r"^# References Register", "## References", references, count=1)
    parts.append(references.rstrip())
    for filename in APPENDIX_FILES:
        appendix = (ROOT / "src" / filename).read_text(encoding="utf-8")
        appendix = re.sub(r"^# ", "## ", appendix, count=1)
        appendix = re.sub(r"(?m)^\\\[$", "$$", appendix)
        appendix = re.sub(r"(?m)^\\\]$", "$$", appendix)
        appendix = appendix.replace(r"\(", "$").replace(r"\)", "$")
        parts.append(appendix.rstrip())
    SOURCE.write_text("\n\n".join(parts) + "\n", encoding="utf-8")

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage{booktabs,longtable,array}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{xurl}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{fancyhdr}
\usetikzlibrary{arrows.meta,positioning,fit,calc}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.65em}
\setlength{\emergencystretch}{3em}
\setlength{\headheight}{14pt}
\setlist{itemsep=0.25em,topsep=0.35em}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  urlcolor=blue,
  citecolor=blue,
  pdftitle={EventFrame Whitepaper: A Mathematical Framework for Event-Centric Prediction},
  pdfauthor={Juan Hua Xu},
  pdfsubject={Event-centric prediction, residual memory retrieval, and adaptive abstraction},
  pdfkeywords={EventFrame, event prediction, memory retrieval, residual prediction, Anti-Pigeon},
  pdfinfo={
    ORCID={https://orcid.org/0009-0008-7305-5690},
    AuthorProfile={https://github.com/JuanHuaXu},
    License={MIT},
    Copyright={Copyright (c) 2026 Juan Hua Xu}
  }
}
\pagestyle{fancy}
\fancyhf{}
\lhead{EventFrame Whitepaper}
\rhead{Working Paper}
\cfoot{\thepage}
\title{EventFrame Whitepaper\\\large A Mathematical Framework for Event-Centric Prediction}
\author{Juan Hua Xu\\\small\href{https://orcid.org/0009-0008-7305-5690}{ORCID: 0009-0008-7305-5690}\\\small\href{https://github.com/JuanHuaXu}{github.com/JuanHuaXu}\\\small MIT License, Copyright (c) 2026 Juan Hua Xu}
\date{}
\begin{document}
\maketitle
\tableofcontents
\newpage
"""

DIAGRAM = r"""\begin{figure}[!htbp]
\centering
\resizebox{\linewidth}{!}{%
\begin{tikzpicture}[
  x=1cm,y=1cm,
  box/.style={draw,rounded corners=2pt,align=center,minimum width=2.15cm,minimum height=0.78cm,inner sep=4pt,font=\small},
  cache/.style={box,fill=blue!5},
  slow/.style={box,fill=gray!8},
  arrow/.style={-{Latex[length=2.4mm]},line width=0.55pt}
]
\node[box] (C) at (0,0) {Context\\\(C_t\)};
\node[box] (N) at (3.0,0) {Bounded Bayesian\\frontier};
\node[box] (J) at (6.0,0) {Admit and\\update belief};
\node[box] (B) at (9.0,0) {Posterior-predictive\\base \(\mathsf Q_t^0\)};
\node[cache] (A) at (2.0,-1.35) {Posterior-aware\\exact residual};
\node[box] (P) at (8.0,-1.35) {Typed\\composition};
\node[box] (Q) at (11.0,-1.35) {Pre-risk and\\validity gate};
\node[box] (L) at (14.0,-1.35) {Elastic rank and\\packet packing};
\node[box] (O) at (17.0,-1.35) {Return\\prediction};
\node[cache] (R) at (4.0,-2.55) {General residual\\cache};
\node[cache] (E) at (8.0,-2.55) {Episodic\\support};

\node[slow] (Z) at (17.0,-4.2) {Observe\\outcome};
\node[slow] (S) at (12.5,-4.2) {Post-observation\\slow path};
\node[slow] (U) at (4.2,-5.35) {Score and update\\memories};
\node[slow] (D) at (7.5,-5.35) {Bayesian audit and\\changepoint review};
\node[slow] (F) at (10.8,-5.35) {Sensitivity\\audit};
\node[slow] (G) at (14.0,-5.35) {Abstraction and\\compatibility audit};

\draw[arrow] (C)--(N);
\draw[arrow] (N)--(J);
\draw[arrow] (J)--(B);
\draw[arrow] (B.south) |- (A.north);
\draw[arrow] (A)--(P);
\draw[arrow] (A)--(R);
\draw[arrow] (R.east)--(P.south);
\draw[arrow] (R)--(E);
\draw[arrow] (E.north)--(P.south);
\draw[arrow] (P)--(Q);
\draw[arrow] (Q)--(L);
\draw[arrow] (L)--(O);
\draw[arrow] (O)--(Z);
\draw[arrow] (Z)--(S);
\draw[arrow] (S.south west) |- (U.north);
\draw[arrow] (S.south west) |- (D.north);
\draw[arrow] (S.south) -- (F.north);
\draw[arrow] (S.south east) |- (G.north);

\node[draw,dashed,rounded corners=3pt,inner xsep=7pt,inner ysep=5pt,fit=(C)(N)(J)(B)(A)(P)(Q)(L)(O)(R)(E),label={[font=\small]above:Prediction-time fast path}] {};
\node[draw,dashed,rounded corners=3pt,inner xsep=7pt,inner ysep=5pt,fit=(Z)(S)(U)(D)(F)(G),label={[font=\small]below:Deferred post-observation refinement}] {};
\end{tikzpicture}%
}
\caption{Reference runtime lifecycle. Realized loss and learning occur only after the outcome is observed.}
\end{figure}
"""


def escape_text(text: str) -> str:
    urls = []

    def hold_url(match):
        urls.append(match.group(1))
        return f"@@URL{len(urls) - 1}@@"

    text = re.sub(r"<([^>]+)>", hold_url, text)
    parts = re.split(r"(\\\(.*?\\\)|\$[^$]*\$)", text)
    for index in range(0, len(parts), 2):
        part = parts[index]
        part = part.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")
        part = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", part)
        parts[index] = part
    text = "".join(parts)
    for index, url in enumerate(urls):
        text = text.replace(f"@@URL{index}@@", rf"\url{{{url}}}")
    return text


assemble_markdown()
tex_source = re.sub(
    r"\$`([^`\n]*)`\$",
    lambda match: f"${match.group(1)}$",
    SOURCE.read_text(encoding="utf-8"),
)
lines = tex_source.splitlines()
out = [PREAMBLE.rstrip(), ""]
in_math = False
in_list = False
in_mermaid = False
skip_table_lines = 0


def table_cells(line: str) -> list[str]:
    # Pipe symbols inside math belong to the cell, not the table grammar.
    cells, current = [], []
    in_inline_math = False
    escaped = False
    for character in line.strip()[1:-1]:
        if character == "$" and not escaped:
            in_inline_math = not in_inline_math
        if character == "|" and not in_inline_math and not escaped:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        escaped = character == "\\" and not escaped
    cells.append("".join(current).strip())
    return cells


def render_table(block: list[str]) -> str:
    header = table_cells(block[0])
    separator = table_cells(block[1])
    if len(separator) != len(header) or not all(
        re.fullmatch(r":?-+:?", cell) for cell in separator
    ):
        raise ValueError("Invalid Markdown table separator")
    rows = [table_cells(line) for line in block[2:]]
    if any(len(row) != len(header) for row in rows):
        raise ValueError("Inconsistent Markdown table width")
    if header[0] == "Claim":
        widths = [0.06, 0.26, 0.20, 0.40]
    elif len(header) == 5:
        widths = [0.24, 0.08, 0.19, 0.19, 0.22]
    elif len(header) == 6:
        widths = [0.30, 0.124, 0.124, 0.124, 0.124, 0.124]
    else:
        widths = [0.92 / len(header)] * len(header)
    columns = "".join(
        rf">{{\raggedright\arraybackslash}}p{{{width:.3f}\linewidth}}"
        for width in widths
    )
    row_tex = lambda row: " & ".join(escape_text(cell) for cell in row) + r" \\"
    heading = row_tex(header)
    return "\n".join([
        r"\begingroup", r"\small", r"\setlength{\tabcolsep}{3pt}",
        r"\setlength{\LTleft}{0pt}", r"\setlength{\LTright}{0pt}",
        rf"\begin{{longtable}}{{@{{}}{columns}@{{}}}}",
        r"\toprule", heading, r"\midrule", r"\endfirsthead",
        r"\toprule", heading, r"\midrule", r"\endhead",
        *[row_tex(row) for row in rows],
        r"\bottomrule", r"\end{longtable}", r"\endgroup",
    ])


for line_no, line in enumerate(lines):
    if skip_table_lines:
        skip_table_lines -= 1
        continue
    if line_no == 0:
        continue
    if (
        line.startswith("**Author:**")
        or line.startswith("**ORCID:**")
        or line.startswith("**Research profile:**")
        or line.startswith("**License:**")
    ):
        continue
    if line.startswith("```mermaid"):
        if in_list:
            out.append(r"\end{enumerate}")
            in_list = False
        in_mermaid = True
        out.append(DIAGRAM.rstrip())
        continue
    if not in_math and not in_mermaid and line.startswith("|"):
        if in_list:
            out.append(r"\end{enumerate}")
            in_list = False
        table_end = line_no
        while table_end < len(lines) and lines[table_end].startswith("|"):
            table_end += 1
        out.append(render_table(lines[line_no:table_end]))
        skip_table_lines = table_end - line_no - 1
        continue
    if in_mermaid:
        if line == "```":
            in_mermaid = False
        continue
    if line in {r"\[", "$$"} and not in_math:
        if in_list:
            out.append(r"\end{enumerate}")
            in_list = False
        in_math = True
        out.append(r"\[")
        continue
    if line in {r"\]", "$$"} and in_math:
        in_math = False
        out.append(r"\]")
        continue
    if in_math:
        out.append(line)
        continue
    heading = re.match(r"^(#{2,4}) (.+)$", line)
    if heading:
        if in_list:
            out.append(r"\end{enumerate}")
            in_list = False
        level = len(heading.group(1))
        title = escape_text(heading.group(2))
        command = {2: "section", 3: "subsection", 4: "subsubsection"}[level]
        out.extend([rf"\{command}*{{{title}}}", rf"\addcontentsline{{toc}}{{{command}}}{{{title}}}", ""])
        continue
    item = re.match(r"^\d+\.\s+(.*)$", line)
    if item:
        if not in_list:
            out.append(r"\begin{enumerate}")
            in_list = True
        out.append(r"\item " + escape_text(item.group(1)))
        continue
    if in_list:
        out.append(r"\end{enumerate}")
        in_list = False
    if not line:
        out.append("")
        continue
    if line.startswith("_") and line.endswith("_") and len(line) > 2:
        out.append(r"\emph{" + escape_text(line[1:-1]) + "}")
        continue
    out.append(escape_text(line))

if in_list:
    out.append(r"\end{enumerate}")
out.extend(["", r"\end{document}", ""])
OUTPUT.write_text("\n".join(out), encoding="utf-8")

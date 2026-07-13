#!/usr/bin/env python3
"""Build an anonymized Synthese submission package from the canonical LaTeX draft.

Synthese takes LaTeX source plus compiled PDF, with anonymized review:
author identification and acknowledgements go on a separate title page.
Outputs under submission/synthese/:
  - main.anon.tex + synthese-anon.pdf  (anonymized manuscript)
  - title-page.tex + title-page.pdf    (author block + acknowledgements)
  - anon-bundle/                        (scrubbed source: tex, preamble, bib)
  - submission-checks.md                (anonymity scan results)
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "submission" / "synthese"
ANON_TEX = SUB / "main.anon.tex"
TITLE_TEX = SUB / "title-page.tex"
BUNDLE = SUB / "anon-bundle"

IDENTIFIERS = ["Reynolds", "Brett", "Humber", "brett.reynolds", "0000-0003-0073-7195"]

TITLE_PAGE = r"""\documentclass[12pt]{article}
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage{fontspec}
\setmainfont{Charis SIL}
\usepackage{orcidlink}
\hypersetup{hidelinks}
\begin{document}
\thispagestyle{empty}

\begin{center}
{\LARGE Effective without warrant: Causal-normative networks and the social life of status}

\vspace{2em}
Brett Reynolds \orcidlink{0000-0003-0073-7195}\\
Humber Polytechnic \& University of Toronto\\
\href{mailto:brett.reynolds@humber.ca}{brett.reynolds@humber.ca}
\end{center}

\vspace{3em}
\noindent\textbf{Acknowledgements.} The large language models Claude (Opus 4.8 and Fable 5) and ChatGPT (GPT-5.6) served as drafting and editing aids throughout the preparation of this paper. I am responsible for all theoretical claims, arguments, errors, and interpretive choices.

\vspace{1em}
\noindent\textbf{Declarations.} The author has no competing interests. No external funding supported this work. A preprint is available at PhilArchive (\url{https://philarchive.org/rec/REYEWW}).

\end{document}
"""


def run(cmd: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def make_anon_tex() -> None:
    text = (ROOT / "main.tex").read_text(encoding="utf-8")
    # Drop the author block (author + thanks + affiliation) entirely.
    text = re.sub(
        r"\\author\{.*?\n.*?\n.*?\}\n",
        "\\\\author{}\n",
        text,
        count=1,
        flags=re.S,
    )
    # Empty the date and force empty PDF author metadata (preamble sets it).
    text = text.replace("\\date{\\today}", "\\date{}")
    text = text.replace(
        "\\hypersetup{\n  pdftitle=",
        "\\hypersetup{\n  pdfauthor={},\n  pdftitle=",
    )
    # Acknowledgements move to the separate title page.
    text = re.sub(r"\\section\*\{Acknowledgements\}.*?(?=\\newpage)", "", text, flags=re.S)
    ANON_TEX.write_text(text, encoding="utf-8")


def build_pdf() -> None:
    args = [
        "xelatex", "-interaction=nonstopmode", "-halt-on-error",
        "-jobname=synthese-anon", "-output-directory", str(SUB), str(ANON_TEX),
    ]
    for step in (args, ["biber", str(SUB / "synthese-anon")], args, args):
        r = run(step)
        if r.returncode != 0 and "xelatex" in step[0]:
            sys.exit(f"build failed: {' '.join(step)}\n{r.stdout[-2000:]}")


def build_title_page() -> None:
    TITLE_TEX.write_text(TITLE_PAGE, encoding="utf-8")
    r = run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
             "-output-directory", str(SUB), str(TITLE_TEX)])
    if r.returncode != 0:
        sys.exit(f"title page build failed\n{r.stdout[-2000:]}")


def make_bundle() -> None:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    (BUNDLE / ".house-style").mkdir(parents=True)
    shutil.copy(ANON_TEX, BUNDLE / "main.anon.tex")
    shutil.copy(ROOT / "references-standalone.bib", BUNDLE / "references-standalone.bib")
    pre = (ROOT / ".house-style" / "preamble.tex").read_text(encoding="utf-8")
    pre = pre.replace("pdfauthor={Brett Reynolds}", "pdfauthor={}")
    pre = re.sub(r"% Purpose: .*house style.*\n", "% House-style preamble.\n", pre)
    (BUNDLE / ".house-style" / "preamble.tex").write_text(pre, encoding="utf-8")


def anonymity_checks() -> str:
    lines = ["# Synthese Submission Checks", ""]
    ok = True
    tex = ANON_TEX.read_text(encoding="utf-8")
    pdftext = run(["pdftotext", str(SUB / "synthese-anon.pdf"), "-"]).stdout
    meta = run(["pdfinfo", str(SUB / "synthese-anon.pdf")]).stdout
    bundle_texts = {
        p.name: p.read_text(encoding="utf-8", errors="replace")
        for p in BUNDLE.rglob("*") if p.is_file()
    }
    for ident in IDENTIFIERS:
        hits = []
        if ident.lower() in tex.lower():
            hits.append("anon tex")
        if ident.lower() in pdftext.lower():
            hits.append("anon PDF text")
        if ident.lower() in meta.lower():
            hits.append("PDF metadata")
        hits += [f"bundle:{n}" for n, t in bundle_texts.items() if ident.lower() in t.lower()]
        status = "CLEAN" if not hits else f"FOUND in {', '.join(hits)}"
        ok = ok and not hits
        lines.append(f"- `{ident}`: {status}")
    author_line = next((l for l in meta.splitlines() if l.startswith("Author")), "Author: (absent)")
    lines.append(f"- PDF metadata author field: `{author_line}`")
    pages = next((l for l in meta.splitlines() if l.startswith("Pages")), "")
    lines.append(f"- {pages}")
    lines.append("")
    lines.append("Overall: " + ("PASS" if ok else "FAIL"))
    return "\n".join(lines) + "\n"


def main() -> None:
    SUB.mkdir(parents=True, exist_ok=True)
    make_anon_tex()
    build_pdf()
    build_title_page()
    make_bundle()
    report = anonymity_checks()
    (SUB / "submission-checks.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

"""Paragraph-TOC page renumber: match each entry to the page where its text starts a
line (the heading), skipping cover/version/TOC pages; rewrite the trailing number."""
import re, subprocess, sys
from docx import Document

for k in ("LP", "LG"):
    docx = f"courseware/{k}-Autodesk Revit Architecture Masterclass (C508).docx"
    pdf = docx[:-5] + ".pdf"
    pages = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
    d = Document(docx)
    n = 0
    for p in d.paragraphs:
        m = re.match(r"(.+)\t(\d+)$", p.text)
        if not m:
            continue
        title = m.group(1).strip()
        hit = [i + 1 for i, pg in enumerate(pages) if i > 2 and
               any(l.strip() == title for l in pg.splitlines())]
        if not hit:
            sys.exit(f"{k}: heading not found: {title}")
        if hit[0] != int(m.group(2)):
            r = [r for r in p.runs if r.text.strip()][-1]
            r.text = re.sub(r"\d+(\s*)$", lambda mm: f"{hit[0]}{mm.group(1)}", r.text)
            n += 1
            print(f"{k}: {title[:50]} {m.group(2)} -> {hit[0]}")
    d.save(docx)
    print(k, "renumbered", n)

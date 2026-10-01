"""C508 LP + LG: convert the WSQ parent's built DOCX in place (design untouched).

Edits only: title, code, version record, WSQ layer (TSC, assessment, attendance,
funding), the 9:30am-5:30pm retiming, and slide refs remapped to the 114-slide deck.
"""
import re
from docx import Document

SRC = "source-wsq/courseware/{}-Architecture Drawing with Revit.docx"
OUT = "courseware/{}-Autodesk Revit Architecture Masterclass (C508).docx"
OLD_TITLE, NEW_TITLE = "Architecture Drawing with Revit", "Autodesk Revit Architecture Masterclass"
CODE = "C508"
VERSION_ROW = ("1.0", "1 October 2026", None, "Dr Alfred Ang")

# 1-based source slides dropped from the deck (0-based 2,9-14,120,121)
DROPPED = {3, 10, 11, 12, 13, 14, 15, 121, 122}
KEPT = [s for s in range(1, 124) if s not in DROPPED]
NEW_NO = {old: i + 1 for i, old in enumerate(KEPT)}


def remap(text):
    def rng(m):
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        ks = [NEW_NO[s] for s in range(a, b + 1) if s in NEW_NO]
        return f"Slides {ks[0]}–{ks[-1]}" if len(ks) > 1 else f"Slide {ks[0]}"
    return re.sub(r"Slides? (\d+)(?:–(\d+))?", rng, text)


def set_par(par, text):
    if not par.runs:
        par.add_run(text)
        return
    # cells may open with an EMPTY run; write into the first run that carries text
    runs = par.runs
    k = next((i for i, r in enumerate(runs) if r.text), 0)
    for i, r in enumerate(runs):
        r.text = text if i == k else ""


def drop(par):
    par._p.getparent().remove(par._p)


def set_cell(cell, text):
    pars = cell.paragraphs
    set_par(pars[0], text)
    for p in pars[1:]:
        drop(p)


def drop_row(table, row):
    table._tbl.remove(row._tr)


def version_record(doc, summary):
    t = doc.tables[0]
    for r in t.rows[2:]:
        drop_row(t, r)
    no, date, _, author = VERSION_ROW
    for c, v in zip(t.rows[1].cells, (no, date, summary, author)):
        set_cell(c, v)


def cover(doc):
    for p in doc.paragraphs[:14]:
        t = p.text
        if t == OLD_TITLE:
            set_par(p, NEW_TITLE)
        elif t.startswith("TGS Ref No"):
            set_par(p, f"Course Code: {CODE}")
        elif t.startswith("Version 12"):
            set_par(p, "Version 1.0")


def strip_tsc(t):
    t = re.sub(r"\s*\(A\d(?:, A\d)* · K\d(?:, K\d)*\)", "", t)      # topic headings
    return re.sub(r"\((LO\d) · A\d(?:, A\d)*\)", r"(\1)", t)         # learning-outcome lines


def schedule(table, plan):
    """plan: list of (match, (start, end, dur), new_text|None) in FINAL order. Rows not
    matched are deleted (tea breaks, assessment, attendance); kept rows are re-appended
    in plan order so a moved lunch lands in the right place."""
    rows = list(table.rows)[1:]
    keep = []
    for match, (start, end, dur), text in plan:
        row = next(r for r in rows if match in r.cells[2].text)
        rows.remove(row)
        c = row.cells
        set_cell(c[0], f"{start}–{end}")
        set_cell(c[1], f"{dur} min")
        set_cell(c[2], remap(text or c[2].text))
        keep.append(row)
    for r in rows:
        drop_row(table, r)
    for r in keep:
        table._tbl.remove(r._tr)
        table._tbl.append(r._tr)


def times(start, durs):
    h, m = map(int, start.split(":"))
    t = h * 60 + m
    out = []
    for d in durs:
        out.append((f"{t // 60}:{t % 60:02d}", f"{(t + d) // 60}:{(t + d) % 60:02d}", d))
        t += d
    assert t == 17 * 60 + 30, f"day ends {t // 60}:{t % 60:02d}"
    return out


def lp():
    doc = Document(SRC.format("LP"))
    cover(doc)
    version_record(doc, "First release of the Autodesk Revit Architecture Masterclass: four "
                        "topics and 12 hands-on Revit labs over two days, 9:30am – 5:30pm "
                        "(7.5 instructional hours per day).")
    for p in list(doc.paragraphs):
        t = p.text
        if t.startswith("Assessment\t") or (p.style.name == "Heading 1" and t == "Assessment"):
            drop(p)
        elif p.style.name == "List Bullet" and re.search(
                r"Written Assessment|Practical Performance|Open Book|Final assessment|75% attendance", t):
            drop(p)
        elif "Documentation, Specification & Assessment" in t:
            set_par(p, t.replace("Documentation, Specification & Assessment",
                                 "Documentation & Specification"))
        elif "Lab Reference (aligned to the Skills Framework TSC)" in t:
            set_par(p, t.replace(" (aligned to the Skills Framework TSC)", ""))
        elif t.startswith("Total training time"):
            set_par(p, "Day total: 7.5 instructional hours (9:30am – 5:30pm, 30-min lunch).")

    info = doc.tables[1]
    for r in list(info.rows):
        k = r.cells[0].text
        if k == "Course Title":
            set_cell(r.cells[1], NEW_TITLE)
        elif k == "WSQ Course Reference":
            set_cell(r.cells[0], "Course Code")
            set_cell(r.cells[1], CODE)
        elif k == "Skills Framework TSC":
            drop_row(info, r)
        elif k == "Duration":
            set_cell(r.cells[1], "2 days · 7.5 instructional hours per day (15 hours)")
        elif k == "Daily Timing":
            set_cell(r.cells[1], "9:30 am – 5:30 pm (30-min lunch)")

    # Day 1: teaching rows already total 450 min; the two tea breaks go and the
    # 60-min lunch becomes 30 min, so the day closes on 17:30.
    d1 = times("9:30", [30, 60, 105, 30, 75, 45, 120, 15])
    schedule(doc.tables[2], [
        ("Welcome", d1[0], "Welcome, trainer and learner introductions, ground rules, course "
                           "material download, lesson plan and course outline. Slides 1–15."),
        ("Revit & BIM fundamentals", d1[1], None),
        ("Lab 1:", d1[2], None),
        ("Lunch", d1[3], "Lunch break."),
        ("Lab 3:", d1[4], None),
        ("Topic 2", d1[5], None),
        ("Lab 5:", d1[6], None),
        ("Day 1 recap", d1[7], "Day 1 recap and Q&A."),
    ])
    # Day 2: the six topic/lab blocks rescaled proportionally 255 -> 420 min
    # (x1.647, 5-min grain, -5 drift on the largest); recap + summary stay 15.
    d2 = times("9:30", [15, 100, 50, 30, 145, 50, 75, 15])
    schedule(doc.tables[3], [
        ("Day 1 recap", d2[0], "Day 1 recap and Q&A."),
        ("Lab 8:", d2[1], None),
        ("Topic 3", d2[2], None),
        ("Lunch", d2[3], "Lunch break."),
        ("Lab 9:", d2[4], None),
        ("Topic 4", d2[5], None),
        ("Lab 12:", d2[6], None),
        ("Course summary", d2[7], "Course summary, practice exam, recommended courses and "
                                  "course feedback. Slides 115–123."),
    ])

    # Lab Reference: drop the TSC mapping column
    lab = doc.tables[4]
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    for r in lab.rows:
        tc = r._tr.tc_lst[1]
        w_from = tc.tcPr.find(W + "tcW")
        tc0 = r._tr.tc_lst[0].tcPr.find(W + "tcW")
        if w_from is not None and tc0 is not None:
            tc0.set(W + "w", str(int(tc0.get(W + "w")) + int(w_from.get(W + "w"))))
        r._tr.remove(tc)
    grid = lab._tbl.tblGrid
    cols = grid.gridCol_lst
    cols[0].w = cols[0].w + cols[1].w
    grid.remove(cols[1])
    doc.core_properties.title = NEW_TITLE
    doc.save(OUT.format("LP"))


LG_SUBS = [
    ("This Learner Guide accompanies the WSQ course Architecture Drawing with Revit "
     "(TGS-2021004287), conducted by Tertiary Infotech Academy Pte Ltd. It provides step-by-step "
     "instructions for all 12 hands-on labs, organised by the four course topics, and is aligned "
     "to the Skills Framework TSC Technical Drawing (BEV-TDR-3005-1.1-1) under the Built "
     "Environment Skills Framework — abilities A1–A5 and knowledge K1–K5.",
     f"This Learner Guide accompanies the course {NEW_TITLE} ({CODE}), conducted by Tertiary "
     "Infotech Academy Pte Ltd. It provides step-by-step instructions for all 12 hands-on labs, "
     "organised by the four course topics."),
    (" The final assessment is open book: the slides, this Learner Guide and approved materials "
     "may be used.", ""),
    ("Assessment Preparation", "Consolidating Your Skills"),
    ("Review the Key Concepts of each topic — the Written Assessment (SAQ, 60 min) tests "
     "knowledge K1–K5.",
     "Review the Key Concepts of each topic to consolidate the theory behind each lab."),
    ("The Practical Performance (90 min) tests abilities A1–A5 with hands-on Revit tasks drawn "
     "from the labs.",
     "Practise end-to-end: model, document and specify a small building in Revit, drawing on "
     "the labs."),
]
LG_DROP = "Both assessments are open book: bring the slides and this Learner Guide."


def lg_text(t):
    for a, b in LG_SUBS:
        t = t.replace(a, b)
    return strip_tsc(t)


def lg():
    doc = Document(SRC.format("LG"))
    cover(doc)
    version_record(doc, "First release of the Autodesk Revit Architecture Masterclass learner "
                        "guide: 12 step-by-step labs with reusable Revit models, environment "
                        "setup, a skills-consolidation checklist and a glossary.")
    pars = doc.paragraphs
    # Skills Framework Mapping section: heading through the last K bullet
    start = next(i for i, p in enumerate(pars) if p.style.name == "Heading 1"
                 and p.text == "Skills Framework Mapping")
    end = next(i for i in range(start + 1, len(pars)) if pars[i].style.name == "Heading 1")
    for p in pars[start:end]:
        drop(p)
    for p in list(doc.paragraphs):
        if p.text.startswith("Skills Framework Mapping\t") or p.text == LG_DROP:
            drop(p)
            continue
        new = lg_text(p.text)
        if new != p.text:
            set_par(p, new)
    doc.core_properties.title = NEW_TITLE
    doc.save(OUT.format("LG"))


def lg_md():
    src = open(f"source-wsq/LG-{OLD_TITLE}.md", encoding="utf-8").read()
    src = src.replace(f"# {OLD_TITLE} — Learner Guide", f"# {NEW_TITLE} — Learner Guide")
    src = src.replace("**WSQ Course Code:** TGS-2021004287", f"**Course Code:** {CODE}")
    src = src.replace("**Version v12 · 18 August 2026**", "**Version v1.0 · 1 October 2026**")
    src = src.replace("(#assessment-preparation)", "(#consolidating-your-skills)")
    src = re.sub(r"--a\d(?:-a\d)*--k\d(?:-k\d)*\)", ")", src)   # TOC anchors for the stripped (A# · K#)
    src = re.sub(r"## Skills Framework Mapping\n.*?(?=\n## )", "", src, flags=re.S)
    lines = [l for l in src.split("\n")
             if "(#skills-framework-mapping)" not in l and l != f"- {LG_DROP}"]
    out = "\n".join(lg_text(l) for l in lines)
    out = re.sub(r"\n{4,}", "\n\n\n", out)
    open(f"LG-{NEW_TITLE} ({CODE}).md", "w", encoding="utf-8").write(out)


if __name__ == "__main__":
    lp()
    lg()
    lg_md()
    print("docs ok")

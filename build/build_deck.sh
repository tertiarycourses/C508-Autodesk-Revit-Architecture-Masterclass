#!/bin/sh
set -e
S=~/.claude/skills/wsq-to-non-wsq/scripts
python3 $S/convert_deck.py \
  --src "source-wsq/courseware/Architecture Drawing with Revit-v12.pptx" \
  --out "courseware/Autodesk Revit Architecture Masterclass (C508)-v1.0.pptx" \
  --old-title "Architecture Drawing with Revit" --new-title "Autodesk Revit Architecture Masterclass" \
  --old-code TGS-2021004287 --new-code C508 \
  --sub "WSQ Course Code: TGS-2021004287=>Course Code: C508" \
  --sub "Version v12  ·  18 August 2026=>Version v1.0  ·  1 October 2026" \
  --sub "COURSE SLIDES  ·  WSQ=>COURSE SLIDES  ·  NON-WSQ COURSE" \
  --sub "75% attendance is required.=>Attend both days in full." \
  --wsq-slides 2,9,10,11,12,13,14,120,121
python3 build/fix_deck.py

#!/bin/sh
# Rebuild the whole C508 set from source-wsq/ (read-only input).
set -e
./build/build_deck.sh
python3 build/build_docs.py
rm -rf labs && cp -R source-wsq/labs labs && python3 build/fix_labs.py
for f in labs/*/Lab-*.docx; do
  soffice --headless --convert-to pdf "$f" --outdir "$(dirname "$f")" >/dev/null 2>&1
done
for f in courseware/*.pptx courseware/*.docx; do
  soffice --headless --convert-to pdf "$f" --outdir courseware >/dev/null 2>&1
done
python3 build/renumber_toc.py
for f in courseware/*.docx; do
  soffice --headless --convert-to pdf "$f" --outdir courseware >/dev/null 2>&1
done
python3 build/renumber_toc.py

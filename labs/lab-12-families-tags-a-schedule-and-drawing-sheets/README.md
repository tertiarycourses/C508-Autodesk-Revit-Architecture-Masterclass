# Lab 12 — Families, Tags, a Schedule and Drawing Sheets

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 04: Design Specification**

**Learning outcome:** produce design specification using Revit (LO4)

## Goal

Load the door, window and wall tag families supplied in the lab folder, tag the model, build a door schedule, then compose a titled drawing sheet with plan, section and schedule — the deliverable construction document.

## You'll build

A construction-document sheet with title block carrying the plan, a section, tags and a live door schedule.

**Tools:** Revit · Load Family · Tag by Category · Schedule/Quantities · Sheet

## Files in this lab

- `LittleHouse.rvt` — open in Autodesk Revit
- `Door Tag FR.rfa` — open in Autodesk Revit
- `Window Tag.rfa` — open in Autodesk Revit
- `Wall tag.rfa` — open in Autodesk Revit

## Step-by-step

1. Load the three tag families supplied in this lab's folder.

   > `Insert ▸ Load from Library ▸ Load Family ▸ select the 3 RFA files`

2. Tag the doors, windows and walls in the entry-level plan.

   > `Annotate ▸ Tag ▸ Tag by Category ▸ click each element`

3. Create a door schedule and choose its fields.

   > `View ▸ Create ▸ Schedules ▸ Schedule/Quantities ▸ Doors ▸ add Mark, Type, Width, Height`

4. Sort the schedule by Mark and format the headers.

   > `Schedule Properties ▸ Sorting/Grouping ▸ Mark ▸ Formatting`

5. Create a sheet from a title block and rename it.

   > `View ▸ Sheet Composition ▸ Sheet ▸ A1 metric ▸ rename A101 - Plans`

6. Drag the plan, the section and the schedule onto the sheet and arrange the viewports.

   > `Drag views from the Project Browser onto the sheet`

7. Print or export the sheet to PDF as the issued document.

   > `File ▸ Print ▸ PDF driver ▸ Selected views/sheets ▸ OK`


## Test it

Sheet A101 shows the plan, section and door schedule inside the title block; the schedule updates live when a door type changes, and the exported PDF matches the sheet.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

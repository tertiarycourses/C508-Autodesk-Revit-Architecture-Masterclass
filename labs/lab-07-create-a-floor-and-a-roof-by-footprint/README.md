# Lab 7 — Create a Floor and a Roof by Footprint

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 02: Part Lists for Modeling in Revit**

**Learning outcome:** create part lists for modeling using Revit (LO2)

## Goal

Create a mezzanine floor by sketching its boundary, edit the sketch with Align and Trim into a closed loop, then complete the envelope with a footprint roof whose slopes you define.

## You'll build

A mezzanine floor in the store-room area and a sloped roof closing the building envelope.

**Tools:** Revit · Floor: Architectural · Roof by Footprint · Shaft Opening

## Files in this lab

- `ModelCreation.rvt` — open in Autodesk Revit

## Step-by-step

1. Open the upper-level plan and start the architectural Floor tool.

   > `Architecture ▸ Build ▸ Floor ▸ Floor: Architectural`

2. Pick the bounding walls, then switch to Line to close the open edge.

   > `Modify | Create Floor Boundary ▸ Pick Walls ▸ Draw ▸ Line`

3. Use Align and Trim to make the sketch one closed loop, then finish.

   > `Modify ▸ Align / Trim ▸ ✓ Finish Edit Mode`

4. Cut a stair opening through the new floor with the Shaft tool.

   > `Architecture ▸ Opening ▸ Shaft ▸ sketch the opening ▸ Finish`

5. Create the roof from the building footprint on the roof level.

   > `Architecture ▸ Build ▸ Roof ▸ Roof by Footprint ▸ Pick Walls`

6. Set which boundary lines define a slope, then finish and view in 3D.

   > `Select a line ▸ Properties ▸ Defines Roof Slope ✓ ▸ ✓ Finish`


## Test it

The mezzanine floor appears with a clean shaft opening, and the 3D view shows a sloped roof sitting on the footprint — no warnings about open loops.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

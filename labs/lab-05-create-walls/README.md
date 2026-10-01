# Lab 5 — Create Walls

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 02: Part Lists for Modeling in Revit**

**Learning outcome:** create part lists for modeling using Revit (LO2)

## Goal

Work on different levels to add the exterior walls, interior partition walls and a corridor to the project, then tidy the joins with the Trim/Extend tool.

## You'll build

A building shell with exterior walls, interior walls and a corridor opening on the lower level.

**Tools:** Revit · Wall: Architectural · Trim/Extend

## Files in this lab

- `ModelCreation.rvt` — open in Autodesk Revit

## Step-by-step

1. Open the lower-level floor plan and start the architectural Wall tool.

   > `Architecture ▸ Build ▸ Wall ▸ Wall: Architectural`

2. Pick the wall type and set base/top constraints in the Properties palette.

   > `Type Selector ▸ Basic Wall: Generic 200mm ▸ Top Constraint: Up to level 02`

3. On the Options Bar set the Location Line and enable Chain, then draw the exterior walls clockwise.

   > `Options Bar ▸ Location Line: Wall Centerline ▸ Chain ✓`

4. Add the interior partition walls with a thinner wall type.

   > `Type Selector ▸ Basic Wall: Interior 135mm Partition`

5. Create the corridor by trimming the partition walls to form the opening.

   > `Modify ▸ Trim/Extend to Corner ▸ click the two walls to keep`

6. Check the shell in 3D and correct any wall join problems.

   > `Default 3D View ▸ inspect ▸ Modify ▸ Wall Joins if needed`


## Test it

The lower level shows a closed exterior shell with interior partitions and a corridor; walls meet cleanly with no gaps or crossing lines. Compare with ModelCreation.rvt in the lab folder.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

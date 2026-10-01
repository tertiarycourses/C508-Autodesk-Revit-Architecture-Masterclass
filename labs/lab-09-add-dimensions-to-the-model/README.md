# Lab 9 — Add Dimensions to the Model

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 03: Model Documentation**

**Learning outcome:** assist in design prototyping and create design documentation (LO3)

## Goal

Dimension the footprint of the main building: overall widths, then aligned dimension strings that automatically pick up grid intersections and window openings on the exterior walls.

## You'll build

A dimensioned floor plan documenting the building footprint, grids and openings.

**Tools:** Revit · Aligned Dimension · Linear Dimension

## Files in this lab

- `LittleHouse.rvt` — open in Autodesk Revit

## Step-by-step

1. Open the entry-level floor plan of LittleHouse.rvt.

   > `Project Browser ▸ Floor Plans ▸ 01 - Entry Level`

2. Start the Aligned dimension tool and set the snap preference.

   > `Annotate ▸ Dimension ▸ Aligned ▸ Options Bar ▸ Prefer: Wall faces`

3. Dimension the overall width: click the two outer wall faces, then click to place the line.

   > `Click wall face ▸ click opposite face ▸ click to place`

4. Dimension the exterior wall with grid intersections picked up automatically.

   > `Options Bar ▸ Pick: Entire Walls ▸ Options ▸ Intersecting Grids ✓`

5. Add the window openings to the same dimension string.

   > `Options ▸ Openings: Centers ✓ ▸ click the exterior wall`

6. Place a linear dimension between two points and align it with the Spacebar.

   > `Annotate ▸ Dimension ▸ Linear ▸ pick two points ▸ Spacebar`


## Test it

The plan shows an overall dimension plus a string that lists every grid intersection and window centre along the exterior wall — values update if a window is moved.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

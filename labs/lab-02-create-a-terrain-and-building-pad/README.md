# Lab 2 — Create a Terrain and Building Pad

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 01: Design Modeling in Revit**

**Learning outcome:** produce and visualise 2D/3D technical drawings using Revit (LO1)

## Goal

Add a toposurface to the building site by placing points at different elevations, then cut a building pad into the terrain based on the footprint of the foundation walls.

## You'll build

A landscaped site with a graded toposurface, a grass material and a building pad ready for the model.

**Tools:** Revit · Toposurface · Building Pad · Section Box

## Files in this lab

- `LittleHouse.rvt` — open in Autodesk Revit

## Step-by-step

1. Open the site plan view of the project.

   > `Project Browser ▸ Floor Plans ▸ Site`

2. Start the Toposurface tool and place boundary points at elevation 0.

   > `Massing & Site ▸ Model Site ▸ Toposurface ▸ Place Point ▸ Elevation 0`

3. Raise the far points: change the elevation on the Options Bar as you place them.

   > `Options Bar ▸ Elevation 900 ▸ click to place the back points`

4. Assign a grass material to the surface, then finish it.

   > `Properties ▸ Material ▸ Grass ▸ Finish Surface`

5. Sketch a building pad over the foundation footprint on the lower level.

   > `Massing & Site ▸ Model Site ▸ Building Pad ▸ Pick Walls ▸ Finish`

6. Frame the result in 3D with a section box to see the pad cutting the terrain.

   > `3D view ▸ Properties ▸ Section Box ✓ ▸ drag the handles`


## Test it

The 3D view shows the terrain with a grass material, and the building pad cuts a level recess into the toposurface at the foundation walls.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

# Lab 1 — Create a Project and Add Levels

**Course:** Autodesk Revit Architecture Masterclass (C508) · **Topic 01: Design Modeling in Revit**

**Learning outcome:** produce and visualise 2D/3D technical drawings using Revit (LO1)

## Goal

Start a new Revit project from the architectural template, rename the default levels and add new levels that become the vertical datums for the whole building model.

## You'll build

A Revit project with four named, correctly-elevated levels and their floor-plan views.

**Tools:** Revit · Architectural Template · Level tool

## Files in this lab

- `LittleHouse.rvt` — open in Autodesk Revit

## Step-by-step

1. Start Revit and create a new project from the architectural template.

   > `File ▸ New ▸ Project ▸ Architectural Template ▸ OK`

2. Open a building elevation so the levels are visible.

   > `Project Browser ▸ Elevations (Building Elevation) ▸ South`

3. Rename Level 1 to '01 - Entry Level'; accept renaming the corresponding views.

   > `Double-click the level name ▸ type 01 - Entry Level ▸ Enter ▸ Yes`

4. Rename Level 2 to '02 - Upper Level' and set its elevation by clicking the blue elevation value.

   > `Double-click the elevation value ▸ type 3000 ▸ Enter`

5. Add a roof level by drawing a new level above the existing ones.

   > `Architecture ▸ Datum ▸ Level ▸ draw left to right above 02`

6. Add another level by offsetting from an existing one, then rename it.

   > `Modify | Place Level ▸ Pick Lines ▸ Offset 3000 ▸ click level 02`


## Test it

The Project Browser lists a floor plan for each new level, and the South elevation shows all four levels with the correct names and elevations. Compare with the completed LittleHouse.rvt model in the lab folder.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. Sample Revit models © their respective authors (MIT licence — see labs/_assets).*

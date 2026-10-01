# Autodesk Revit Architecture Masterclass — Learner Guide

**Course Code:** C508  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 1 October 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Environment Setup](#before-you-start--environment-setup)
- [Topic 01 — Design Modeling in Revit](#topic-01--design-modeling-in-revit)
  - [Lab 1 — Create a Project and Add Levels](#lab-1--create-a-project-and-add-levels)
  - [Lab 2 — Create a Terrain and Building Pad](#lab-2--create-a-terrain-and-building-pad)
  - [Lab 3 — Create an In-Place Mass and Apply Materials](#lab-3--create-an-in-place-mass-and-apply-materials)
  - [Lab 4 — Render a Photorealistic View](#lab-4--render-a-photorealistic-view)
- [Topic 02 — Part Lists for Modeling in Revit](#topic-02--part-lists-for-modeling-in-revit)
  - [Lab 5 — Create Walls](#lab-5--create-walls)
  - [Lab 6 — Place Doors and Windows](#lab-6--place-doors-and-windows)
  - [Lab 7 — Create a Floor and a Roof by Footprint](#lab-7--create-a-floor-and-a-roof-by-footprint)
  - [Lab 8 — Create Stairs and Railings](#lab-8--create-stairs-and-railings)
- [Topic 03 — Model Documentation](#topic-03--model-documentation)
  - [Lab 9 — Add Dimensions to the Model](#lab-9--add-dimensions-to-the-model)
  - [Lab 10 — Create Rooms, an Area Plan and a Color Fill Legend](#lab-10--create-rooms-an-area-plan-and-a-color-fill-legend)
  - [Lab 11 — Create Section, Callout and Dependent Views](#lab-11--create-section-callout-and-dependent-views)
- [Topic 04 — Design Specification](#topic-04--design-specification)
  - [Lab 12 — Families, Tags, a Schedule and Drawing Sheets](#lab-12--families-tags-a-schedule-and-drawing-sheets)
- [Consolidating Your Skills](#consolidating-your-skills)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the course Autodesk Revit Architecture Masterclass (C508), conducted by Tertiary Infotech Academy Pte Ltd. It provides step-by-step instructions for all 12 hands-on labs, organised by the four course topics.

Use this guide alongside the course slides and the lab folders in the labs/ directory of the course repository. Each lab folder contains this guide's instructions as a README.md and a PDF, together with the Autodesk Revit file(s) used in that lab.


## Course Learning Outcomes

- LO1: Produce and visualise 2D/3D technical drawings using Revit
- LO2: Create part lists for modeling using Revit
- LO3: Assist in design prototyping and create design documentation
- LO4: Produce design specification using Revit


## Before You Start — Environment Setup

**What you need**

- Autodesk Revit (a recent release — the labs use the Architecture tools; the free 30-day trial or an education licence from autodesk.com works).
- A Windows PC that meets the Revit system requirements (Revit does not run natively on macOS — use Boot Camp/Parallels or a lab machine).
- The course lab files: download them from the LMS/TMS portal (https://lms-tms.tertiaryinfotech.com) or copy the labs/ folder from the course repository.
- Each lab folder contains the Revit model(s) it uses — e.g. LittleHouse.rvt, ModelCreation.rvt and the door/window/wall tag families (RFA).

**Launch and verify Revit**

Start Revit from the Windows Start menu. On the Home page you should see Models (New / Open) and Families. Create a test project from the Architectural Template — if the template list is empty, install the Revit content packs or point Revit at the template folder under File Locations in the Options dialog.

**Conventions used in every lab**

- Ribbon paths are written as Tab ▸ Panel ▸ Tool, e.g. Architecture ▸ Build ▸ Wall.
- Steps assume the metric architectural template unless the lab says otherwise.
- Save your work as <lab-number>-<your-name>.rvt inside the lab folder so the trainer can review it.
- If a tool is greyed out, check the active view type — many tools only work in a plan, elevation or 3D view.
- Press Esc twice to exit any active tool; Ctrl+Z undoes the last action.


## Topic 01 — Design Modeling in Revit

BIM & the Revit platform · User interface · Site design & toposurfaces · Massing · Materials · Rendering

**Key concepts**

- BIM platform — Revit supports design, drawings and schedules for building information modeling — every sheet, view and schedule presents the same virtual building model.
- Parametric change engine — A change made anywhere — model views, sheets, schedules, sections, plans — is coordinated automatically everywhere else.
- Revit user interface — Ribbon, Application Menu, Quick Access Toolbar, Project Browser, Properties palette, Options Bar and View Control Bar.
- Site design — Sketch a toposurface, then add property lines, a building pad, parking and site components; present it in 3D or rendered views.
- Massing studies — Conceptual mass families and in-place masses let you study volumes, zoning and floor-area ratio before detailed modeling.
- Materials & rendering — Materials control graphics, appearance, thermal and physical data; the Render tool produces photorealistic images of the model.


### Lab 1 — Create a Project and Add Levels

Learning outcome: produce and visualise 2D/3D technical drawings using Revit (LO1).

Goal: Start a new Revit project from the architectural template, rename the default levels and add new levels that become the vertical datums for the whole building model.

**Workflow**

![Lab 1 workflow — Create a Project and Add Levels](courseware/assets/lg/lab-01.png)

*Lab 1 workflow — Create a Project and Add Levels*

**What you'll build**

A Revit project with four named, correctly-elevated levels and their floor-plan views.   (Tools: Revit · Architectural Template · Level tool.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-01-create-a-project-and-add-levels/

**Step-by-step**

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


**Test it**

The Project Browser lists a floor plan for each new level, and the South elevation shows all four levels with the correct names and elevations. Compare with the completed LittleHouse.rvt model in the lab folder.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-01-create-a-project-and-add-levels/.

---


### Lab 2 — Create a Terrain and Building Pad

Learning outcome: produce and visualise 2D/3D technical drawings using Revit (LO1).

Goal: Add a toposurface to the building site by placing points at different elevations, then cut a building pad into the terrain based on the footprint of the foundation walls.

**Workflow**

![Lab 2 workflow — Create a Terrain and Building Pad](courseware/assets/lg/lab-02.png)

*Lab 2 workflow — Create a Terrain and Building Pad*

**What you'll build**

A landscaped site with a graded toposurface, a grass material and a building pad ready for the model.   (Tools: Revit · Toposurface · Building Pad · Section Box.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-02-create-a-terrain-and-building-pad/

**Step-by-step**

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


**Test it**

The 3D view shows the terrain with a grass material, and the building pad cuts a level recess into the toposurface at the foundation walls.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-02-create-a-terrain-and-building-pad/.

---


### Lab 3 — Create an In-Place Mass and Apply Materials

Learning outcome: produce and visualise 2D/3D technical drawings using Revit (LO1).

Goal: Model a conceptual building volume as an in-place mass, then use the Materials browser to control how model elements display in shaded and rendered views.

**Workflow**

![Lab 3 workflow — Create an In-Place Mass and Apply Materials](courseware/assets/lg/lab-03.png)

*Lab 3 workflow — Create an In-Place Mass and Apply Materials*

**What you'll build**

An in-place conceptual mass with materials applied by category and by face.   (Tools: Revit · In-Place Mass · Materials Browser · Paint tool.)

**Files for this lab**

- ModelCreation.rvt — in labs/lab-03-create-an-in-place-mass-and-apply-materials/

**Step-by-step**

1. Start an in-place mass and name the new mass family.

   > `Massing & Site ▸ Conceptual Mass ▸ In-Place Mass ▸ name it Tower ▸ OK`

2. Draw a closed profile and create a form from it.

   > `Draw ▸ Rectangle ▸ select the profile ▸ Modify ▸ Create Form ▸ Solid Form`

3. Finish the mass to return to the project environment.

   > `In-Place Editor ▸ Finish Mass`

4. Open the Materials browser and duplicate a material to customise it.

   > `Manage ▸ Settings ▸ Materials ▸ right-click Concrete ▸ Duplicate`

5. Set the material's graphics: shading colour, surface pattern and cut pattern.

   > `Material Editor ▸ Graphics ▸ Shading ▸ choose a colour ▸ OK`

6. Paint the new material onto one face of the mass.

   > `Modify ▸ Geometry ▸ Paint ▸ pick the material ▸ click a face`


**Test it**

The mass displays the painted material on the selected face in a shaded 3D view, and the duplicated material appears in the project's material library.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-03-create-an-in-place-mass-and-apply-materials/.

---


### Lab 4 — Render a Photorealistic View

Learning outcome: produce and visualise 2D/3D technical drawings using Revit (LO1).

Goal: Present the design by producing a photorealistic image of the building model: set the render quality, resolution, lighting and background, then export the image.

**Workflow**

![Lab 4 workflow — Render a Photorealistic View](courseware/assets/lg/lab-04.png)

*Lab 4 workflow — Render a Photorealistic View*

**What you'll build**

A rendered exterior image of the LittleHouse model, exported to the project and saved as a file.   (Tools: Revit · Render dialog · Realistic visual style.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-04-render-a-photorealistic-view/

**Step-by-step**

1. Open LittleHouse.rvt from the lab folder and open the default 3D view.

   > `Quick Access Toolbar ▸ Default 3D View`

2. Preview materials in real time with the Realistic visual style.

   > `View Control Bar ▸ Visual Style ▸ Realistic`

3. Open the Rendering dialog from the View tab.

   > `View ▸ Graphics ▸ Render`

4. Set Quality to Medium and Output to Screen resolution.

   > `Rendering dialog ▸ Quality: Medium ▸ Resolution: Screen`

5. Set the lighting scheme and a sky background, then render.

   > `Lighting: Exterior Sun only ▸ Background: Sky ▸ Render`

6. Adjust exposure if needed, then save the image into the project and export it.

   > `Adjust Exposure ▸ Save to Project ▸ Export ▸ littlehouse-render.png`


**Test it**

A photorealistic rendering of the house appears under Project Browser ▸ Renderings, and the exported PNG opens outside Revit.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-04-render-a-photorealistic-view/.

---


## Topic 02 — Part Lists for Modeling in Revit

Levels & grids · Stacked, basic and curtain walls · Doors & windows · Roofs · Ceilings · Floors & openings · Stairs · Columns

**Key concepts**

- Levels & grids — Levels are datums for each storey or reference height; grids are annotation elements that organise the design — add columns at grid intersections.
- Wall types — Basic walls, stacked walls (two or more subwalls of different thickness) and curtain walls with grids, panels and mullions.
- Doors & windows — Hosted components that automatically cut their opening; press Spacebar to flip the swing before placement.
- Roofs & ceilings — Create roofs by footprint, extrusion, sloped glazing or from a mass; place ceilings automatically inside walls or by sketch.
- Floors & openings — Sketch floor boundaries as closed loops; cut openings By Face, Vertical, or through the full height with the Shaft tool.
- Stairs & railings — Assemble runs, landings, supports and railings in stair assembly edit mode, in plan or 3D views.


### Lab 5 — Create Walls

Learning outcome: create part lists for modeling using Revit (LO2).

Goal: Work on different levels to add the exterior walls, interior partition walls and a corridor to the project, then tidy the joins with the Trim/Extend tool.

**Workflow**

![Lab 5 workflow — Create Walls](courseware/assets/lg/lab-05.png)

*Lab 5 workflow — Create Walls*

**What you'll build**

A building shell with exterior walls, interior walls and a corridor opening on the lower level.   (Tools: Revit · Wall: Architectural · Trim/Extend.)

**Files for this lab**

- ModelCreation.rvt — in labs/lab-05-create-walls/

**Step-by-step**

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


**Test it**

The lower level shows a closed exterior shell with interior partitions and a corridor; walls meet cleanly with no gaps or crossing lines. Compare with ModelCreation.rvt in the lab folder.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-05-create-walls/.

---


### Lab 6 — Place Doors and Windows

Learning outcome: create part lists for modeling using Revit (LO2).

Goal: Load door families into the project, then place interior and exterior doors and windows — flipping swing and orientation with the Spacebar and flip controls.

**Workflow**

![Lab 6 workflow — Place Doors and Windows](courseware/assets/lg/lab-06.png)

*Lab 6 workflow — Place Doors and Windows*

**What you'll build**

A model with doors and windows placed and correctly oriented in the walls, each opening cut automatically.   (Tools: Revit · Door tool · Window tool · Load Family.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-06-place-doors-and-windows/

**Step-by-step**

1. Open the entry-level floor plan and start the Door tool.

   > `Architecture ▸ Build ▸ Door`

2. Load additional door families from the library.

   > `Modify | Place Door ▸ Mode ▸ Load Family ▸ Doors ▸ choose an entrance door`

3. Enable tagging on placement so each door is numbered automatically.

   > `Modify | Place Door ▸ Tag ▸ Tag on Placement`

4. Hover over a wall, press Spacebar to flip the swing, then click to place the door.

   > `Spacebar to flip ▸ click to place`

5. Place windows on the exterior walls with the Window tool.

   > `Architecture ▸ Build ▸ Window ▸ click the exterior walls`

6. Fix any wrongly-placed component with the blue flip-control arrows.

   > `Select the door/window ▸ click the flip arrows`


**Test it**

Every door and window sits in a wall with its opening cut automatically, tags show sequential numbers, and all swings open the intended way.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-06-place-doors-and-windows/.

---


### Lab 7 — Create a Floor and a Roof by Footprint

Learning outcome: create part lists for modeling using Revit (LO2).

Goal: Create a mezzanine floor by sketching its boundary, edit the sketch with Align and Trim into a closed loop, then complete the envelope with a footprint roof whose slopes you define.

**Workflow**

![Lab 7 workflow — Create a Floor and a Roof by Footprint](courseware/assets/lg/lab-07.png)

*Lab 7 workflow — Create a Floor and a Roof by Footprint*

**What you'll build**

A mezzanine floor in the store-room area and a sloped roof closing the building envelope.   (Tools: Revit · Floor: Architectural · Roof by Footprint · Shaft Opening.)

**Files for this lab**

- ModelCreation.rvt — in labs/lab-07-create-a-floor-and-a-roof-by-footprint/

**Step-by-step**

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


**Test it**

The mezzanine floor appears with a clean shaft opening, and the 3D view shows a sloped roof sitting on the footprint — no warnings about open loops.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-07-create-a-floor-and-a-roof-by-footprint/.

---


### Lab 8 — Create Stairs and Railings

Learning outcome: create part lists for modeling using Revit (LO2).

Goal: Complete the interior by adding a staircase from the store floor to the mezzanine, then modify the mezzanine railing and change its type to a pipe railing.

**Workflow**

![Lab 8 workflow — Create Stairs and Railings](courseware/assets/lg/lab-08.png)

*Lab 8 workflow — Create Stairs and Railings*

**What you'll build**

A staircase connecting the store floor to the mezzanine, with a matching pipe railing on the mezzanine edge.   (Tools: Revit · Stair tool · Railing tool.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-08-create-stairs-and-railings/

**Step-by-step**

1. Open the lower-level plan and start the Stair tool.

   > `Architecture ▸ Circulation ▸ Stair`

2. Set the base and top levels for the run in the Properties palette.

   > `Properties ▸ Base Level: 01 ▸ Top Level: Mezzanine`

3. Choose the railing type to generate with the stair.

   > `Modify | Create Stair ▸ Tools ▸ Railing ▸ pick a type`

4. Draw the run: click the start point, move up-screen, click the end point.

   > `Components ▸ Run ▸ Straight ▸ click start ▸ click end`

5. Finish the stair and inspect it in 3D.

   > `✓ Finish Edit Mode ▸ Default 3D View`

6. Select the mezzanine railing and change it to a pipe railing type.

   > `Select railing ▸ Type Selector ▸ Railing: Pipe`


**Test it**

The 3D view shows a complete stair with railings from the store floor to the mezzanine, and the mezzanine edge railing is the pipe type.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-08-create-stairs-and-railings/.

---


## Topic 03 — Model Documentation

Dimensions · Rooms · Area plans · Furniture plans · Color fill legends · Dependent views · Object styles · Callout & section views

**Key concepts**

- Dimensions — Temporary dimensions appear while placing; permanent dimensions (aligned, linear, angular, radial, arc length) document the design and print on sheets.
- Rooms — Rooms are subdivisions bounded by walls, floors, roofs and ceilings; Revit computes perimeter, area and volume, and room separation lines subdivide open space.
- Area plans — Area schemes and boundary lines measure gross/rentable areas per level, created from the Room & Area panel.
- Color fill legends — Color schemes paint rooms or areas in plan views; the legend provides the key and is edited from the Scheme panel.
- Views for a purpose — Duplicate (with detailing / as dependent) to make furniture plans, callouts of wall details and building sections.
- Object styles & visibility — Object Styles set project-wide line weight, colour, pattern and material per category; Visibility/Graphics overrides them per view.


### Lab 9 — Add Dimensions to the Model

Learning outcome: assist in design prototyping and create design documentation (LO3).

Goal: Dimension the footprint of the main building: overall widths, then aligned dimension strings that automatically pick up grid intersections and window openings on the exterior walls.

**Workflow**

![Lab 9 workflow — Add Dimensions to the Model](courseware/assets/lg/lab-09.png)

*Lab 9 workflow — Add Dimensions to the Model*

**What you'll build**

A dimensioned floor plan documenting the building footprint, grids and openings.   (Tools: Revit · Aligned Dimension · Linear Dimension.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-09-add-dimensions-to-the-model/

**Step-by-step**

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


**Test it**

The plan shows an overall dimension plus a string that lists every grid intersection and window centre along the exterior wall — values update if a window is moved.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-09-add-dimensions-to-the-model/.

---


### Lab 10 — Create Rooms, an Area Plan and a Color Fill Legend

Learning outcome: assist in design prototyping and create design documentation (LO3).

Goal: Subdivide the model into rooms, create an area plan for the level, then colour the plan with a colour scheme and place its legend as the key.

**Workflow**

![Lab 10 workflow — Create Rooms, an Area Plan and a Color Fill Legend](courseware/assets/lg/lab-10.png)

*Lab 10 workflow — Create Rooms, an Area Plan and a Color Fill Legend*

**What you'll build**

A room-tagged plan, a gross-area plan and a colour-filled plan with legend.   (Tools: Revit · Room tool · Area Plan · Color Fill Legend.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-10-create-rooms-an-area-plan-and-a-color-fill-legend/

**Step-by-step**

1. Place rooms in every enclosed space on the entry level.

   > `Architecture ▸ Room & Area ▸ Room ▸ click inside each space`

2. Rename the rooms by editing their tags.

   > `Double-click a room tag ▸ type the name ▸ Enter`

3. Create an area plan for the entry level, letting Revit add the boundary lines.

   > `Architecture ▸ Room & Area ▸ Area ▸ Area Plan ▸ Level 01 ▸ Yes`

4. Place a colour fill legend beside the plan.

   > `Annotate ▸ Color Fill ▸ Legend ▸ click in the drawing area`

5. Choose the space type and colour scheme for the legend.

   > `Choose Space Type: Rooms ▸ Color Scheme: Name ▸ OK`

6. Edit the scheme to colour by department or by name.

   > `Select legend ▸ Edit Scheme ▸ pick a scheme ▸ OK`


**Test it**

Every space carries a named room tag, the area plan reports the level's areas, and the plan is colour-filled with a legend that matches the scheme.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-10-create-rooms-an-area-plan-and-a-color-fill-legend/.

---


### Lab 11 — Create Section, Callout and Dependent Views

Learning outcome: assist in design prototyping and create design documentation (LO3).

Goal: Create a building section through the model, a callout view of the exterior wall, and a detail callout of the parapet; then duplicate a plan as a dependent view and as a furniture plan.

**Workflow**

![Lab 11 workflow — Create Section, Callout and Dependent Views](courseware/assets/lg/lab-11.png)

*Lab 11 workflow — Create Section, Callout and Dependent Views*

**What you'll build**

A section view, wall-section callout, detail callout and purpose-made duplicate views.   (Tools: Revit · Section tool · Callout tool · Duplicate View.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-11-create-section-callout-and-dependent-views/

**Step-by-step**

1. Draw a building section through the model from the entry-level plan.

   > `View ▸ Create ▸ Section ▸ click start ▸ click end`

2. Resize the crop region and flip the view direction if needed, then open the section.

   > `Drag the blue controls ▸ double-click the section head`

3. Create a wall-section callout of the exterior wall in the section view.

   > `View ▸ Create ▸ Callout ▸ Rectangle ▸ drag around the wall`

4. Create a detail callout of the parapet inside the wall section.

   > `View ▸ Create ▸ Callout ▸ Detail ▸ drag around the parapet`

5. Duplicate the entry-level plan as a dependent view and crop it to one wing.

   > `Project Browser ▸ right-click plan ▸ Duplicate View ▸ Duplicate as Dependent`

6. Duplicate with detailing to make a furniture plan, half-toning the model categories.

   > `Duplicate with Detailing ▸ Visibility/Graphics ▸ Halftone`


**Test it**

The Project Browser shows the section, the two callouts and the dependent/furniture views; each callout head links to its enlarged view.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-11-create-section-callout-and-dependent-views/.

---


## Topic 04 — Design Specification

System, loadable & in-place families · Type catalogs · Detail components · Schedules · Drawing sheets · Worksharing · CAD links · Project management

**Key concepts**

- Three kinds of families — System families (walls, roofs, floors), loadable families (doors, windows, furniture, title blocks — RFA files) and in-place families for one-off elements.
- Type catalogs — Load only the family types you need to keep the project small and the Type Selector short.
- Schedules — Schedule/Quantities lists building components; choose fields, filter, sort, group and format — the schedule is live model data.
- Drawing sheets — A construction document set is composed of sheets; each placed view becomes a viewport with a title block, then print or export to PDF.
- Worksharing — Team members share a central model and work simultaneously in local copies organised by worksets.
- Link & import CAD — Link or import DWG/DXF data, acquire or publish shared coordinates, audit the model and transfer project standards.


### Lab 12 — Families, Tags, a Schedule and Drawing Sheets

Learning outcome: produce design specification using Revit (LO4).

Goal: Load the door, window and wall tag families supplied in the lab folder, tag the model, build a door schedule, then compose a titled drawing sheet with plan, section and schedule — the deliverable construction document.

**Workflow**

![Lab 12 workflow — Families, Tags, a Schedule and Drawing Sheets](courseware/assets/lg/lab-12.png)

*Lab 12 workflow — Families, Tags, a Schedule and Drawing Sheets*

**What you'll build**

A construction-document sheet with title block carrying the plan, a section, tags and a live door schedule.   (Tools: Revit · Load Family · Tag by Category · Schedule/Quantities · Sheet.)

**Files for this lab**

- LittleHouse.rvt — in labs/lab-12-families-tags-a-schedule-and-drawing-sheets/
- Door Tag FR.rfa — in labs/lab-12-families-tags-a-schedule-and-drawing-sheets/
- Window Tag.rfa — in labs/lab-12-families-tags-a-schedule-and-drawing-sheets/
- Wall tag.rfa — in labs/lab-12-families-tags-a-schedule-and-drawing-sheets/

**Step-by-step**

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


**Test it**

Sheet A101 shows the plan, section and door schedule inside the title block; the schedule updates live when a door type changes, and the exported PDF matches the sheet.

> **Note:** This lab's instructions, PDF and Revit file(s) are in labs/lab-12-families-tags-a-schedule-and-drawing-sheets/.

---


## Consolidating Your Skills

- First pass: complete every lab in Revit, comparing your result with the Test-it check.
- Second pass: redo the labs from memory until the ribbon paths and workflows are automatic.
- Review the Key Concepts of each topic to consolidate the theory behind each lab.
- Practise end-to-end: model, document and specify a small building in Revit, drawing on the labs.
- Sharpen your readiness with the practice exams at https://exams.tertiaryinfotech.com.


## Glossary

- **BIM** — Building Information Modeling — a single coordinated virtual building model that drives every drawing, view and schedule.
- **Parametric change engine** — Revit's coordination mechanism: a change made anywhere updates every view, sheet and schedule.
- **Level** — A horizontal datum plane for a storey or reference height (e.g. sill level); floor plans attach to levels.
- **Grid** — An annotation datum used to organise the design; columns can be placed at grid intersections.
- **Toposurface** — A topographical surface defined by points or imported data, used for site modeling.
- **Building pad** — A flat pad sketched on a toposurface that cuts the terrain to level ground for the building.
- **Mass** — A conceptual volume (family-based or in-place) used for early design studies; can generate walls, floors and roofs.
- **Family** — A group of elements with a common set of properties: system families, loadable families (RFA) and in-place families.
- **Type / Instance** — A type defines shared parameters for all its elements; an instance carries the parameters of one placed element.
- **Curtain wall** — A wall type made of panels, curtain grids and mullions.
- **Callout view** — An enlarged view of part of a parent view, linked by the callout tag.
- **Section view** — A view that cuts through the model along a drawn section line.
- **Dependent view** — A duplicate view that stays synchronised with its primary view — used to split a large plan across sheets.
- **Room** — A subdivision of space bounded by room-bounding elements; Revit computes its perimeter, area and volume.
- **Schedule** — A live tabular view of model data (e.g. a door schedule) created with Schedule/Quantities.
- **Sheet** — A drawing sheet with a title block; placed views become viewports and form the construction document set.
- **Workset** — A subdivision of a workshared project that lets team members edit a central model simultaneously.
- **RVT / RFA / RTE** — Revit file types: project, loadable family and project template respectively.

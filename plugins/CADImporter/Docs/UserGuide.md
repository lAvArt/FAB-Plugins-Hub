# CAD 2D Importer - User Guide

Version 1.1.0. Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8.

## 1. Introduction

CAD 2D Importer brings 2D vector drawings into Unreal Engine as native spline actors. It suits architectural floor plans, site plans, paths and reference lines. A 3D toolbox turns splines into simple walls and converts them to static meshes.

It is a 2D importer. It does not read 3D CAD formats (DWG, STEP, IFC, Revit); use Datasmith for those.

### What it reads

- **DXF (ASCII)**, entities:
  - LINE
  - LWPOLYLINE (bulge arcs are tessellated)
  - POLYLINE (2D; the vertices' Z is not read)
  - CIRCLE and ARC (tessellated: a circle in 32 segments, an arc in 32 segments however short its sweep)
  - SPLINE with fit points
  - 3DFACE (gathered into one outline actor per layer)
- **JSON** in the plugin's own format, written by the plugin ("Export to JSON") or by the included 3ds Max, Blender and Cinema 4D scripts (see section 7).

### What it does not read

- DWG (save as DXF from your CAD application), binary DXF.
- Block references (INSERT): blocks placed in the drawing are not expanded. Entities inside block definitions are read as if they were drawing geometry, at their block-local coordinates. Explode blocks before exporting if you need them.
- SPLINE entities defined only by control points (NURBS without fit points): skipped with a warning. Export them as polylines.
- POLYLINE polyface meshes: skipped with a warning.
- TEXT, MTEXT, HATCH, DIMENSION, ELLIPSE, POINT, SOLID and other entity types.
- Layers whose name starts with ASHADE (shading helpers) are always dropped.

## 2. Installation

1. Install the plugin from Fab, or place the `CADImporter` folder in your project's `Plugins` folder.
2. Open the project, go to **Edit > Plugins** and make sure **CAD 2D Importer** is enabled. It enables the engine's **Procedural Mesh Component** plugin, which it needs.
3. Restart the editor if prompted.

## 3. Importing a file

1. Open **Tools > CAD 2D Importer** (in the CAD Tools section of the Tools menu). The importer opens in its own window.
2. Under **Import New > Import File**, click **Import File** and pick a `.dxf` or `.json` file. The file is read at once; nothing is placed in the level yet. Reader warnings (skipped entities) appear as notifications.
3. Choose the **Units** the drawing was made in: mm, cm, m, in or ft. The import button stays disabled until you choose. The dialog does not read the units from the file. (The AI tools do: see the AI Assistant Guide.)
4. **Settings**:
   - **Scale**: an extra factor on top of the units.
   - **Z Offset**: the height the drawing is placed at, in cm.
5. Choose the layers (section 4), then click **Import Selected Layers**.

If actors from the same file are already in the level, the importer asks:

- **Yes** replaces them;
- **No** imports a second copy alongside;
- **Cancel** stops.

The import is one undo step (Ctrl+Z).

### Units

Unreal works in centimetres. The importer scales by the unit you pick: mm x0.1, cm x1, m x100, in x2.54, ft x30.48, then by **Scale**. A plan drawn in millimetres but imported as metres comes out 1000 times too large.

## 4. Layers

After loading a file the **Layers** list shows every layer:

- **Checkbox**: include or leave out the layer. **Select All**, **Deselect All** and **Invert** act on the whole list.
- **Colour**: the spline colour for the layer.
- **Count**: the number of entities on the layer.

Tip: leave out dimension, text and hatch layers to keep the level clean.

## 5. What the import creates

- One actor with a spline component per entity. 3DFACEs are the exception: they become one actor per layer with an outline spline per face.
- Actors are labelled `CI_<Layer>_<Type>_<id>` and placed in the outliner under `CAD/<file name>/<layer>`.
- Every actor is tagged:
  - `CAD_Import`;
  - `CAD_Source_<hash>`, which identifies the file;
  - `CAD_Layer_<layer>`.

## 6. Managing imports

The **Management > Imported CAD** section lists every import in the level. For each one you can:

- rename it (the outliner folder follows);
- show or hide it;
- frame it in the viewport;
- select its actors;
- delete it.

Per layer you can:

- change the spline colour (Shift+click copies the hex value, Alt+click pastes one);
- assign a material, used when walls are generated from that layer;
- select the layer's actors.

At the top of the section:

- **Select by Layer** selects a layer across all imports;
- **Delete All** removes every imported CAD actor;
- the eye icon toggles the visibility of all of them.

**Export to JSON** writes the drawing currently loaded in the dialog to a JSON file.

## 7. 3D Tools

Click the arrow at the right edge of the window to open the **3D Tools** panel.

### Settings

- **Wall Height** (cm, default 300).
- **Weld Threshold** (cm, default 1): points along a spline closer than this are merged. With **Close Loop** on, an open spline whose two ends are within the threshold is closed. It does not join separate splines.
- **Smoothing Angle** (degrees, default 60), used by **Smooth**.
- **Cap Holes on Generate**: closed outlines get a top and a bottom cap.
- **Process Only Selected**: on, the tools use the selected actors. Off, **Extrude** uses every imported CAD actor in the level.
- **Auto Reverse Normals**: builds the walls facing the other way.

### Actions

- **Extrude**: turns each spline into a wall: a single surface of the given height along the spline (no thickness), as a procedural mesh actor in a `Walls` subfolder of its layer. It uses the layer's material, or the default material.
- **Reverse Normals**, **Cap Holes**, **Smooth**: act on selected wall (procedural mesh) actors.
- **Material Override** and **Convert To Static Mesh**: turn the selected walls into static mesh assets, then replace the walls with static mesh actors in the folder `CAD/CI_StaticMeshes`.
  - The assets go to `/Game/CI_StaticMeshes/`. An existing asset of the same name is overwritten.
  - The conversion recomputes normals and tangents and generates lightmap UVs.
  - The assets are not saved until you save them (File > Save All).

## 8. JSON from 3ds Max, Blender and Cinema 4D

The `Extras` folder of the plugin holds three exporter scripts; `Extras/README.md` explains each.

- 3ds Max: `Extras/3dsmax/export_cad_json_3dsmax.py`
- Blender: `Extras/blender/export_cad_json_blender.py`
- Cinema 4D: `Extras/c4d/export_cad_json_c4d.py`

Export the shapes to a `.json` file, then import it like a DXF.

## 9. AI assistant (optional, beta)

Since 1.1.0 an AI assistant can drive the importer through MCP. This part is optional and editor-only. See [AI_ASSISTANT_GUIDE.md](AI_ASSISTANT_GUIDE.md).

## 10. Troubleshooting

- **The drawing is huge or tiny**: wrong units. Delete the import and import again with the right unit.
- **Walls have gaps**: the weld threshold only merges points along one spline and closes a spline whose ends meet. Lines that do not touch in the drawing stay separate: fix them in the CAD application, or join them into polylines.
- **Walls are black or invisible from one side**: walls are single-sided surfaces. Use **Reverse Normals** on them, or a two-sided material.
- **Missing furniture or symbols**: they were block references (INSERT), which are not expanded. Explode the blocks before exporting.
- **Text or hatching missing**: these entity types are not imported.

More answers: [FAQ.md](FAQ.md).

---
*Support: [GitHub](https://github.com/lAvArt/FAB-Plugins-Hub) | Copyright 2026 lAvArt Studio*

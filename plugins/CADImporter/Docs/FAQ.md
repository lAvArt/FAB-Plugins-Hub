# CAD 2D Importer - FAQ

## Files and formats

**Does it read DWG?**
No. DWG is a proprietary format. Save the drawing as DXF (ASCII) from AutoCAD, Revit, Rhino or your CAD application.

**Can it import 3D models?**
No. The plugin is for 2D vector drawings: floor plans, site plans, schematics. For 3D CAD and BIM use Datasmith, or FBX for meshes.

**Which DXF entities are imported?**

- LINE
- LWPOLYLINE, including bulge arcs
- 2D POLYLINE
- CIRCLE and ARC
- SPLINE with fit points
- 3DFACE

The [User Guide](UserGuide.md) lists the details.

**What is not imported?**

- Block references (INSERT): blocks are not expanded. Entities inside block definitions are read as geometry at their block-local coordinates, so stray pieces can appear near the origin.
- SPLINE entities with only control points (NURBS): skipped, with a warning.
- POLYLINE polyface meshes: skipped, with a warning.
- TEXT, MTEXT, HATCH, DIMENSION, ELLIPSE, POINT, SOLID.
- ASHADE layers.
- Binary DXF.

**Why are furniture, doors or symbols missing?**
They are almost always block references (INSERT), which are not expanded. Explode the blocks in your CAD application before exporting the DXF.

**Do arcs and circles look smooth?**
Circles and arcs are tessellated into 32 segments each (an arc gets 32 however short its sweep) and use curved spline interpolation. Bulge arcs inside polylines get 8 points per arc; polylines use straight segments.

## Units

**How does the importer know the units?**

- **Import dialog:** you choose the unit (mm, cm, m, in, ft). The import button stays disabled until you do. The dialog does not read units from the file.
- **AI tools:** `import_inspect` reads the DXF header variable `$INSUNITS` and reports it with a confidence. When the file declares nothing, it suggests a unit from the drawing's size. `import_file` uses the declared unit when you do not give one, and refuses when the file declares none.

**My drawing is 1000 times too big or too small.**
The unit was wrong (for example a plan in millimetres imported as metres). Delete the import (or replace it) and import again with the right unit.

## The 3D toolbox

**Do walls have a thickness?**
No. Extrude makes a single surface of the chosen height along each spline. **Cap Holes on Generate** closes the top and bottom of closed outlines.

**Does the plugin generate collision?**
The import and the wall tools do not add collision.

- **Convert To Static Mesh** makes ordinary static mesh assets. They use Unreal's default collision settings.
- The AI tool `cleanup_set_collision` can set collision on the converted meshes: on or off, complexity, or a box.

**Why are my walls black or invisible from one side?**
Walls are single-sided. Use **Reverse Normals** (or the AI tool `model_fix_normals`), or a two-sided material. **Convert To Static Mesh** also generates lightmap UVs for baked lighting.

**Walls have gaps.**
**Weld Threshold** merges points along one spline and, with **Close Loop**, closes a spline whose two ends meet. It does not join separate lines. Join them into polylines in the CAD application.

## AI assistant (MCP)

**What is MCP, and do I need it?**
MCP (Model Context Protocol) is an open protocol that lets an AI assistant call tools. Since 1.1.0 the plugin can serve its import, layer, wall, cleanup and viewport tools over MCP, so an assistant can prepare drawings for you.

It is optional, editor-only and in beta. You do not need it: the import dialog and the 3D toolbox work as before.

**Does the plugin send my data anywhere?**
The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

**Which assistants work?**
Claude Code (the plugin ships a ready Claude Code plugin pack), and any client that speaks MCP over Streamable HTTP with a bearer-token header.

**How do I connect?**

1. Open the project in the editor.
2. Run `CAD.Mcp` in the Output Log. It prints:
   - the endpoint, `http://127.0.0.1:47920/mcp` (or the next free port up to 47929);
   - a ready `claude mcp add ...` command with the token.
3. Settings are in **Project Settings > Plugins > CAD Importer MCP**.

The [AI Assistant Guide](AI_ASSISTANT_GUIDE.md) has the details.

**Is it safe? Can I undo what the assistant does?**

- Every tool that changes the level is one undo step (Ctrl+Z). These tools are marked as changing something, so a client can ask you first.
- The tools that delete or merge actors are marked destructive.
- Assets created by conversions and merges are not removed by undo. They stay unsaved until you save.
- The tools read files only inside the project folder.

**Why does `import_file` refuse to import a file a second time?**
To avoid silent duplicates. When actors from the same file are already in the level, it stops and tells you how many there are. Ask the assistant to replace them (`replaceExisting`) or to add a second copy (`allowDuplicate`). This is the same choice the dialog asks for.

**Does it work during Play-In-Editor?**
No. The tools work on the editor level and refuse while a Play session runs.

## Engines and platforms

**Which engine versions are supported?**
1.1.0 is built and tested on Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8.

**Which platforms?**
The importer, its dialog and the AI interface exist only in the editor; CADCore (data types and the spawn service) is a runtime module. The descriptor allows Windows, Mac and Linux. It has been compiled and tested on Windows.

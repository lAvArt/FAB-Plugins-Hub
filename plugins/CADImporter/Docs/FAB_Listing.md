# FAB Listing Details

## Short Description
Import 2D CAD drawings (DXF, JSON) into Unreal Engine as clean native Splines. Includes Layer support, Unit conversion, and tools to generate 3D Walls and Floors directly from plans.

## Long Description
**CAD 2D Importer** is the ultimate workflow accelerator for ArchViz, Engineering, and Simulation projects. Stop wasting time manually tracing spline references or dealing with messy "Datasmith" imports for simple 2D plans. 

This plugin reads standard **DXF** (AutoCAD) files and our custom **JSON** schema (3ds Max Exporter included!) and converts them into **Unreal Engine Spline Actors**, organized neatly by Layer.

### Key Features:
*   **DXF Support**: Imports Lines, Polylines, Circles, Arcs, and Splines (NURBS).
*   **Layer System**: Preserves CAD layers, allowing you to select, hide, or colorize groups of splines instantly.
*   **Smart Unit Conversion**: Automatically detects unit setup (mm, cm, m, in, ft) or allows manual override.
*   **3ds Max Integration**: Includes a Python script (`export_cad_json.py`) to export shapes from 3ds Max with 1:1 fidelity.
*   **3D Building Tools**:
    *   **Generate Walls**: Extrude selected splines into 3D walls with adjustable height and thickness.
    *   **Weld Seams**: Automatically merge disconnected vertices with a configurable threshold.
    *   **Mesh Operations**: Clean normals, generate tangents, and collision.

### Workflow
1.  **Import**: Select your `.dxf` or `.json` file.
2.  **Review**: See a preview of layers, toggle visibility, and set colors.
3.  **Spawn**: Click to generate Spline Actors in your level.
4.  **Build**: Use the built-in "3D Toolbox" to extrude walls or floors from your splines.

## Technical Information

Features:

*   **Direct DXF & JSON Import**: Import CAD drawings as native Unreal Splines, preserving Layers and Units.
*   **3D Building Tools**: Generate clean 3D Walls and Floors directly from 2D plans with extrusion and welding.
*   **Batch Processing**: Organize, select, and process actors by Layer for rapid iteration.

Code Modules:

*   **CADCore** (Runtime)
*   **CADIO** (Editor)
*   **CADEditor** (Editor)

Required Plugins:
*   **ProceduralMeshComponent** (Built-in)

Number of Blueprints: 0
Number of C++ Classes: 15+
Network Replicated: No
Supported Development Platforms:
*   Windows: Yes
*   Mac: Yes
Supported Target Build Platforms: Windows, Mac, Linux
Documentation Link: https://github.com/lAvArt/CADImporter/blob/main/Plugins/CADImporter/Docs/UserGuide.md
Example Project: N/A

Important/Additional Notes:
NURBS Splines are tessellated into Polylines during import for maximum compatibility and performance.

## FAQ

**Q: Does this support DWG?**
A: No, DWG is a proprietary format. Please save your file as **DXF** (2010 or newer) from AutoCAD, Revit, or Rhino.

**Q: Can I import 3D meshes with this?**
A: No, this plugin is specialized for **2D vector lines** (Floor plans, schematics). For 3D meshes, use Datasmith or FBX.

**Q: The generated lines look jagged?**
A: The plugin respects the resolution of the source data. For NURBS Splines, we tessellate them into smooth Polylines during import.

**Q: Why are my walls black (no lighting)?**
A: Ensure you have "Generate Lightmap UVs" enabled if using baking, or use the "Fix Normals" tool in our 3D Toolbox to ensure valid tangent data is generated.

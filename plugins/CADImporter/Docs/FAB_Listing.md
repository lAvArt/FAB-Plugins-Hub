# FAB Listing Details

Version 1.1.0. Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8.

## Short Description

Import 2D CAD drawings (DXF, JSON) into Unreal Engine as native spline actors organised by layer, extrude them into simple walls, and convert those to static meshes. Optional AI assistant tools (MCP, beta).

## Long Description

**CAD 2D Importer** brings 2D vector drawings into Unreal Engine for architectural visualisation, site layouts and reference lines. Each DXF entity becomes a spline actor, grouped by layer in the outliner and tagged with its source file and layer, so a whole layer can be selected, recoloured, hidden or processed at once.

It reads ASCII **DXF** files and the plugin's own **JSON** format. Exporter scripts for 3ds Max, Blender and Cinema 4D are included.

### Key Features

* **DXF import**: LINE, LWPOLYLINE (with bulge arcs), 2D POLYLINE, CIRCLE, ARC, SPLINE (fit points) and 3DFACE.
* **Layers**: choose which layers to import, set their colours, and select, hide, recolour or assign a material to a layer after import.
* **Units**: choose mm, cm, m, in or ft when importing (plus an extra scale and a Z offset). The AI tools also read the DXF `$INSUNITS` header and report it.
* **Re-import handling**: importing the same file again offers replace, duplicate or cancel.
* **3D toolbox**:
  * **Extrude**: turn splines into walls of a chosen height (single surfaces, no thickness). Closed outlines can be capped top and bottom.
  * **Weld threshold**: merge near-duplicate points along a spline and close splines whose ends meet.
  * **Reverse Normals**, **Cap Holes**, **Smooth**.
  * **Convert To Static Mesh**: bake walls into static mesh assets, with normals and tangents recomputed and lightmap UVs generated.
* **DCC exporters**: `export_cad_json_3dsmax.py`, `export_cad_json_blender.py` and `export_cad_json_c4d.py` in the `Extras` folder.
* **AI assistant tools (new in 1.1.0, optional, editor-only, beta)**: an assistant connected over MCP can:
  * inspect a drawing before importing it;
  * import it with explicit options;
  * manage layers and generate walls;
  * clean up the scene (duplicates, labels, pivots, merging per layer, collision and Nanite on converted meshes);
  * check the result with a viewport screenshot.

### Not supported

* DWG, binary DXF, and 3D CAD formats.
* Block references (INSERT) are not expanded.
* POLYFACE meshes and NURBS splines without fit points (both skipped, with a warning).
* TEXT, MTEXT, HATCH, DIMENSION, ELLIPSE.

### Workflow

1. **Open**: Tools > CAD 2D Importer, then Import File (.dxf or .json).
2. **Review**: pick the units, tick the layers, set colours.
3. **Import**: Import Selected Layers spawns the spline actors.
4. **Build**: open the 3D Tools panel to extrude walls and convert them to static meshes.

### Privacy and safety

The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

## Technical Information

* **Features**: DXF and JSON import as spline actors by layer; per-layer colour, visibility and material; wall extrusion; static mesh conversion; DCC exporter scripts; optional MCP tools for AI assistants.
* **Code Modules**:
  * CADCore (Runtime)
  * CADIO (Editor)
  * CADEditor (Editor)
  * CADMcp (Editor)
  * CADMcpEditor (Editor)
* **Required Plugins**: Procedural Mesh Component (engine plugin, enabled automatically)
* **Number of Blueprints**: 0
* **Input**: Editor UI (mouse and keyboard). No runtime input.
* **Network Replicated**: No
* **Supported Development Platforms**:
  * Windows: Yes
  * Mac: Yes (allowed by the descriptor; built and tested on Windows only)
* **Supported Engine Versions**: 5.3, 5.4, 5.5, 5.6, 5.7, 5.8
* **Documentation Link**: <https://github.com/lAvArt/FAB-Plugins-Hub/blob/main/plugins/CADImporter/Docs/UserGuide.md>
* **Important/Additional Notes**:
  * The importer, its dialog and the AI interface exist only in the editor; CADCore (data types and the spawn service) is a runtime module.
  * The AI assistant layer is optional, editor-only and in beta, and contains no AI service.
  * Parts of the 1.1.0 AI assistant layer (MCP server, tools, automated tests and documentation) were developed with AI assistance (Claude, by Anthropic) and reviewed by lAvArt Studio.

## Documentation

* [User Guide](UserGuide.md)
* [FAQ](FAQ.md)
* [AI Assistant Guide](AI_ASSISTANT_GUIDE.md)

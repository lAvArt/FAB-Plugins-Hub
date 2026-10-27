# CAD 2D Importer

![Banner](Resources/Banner.png)

**Bring 2D CAD drawings into Unreal Engine as native splines, and turn them into simple 3D walls.**

CAD 2D Importer imports ASCII **DXF** files and the plugin's own **JSON** format into Unreal Engine as spline actors, organised by layer. It is for architects, level designers and visualisation artists who need precise reference lines, or want walls extruded from floor plans.

Version 1.1.0. Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8.

## 🚀 Key Features

* **DXF and JSON import**: LINE, LWPOLYLINE (with bulge arcs), 2D POLYLINE, CIRCLE, ARC, SPLINE (fit points) and 3DFACE. One spline actor per entity, grouped under `CAD/<file>/<layer>` and tagged with its source and layer.
* **Layer system**: choose layers before importing. After import, colour, hide, select or assign a material per layer.
* **Units**: choose mm, cm, m, in or ft when importing, plus a scale factor and a Z offset.
* **3D generation tools**:
  * **Extrude walls**: single-surface walls of a chosen height from splines, with optional caps on closed outlines.
  * **Weld threshold**: merges near-duplicate points along a spline and closes splines whose ends meet.
  * **Reverse Normals, Cap Holes, Smooth.**
  * **Static mesh conversion**: bakes walls into static mesh assets.
* **DCC exporters**: scripts for 3ds Max, Blender and Cinema 4D write the JSON format ([Extras](Extras/README.md)).

**Not supported:**

* DWG, binary DXF and 3D CAD formats.
* Block references (INSERT), which are not expanded.
* POLYFACE meshes and NURBS splines without fit points.
* TEXT, HATCH, DIMENSION.

## 🤖 AI Assistant (MCP, beta)

Optional and editor-only. Connect an AI assistant such as Claude Code to the editor and ask it to prepare your drawings:

* **Inspect before importing**, without touching the level: units read from the DXF header with a confidence, size, layers, entity counts, and what the importer cannot read.
* **Import with explicit options**: units, scale, layers, materials and re-centring. A second import of the same file is refused unless you say replace or duplicate.
* **Prepare and clean**: generate walls, fix normals, cap holes, convert to static meshes, remove duplicates, rename by rule, set pivots, merge by layer, set collision and Nanite on converted meshes.
* **Check its own work**: it can frame the viewport and take a screenshot.

The plugin never calls an AI service and never sends your project anywhere. The MCP server exists only in the editor session; it is loopback-only and token-protected, and changes are undoable.

To set it up, run `CAD.Mcp` in the Output Log, then follow the [AI Assistant Guide](Docs/AI_ASSISTANT_GUIDE.md). The tool reference is in `Resources/Agent/TOOLS.md` inside the installed plugin.

## 🖼️ Screenshots

![CAD 2D Importer](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Cover.jpg)

### Import DXF and JSON

![Import DXF and JSON](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_01_import.png)

### Layer system

![Layer system](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_02_layers.png)

### Spline actors by layer

![Spline actors by layer](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_03_plan.png)

### 3D generation tools

![3D generation tools](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_04_walls.png)

### Walls that light correctly

![Walls that light correctly](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_05_walls_lit.png)

### Several drawings, several levels

![Several drawings, several levels](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_06_storeys.png)

### AI assistant: inspect before you import

![AI assistant: inspect before you import](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_07_ai_inspect.png)

### AI assistant: scene hygiene report

![AI assistant: scene hygiene report](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_08_ai_report.png)

### AI assistant (MCP) settings

![AI assistant (MCP) settings](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/CADImporter/Resources/Gallery/cad_gallery_09_mcp_settings.png)

## 📦 Installation

1. Copy the `CADImporter` folder into your project's `Plugins/` directory, or install it from Fab.
2. Enable the plugin in **Edit > Plugins > CAD 2D Importer**. It also enables the engine's Procedural Mesh Component plugin.
3. Restart the editor.

## 📖 Documentation

* [User Guide](Docs/UserGuide.md)
* [FAQ](Docs/FAQ.md)
* [AI Assistant Guide](Docs/AI_ASSISTANT_GUIDE.md)
* [FAB Listing Info](Docs/FAB_Listing.md)
* [Changelog](CHANGELOG.md)

## 🎮 Quick Start

1. Open **Tools > CAD 2D Importer**.
2. Click **Import File** and pick a `.dxf` or `.json` file.
3. Choose the drawing's units and the layers you want.
4. Click **Import Selected Layers**.
5. (Optional) Open the **3D Tools** panel, select the wall splines and click **Extrude**.

## 🔧 Technical Support

* **Engine versions**: 5.3, 5.4, 5.5, 5.6, 5.7, 5.8.
* **Platforms**: Windows (built and tested). The descriptor also allows Mac and Linux.
* **Required plugins**: Procedural Mesh Component (engine plugin).
* **Support**: [GitHub Issues](https://github.com/lAvArt/CADImporter/issues) or `contact@lavartstudio.com`

---
*Created by [lAvArt Studio](https://www.lavartstudio.com)*

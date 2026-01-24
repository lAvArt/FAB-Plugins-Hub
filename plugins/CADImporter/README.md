![Banner](Resources/Banner.png)

**Transform 2D CAD drawings into native Unreal Engine Splines and 3D Geometry.**

This plugin provides a robust pipeline for importing AutoCAD **DXF** and generic **JSON** spline data into Unreal Engine. It is designed for Architects, Level Designers, and Visualization specialists who need precise reference lines or want to auto-generate walls from floor plans.

## 🚀 Key Features

*   **Import DXF & JSON**: Full support for Lines, Polylines, Arcs, Circles, and Splines.
*   **Layer System**: Retain layer names, visibility, and colors from your CAD file.
*   **Precise Scaling**: Automatic unit conversion (mm, cm, m, inch, ft).
*   **3D Generation Tools**:
    *   **Extrude Walls**: Instantly turn 2D plans into 3D structures.
    *   **Weld Vertices**: Automatically heal gaps in messy CAD drawings.
    *   **Static Mesh Conversion**: Bake procedural output into efficient Static Mesh Assets.
*   **3ds Max Integration**: Export directly to our JSON format for 1:1 fidelity using the included script.

## 📦 Installation

1.  Copy the `CADImporter` folder into your project's `Plugins/` directory.
2.  Enable the plugin in **Edit > Plugins > CAD 2D Importer**.
3.  Restart the Editor.

## 📖 Documentation

*   [**FAB Listing Info**](Docs/FAB_Listing.md)
*   [**User Guide**](Docs/UserGuide.md)
*   [**Export Scripts**](Extras/README.md)

## 🎮 Quick Start

1.  Open **Tools > CAD 2D Importer**.
2.  Select a `.dxf` file.
3.  Select the layers you wish to import.
4.  Click **Import**.
5.  (Optional) Select the created actors and use the **3D Toolbox** to extrude walls.

## 🔧 Technical Support

*   **Supported Platforms**: Windows, Mac, Linux
*   **Engine Versions**: 5.3+
*   **Required Plugins**: ProceduralMeshComponent (Enabled by default)
*   **Support**: [GitHub Issues](https://github.com/lAvArt/CADImporter/issues) or `contact@lavartstudio.com`

---
*Created by [lAvArt Studio](https://www.lavartstudio.com)*

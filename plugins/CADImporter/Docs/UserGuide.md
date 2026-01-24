# CAD 2D Importer - User Guide

## 1. Introduction
Thank you for using the **CAD 2D Importer**. This plugin allows you to seamlessly bring 2D vector data (DXF) into Unreal Engine as native Spline Components. This is ideal for ArchViz floor plans, path generation, and procedural modeling referencing.

## 2. Installation
1.  Place the `CADImporter` folder into your project's `Plugins` directory (e.g., `MyProject/Plugins/CADImporter`).
2.  Open your project.
3.  Go to **Edit > Plugins**, verify "CAD 2D Importer" is enabled.
4.  Restart the Editor if prompted.

## 3. Importing a File
1.  Open the **CAD Importer** tab via **Tools > CAD 2D Importer**.
2.  Locate the **Import Settings** panel.
3.  **File Path**: Click `...` to select a `.dxf` or `.json` file.
4.  **Units**: 
    *   *Auto-Detect*: Tries to read the header variable `$INSUNITS`.
    *   *Manual*: Force a specific unit (e.g., Millimeters) if the file scales incorrectly.
5.  Click **Load File**. This parses the file but does not spawn actors yet.

## 4. Layer Management
Once a file is loaded, the **Layers List** will populate:
*   **Checkbox**: Toggle to include/exclude this layer from import.
*   **Color**: Click to override the spline visualization color.
*   **Count**: Shows how many entities are in that layer.
*   **Select**: Post-import, use this to select all actors created from this layer.

**Tips**:
*   Uncheck layers like "Dimensions", "Text", or "Hatch" to keep your scene clean.

## 5. Spawning Splines
Click **Import Selected Layers** to generate actors in the level.
*   The plugin creates an `Actor` for each CAD Entity (or groups them, depending on settings).
*   Actors are tagged with `CAD_Layer_[LayerName]`.

## 6. 3D Toolbox (Post-Process)
After importing, you can use the **3D Toolbox** section in the plugin window to generate geometry.

### Generate Walls
1.  Select the Spline Actors you want to convert.
2.  Set **Wall Height** (e.g., 300 cm) and **Thickness** (e.g., 20 cm).
3.  Set **Weld Threshold**:
    *   If your CAD drawing has small gaps between lines, increase this (e.g., 1.0 - 5.0 cm) to merge them into a continuous loop.
4.  Click **Generate Walls**.

### Static Mesh Conversion
Splines generated as "Procedural Mesh" can be converted to static assets:
1.  Select the Procedural Mesh actors.
2.  Click **Convert to Static Mesh**.
3.  The asset is saved to the Content Browser, and the actor is replaced with a Static Mesh Actor.

## 7. 3ds Max Workflow (JSON)
For complex shapes that DXF handles poorly, use our included Python script:
1.  In 3ds Max, open `Scripting > Run Script...`
2.  Select `Plugins/CADImporter/Extras/3dsmax/export_cad_json.py`.
3.  Select the splines you want to export.
4.  Run the script and save the `.json` file.
5.  Import this JSON into Unreal using the standard plugin workflow.

## 8. Troubleshooting
*   **"Lines are huge/tiny"**: Check your Unit Scale. If you drew in Meters but imported as Millimeters, scale will be off by 1000x.
*   **"Walls have gaps"**: Increase the **Weld Threshold**.
*   **"Black Lighting"**: Use **Convert to Static Mesh** to generate proper lightmap UVs and normals.

---
*Support: contact@lavartstudio.com | Copyright © 2026 lAvArt Studio*

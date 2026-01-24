# CAD Importer Export Scripts

This directory contains Python scripts to export spline data from various DCC apps (3ds Max, Cinema 4D, Blender) into the JSON format used by the **Unreal Engine CAD Importer** plugin.

## 3ds Max
**Script:** `3dsmax/export_cad_json_3dsmax.py`

### How to use:
1. Open **Scripting** > **Run Script...**
2. Select `export_cad_json_3dsmax.py`.
3. A file dialog will appear. Choose where to save the `.json` file.
4. The script will export **all selected shapes**. If nothing is selected, it will attempt to export all shapes in the scene.

> **Note:** Supports Line, Circle, Rectangle, Arc, Star, Text, and any other Shape object that can be converted to a Spline.

---

## Cinema 4D
**Script:** `c4d/export_cad_json_c4d.py`

### How to use:
1. Open **Extensions** > **Script Manager...** (or **Script** > **Script Manager**)
2. **File** > **Import...** and select `export_cad_json_c4d.py`.
3. Click **Execute**.
4. A file dialog will appear. Choose where to save the `.json` file.

Alternatively, you can drag the script into your Cinema 4D viewport to run it instantly.

> **Note:** Supports standard Spline objects. Generators (like Circle, Rectangle) are automatically converted to splines during export. Only exports the current state of the object (modifiers applied).

---

## Blender
**Script:** `blender/export_cad_json_blender.py`

### How to use (As Add-on):
1. In Blender, go to **Edit** > **Preferences** > **Add-ons**.
2. Click **Install...** and select `export_cad_json_blender.py`.
3. Enable the add-on by checking the box next to **Import-Export: Export CAD JSON**.
4. Go to **File** > **Export** > **CAD Importer JSON (.json)**.

### How to use (One-time Run):
1. Go to the **Scripting** tab.
2. Open `export_cad_json_blender.py`.
3. Press the **Play** button (Run Script).
4. Go to **File** > **Export** > **CAD Importer JSON (.json)** (The menu item is registered by the script).

> **Note:** Supports Bezier and Poly curves. Modifiers (Geometry Nodes, etc.) are applied before export.

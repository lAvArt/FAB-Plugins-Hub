# Advanced Measurement Tool (AMT)

A measurement and dimensioning plugin for the Unreal Editor, for level designers, architects and QA teams who need exact numbers from their scenes: click to measure in the viewport, or let an AI assistant measure and dimension for you.

![AMT Banner](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Banner.png)

## Overview

AMT draws distance, angle, area and volume measurements directly in the level viewport, keeps them in a list, converts them to metric or imperial units, and exports them to CSV or JSON. Version 1.1 adds an optional **AI assistant interface (MCP)**: a connected assistant such as Claude can find actors, measure actors, regions, brush volumes and rooms, add length, width and height dimensions around actors, and check its own work in a viewport screenshot.

- **Current version:** 1.1.0
- **Unreal Engine:** 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8. Fab provides a separate download for each version; choose the one that matches your engine.
- **Platforms:** the plugin's descriptor allows Windows, macOS and Linux editors. It is developed and tested on Windows.
- **Editor tool.** The viewport tools, the dashboard and the AI interface exist only in the editor. The plugin's small runtime modules (measurement types, the measurement subsystem, unit and export helpers, UMG list widget bases) are compiled into a game that enables the plugin.

## Features

### Core measurement tools (interactive)
*   **Distance**: two points. *Singular* mode measures one distance; *Continuous* mode keeps going. Optional ground projection shows the horizontal distance and the slope.
*   **Angle**: three points (start of the first leg, the vertex, end of the second leg).
*   **Area**: any polygon of three or more points, measured in 3D.
*   **Volume**: a box from two opposite corners. *Boundary* mode measures the box, *Geometry* mode measures the actor's collision geometry.
*   **Polyline** (`L`): click points along a path; the live length follows the cursor and `Enter` finishes it. Two points or more.
*   **Perimeter** (`O`): click the corners of a shape; the length of its outline follows the cursor and `Enter` finishes it. Three points or more.
*   **Radius** (`C`): three points on a circle give its radius and diameter.
*   **Slope** (`S`): two points give the slope in degrees and percent, with the rise and run drawn dashed.
*   **Pick Mode** (`P`): hover an actor and click. Distance gives its length, width and height, Area its footprint rectangle, Volume its bounds or geometry volume. An optional actor tag filter limits what can be picked. Not available with the Angle tool or with Polyline, Perimeter, Radius and Slope, which are placed point by point.

### Snapping
*   **Grid Snap** to the editor grid, **Vertex Snap** to the corners of actor bounds, and **Complex Snap** to the real mesh vertices.

### Data
*   **Measurement list** in the dashboard, with per-measurement visibility, isolate-latest and delete.
*   **Export** to CSV or JSON and **import** from JSON.
*   **Units**: metric or imperial, with separate area, volume and angle unit settings.
*   **Appearance**: architectural or classic dimension style, line colour and thickness, point size, text scale, always-on-top (X-ray), screen or world space labels.
*   **Blueprint and C++ access**: `UAMTMeasurementSubsystem` stores the measurements; `UAMTMeasurementFactory` builds any measurement from points, with the result and label computed the way the tools do.

### New in 1.1: more measurement types
*   **Polyline** (path length), **Perimeter** (closed loop), **Radius** (circle through three points, with its diameter) and **Slope** (degrees and percent). They have their own viewport tools and panel buttons (see above), are drawn and labelled like the others, and can also be created by the AI assistant tools and from Blueprint or C++ (`UAMTMeasurementFactory`).

### New in 1.1: an architectural drawing style
*   Stored measurements are drawn like a dimensioned drawing: thin lines that run a little past their ends, 45 degree ticks instead of point markers, fine extension lines from an automatic dimension back to the geometry, dashed construction lines for a slope's rise and run and a radius, and a quiet label that sits beside its line and shows a delete button only while it is selected. Ticks and dots keep their size on screen, near or far.
*   Prefer the 1.0 look (plain lines, a square marker at every point, a boxed label)? Set **Dimension Style** to **Classic** in `Project Settings > Plugins > Advanced Measurement Tool > Appearance`.

### AI assistant interface (MCP, beta)
*   32 tools an assistant can call: see what the level contains (folders, tags, classes, layers), find actors by tag, folder, layer, class, name or a storey of a building, measure one actor or a whole group at once, between two things, a region, a room (detected with rays from a point), add dimensions or area and volume measurements to a group of actors and keep them in step with the actors, manage and export measurements, show them, frame the viewport and take a screenshot.
*   **Optional and local.** It is part of the editor session only (a packaged game does not contain it), listens on 127.0.0.1, needs a token, and the plugin itself never calls an AI service or sends your project anywhere. Changes are undoable with Ctrl+Z.
*   Setup in two minutes: [AI_ASSISTANT_GUIDE.md](AI_ASSISTANT_GUIDE.md). Every tool and argument: `Resources/Agent/TOOLS.md` in the plugin folder.

## Screenshots

![Advanced Measurement Tool](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Cover.jpg)

### Angle

![Angle](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_01_angle.png)

### Distance

![Distance](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_02_distance.png)

### Area

![Area](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_03_area.png)

### Volume

![Volume](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_04_volume.png)

### Pick Mode

![Pick Mode](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_05_pick.png)

### Snapping

![Snapping](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_06_snap.png)

### Measurement list and export

![Measurement list and export](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_07_history.png)

### Architectural drawing style

![Architectural drawing style](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_08_architectural.png)

### Settings

![Settings](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_09_settings.png)

### AI assistant interface (MCP) settings

![AI assistant interface (MCP) settings](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_10_mcp_settings.png)

### Polyline

![Polyline](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_11_polyline.png)

### Perimeter

![Perimeter](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_12_perimeter.png)

### Radius

![Radius](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_13_radius.png)

### Slope

![Slope](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/Advanced-Measurement-Tool/Resources/Gallery/amt_gallery_14_slope.png)

## Installation

**From Fab:** add the plugin to your library, choose *Install to Engine* for your engine version, then enable it in `Edit > Plugins` and restart the editor.

**From source:** close the editor, copy the `AdvancedMeasurementTool` folder into your project's `Plugins` folder, open the project (Unreal asks to build the plugin), and enable *Advanced Measurement Tool* in `Edit > Plugins`.

## Usage

### Open the tool
Click **Measurement Tool** in the Level Editor toolbar, or press `Ctrl+M` to show or hide the dashboard. One button per measurement tool sits next to it.

### Controls

| Action | Key |
| :--- | :--- |
| Distance / Angle / Area / Volume tool | `D` / `A` / `R` / `V` |
| Polyline / Perimeter / Radius / Slope tool | `L` / `O` / `C` / `S` |
| Pick Mode | `P` |
| Place a point | Left mouse button |
| Confirm / cancel the measurement in progress | `Enter` / `Esc` |
| Delete the selected measurement | `Delete` (or its **[X]** label button) |
| Clear all | `Shift+Delete` |
| Show or hide all measurements | `Shift+H` |
| Show only the latest measurement | `Shift+I` |
| Toggle the dashboard | `Ctrl+M` |

The tool keys work with the plain key only: with `Ctrl`, `Shift` or `Alt` held, or while the right mouse button flies the camera, the editor's own keys (`Ctrl+S`, `Ctrl+D`, `W A S D`...) are left alone.

### Dashboard
*   **Measurement Tools**: pick a tool, the Distance mode and the Volume mode.
*   **Snapping**: master toggle, Grid, Vertex, Complex.
*   **Interaction**: Pick Mode and its tag filter.
*   **Actions**: show or hide, isolate, delete, clear.
*   **Settings**: opens the plugin settings, restores the defaults, **Export** and **Import**.

### Settings
`Project Settings > Plugins > Advanced Measurement Tool`: Snapping, Appearance, Interaction and Measurement Display (units, widget space and alignment, projection lines).

## Documentation
*   [AI assistant guide](AI_ASSISTANT_GUIDE.md)
*   [FAQ](FAQ.md)
*   [Changelog](CHANGELOG.md)
*   Report problems on the [issue page](https://github.com/lAvArt/FAB-Plugins-Hub/issues) with your engine version and the steps to reproduce.

---

**Developed by lAvArt Studio**  
[www.lavartstudio.com](http://www.lavartstudio.com)  
[GitHub Repository](https://github.com/lAvArt/FAB-Plugins-Hub/tree/main/plugins/Advanced-Measurement-Tool)

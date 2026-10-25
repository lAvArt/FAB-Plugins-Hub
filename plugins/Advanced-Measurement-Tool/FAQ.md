# Advanced Measurement Tool: FAQ

## Installation and versions

### Which Unreal Engine versions are supported?
**A:** 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8. Fab provides a separate download for each version: choose the one that matches your engine. The plugin is built from source for the version you install.

### Why do I see "Missing Modules" when I open the project?
**A:** The plugin was not built for your engine version. Installing it from Fab for the right version avoids this. If you copied the folder in by hand, right-click your `.uproject`, choose **Generate Visual Studio project files**, and build; or delete the plugin's `Binaries` and `Intermediate` folders and let Unreal rebuild it when it asks.

### How do I update the plugin?
**A:** Through Fab: the Library shows when a new version is available. The plugin has no built-in updater and makes no network requests of its own.

### Does it work in a packaged game?
**A:** AMT is an editor tool: the viewport tools, the dashboard and the AI interface exist only in the editor, and the AI interface is not part of a packaged game at all. The plugin's small runtime modules (measurement types, the measurement subsystem, unit and export helpers, UMG list widget bases) are compiled into a game that enables the plugin, so Blueprint and C++ can use that data there; the interactive measuring is an editor feature.

### Which platforms?
**A:** The plugin allows Windows, macOS and Linux editors. It is developed and tested on Windows.

## Using the tools

### How do I open the tool?
**A:** Click **Measurement Tool** in the Level Editor toolbar, or press `Ctrl+M` to show or hide the dashboard.

### My shortcuts (D, A, R, V, L, O, C, S, P) do not work.
**A:** They work only while the Advanced Measurement Tool mode is active and the viewport has focus. Click **Measurement Tool** in the toolbar first. `D` is Distance, `A` Angle, `R` Area, `V` Volume, `L` Polyline, `O` Perimeter, `C` Radius, `S` Slope, `P` Pick Mode.

### How do I measure an angle?
**A:** Press `A`, click the start of the first leg, then the vertex, then the end of the second leg.

### How do I measure a volume?
**A:** Press `V`, click one corner, then the opposite corner: the volume of that box is shown. Or use Pick Mode (`P`) and click an actor. In *Boundary* mode you get the bounds box, in *Geometry* mode the volume of the actor's collision geometry.

### What is Pick Mode?
**A:** Hover an actor and click to measure it at once: Distance gives its length, width and height, Area its footprint, Volume its bounds or geometry. Type an actor tag in the dashboard to pick only actors with that tag. It is not available with the Angle tool.

### How do I delete a measurement?
**A:** Select it (click it, or use the list in the dashboard) and press `Delete`, or click the small **[X]** on its label. `Shift+Delete` clears all of them.

### Snapping is not accurate enough for my mesh.
**A:** Turn on **Vertex Snap**, and for detailed meshes also **Complex Snap**, which checks the real mesh vertices (within 50 cm of the cursor) instead of only the bounding box corners.

### Can I export my measurements?
**A:** Yes. In the dashboard's **Settings** section, **Export** writes CSV or JSON and **Import** reads a JSON file back. Distances, areas and volumes are stored in centimetres, square centimetres and cubic centimetres; the export says which unit each value is in.

### Can I measure in feet and inches?
**A:** Yes. In `Project Settings > Plugins > Advanced Measurement Tool` set the unit system to Imperial. You can also choose the area, volume and angle units separately.

### The text is too small or too large.
**A:** In the same settings, adjust **Text Scale** and **Global Widget Scale**.

### The measurements look different from version 1.0.
**A:** Version 1.1 draws measurements in an architectural style: thin lines with ticks at the ends, extension lines on automatic dimensions, and a smaller label beside the line. To get the old look back, set **Dimension Style** to **Classic** in `Project Settings > Plugins > Advanced Measurement Tool > Appearance`.

### Where did the red delete button on the labels go?
**A:** In the architectural style the label shows a delete button only while its measurement is selected (rest the pointer on the line or on the label). The Classic style keeps the button on every label. `Delete` and **Clear All** work in both.

### What does "Restore Defaults" do?
**A:** It puts every setting back to the value the plugin ships with.

## AI assistant interface (MCP)

### What is MCP and do I need it?
**A:** MCP (Model Context Protocol) is a standard way for an AI assistant to use tools. AMT includes an optional MCP server so an assistant can measure and dimension your scene. You do not need it: everything in the viewport works without it, and it can be switched off in `Project Settings > Plugins > Advanced Measurement Tool MCP`.

### Does the plugin send my project or measurements anywhere?
**A:** No. The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice.

### Which assistants work?
**A:** Claude Code (a ready-made plugin pack is included) and any MCP client that supports Streamable HTTP. See the [AI assistant guide](AI_ASSISTANT_GUIDE.md).

### Is it safe? Can I undo what it does?
**A:** Changes the tools make to the level are undoable with `Ctrl+Z`. Tools that change or delete something say so, so an assistant's client can ask you first. File access is limited to your project folder.

### It says the room is "not enclosed".
**A:** The room detection casts rays from a point and needs collision on the walls to stop them. Open space, a missing ceiling or walls without collision give that answer: the area is not a room.

### The viewport screenshot fails.
**A:** The Level Editor viewport tab must be visible in the editor.

### Where is the list of tools?
**A:** In `Resources/Agent/TOOLS.md` inside the plugin folder, generated from the plugin itself.

## Troubleshooting

### I found a bug. Where do I report it?
**A:** On the [issue page](https://github.com/lAvArt/FAB-Plugins-Hub/issues). Include your engine version and the steps to reproduce.

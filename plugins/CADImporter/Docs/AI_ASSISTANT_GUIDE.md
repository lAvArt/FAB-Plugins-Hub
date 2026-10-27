# CAD 2D Importer - AI Assistant Guide

Since 1.1.0 an AI assistant can drive CAD 2D Importer in the Unreal Editor through MCP (Model Context Protocol). This part of the plugin is **optional, editor-only and in beta**. Nothing in the plugin needs it, and the plugin contains no AI service of its own.

> The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

## 1. Connect

1. Open your project in the Unreal Editor with the plugin enabled. A level must be open.
2. In the **Output Log**, run `CAD.Mcp`. It prints:
   - the endpoint, `http://127.0.0.1:47920/mcp` (or the next free port up to 47929);
   - a ready command for Claude Code, with the token.
3. Settings are in **Project Settings > Plugins > CAD Importer MCP**: serve MCP on or off, port range, token, timeout.

### Claude Code, with the plugin pack (recommended)

The plugin ships a Claude Code plugin pack in `Plugins/CADImporter/Resources/Agent`. It holds the MCP connection and a skill that teaches the assistant the workflow. From your project folder:

```
claude plugin marketplace add ./Plugins/CADImporter/Resources/Agent
claude plugin install cad@cad
```

Claude Code asks for the token once. If the editor did not get port 47920, set `CAD_MCP_URL` to the URL that `CAD.Mcp` printed.

### Claude Code, the server only

Paste the command `CAD.Mcp` prints:

```
claude mcp add --transport http cad http://127.0.0.1:47920/mcp --header "Authorization: Bearer <token>"
```

### Other MCP clients

Any client that speaks MCP over Streamable HTTP works:

- connect to the URL;
- send the header `Authorization: Bearer <token>`.

The token is in `Saved/CADImporter/McpToken.txt`. `CAD.Mcp newtoken` replaces it.

### Without an assistant

The same tools run from the Unreal console:

- `CAD.Tools` lists them;
- `CAD.Tool <name> {json}` calls one.

## 2. The recommended workflow

1. **Inspect** (`import_inspect`). Nothing changes. It reports:
   - the units the DXF declares, with a confidence;
   - the size in drawing units and in cm;
   - the layers with their entity counts;
   - what will not be imported;
   - anything suspicious.
2. **Import** (`import_file`). Agree the units first when the confidence is not high. Choose layers, materials per layer, heights per layer, and whether to re-centre a drawing that is far from the origin.
3. **Layers and materials** (`layer_list`, `layer_set`): show or hide layers, set colours, map materials, move layers in height.
4. **Walls** (`model_generate_walls` on the wall layers). Then, as needed:
   - `model_fix_normals`
   - `model_cap_holes`
   - `model_smooth`
   - `model_to_static_mesh`
5. **Clean up** (`cleanup_report` first). Then the fix each finding names: duplicates, labels, pivots, merging per layer, collision, Nanite.
6. **Check** (`viewport_focus`, `viewport_screenshot`). The assistant looks at the result before it tells you it worked.

## 3. Example prompts

- "Inspect `Drawings/plan.dxf` and tell me its units, its size and which layers have geometry."
- "Import `Drawings/plan.dxf` in millimetres, only the layers `A-WALL*` and `A-DOOR*`, and re-centre it on the origin."
- "Map the layer `A-WALL` of the plan to `/Game/Materials/M_Plaster` and hide the layer `A-ANNO`."
- "Extrude the `A-WALL` layer into 280 cm walls, then make sure they face outward."
- "Convert those walls to static meshes in `/Game/CAD/Plan` and give them complex-as-simple collision."
- "Run a cleanup report on the plan, show me the duplicates, and remove them once I agree."
- "Preview renaming the plan's actors as `{layer}_{kind}_{index}`; apply it if I say yes."
- "Frame the plan from the top and take a screenshot."

## 4. Tool families

- **import_**: inspect a file without importing, import it with explicit options, and list, frame or delete imported drawings.
- **layer_**: list layers and their actors, and change their visibility, colour, material mapping and height.
- **model_**: the 3D toolbox without the selection. Generate walls from splines, fix normals, cap holes, smooth, convert to static meshes.
- **cleanup_**: a hygiene report, then removing duplicates, renaming by rule, setting pivots, merging meshes per layer, and setting collision and Nanite on converted meshes.
- **viewport_**: frame the drawing (fit, top or 3/4 view) and take a screenshot the assistant can look at.
- **cad_status**: says which project and level are open.

The full tool reference, generated from the plugin, is in `Resources/Agent/TOOLS.md` inside the plugin folder, and published on the documentation site as AI_TOOLS.md.

## 5. Limits

- 2D drawings only. No DWG, no 3D CAD. Block references (INSERT), polyface meshes, NURBS splines without fit points, text, hatches and dimensions are not imported.
- The tools act on what they are told: actors, a drawing, or layers. They never act on the editor selection.
- Files are read only from inside the project folder.
- Destructive tools ask for your confirmation through the client: `import_delete_source`, `cleanup_remove_duplicates`, `cleanup_merge_by_layer`.
- Every change to the level is one undo step. Assets created by conversions and merges stay unsaved until you save, and undo does not remove them.
- Editor only, not during Play-In-Editor.

## 6. Troubleshooting

- **Connection refused:** the editor is not running, or **Serve MCP** is off in Project Settings.
- **Wrong port:** another program held 47920, so the editor took the next free port, up to 47929. Run `CAD.Mcp` to see the URL, and update the client (or set `CAD_MCP_URL` for the Claude Code pack).
- **403:** the token is missing or wrong. Run `CAD.Mcp` and copy the command again. `CAD.Mcp newtoken` makes a new token; reconnect the client afterwards.
- **"There is no editor level open":** open a level in the editor.
- **"A Play-In-Editor session is running":** stop Play first.
- **A screenshot is black or fails:** the level viewport must be visible. Show a level viewport tab and do not minimise the editor.
- **A tool answers with an error:** its text says what is missing (units, a source, a layer name, a path inside the project) and what to call next.

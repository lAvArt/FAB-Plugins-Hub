# Advanced Measurement Tool: AI assistant guide

Version 1.1 adds an optional interface that lets an AI assistant use Advanced Measurement Tool inside your Unreal Editor. You describe what you want ("dimension the selected walls", "how big is the room around this point?"); the assistant finds the actors, measures them, draws the dimensions and shows you the result.

It uses MCP (Model Context Protocol), a standard way for assistants to use tools. It is **beta**, **optional** and **local**.

## What you need

- Unreal Engine 5.3 to 5.8 with the plugin enabled, and a level open in the editor.
- An assistant that speaks MCP over HTTP. **Claude Code** works with the plugin pack that ships inside the plugin; any other MCP client that supports Streamable HTTP can connect too.
- Nothing else. The plugin does not call an AI service itself.

## Privacy and safety

The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice.

- Changes the tools make to the level are undoable with `Ctrl+Z`.
- Tools that change or delete something are marked as such, so an assistant's client can ask you first.
- Files are read and written only inside your project folder.
- You can turn the server off in `Project Settings > Plugins > Advanced Measurement Tool MCP > Serve MCP`.

## Connect

1. Open your project with the plugin enabled.
2. Open the Output Log and run `AMT.Mcp`. It prints the endpoint (`http://127.0.0.1:47910/mcp`, or the next free port up to 47919), the token, and a ready-made connect command.
3. Connect your assistant:
   - **Claude Code, with the skill (recommended).** In a terminal:
     ```
     claude plugin marketplace add ./Plugins/AdvancedMeasurementTool/Resources/Agent
     claude plugin install amt@amt
     ```
     Claude Code asks for the token once. The skill teaches the assistant the order to call the tools in and the rules for changes.
   - **Claude Code, the server only.** Paste the `claude mcp add ...` line that `AMT.Mcp` printed.
   - **Another MCP client.** Streamable HTTP at the endpoint, with the header `Authorization: Bearer <token>`.
4. Ask the assistant to call `amt_status`. It answers with the project, the level and how many tools are available.

`AMT.Mcp newtoken` replaces the token if you ever need to.

## What it can do

| You want | The assistant uses |
|---|---|
| See what the level contains: folders (with the heights they span), tags, classes, layers | `scene_outline` |
| Find "the north wall", "every wall tagged `structure`", "the doors in `Office/Floor2`", or use what you selected | `scene_find_actors`: by name, class, tag or tags, outliner folder (with its subfolders), layer, the selection, or one storey of a building by height (`minZ`, `maxZ`); `scene_get_selection`, `scene_get_actor`, `scene_select` |
| The sizes of a whole group at once | `measure_actors`: length, width and height of each actor, its box volume and footprint, with totals and a summary by class; takes the same filters |
| An area or a volume measurement on each actor of a group | `measurement_from_actors` (area of each actor's footprint, or the volume of its box), titled with the actor's label |
| Size of an actor | `measure_actor`: length, width, height along its own axes, bounds, and with the mesh the surface area and (for a closed mesh) the volume |
| Distance or clearance between things | `measure_between`: centre to centre, or the gap between the actors' bounds |
| A group of actors, a brush volume or a box | `measure_region` |
| A room | `measure_room`: casts rays from a point against the collision; gives floor area, perimeter, spans, ceiling height and volume, and says if the space is not enclosed. The outline is reduced to the room's corners, so a rectangular room is four points; furniture at the probe height (120 cm) becomes part of the outline, so change `probeHeightCm` to clear it |
| What is in front of a point | `measure_raycast` |
| Any type from points you give | `measure_points`: distance, angle, area, volume, polyline, perimeter, radius, slope |
| Dimensions around actors (one, several, or every actor a filter names) | `dimension_auto`, then `dimension_refresh` when the actors move and `dimension_clear` |
| Keep, edit, export, import | `measurement_list`, `_get`, `_create`, `_update`, `_delete`, `_clear`, `_export`, `_import` |
| Look at the result | `viewport_show`, `viewport_focus`, `viewport_camera`, `viewport_screenshot` |
| Units and appearance | `settings_get`, `settings_set`, `settings_reset` |

The full list with every argument is in `Resources/Agent/TOOLS.md` inside the plugin folder, and published on the documentation site as AI_TOOLS.md.

Numbers come in centimetres, square centimetres, cubic centimetres and degrees, each with a text in your own unit system (metric or imperial, from the settings).

## Things to ask

1. "Select the three walls I picked and add length, width and height dimensions to each. Show me a screenshot."
2. "How far apart are `Sofa_01` and `Wall_East`? I want the clear gap, not centre to centre."
3. "What is the floor area and ceiling height of the room around the origin? Save the area as a measurement called Living room."
4. "Measure the whole building (everything in the folder `Building`) and give me its footprint and height."
   - "Give me the length, width and height of every wall and door on the second floor of the office building." (The assistant looks at `scene_outline`, finds the folder or the height band that is the second floor, and measures the walls and doors in it.)
   - "Add an area measurement to every actor tagged `Room`."
5. "I moved the boxes. Update the dimensions."
6. "Export all measurements to a CSV file named `survey.csv`."
7. "Switch the units to imperial and tell me the width of `Door_02` in feet and inches." (It asks you first, because it changes a setting.)
8. "The dimension on the left wall looks wrong. Take a screenshot and tell me what you see."

## How it works with you

The assistant should check its work: after drawing dimensions it frames them and looks at a screenshot before it tells you they are right. It should ask you before it clears or deletes measurements, imports over existing ones, or changes your settings. A result it could not measure is reported as such: an open mesh has no volume, and a space with gaps is not a room.

Dimensions made with `dimension_auto` stay linked to their actor. `dimension_refresh` updates them after the actor moves, rotates or scales; if the actor was deleted, they are marked stale and `dimension_clear` removes them. Measurements you drew by hand are never touched by the dimension tools.

## Limits

- The viewport screenshot needs the Level Editor viewport tab to be visible.
- Room detection needs collision on the walls, floor and ceiling.
- A mesh volume is given only for a closed mesh (every edge shared by two triangles).
- Instanced static meshes are not included in mesh measurements.
- Measurements are stored in the level's subsystem. A Play-In-Editor session reads the saved measurements but does not write them back.
- Polyline, Perimeter, Radius and Slope have viewport tools of their own (`L`, `O`, `C`, `S`) and are also created by the assistant tools and from Blueprint and C++.
- Groups of actors are named by what the outliner holds: folder, tags, layers, class and name, or a height band. A level with none of those can still be asked about by name or by height. Information an import adds to an actor (a Revit parameter, for example) is not read.
- One call works on up to 200 actors (100 when it adds measurements, 50 when it reads meshes); the assistant works in groups beyond that.

## Troubleshooting

| Symptom | What to do |
|---|---|
| `AMT.Mcp` says MCP is not being served | Check `Project Settings > Plugins > Advanced Measurement Tool MCP`: Serve MCP must be on and a port in the range free. `AMT.Mcp restart` tries again. |
| The assistant gets "403" | The token is missing or wrong. Run `AMT.Mcp` again and reconnect with its token. |
| "There is no editor level open" | Open a level in the editor. |
| `viewport_screenshot` fails | Make the Level Editor viewport tab visible. |
| Measurements do not show | Ask for `viewport_show`, or click **Measurement Tool** in the toolbar. |
| An actor is not found | Ask the assistant to run `scene_find_actors` and use the `id` it returns. |
| Another plugin of ours uses a nearby port | Each plugin takes its own range (Advanced Measurement Tool 47910-47919), so they can run together. |

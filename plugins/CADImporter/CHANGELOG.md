# Changelog

## [1.1.0] - 2026-10-22

AI assistant tools (optional, editor-only, beta). Existing workflows are unchanged.

### Added

- **MCP server for AI assistants:**
  - runs inside the editor session, on 127.0.0.1, ports 47920-47929;
  - needs a bearer token;
  - console commands `CAD.Mcp`, `CAD.Tools` and `CAD.Tool`;
  - settings in Project Settings > Plugins > CAD Importer MCP.
- **23 tools, `cad_status` included**. The reference is in `Resources/Agent/TOOLS.md`.
  - import_: inspect a drawing without importing it, import with explicit options, list, frame and delete imports.
  - layer_: list layers and actors; visibility, colour, material mapping, height.
  - model_: generate walls, fix normals, cap holes, smooth, convert to static meshes, without using the editor selection.
  - cleanup_: report, remove duplicates, rename by rule, set pivots, merge per layer, collision, Nanite.
  - viewport_: frame and screenshot.
- **Claude Code plugin pack** with a skill, in `Resources/Agent`.
- **DXF parser** reads the header variables `$INSUNITS`, `$MEASUREMENT`, `$ACADVER` and the extents. It also counts skipped and unsupported entities, block references and ignored layers. The AI tools report this; the import dialog still asks for the units.
- **Headless import pipeline** in the editor module (`FCADImportPipeline`): loads a drawing and imports it without dialogs.
- **Selection-free versions** of the 3D toolbox operations.
- **Log category** `LogCADImporter`.
- **Docs:** FAQ and AI Assistant Guide. The user guide and the listing text were corrected.

### Fixed

- **Generated walls were drawn inside out.** The triangles of a generated wall were wound the opposite way from its normals, so a one-sided material showed the far inner faces: walls looked dark, flat and open at the top, and Reverse Normals only moved the problem. The winding now matches the normals, so walls light correctly, show their tops, and look the same from either side of a two-sided material.
- **Caps now follow the way the outline is drawn.** A clockwise outline gives a wall that is inside out as a whole (sides and caps together), and Reverse Normals or the Fix Wall Normals tool turns it right in one step. Before, the caps kept their direction and stayed dark after the fix.
- **Convert To Static Mesh** removed every selected procedural actor, even ones it had not converted (for example after Cancel). It now removes only the converted ones.
- **Undo for edited walls:** generated walls are transactional, so Reverse Normals, Cap Holes and Smooth can be undone.

### Changed

- The import dialog and the 3D toolbox behave as in 1.0. One visible difference: walls you generate in 1.1 are drawn on the other side of their faces than in 1.0 (see Fixed), so they look right without Reverse Normals. Walls made in 1.0 are not changed. If you used Reverse Normals to work around dark walls, try without it first.

Parts of the 1.1.0 AI assistant layer (MCP server, tools, automated tests and documentation) and the fix to wall generation were developed with AI assistance (Claude, by Anthropic) and reviewed by lAvArt Studio.

## [1.0] - 2026-01-24

### Added

- Initial release of CAD 2D Importer.
- DXF and JSON import as spline actors.
- Layer management.
- Wall generation tools.
- Static mesh conversion.

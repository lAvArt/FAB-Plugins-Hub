# Changelog

All notable changes to the "Advanced Measurement Tool" will be documented in this file.

## [1.1.0] - 2026-10-22

### Added
- **AI assistant interface (MCP), beta.** An optional, editor-only server that lets an AI assistant such as Claude use the plugin: 32 tools to see what the level contains, find actors by tag, folder, layer, class, name or storey, measure actors (one or a whole group), regions, brush volumes and rooms, add length, width and height dimensions or area and volume measurements to groups of actors (dimensions are kept linked to them), manage, export and import measurements, show them, frame the viewport and take a screenshot. It listens on 127.0.0.1 only and needs a token; the plugin never calls an AI service itself. Setup: `AI_ASSISTANT_GUIDE.md`. Tool reference: `Resources/Agent/TOOLS.md`. Turn it off in Project Settings > Plugins > Advanced Measurement Tool MCP.
- New measurement types with viewport tools and panel buttons: **Polyline** (`L`, path length), **Perimeter** (`O`), **Radius** (`C`, circle through three points) and **Slope** (`S`, degrees and percent). They are drawn and labelled in the viewport like the others, and can also be created from the assistant tools and from Blueprint or C++.
- `UAMTMeasurementFactory`: build a measurement from points without the mouse, with the result and label computed the way the viewport tools do.
- A measurement can carry a title (metadata `title`) that replaces the type's name in its viewport label.
- `FAQ.md` and `AI_ASSISTANT_GUIDE.md`.

### Changed
- **Measurements are drawn in an architectural style by default**: thin lines that run a little past their ends, 45 degree ticks instead of square point markers, extension lines from automatic dimensions back to the geometry, dashed construction lines for slope and radius, an arc for angles, and a quieter label (name in grey, value in white, a hairline in the measurement's colour) that sits beside its line. The delete button on a label shows only while its measurement is selected. Set **Dimension Style** to **Classic** in the plugin settings for the 1.0 look.
- Supported engines are 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8, one download per version on Fab.
- The documentation now matches the plugin: the dashboard shortcut is `Ctrl+M`, the Angle tool takes start, vertex and end, and the Volume tool takes two opposite corners.
- The Settings buttons of the panel (Open Full Settings, Restore Defaults, Export, Import) sit in two rows, so their names are not cut off.

### Fixed
- **Restore Defaults** in the dashboard did nothing: it targeted a settings section that does not exist. It now restores every setting.
- The CSV export labelled volumes in cubic metres although the values are in cubic centimetres.
- `GetAllMeasurements` returns measurements oldest first, so "latest" and "isolate latest" are reliable.
- A Play-In-Editor session no longer overwrites the saved measurements file.
- The plugin's `DefaultEditor.ini` no longer carries a placeholder URL and keys that matched no setting.
- Builds cleanly with the strict include checks Epic uses for Fab (several headers were missing declarations) and without deprecation warnings on 5.8.
- The tool keys no longer take over Ctrl+S, Ctrl+D and the like, or W A S D while the right mouse button flies the camera.
- The version at the bottom of the panel follows the plugin's version.
- Undo (Ctrl+Z) after a new measurement removes it: the undo step used to be recorded after the measurement was added, so it left the measurement in place.

### Removed
- The "Check for Updates" settings (check on startup, URL, interval). They had no effect: the plugin has no built-in updater. Updates come through Fab.

## [1.0] - 2026-01-16
### Added
- Initial Release (v1.0).
- New professional plugin icon and banner.
- "Hand" cursor interaction for dashboard buttons to improve UX.
- `RepoDistributionContent` folder for easy repository management.
- **Measurement Tools**: Distance, Angle, Area, and Volume tools.
- **Snapping System**: Grid, Bounding Box, and high-precision Mesh Vertex snapping.
- **Dashboard**: Centralized "AMT Dashboard" for tool management and history.
- **Export**: Ability to export measurement history to CSV and JSON.
- **Settings**: Comprehensive editor settings for units (Metric/Imperial), colors, and widget scaling.
- **Update Checker**: Built-in notification for new versions.

### Changed
- Dashboard footer layout simplified and polished.
- GitHub link now uses a dedicated icon button.
- Version updated to 1.0.0.

### Fixed
- N/A (Initial Release)

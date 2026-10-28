# Changelog

Changes to the Pixel Streaming Bridge (PSB) Unreal Engine plugin.

## [1.1.0] - 2026-10-22

Supported engines: Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8. Windows; the descriptor also allows Linux (not built for this release). The message envelope and every wire name are unchanged.

### Added
- **Message manifest** (optional): a `PSB Message Manifest` asset, or a `*.psb.json` file, listing every command and event with its direction, description, typed payload fields and response event. Load it with the project setting Default Manifest (or Manifest Json File), the `Manifest` property of a PSBBootstrap, or Load Manifest.
- **Payload validation** (opt-in, project setting Validate Against Manifest, off by default): commands the manifest lists are checked; an invalid one is not dispatched and is answered with `psb.error` and a code (`MISSING_FIELD`, `INVALID_FIELD_TYPE`, `INVALID_FIELD_VALUE`, `FIELD_OUT_OF_RANGE`, `INVALID_DIRECTION`), the field and the command.
- **Bind Command** (subsystem) and **Bind PSB Command** (function library): bind a Blueprint event to one command name; Unbind Command, Unbind All Commands, Get Bound Command Names.
- **Typed payload getters**: Get String Field, Get Number Field, Get Integer Field, Get Bool Field, Get String Array, Get Number Array, Get Object Json, Has Field, Make Payload From Json.
- **Replies**: Reply To Command Json emits an event carrying the command's `requestId` (it uses the manifest's response event when no name is given). `FPSBStructuredPayload` gains `CommandName` and `RequestId`.
- Payload Builder **Get Json String**; subsystem **Has Active Transport**; a traffic log of recent envelopes (Get Recent Traffic, project setting Traffic History Size) and a C++ traffic tap.
- **AI assistant layer (optional, editor-only, beta)**: modules `PSBMcp` and `PSBMcpEditor` serve 24 tools over MCP on 127.0.0.1 to an assistant you connect yourself: edit and validate the manifest, import existing wire names from TypeScript constants or a Markdown table, generate JSON Schemas, TypeScript typings with a typed sendCommand, a commands reference and a DataTable, create Blueprint handlers whose `On<Command>` events receive typed fields, place the bridge in the level, print the streaming launch arguments, and test commands in Play-In-Editor. Nothing of it is in a packaged game. See `docs/AI_ASSISTANT_GUIDE.md`.
- Automation tests for the manifest, Bind Command, replies, the 1.0 defaults and the editor tools.
- `psb.error` may now carry `field`, `command` and the command's `requestId` in addition to `code` and `message` (additive).
- **Blueprint Owns Responses** setting (on by default, which is the 1.0 behaviour: a bound On Emit Response sends the envelope and the transport skips it). Turn it off to only observe outgoing envelopes while the transport sends them, for logging or analytics.
- **Auto Start Without Bootstrap** setting (opt-in, off by default): packaged and standalone games start the transport after a map loads even when no PSBBootstrap is in the level (needs Auto Start Transport). For projects that want a packaged app to work without a Bootstrap actor. With Bind Input Handlers on, PSB then takes Pixel Streaming's `UIInteraction` messages, so Pixel Streaming Input components no longer fire On Input Event for them (as already happens when a PSBBootstrap starts the transport).

### Changed
- Nothing changes an existing project's behaviour by default: messages, Blueprint events, sending and starting work as in 1.0. The editor does serve its local, optional AI interface (MCP, 127.0.0.1 only) unless Serve MCP is turned off in Project Settings.
- One source tree serves every supported engine version; each download on Fab is made for one engine.

### Fixed
- A native PSBBootstrap placed without a Blueprint subclass dropped every outgoing event (it bound On Emit Response to an event nothing implemented). It now binds On Emit Response only when its Blueprint implements On Emit Response BP, so its events reach the web client through the transport. BP_PSBBootstrap still sends each event once, itself.
- Builds on UE 5.3 to 5.8: the Pixel Streaming input handler signatures changed in 5.4 (the peer id is passed first); PSB selects the right ones at compile time.
- Builds with strict includes (a missing include in PSBBootstrap) and on UE 5.8 (JSON object keys).
- The automation tests build and pass on every supported engine (5.3 to 5.8).
- A message that reached the bridge's input handlers after a Play session had ended could call into a bridge that no longer existed; the handlers now check that it is alive.

### Documentation
- The error event is emitted as `psb.error`; earlier documents said `psb_error`. The emitted name is unchanged; the documents now say so.
- New: FAQ, AI assistant guide, compatibility notes; the message contract describes the manifest, Bind Command and replies.

### AI development disclosure
Parts of the 1.1.0 AI assistant layer (MCP server, tools, automated tests and documentation) were developed with AI assistance (Claude, by Anthropic) and reviewed by lAvArt Studio.

## [1.0] - earlier
- Initial release: PSB subsystem (Game Instance), JSON envelope v1.0, C++ command router, On Command Received / On Command Received Structured, Emit Event From Json, Emit Event Simple, Payload Builder, PSBBootstrap and BP_PSBBootstrap, project settings.

# Pixel Streaming Bridge: AI assistant guide (beta)

PSB 1.1.0 includes an optional, editor-only MCP server. An AI assistant you connect to it (Claude Code, or any MCP client) can define the messages between your web page and Unreal, generate the web typings and docs from them, write the Blueprint that receives them, set up the level and test commands in Play-In-Editor. You do not need it to use PSB, and the plugin does not include or require any AI service.

The full, generated list of tools and their arguments is in the plugin at `Plugins/PSB/Resources/Agent/TOOLS.md`, and published on the documentation site as AI_TOOLS.md. This guide describes how to connect and how the tools fit together.

## Safety and privacy

The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

Also:
- Every tool says whether it only reads, changes something, or removes something (MCP tool annotations), so your client can ask you before a change.
- Asset tools only create or change assets under `/Game`. Generated files are only written inside the project directory.
- Project settings changed by `settings_set` or `scene_setup_bridge` are written to `DefaultGame.ini`; Ctrl+Z does not undo them.
- Turn the server off in Project Settings > Plugins > Pixel Streaming Bridge MCP > Serve MCP.

## Connect

1. Open the project in the Unreal Editor with the plugin enabled.
2. In the Output Log, run `PSB.Mcp`. It prints the endpoint, `http://127.0.0.1:47930/mcp` (or the next free port up to 47939), and a ready `claude mcp add ...` command with the token.
3. Connect your assistant:
   - **Claude Code with the skill (recommended).** The plugin ships a Claude Code plugin pack in `Plugins/PSB/Resources/Agent`: the MCP connection plus a skill that explains the workflow.
     ```
     claude plugin marketplace add ./Plugins/PSB/Resources/Agent
     claude plugin install psb@psb
     ```
     Claude Code asks for the token once. If the editor is not on port 47930, set `PSB_MCP_URL` to the URL `PSB.Mcp` printed.
   - **Claude Code, server only.** Paste the command `PSB.Mcp` printed:
     `claude mcp add --transport http psb http://127.0.0.1:47930/mcp --header "Authorization: Bearer <token>"`
   - **Other MCP clients.** Streamable HTTP at the URL, header `Authorization: Bearer <token>`.
4. The token is kept in `Saved/PixelStreamingBridge/McpToken.txt`. `PSB.Mcp newtoken` replaces it (connected clients must be set up again).

The same tools also run from the Unreal console (`PSB.Tools` lists them, `PSB.Tool <name> {json}` calls one).

## Workflow

1. **Look first.** `psb_status`, then `scene_status` (Pixel Streaming plugin, PSBBootstraps in the level, settings, the live subsystem while playing) and `manifest_list_messages`.
2. **Define the messages** in the manifest (default asset `/Game/PSB/PSB_Messages`; any tool also takes `file` for a `*.psb.json`):
   - `manifest_from_use_case` creates every message of a use case at once; nothing is written if one is wrong or already exists;
   - `manifest_put_message` adds or replaces one;
   - `manifest_import_existing` seeds the manifest from what a web app already sends (a `.ts` constants file or a Markdown commands table inside the project), keeping every name exactly.
3. **Validate.** `manifest_validate`: duplicates, characters a wire name cannot carry, reserved `psb.*` names (a warning, fine for names a client already sends), field rules, responses that must be events.
4. **Generate.** `gen_all` writes `messages.psb.json`, JSON Schemas, `psb-messages.ts` (constants, payload interfaces, a typed `sendCommand` wrapper) and `PSB_MESSAGES.md` into `PSBGenerated/`, and creates the DataTable `/Game/PSB/DT_PSBMessages`. Copy `psb-messages.ts` into your web app.
5. **Create the handler.** `bp_create_handler` creates `/Game/PSB/BP_PSBCommandHandler` (parent PSBBootstrap): BeginPlay binds every command with Bind PSB Command, and each command calls a Custom Event `On<Command>` (for example `OnAppSetColor`) whose inputs are the payload fields plus `PSBCommand`, the payload, for Reply To Command Json. It is compiled; the result lists any compile errors. Put your logic in the `On<Command>` events. Later, `bp_add_command_handler` adds a new command.
6. **Set up the level.** `scene_setup_bridge` places the handler (or BP_PSBBootstrap), adds a Pixel Streaming Input component if needed, and can load the manifest at runtime and turn payload validation on. Save the level.
7. **Test in Play-In-Editor.** Press Play, then `scene_send_test_command` feeds a command in as the page would and reports who handled it, any `psb.error`, and what went out; `scene_list_message_traffic` shows recent envelopes; `viewport_screenshot` shows the result.
8. **Stream.** `scene_launch_args` prints the command line for local Pixel Streaming. It never launches anything.

## Example prompts

- "Check whether this level is ready for Pixel Streaming Bridge and tell me what is missing."
- "I am building a car configurator page. The page sets the paint color (red, blue or black) with an optional intensity from 0 to 1, switches the camera to a named view, and Unreal reports the current color back. Create those messages in the PSB manifest, with reply events."
- "Import the commands our web app already sends from `WebApp/config.ts` in this project, then validate the manifest and tell me which field types you had to guess."
- "Validate the manifest and generate everything into PSBGenerated."
- "Create a handler Blueprint for all commands, place it in the level, and turn payload validation on."
- "Add a command `app.reset` with no payload, then add it to the handler Blueprint."
- "I pressed Play. Send `app.set_color` with color green and tell me what happened." (With validation on, the answer is a `psb.error` `INVALID_FIELD_VALUE` for `color`.)
- "Give me the command line to stream this project to my local signalling server on port 8888."

## Limits

- Beta. The tools act on the level open in the editor; Play-only tools (`scene_send_test_command`, `scene_list_message_traffic`) need Play-In-Editor running, and level tools need it stopped.
- A field of type `object` reaches the handler as JSON text (Get Object Json); number arrays arrive as Float (double) arrays. Manifest validation checks the top-level fields of the commands it lists, not the inside of objects.
- `bp_create_handler` never overwrites an existing asset. `bp_add_command_handler` only adds commands and skips those already handled; it does not remove the bindings of commands you removed from the manifest. Handlers bind in BeginPlay, so they must be Actors placed in the level.
- Generated files are written inside the project only; copying them to the web app is up to you.
- `manifest_import_existing` is best effort: types come from a Markdown payload shape when there is one; field names taken from TypeScript comments are typed as strings and reported as guessed.
- Manifest and DataTable changes are saved to disk by default (`save: false` leaves them unsaved). Ctrl+Z undoes them in the editor; save again to keep the undo.
- `viewport_screenshot` needs a visible level viewport (it cannot capture an editor started without rendering).

## Troubleshooting

- **`PSB.Mcp` says MCP is not being served.** Check Serve MCP in Project Settings > Plugins > Pixel Streaming Bridge MCP and the log for a port range that is taken; `PSB.Mcp restart` tries again.
- **The client gets 403 / unauthorized.** The token changed: run `PSB.Mcp` and set the client up again with the new token.
- **"No Play-In-Editor session is running."** Press Play first (with a PSBBootstrap or the handler in the level).
- **A handler Blueprint does not compile.** The tool result lists `compileErrors` and `wiringProblems`; open the Blueprint to see them.
- **A command does not reach the handler.** `scene_status` while playing shows whether the transport is active and which commands are bound; `scene_list_message_traffic` says what became of each message (handled, rejected with which `psb.error`, or nobody listening).
- **The page receives every event twice.** Blueprint Owns Responses was turned off while a Blueprint bound to On Emit Response also sends: turn it back on (see FAQ).

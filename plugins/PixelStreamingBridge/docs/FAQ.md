# Pixel Streaming Bridge (PSB): FAQ

Answers for version 1.1.0 of the PSB Unreal Engine plugin.

## General

**Q: Do I need to use the provided Web UI?**
A: No. Any web stack works, as long as it sends JSON messages in the PSB envelope (see `message-contract.md`) over Pixel Streaming (`emitUIInteraction`). The reference web packages (`@psb-ui/*`) are optional and are not part of the plugin.

**Q: Does the plugin include a signalling server or a web page?**
A: No. You need a Pixel Streaming signalling server (Epic's reference server, a cloud provider, or your own) and your own web page. Epic's reference servers are fetched with `get_ps_servers` in the engine's `Engine/Plugins/Media/PixelStreaming/Resources/WebServers` folder; PSB web UI templates are available as separate products.

**Q: Which engine versions are supported?**
A: Version 1.1.0 is verified on Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7 and 5.8, built on Windows. Platforms: Windows (Win64); the descriptor also allows Linux, which was not built for this release; macOS is not supported. Details: `COMPATIBILITY.md`.

**Q: Which Pixel Streaming plugin does it need?**
A: Epic's Pixel Streaming plugin (`PixelStreaming`), enabled in the project. PSB does not use Pixel Streaming 2.

**Q: Can I send large files?**
A: Pixel Streaming data channels are meant for control messages (JSON). For large files use a separate HTTP API.

**Q: Does it work with matchmakers?**
A: PSB works inside Unreal at the application level; it does not take part in signalling. Matchmaking depends on your signalling setup.

**Q: Does it change touch, mouse or keyboard input?**
A: No. Pixel Streaming handles those as usual. PSB handles the custom JSON messages the page sends with `emitUIInteraction` (and the `PSBMessage` command). See "What changed" below for what that means for Pixel Streaming Input components.

**Q: How do I debug messages?**
A: In Unreal, the `LogPSB` log category shows incoming commands, rejections and errors. The subsystem keeps the latest envelopes in and out (Get Recent Traffic; project setting Traffic History Size). On the web side, `PSBProvider` from `@psb-ui/provider` takes `debug={true}`.

**Q: Why does the web side receive `psb.error` and not `psb_error`?**
A: Unreal emits `psb.error`. Earlier documents and the `@psb-ui/events` constant said `psb_error`, which Unreal never sent. The emitted name is not changed (shipped builds may depend on it); listen to `psb.error`.

## The manifest

**Q: What is the manifest, and do I need it?**
A: It is one list of every command and event your project uses: the wire name, the direction, typed payload fields and, for a command, the event that answers it. It is optional: without it PSB works exactly as before. With it you can check inbound payloads (Validate Against Manifest), reply without repeating event names, and generate JSON Schemas, TypeScript typings, a commands reference, a DataTable and Blueprint handlers (with the editor tools). It is an asset (PSB Message Manifest) or a `*.psb.json` file; `message-contract.md` describes the format.

**Q: Does the manifest change the envelope or my existing message names?**
A: No. The envelope is unchanged and wire names are never renamed by the tools. Names a client already sends, including legacy ones, are imported as they are.

## Blueprint

**Q: How do I bind a command in Blueprint now?**
A: Use **Bind PSB Command** (or Bind Command on the PSB subsystem) once per command, for example in BeginPlay: give the command name and a Custom Event; the event receives `(CommandName, Payload)`. Read fields with Get String Field, Get Number Field, Get Integer Field, Get Bool Field, Get String Array, Get Number Array, Get Object Json and Has Field. Answer with Reply To Command Json. Unbind with Unbind PSB Command, or Unbind All Commands in EndPlay.
The old way still works: bind **On Command Received** (or On Command Received Structured) and branch on the command name with Switch on String. It receives every command; Bind Command receives only its own.

**Q: Can the plugin write that Blueprint for me?**
A: Yes, with the optional AI assistant tools: `bp_create_handler` creates an Actor Blueprint that binds every command of the manifest and calls an `On<Command>` Custom Event with typed inputs. See `AI_ASSISTANT_GUIDE.md`.

## What changed in 1.1.0

**Q: Does updating to 1.1.0 change how my project behaves?**
A: No. With the default settings, messages, Blueprint events, sending and starting the transport work as in 1.0. Everything new is either additive (Bind PSB Command, replies, the manifest, extra fields on `psb.error`) or opt-in (payload validation, the two settings below, the AI assistant tools). One bug was fixed: a native PSBBootstrap placed without a Blueprint subclass used to drop every outgoing event; it now sends them through the transport.

**Q: What does Blueprint Owns Responses do?**
A: It decides who sends an outgoing envelope when something is bound to **On Emit Response**. On (the default, the 1.0 behaviour): the bound Blueprint receives the envelope and sends it itself (for example with Send Pixel Streaming Response); the C++ transport skips it. Off: On Emit Response only observes the envelope (for logging or analytics) and the transport sends it. With nothing bound, the transport always sends. The included BP_PSBBootstrap implements On Emit Response BP and sends each event once; it keeps Blueprint Owns Responses on for its game session.

**Q: Can my packaged app work without a PSBBootstrap actor?**
A: Yes, if you opt in: turn on **Auto Start Without Bootstrap** (Project Settings > Plugins > Pixel Streaming Bridge, together with Auto Start Transport). Packaged and standalone games then start the transport once a map has loaded, even with no PSBBootstrap in the level. It is off by default. Play-In-Editor still uses a PSBBootstrap. With Bind Input Handlers on (default), PSB then takes Pixel Streaming's `UIInteraction` messages in C++, so Pixel Streaming Input components no longer fire On Input Event for them (the same happens whenever a PSBBootstrap starts the transport). If your project handles `UIInteraction` itself, leave it off or turn Bind Input Handlers off.

**Q: Is anything different between engine versions?**
A: Only internally: from UE 5.4, Pixel Streaming passes the sending peer's id to input handlers, and PSB uses the matching signatures on 5.4 and later. Behaviour is the same.

## The AI assistant (MCP)

**Q: What is MCP?**
A: The Model Context Protocol, an open standard that lets an AI assistant (Claude Code, for example) call tools. PSB 1.1.0 includes an optional, editor-only MCP server (beta) with tools to edit the manifest, generate typings and docs, create Blueprint handlers, set up the level and test commands in Play-In-Editor. You do not need it to use PSB.

**Q: Does the plugin send my data anywhere?**
A: The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.
(The plugin's runtime part exchanges messages only with the web page connected through your Pixel Streaming setup, as before.)

**Q: How do I connect an assistant?**
A: Open the project in the editor and run `PSB.Mcp` in the Output Log. It prints the endpoint (`http://127.0.0.1:47930/mcp`, or the next free port up to 47939) and a ready `claude mcp add ...` command with the token. The token is kept in `Saved/PixelStreamingBridge/McpToken.txt`; `PSB.Mcp newtoken` replaces it. For Claude Code, the plugin also ships a plugin pack with the skill in `Plugins/PSB/Resources/Agent`. Settings: Project Settings > Plugins > Pixel Streaming Bridge MCP (Serve MCP, port range, token, timeout). Full guide: `AI_ASSISTANT_GUIDE.md`.

**Q: Can I turn it off?**
A: Yes: Project Settings > Plugins > Pixel Streaming Bridge MCP > Serve MCP.

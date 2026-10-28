# Pixel Streaming Bridge (PSB)

Pixel Streaming Bridge (PSB) is an Unreal Engine plugin for JSON messaging between a web page and an Unreal app streamed with Pixel Streaming: the page sends commands, Unreal answers with events. Current version: **1.1.0** ([changelog](./CHANGELOG.md)).

## Features
- One small JSON envelope for commands (web -> Unreal) and events (Unreal -> web), with optional `requestId` replies.
- Blueprint and C++: **Bind PSB Command** per command with typed payload getters, or **On Command Received** for all; **Emit Event From Json**, **Reply To Command Json**, a Payload Builder.
- **Message manifest** (optional, new in 1.1.0): one list of your commands and events with typed fields; opt-in payload validation; generators for JSON Schemas, TypeScript typings, a commands reference, a DataTable and a handler Blueprint.
- **BP_PSBBootstrap**: drop it in a level to start the bridge.
- Provider agnostic: works with any standard Pixel Streaming signalling server (Epic's reference server, cloud providers, your own). No signalling server or web page is included.

## Supported engines and platforms
- Unreal Engine **5.3, 5.4, 5.5, 5.6, 5.7, 5.8**.
- Windows (Win64). The descriptor also allows Linux (not built for this release). macOS is not supported.
- Requires Epic's **Pixel Streaming** plugin (enabled with PSB).

Details: [Compatibility](./docs/COMPATIBILITY.md).

## Install
1. Install the plugin from Fab into your engine, or copy the `PSB` folder into your project's `Plugins` folder.
2. Enable **Pixel Streaming Bridge** in Edit > Plugins and restart the editor.
3. Drag **BP_PSBBootstrap** (Plugin Content > Blueprints) into your level. See the [User Guide](./docs/USER_GUIDE.md).

## AI assistant (optional, editor-only, beta)
PSB 1.1.0 includes an editor-only MCP server. An AI assistant you connect yourself (for example Claude Code) can define your messages, generate the web typings and docs, create the Blueprint handler, set up the level and test commands in Play-In-Editor. You do not need it to use PSB, and the plugin does not include or require an AI service.

The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

Connect: run `PSB.Mcp` in the Output Log. Guide: [AI Assistant Guide](./docs/AI_ASSISTANT_GUIDE.md). The tool reference ships with the plugin in `Plugins/PSB/Resources/Agent/TOOLS.md`.

## Updating from 1.0
With the default settings a project behaves exactly as with 1.0. The editor does serve its local, optional AI interface (MCP, 127.0.0.1 only) unless Serve MCP is turned off in Project Settings. New behaviour is opt-in: payload validation, **Auto Start Without Bootstrap** (a packaged app starts the transport without a PSBBootstrap actor) and **Blueprint Owns Responses** off (a bound On Emit Response only observes while the transport sends). Details in the [changelog](./CHANGELOG.md) and the [FAQ](./docs/FAQ.md).

## Screenshots

![Pixel Streaming Bridge](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Cover.jpg)

### BP_PSBBootstrap in the level

![BP_PSBBootstrap in the level](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_01_bootstrap.png)

### Blueprint nodes

![Blueprint nodes](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_02_nodes.png)

### Binding a command

![Binding a command](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_03_binding_init.png)

### Receiving and replying

![Receiving and replying](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_04_binding_receive.png)

### Project settings

![Project settings](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_05_settings.png)

### AI assistant settings (optional)

![AI assistant settings](https://raw.githubusercontent.com/lAvArt/FAB-Plugins-Hub/main/plugins/PixelStreamingBridge/Resources/Gallery/psb_gallery_06_mcp_settings.png)

## Documentation
- [User Guide](./docs/USER_GUIDE.md) - setup, Blueprint, sending and receiving, settings.
- [FAQ](./docs/FAQ.md) - engines, the manifest, what changed in 1.1.0, MCP and privacy.
- [Message Contract](./docs/message-contract.md) - the envelope, replies, the manifest format, errors.
- [AI Assistant Guide](./docs/AI_ASSISTANT_GUIDE.md) - connect an assistant, workflow, example prompts, limits.
- [Technical Details](./docs/FAB_PRODUCT_DOCS.md) - modules, architecture, deployment.
- [Compatibility](./docs/COMPATIBILITY.md) - engine versions and version-specific behaviour.
- [Architecture](./docs/architecture.md) - data flow.
- [Web UI Guide](./docs/WEB_UI_DOCS.md) - the separate Next.js web templates.

## Support
For issues or questions, please open an issue in this repository.

# PSB - Technical Documentation

Pixel Streaming Bridge (PSB) 1.1.0. Questions and answers are in [FAQ.md](./FAQ.md).

## Technical Specifications
*   **Supported Engine Versions**: Unreal Engine 5.3, 5.4, 5.5, 5.6, 5.7, 5.8. See [COMPATIBILITY.md](./COMPATIBILITY.md).
*   **Platforms**: Windows (Win64). The descriptor also allows Linux (not built for this release). macOS is not supported.
*   **Required Engine Plugin**: Pixel Streaming (`PixelStreaming`), enabled automatically with PSB.
*   **Code Modules** (in the Fab package):
    *   `PSB` (Runtime) - subsystem, envelope checks, command dispatch, message manifest, Blueprint function library, PSBBootstrap.
    *   `PSBMcp` (Editor) - the optional MCP server (127.0.0.1 only), tool registry and console commands.
    *   `PSBMcpEditor` (Editor) - the optional PSB tools for AI assistants.
    *   The repository also has `PSBTests` (DeveloperTool, automation tests); it is not part of the Fab package.
*   **Content**: 1 Blueprint, `BP_PSBBootstrap`.
*   **Network**: messages travel over Pixel Streaming's data channel (WebRTC). Nothing is replicated.
*   **Message Format** (see [message-contract.md](./message-contract.md)):
    ```json
    {
      "version": "1.0",
      "type": "command|event",
      "name": "namespace.action",
      "payload": { ... },
      "requestId": "optional"
    }
    ```
    Commands go from the web page to Unreal, events from Unreal to the page. Errors are events named `psb.error` (earlier documents said `psb_error`; the emitted name is `psb.error`).

## Architecture
PSB sits between the Pixel Streaming plugin and your game logic. Its transport receives the page's messages (Pixel Streaming `UIInteraction` and the `PSBMessage` command), the subsystem checks the envelope and routes each command to:
1.  a **C++ handler** registered with `RegisterCommand`;
2.  **Blueprint handlers** bound to that command with **Bind PSB Command** / **Bind Command** (since 1.1.0);
3.  **On Command Received** / **On Command Received Structured** listeners (all commands).

With **Accept Raw Messages** on (default), JSON without the envelope is wrapped into a command instead of being rejected. With a manifest loaded and **Validate Against Manifest** on, payloads of the commands it lists are checked first, and invalid ones are answered with `psb.error` and never reach your handlers.

Outgoing events go through `SendEnvelopeJson`. With nothing bound to **On Emit Response**, the transport sends each one to every connected viewer. When a Blueprint binds On Emit Response, it sends them itself and the transport skips them (**Blueprint Owns Responses**, on by default, as in 1.0; BP_PSBBootstrap works this way). With Blueprint Owns Responses off, On Emit Response only observes and the transport sends.

## Deployment Guide
1.  **Install the plugin** from Fab, or copy `Plugins/PSB` into your project.
2.  **Signalling Server**: PSB works with Epic's reference signalling server (Cirrus) and with providers that use the standard Pixel Streaming protocol.
3.  **Web Client**: any page that sends the envelope through Pixel Streaming. Reference web packages and templates are separate.
4.  **Launch**: start the packaged app with the Pixel Streaming arguments, for example `-RenderOffScreen -PixelStreamingURL=ws://127.0.0.1:8888` (older form: `-PixelStreamingIP=127.0.0.1 -PixelStreamingPort=8888`). In the editor, the `scene_launch_args` tool prints the line for your project.

## The optional AI assistant layer
The editor modules serve tools over MCP (Model Context Protocol) to an AI assistant you connect yourself; see [AI_ASSISTANT_GUIDE.md](./AI_ASSISTANT_GUIDE.md).

The plugin never calls an AI service and never sends your project anywhere. The MCP server is part of the Unreal Editor session only (a packaged game does not contain it). It listens on 127.0.0.1, refuses requests from web pages and other machines, and needs a bearer token. Which assistant you connect, and what it does with what it reads, is your choice. Changes it makes to the level are undoable with Ctrl+Z, and file access is limited to the project folder.

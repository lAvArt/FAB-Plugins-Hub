# PSB - Technical Documentation & FAQ

## Technical Specifications
*   **Supported Engine Versions**: Unreal Engine 5.3+ (Tested on 5.6)
*   **Code Modules**:
    *   `PSB` (Runtime) - Core subsystem and messaging logic.
    *   `PSBTests` (DeveloperTool) - Automation tests.
*   **Network Protocol**: Uses standard Pixel Streaming Data Channels (WebRTC).
*   **Message Format**:
    ```json
    {
      "version": "1.0",
      "type": "command|event|response|error",
      "name": "namespace.action",
      "payload": { ... }
    }
    ```

## Architecture
PSB sits between the Pixel Streaming plugin and your game logic. It intercepts Data Channel messages, validates them against the PSB Envelope schema, and routes them to:
1.  **C++ Delegate** (`FPSBCommandRouter`)
2.  **Blueprint Event** (`OnCommandReceived`)

This ensures that only valid, structured JSON reaches your game logic, protecting against malformed data.

## Deployment Guide
1.  **Package Plugin**: Run the standard plugin packaging command or copy `Plugins/PSB` to your project.
2.  **Signalling Server**: PSB is compatible with the standard `Cirrus` server. For production, we recommend scalable solutions matching the standard Pixel Streaming protocol.
3.  **Web Client**: Deploy the provided Next.js template to Vercel, Netlify, or your preferred host.

## FAQ

**Q: Do I need to use the provided Web UI?**
A: No! You can use any web stack. As long as you send JSON messages matching the PSB schema (see `docs/message-contract.md`), Unreal will understand them.

**Q: Can I send large files?**
A: Pixel Streaming Data Channels are optimized for control signals (JSON). For large file transfers, consider using a separate HTTP API or checking Data Channel size limits.

**Q: Is this compatible with finding peers / matchmakers?**
A: Yes. PSB operates at the application layer inside Unreal. usage of matchmakers depends on your Signalling setup (Matchmaker -> SS -> Unreal).

**Q: Does it support Touch Input?**
A: Yes, standard Pixel Streaming input (Touch, Mouse, Keyboard) is passed through. PSB handles the *custom* application messages (UI interactions).

**Q: How do I debug messages?**
A: In `psb-ui`, enable `debug={true}` in `PSBProvider` to see a live log of all messages. In Unreal, use `LogPSB` to see incoming traffic.

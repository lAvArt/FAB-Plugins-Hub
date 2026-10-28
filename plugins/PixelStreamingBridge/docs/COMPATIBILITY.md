# Compatibility

From version 1.1.0 one source tree of the PSB plugin serves every supported engine version. Each download is made for one engine; code that differs between engine versions is selected at compile time (`ENGINE_MAJOR_VERSION` / `ENGINE_MINOR_VERSION`).

## Engine versions (PSB plugin 1.1.0)

| Engine | Status |
| :--- | :--- |
| **5.8** | Verified: packaged with Epic's `BuildPlugin` (strict includes, Editor and Game targets) |
| **5.7** | Verified: packaged as above; automation tests (23) run in the editor |
| **5.6** | Verified (5.6.1): built with the strict include check, live suite and automation tests pass |
| **5.5** | Verified: packaged as above |
| **5.4** | Verified (5.4.4): built, live suite and automation tests pass |
| **5.3** | Verified (5.3.2, built with the MSVC 14.38 toolset that 5.3 needs): live suite and automation tests pass |

All builds and tests were run on Windows (Win64). The plugin descriptor also allows Linux; Linux was not built here. macOS is not supported (the descriptor does not list it).

## Behaviour that depends on the engine version

- **Pixel Streaming input handlers.** From UE 5.4, Pixel Streaming passes the id of the sending peer to input handlers. PSB uses the 5.4+ handler signatures on 5.4 and later, and the 5.3 ones before. The JSON that reaches PSB is the same.
- **Automation tests** use the 5.5+ test flags on 5.5 and later.
- **JSON keys.** From UE 5.8 the keys of a JSON object are no longer `FString`; PSB reads them through a string view on every version.

Everything else (the subsystem, the manifest, Bind Command, replies, the editor tools) is the same on every supported version.

## Upgrading from 1.0
With the default settings, 1.1.0 behaves as 1.0 on every engine version: a Blueprint bound to On Emit Response sends the events (Blueprint Owns Responses, on), and the transport starts from a PSBBootstrap. Starting without a Bootstrap in packaged games (Auto Start Without Bootstrap) and observe-only On Emit Response are opt-in.

## Pixel Streaming

PSB is built on Epic's **Pixel Streaming** plugin (the first generation, `PixelStreaming`), which must be enabled. It does not use `PixelStreaming2`.

## Earlier branches

Before 1.1.0 the plugin source was kept in one branch per engine version (`main` for 5.3, `ue-5.x` for others). Since 1.1.0 one source tree serves every supported engine; on Fab, each engine version has its own download built from it.

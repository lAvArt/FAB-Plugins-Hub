# Architecture

## High-Level Data Flow

```mermaid
graph TD
    User[User / Browser] -->|Interacts| WebUI[Next.js Web UI]
    
    subgraph "Web Layer"
        WebUI -->|Config| ProviderConfig[Provider Config]
        WebUI -->|JSON Command| PixelStreaming[Pixel Streaming API]
    end

    subgraph "Transport"
        PixelStreaming <-->|WebRTC Data Channel| SignalingServer[Signaling Server]
    end

    subgraph "Unreal Engine"
        SignalingServer <-->|Data Channel| UE_PS[Pixel Streaming Plugin]
        UE_PS -->|Input Input| PSB_Subsystem[PSB Runtime Subsystem]
        
        PSB_Subsystem -->|Validate| SchemaValidator[JSON Schema Validator]
        SchemaValidator -->|Route| CommandRouter[Command Router]
        
        CommandRouter -->|Dispatch| GameLogic[Game/Business Logic]
        
        GameLogic -->|Emit Event| PSB_EventEmitter[PSB Event Emitter]
        PSB_EventEmitter -->|JSON Event| UE_PS
    end
```

## Core Components

### 1. Web UI (Reference)
- **Role**: Demonstrates how to connect, configure providers, and send commands.
- **Tech**: Next.js.
- **Key Files**: `psbClient.ts` (wraps the Pixel Stream emit functions).

### 2. PSB Runtime Subsystem (Unreal)
- **Role**: The central hub for the bridge. Lives on `GameInstance`.
- **Responsibilities**:
    - Listening to Pixel Streaming input.
    - Parsing inbound JSON.
    - Validating the envelope against `message-contract.md` (and, optionally, payloads against the message manifest).
    - Routing commands to registered delegates.
    - Emitting events via `SendEnvelopeJson`: a Blueprint bound to `OnEmitResponse` sends them, otherwise the C++ transport does (with **Blueprint Owns Responses** off, since 1.1.0, `OnEmitResponse` only observes and the transport sends).

### 3. Command Router
- **Role**: Maps string names (e.g., "spawn_object") to C++ Delegates or Blueprint Event Dispatchers.
- **Constraint**: strictly string-to-delegate. No hardcoded logic.
```

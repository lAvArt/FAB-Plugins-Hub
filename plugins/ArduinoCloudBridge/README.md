# Twinise | Arduino Cloud Bridge

**Unreal Engine Plugin for Arduino IoT Cloud**

Connect your Unreal Engine project to Arduino Cloud devices in minutes. Blueprint-first, production-ready, FAB-compliant.

[![UE Version](https://img.shields.io/badge/Unreal%20Engine-5.3%2B-blue)](https://www.unrealengine.com/)
[![Platforms](https://img.shields.io/badge/Platforms-Win64%20%7C%20Mac%20%7C%20Linux%20%7C%20Android%20%7C%20iOS-green)]()
[![Publisher](https://img.shields.io/badge/Publisher-Twinise-teal)](https://twinise.com/)
[![License](https://img.shields.io/badge/License-Proprietary-orange)]()

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start-5-minutes)
- [Core Concepts](#core-concepts)
- [Blueprint API Reference](#blueprint-api-reference)
- [Component & Actor System](#component--actor-system)
- [Editor Workflow](#editor-workflow)
- [Project Settings](#project-settings)
- [Error Handling](#error-handling)
- [Security Notes](#security-notes)
- [Troubleshooting](#troubleshooting)
- [Module Structure](#module-structure)
- [Requirements](#requirements)
- [Support](#support)
- [Examples](#examples)

---

## Features

### Core
- ✅ **OAuth2 Authentication** - Automatic token management with refresh before expiry
- ✅ **Read & Write Properties** - Full bidirectional communication with Arduino Cloud
- ✅ **Automatic Polling** - Configurable polling with retry logic and exponential backoff
- ✅ **Multi-Platform** - Win64, Mac, Linux, Android, iOS support

### Blueprint Integration
- ✅ **Runtime Subsystem** - Central access point for all Arduino Cloud operations
- ✅ **Device Component** - Attach to any actor for device-specific functionality
- ✅ **Device Actor** - Pre-built actor with billboard visualization and property bindings
- ✅ **Event-Driven** - Full delegate support for reactive Blueprint programming

### Value Types
- ✅ Boolean, Integer, Float, String
- ✅ Color (with hex string support)
- ✅ Enum (string or integer backing)
- ✅ CloudLight (HSB + Switch control)

### Editor Tools
- ✅ **Editor Window** - Visual device management (Window → Arduino Cloud)
- ✅ **Editor Subsystem** - Blueprint-accessible editor operations
- ✅ **Device Browser Widget** - C++ Slate-based device card list
- ✅ **Actor Spawning** - Spawn device actors from editor

### Error Handling & Diagnostics
- ✅ **Request Error Events** - Error code and message propagation
- ✅ **Connection Status Events** - Connected/disconnected notifications
- ✅ **Human-Readable Errors** - `GetErrorDescription()` helper on all classes
- ✅ **Validation Functions** - `ValidateConfiguration()`, `ValidateCredentials()`

---

## Quick Start (5 Minutes)

### 1. Get API Credentials
1. Go to [Arduino Cloud API Keys](https://cloud.arduino.cc/home/api-keys)
2. Create a new API key
3. Copy your **Client ID** and **Client Secret**

### 2. Configure in Editor
1. Open your UE project with the plugin enabled
2. Go to **Window → Arduino Cloud**
3. Enter your Client ID and Client Secret
4. Click **Save Credentials**
5. Click **Test Connection & List Devices**
6. *(Optional)* Set **Organization Id** in Project Settings for organization accounts

### 3. Use in Blueprints (Runtime)

```
Event BeginPlay
  → Get Game Instance
  → Get Subsystem (UArduinoCloudRuntimeSubsystem)
  → Bind to OnThingValuesUpdated
  → RefreshDevices
  → [Your Update Logic]
```

### 4. Read a Value

```
Get Subsystem (UArduinoCloudRuntimeSubsystem)
  → Get Value (ThingId, "temperature")
  → Break ArduinoValue
  → FloatValue → [Use Temperature]
```

### 5. Write a Value

```
Get Subsystem (UArduinoCloudRuntimeSubsystem)
  → Set Float Property (ThingId, "led_brightness", 0.75)
```

---

## Core Concepts

### Thing ID vs Device ID
- **Thing ID** - The unique identifier for an Arduino Cloud "Thing" (required for property access)
- **Device ID** - The hardware device identifier (deprecated in API, use ThingId)

### Property Key vs Property ID
- Both are accepted anywhere a property is needed
- The plugin automatically resolves names to IDs internally

### Polling vs Manual Refresh
- **Polling** - Automatic periodic fetching (controlled via Project Settings)
- **Manual** - Call `RefreshDevices()` or `RefreshDeviceValues()` explicitly

---

## Blueprint API Reference

### Runtime Subsystem (`UArduinoCloudRuntimeSubsystem`)

Access via: `Get Game Instance → Get Subsystem (ArduinoCloudRuntimeSubsystem)`

#### Read Operations
| Node | Description |
|------|-------------|
| `Get Devices` | Returns array of all cached Things |
| `Get Value (ThingId, PropertyKey)` | Get a specific property value |
| `Get All Values (ThingId)` | Get all properties for a Thing |
| `Get Raw Device JSON (ThingId)` | Debug: raw API response |
| `Ensure Devices Loaded` | Returns true if cached; triggers refresh if not |

#### Write Operations
| Node | Description |
|------|-------------|
| `Set Property Value` | Generic write (FArduinoValue struct) |
| `Set Bool Property` | Write boolean |
| `Set Int Property` | Write integer |
| `Set Float Property` | Write float/double |
| `Set String Property` | Write string |
| `Set Cloud Light Property` | Write full HSB + switch |
| `Set Cloud Light Switch` | Toggle switch only (preserves HSB) |

#### Control Operations
| Node | Description |
|------|-------------|
| `Refresh Devices` | Fetch Things list from cloud |
| `Refresh Device Values (ThingId)` | Fetch properties for specific Thing |
| `Enable Device List Polling` | Enable/disable automatic polling |
| `Set Credentials` | Inject credentials at runtime |

#### Diagnostics
| Node | Description |
|------|-------------|
| `Is Ready` | Check if subsystem is initialized |
| `Is Connected` | Check if connected to Arduino Cloud |
| `Validate Credentials` | Validate credentials with message output |
| `Get Error Description` | Convert error code to human-readable text |

#### Events
| Event | Parameters | Description |
|-------|------------|-------------|
| `On Devices Updated` | — | Fires when device list changes |
| `On Thing Values Updated` | ThingId | Fires when values are polled |
| `On Request Error` | Code, Message | Fires on API errors |
| `On Connection Status Changed` | bSuccess, Code, Message | Fires on connect/disconnect |

---

## Component & Actor System

### Device Component (`UArduinoCloudDeviceComponent`)

Add to any actor to link it to an Arduino Cloud Thing.

#### Properties
| Property | Description |
|----------|-------------|
| `Thing Id` | The Arduino Cloud Thing to link to |
| `Enable Editor Preview` | Update values in editor without PIE |
| `Local Poll Override Seconds` | Override global poll rate (0 = use global) |
| `Auto Sync On Edit` | Automatically push changes when edited |

#### Read Operations
| Node | Description |
|------|-------------|
| `Get Bool Property` | Read boolean by key |
| `Get Int Property` | Read integer by key |
| `Get Float Property` | Read float by key |
| `Get String Property` | Read string by key |
| `Get Property Value` | Read generic FArduinoValue |

#### Write Operations (Queue-Based)
| Node | Description |
|------|-------------|
| `Set Bool Property` | Queue boolean write |
| `Set Int Property` | Queue integer write |
| `Set Float Property` | Queue float write |
| `Set String Property` | Queue string write |
| `Set Cloud Light Property` | Queue CloudLight write |
| `Set Property Value` | Queue generic write |
| `Sync To Cloud` | Push all queued changes |
| `Has Pending Changes` | Check if changes are queued |
| `Clear Pending Changes` | Discard queued changes |

#### Control
| Node | Description |
|------|-------------|
| `Refresh From Cloud` | Fetch latest values |
| `Validate Configuration` | Check if properly configured |

#### Diagnostics
| Node | Description |
|------|-------------|
| `Is Connected` | Connection status |
| `Get Last Status Code` | Last HTTP status |
| `Get Last Status Message` | Last status message |
| `Get Error Description` | Error code to text |

#### Events
| Event | Description |
|-------|-------------|
| `On Values Updated` | Values refreshed from cloud |
| `On Property Changed` | Individual property changed |
| `On Request Error` | API error occurred |
| `On Connection Status Changed` | Connection state changed |
| `On Sync Complete` | SyncToCloud() finished |

### Device Actor (`AArduinoCloudDeviceActor`)

Pre-built actor with visual billboard and property binding system.

#### Property Bindings
Add entries to `PropertyBindings` array to map cloud properties to local values:
- **PropertyKey** - Cloud variable name (dropdown from cached properties)
- **Type** - Boolean, Integer, Float, String, Color, or CloudLight
- **Value Fields** - Sequencer-animatable value containers
- **Pull From Cloud** - Receive updates from cloud
- **Push To Cloud** - Send changes to cloud

#### CloudLight Support
- `CloudLightColor` - FLinearColor color picker
- `bCloudLightSwitchOn` - Toggle switch state

#### Actor-Specific Functions
| Node | Description |
|------|-------------|
| `Set Thing Id` | Change linked Thing |
| `Get Thing Id` | Get current Thing ID |
| `Push Local Changes To Cloud` | Sync all bindings |
| `Has Valid Thing Id` | Validation check |
| `Get Binding Count` | Number of property bindings |
| `Get Error Description` | Error code to text |

---

## Editor Workflow

### Editor Subsystem (`UArduinoCloudEditorSubsystem`)

Access via: `Get Editor Subsystem (ArduinoCloudEditorSubsystem)`

Provides editor-only operations for device management **without Play-In-Editor**.

#### Credential Management
| Node | Description |
|------|-------------|
| `Save Credentials` | Store Client ID and Secret |

#### Device Management
| Node | Description |
|------|-------------|
| `Refresh Devices` | Fetch Things list |
| `Refresh Device Values` | Fetch Thing properties |
| `Get Devices` | Get cached Things |
| `Get Value` / `Get All Values` | Read properties |

#### Write Operations
| Node | Description |
|------|-------------|
| `Set Property Value` | Write generic FArduinoValue |
| `Set Bool Property` | Write boolean |
| `Set Int Property` | Write integer |
| `Set Float Property` | Write float/double |
| `Set String Property` | Write string |
| `Set Cloud Light Property` | Write full HSB + switch |
| `Set Cloud Light Switch` | Toggle switch only (preserves HSB) |

#### Polling Control
| Node | Description |
|------|-------------|
| `Start Polling` | Begin automatic updates |
| `Stop Polling` | Stop automatic updates |
| `Enable Device List Polling` | Control what gets polled |
| `Is Polling Active` | Check polling state |

#### Actor Spawning
| Node | Description |
|------|-------------|
| `Spawn Device Actor` | Spawn at specific transform |
| `Spawn Device Actor At Editor Camera` | Spawn in front of viewport |
| `Spawn Device Actor At Selected Actor` | Spawn relative to selection |

#### Status Tracking
| Node | Description |
|------|-------------|
| `Get Devices Revision` | Change counter for devices |
| `Get Values Revision` | Change counter for values |
| `Get Last Devices Update Time` | Timestamp of last refresh |
| `Get Last Error Code/Message/Time` | Error tracking |
| `Get Last Connection Status` | Connection state details |

### Editor Utility Widget Workflow

Build custom editor tools using `UArduinoCloudEditorSubsystem`:

```
OnClicked_Connect
  → Get Editor Subsystem (UArduinoCloudEditorSubsystem)
  → Save Credentials (ClientId, ClientSecret)
  → Start Polling
  → Refresh Devices
```

### C++ Editor Utility Widget

`UArduinoCloudDeviceBrowserEUW` provides a Slate-based device card list with:
- Semantic search (name/id/property/type)
- Filters (writable/has properties/type)
- Auto-refresh on telemetry updates

---

## Project Settings

**Edit → Project Settings → Game → Arduino Cloud Bridge**

| Setting | Default | Description |
|---------|---------|-------------|
| Poll Rate | 1.0s | How often to fetch values (min 0.5s) |
| Cache Lifetime | 60s | How long to keep stale data |
| Auto Refresh On Init | Off | Fetch devices when subsystem initializes |
| Organization Id | *(empty)* | Header for organization accounts |
| Show Properties In Things List | On | Reduces per-Thing API requests |
| Request Retry Count | 3 | Retries for failed requests |
| Request Retry Base Delay | 0.5s | Base backoff delay |
| Request Retry Max Delay | 8.0s | Maximum backoff delay |
| Editor Preview | Off | Enable live values in Editor window |
| Verbose Logging | Off | Extra debug output |

---

## Error Handling

### Error Events
All classes expose `OnRequestError` delegate with:
- `ErrorCode` - HTTP status code (0 = connection failure)
- `ErrorMessage` - Raw error message from API

### Human-Readable Errors
Use `GetErrorDescription(ErrorCode)` to convert codes:

| Code | Description |
|------|-------------|
| 0 | Connection failed (check internet) |
| 400 | Bad request (check property names/values) |
| 401 | Unauthorized (check credentials) |
| 403 | Forbidden (check API key permissions) |
| 404 | Not found (check Thing ID / property name) |
| 422 | Invalid value type |
| 429 | Rate limited (increase poll rate) |
| 500+ | Server errors (retry later) |

### Validation Functions
- `ValidateConfiguration()` on Component - Returns success/failure with message
- `ValidateCredentials()` on Subsystem - Checks credential state

### Sync Feedback
Component's `OnSyncComplete` event fires after `SyncToCloud()`:
- `bSuccess` - Whether all changes were pushed
- `Message` - Details (e.g., "Synced 3 properties" or "Failed: temperature")

---

## Security Notes

### Credential Storage
- **Editor**: Stored in `EditorPerProjectUserSettings.ini` (project-specific, not in source control)
- **Runtime**: Credentials are NOT stored in `DefaultEngine.ini`

### Packaged Games
For shipped games, inject credentials at runtime:
```
Set Credentials (ClientId, ClientSecret)
```
Use encrypted config files or secure backend to provide credentials.

### OAuth2 Tokens
- Tokens auto-refresh before expiry
- No user action required after initial setup

---

## Troubleshooting

### "Auth Failed" Error
- Verify Client ID and Secret are correct
- Check your Arduino Cloud API key hasn't expired
- Ensure the API key has correct permissions

### No Devices Appearing
- Ensure your Arduino Cloud account has at least one "Thing" configured
- ThingId is required for property access
- Check Output Log for detailed error messages

### Rate Limiting (429 Errors)
- Increase Poll Rate in Project Settings
- Arduino Cloud has strict API limits (typically 1 request/second)
- Reduce number of simultaneous device refreshes

### Values Not Updating
- Check `Enable Editor Preview` is on for editor mode
- Verify ThingId is correct
- Ensure polling is active (`IsPollingActive()`)

### Write Operations Failing
- Check property is writable (not read-only in Arduino Cloud dashboard)
- Verify property type matches (use correct Set*Property function)
- Check `OnRequestError` for detailed error messages

---

## Module Structure

```
Plugins/ArduinoCloudBridge/
├── ArduinoCloudBridge.uplugin
├── README.md
├── Content/
│   └── StaticMeshes/          (Device visualization mesh)
└── Source/
    ├── ArduinoCloudBridgeRuntime/   (Game module - ships with game)
    │   ├── Public/
    │   │   ├── UArduinoCloudRuntimeSubsystem.h
    │   │   ├── ArduinoCloudDeviceComponent.h
    │   │   ├── ArduinoCloudDeviceActor.h
    │   │   ├── ArduinoCloudTypes.h
    │   │   └── ...
    │   └── Private/
    └── ArduinoCloudBridgeEditor/    (Editor module - editor only)
        ├── Public/
        │   ├── UArduinoCloudEditorSubsystem.h
        │   └── ...
        └── Private/
            └── Tests/               (Automation tests)
```

---

## Requirements

- **Unreal Engine**: 5.3+
- **Platforms**: Win64, Mac, Linux, Android, iOS (Runtime); Win64, Mac, Linux (Editor)
- **Arduino Cloud**: Account with API access ([Get API Key](https://cloud.arduino.cc/home/api-keys))

---

## Examples

### BP_CloudLight - Smart Light Actor

A pre-built example Blueprint derived from `AArduinoCloudDeviceActor` that responds to Arduino Cloud's **CloudLight** property type.

**Location:** `Plugins/ArduinoCloudBridge/Content/Blueprints/Examples/`

**Features:**
- Point Light with dynamic color from Arduino Cloud HSB values
- Emissive material that glows with the light color
- On/Off switch control
- Click-to-toggle interactivity

📄 **[Setup Instructions](Content/Blueprints/Examples/README.md)** | **[Full Tutorial](Docs/EXAMPLE_DEVICE_ACTOR_BLUEPRINT.md)**

### Creating Your Own Device Actor

Derive from `AArduinoCloudDeviceActor` to create custom device representations:

1. Right-click in Content Browser → Blueprint Class → Search `ArduinoCloudDeviceActor`
2. Add visual components (meshes, lights, particles)
3. Configure **Property Bindings** in the Details panel
4. Bind to `OnValuesUpdated` event to update visuals
5. Use `Get Cloud Light Property` / `Set Cloud Light Property` for CloudLight types

---

## Support

- **Documentation**: [User Guide](https://github.com/lAvArt/FAB-Plugins-Hub/blob/main/plugins/ArduinoCloudBridge/Docs/USER_GUIDE.md)
- **Issues**: [GitHub Issues](https://github.com/lAvArt/FAB-Plugins-Hub/tree/main/Issues)
- **Publisher**: [Twinise](https://twinise.com/)

---

## License

Proprietary. See LICENSE file for terms.

---

*Twinise | Arduino Cloud Bridge © 2026*

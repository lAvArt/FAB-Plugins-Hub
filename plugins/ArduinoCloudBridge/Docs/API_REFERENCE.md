# Arduino Cloud Bridge - API Reference

Complete API documentation for all Blueprint-exposed functions.

---

## Table of Contents

- [Runtime Subsystem](#runtime-subsystem)
- [Editor Subsystem](#editor-subsystem)
- [Device Component](#device-component)
- [Device Actor](#device-actor)
- [Data Types](#data-types)
- [Events & Delegates](#events--delegates)

---

## Runtime Subsystem

**Class:** `UArduinoCloudRuntimeSubsystem`  
**Access:** `Get Game Instance → Get Subsystem (ArduinoCloudRuntimeSubsystem)`  
**Availability:** Runtime + PIE

### Functions

#### Connection & Status

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Is Ready` | — | bool | True if subsystem is initialized |
| `Is Connected` | — | bool | True if connected to Arduino Cloud |
| `Validate Credentials` | out Message | bool | Validates current credentials |
| `Get Error Description` | ErrorCode | FString | Human-readable error message |

#### Device Operations

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Get Devices` | — | TArray\<FArduinoDevice\> | All cached Things |
| `Refresh Devices` | — | void | Fetch device list from cloud |
| `Refresh Device Values` | ThingId | void | Fetch properties for Thing |
| `Ensure Devices Loaded` | — | bool | Returns true if cached, triggers refresh if not |

#### Read Operations

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Get Value` | ThingId, PropertyKey | FArduinoValue | Get property value |
| `Get All Values` | ThingId | TMap\<FString, FArduinoValue\> | All properties for Thing |
| `Get Raw Device JSON` | ThingId | FString | Raw API response (debug) |

#### Write Operations

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Set Property Value` | ThingId, PropertyKey, Value | void | Generic write |
| `Set Bool Property` | ThingId, PropertyKey, Value | void | Write boolean |
| `Set Int Property` | ThingId, PropertyKey, Value | void | Write integer |
| `Set Float Property` | ThingId, PropertyKey, Value | void | Write float |
| `Set String Property` | ThingId, PropertyKey, Value | void | Write string |
| `Set Cloud Light Property` | ThingId, PropertyKey, Hue, Sat, Bri, Switch | void | Write CloudLight |
| `Set Cloud Light Switch` | ThingId, PropertyKey, bSwitchOn | void | Toggle CloudLight switch |

#### Polling Control

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Enable Device List Polling` | bEnable | void | Start/stop auto polling |
| `Set Credentials` | ClientId, ClientSecret | void | Set runtime credentials |

---

## Editor Subsystem

**Class:** `UArduinoCloudEditorSubsystem`  
**Access:** `Get Editor Subsystem (ArduinoCloudEditorSubsystem)`  
**Availability:** Editor only (EUW, Editor Blueprints)

### Functions

#### Credentials

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Save Credentials` | ClientId, ClientSecret | void | Save to editor config |

#### Device Operations

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Get Devices` | — | TArray\<FArduinoDevice\> | All cached Things |
| `Refresh Devices` | — | void | Fetch device list |
| `Refresh Device Values` | ThingId | void | Fetch Thing properties |
| `Get Value` | ThingId, PropertyKey | FArduinoValue | Get property value |
| `Get All Values` | ThingId | TMap\<FString, FArduinoValue\> | All properties |

#### Polling Control

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Start Polling` | — | void | Begin auto-refresh |
| `Stop Polling` | — | void | Stop auto-refresh |
| `Enable Device List Polling` | bEnable | void | Control polling |
| `Is Polling Active` | — | bool | Check polling state |

#### Actor Spawning

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Spawn Device Actor` | ThingId, Transform, bSelect | AActor* | Spawn at transform |
| `Spawn Device Actor At Editor Camera` | ThingId, Distance, bSelect | AActor* | Spawn at viewport |
| `Spawn Device Actor At Selected Actor` | ThingId, Offset, bSelect | AActor* | Spawn relative to selection |

#### Status

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Get Last Connection Status` | out bSuccess, out Code, out Message | bool | Get connection status |
| `Get Devices Revision` | — | int32 | Cache revision number |
| `Get Values Revision` | — | int32 | Values revision number |

---

## Device Component

**Class:** `UArduinoCloudDeviceComponent`  
**Add to:** Any Actor  

### Properties (Details Panel)

| Property | Type | Description |
|----------|------|-------------|
| `Thing Id` | FString | Arduino Cloud Thing ID |
| `Enable Editor Preview` | bool | Update in editor without PIE |
| `Local Poll Override Seconds` | float | Override global poll (0 = global) |
| `Auto Sync On Edit` | bool | Auto-push changes on property edit |

### Functions

#### Read Operations

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Get Bool Property` | PropertyKey | bool | Read boolean |
| `Get Int Property` | PropertyKey | int32 | Read integer |
| `Get Float Property` | PropertyKey | float | Read float |
| `Get String Property` | PropertyKey | FString | Read string |
| `Get Property Value` | PropertyKey | FArduinoValue | Read generic value |

#### Write Operations (Queue-Based)

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Set Bool Property` | PropertyKey, Value | void | Queue boolean write |
| `Set Int Property` | PropertyKey, Value | void | Queue integer write |
| `Set Float Property` | PropertyKey, Value | void | Queue float write |
| `Set String Property` | PropertyKey, Value | void | Queue string write |
| `Set Cloud Light Property` | PropertyKey, H, S, B, Switch | void | Queue CloudLight |
| `Set Property Value` | PropertyKey, Value | void | Queue generic write |

#### Sync Control

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Sync To Cloud` | — | void | Push all queued changes |
| `Has Pending Changes` | — | bool | Check if changes queued |
| `Clear Pending Changes` | — | void | Discard queued changes |
| `Refresh From Cloud` | — | void | Fetch latest values |

#### Validation

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Validate Configuration` | out Message | bool | Check if properly configured |
| `Is Connected` | — | bool | Connection status |
| `Resolve Thing Id` | — | FString | Get resolved Thing ID |

---

## Device Actor

**Class:** `AArduinoCloudDeviceActor`  
**Inherits:** AActor with UArduinoCloudDeviceComponent

### Properties (Details Panel)

#### Arduino Cloud

| Property | Type | Description |
|----------|------|-------------|
| `Thing Id` | FString | Arduino Cloud Thing ID |
| `Property Bindings` | TArray\<FArduinoPropertyBinding\> | Cloud-to-local mappings |

#### Billboard

| Property | Type | Description |
|----------|------|-------------|
| `Billboard Screen Size` | float | Size in editor viewport |
| `Show Billboard In Game` | bool | Visible in packaged game |

#### CloudLight

| Property | Type | Description |
|----------|------|-------------|
| `Cloud Light Color` | FLinearColor | HSB color picker |
| `Cloud Light Switch On` | bool | On/Off toggle |

### Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `Set Thing Id` | NewThingId | void | Change linked Thing |
| `Get Thing Id` | — | FString | Get current Thing ID |
| `Has Valid Thing Id` | — | bool | Validation check |
| `Push Local Changes To Cloud` | — | void | Sync all bindings |
| `Get Binding Count` | — | int32 | Number of bindings |
| `Get Error Description` | ErrorCode | FString | Error to text |

---

## Data Types

### FArduinoDevice

Represents an Arduino Cloud Thing.

| Field | Type | Description |
|-------|------|-------------|
| `Id` | FString | Thing ID (use this for API calls) |
| `Name` | FString | Display name |
| `DeviceId` | FString | Hardware device ID |
| `bOnline` | bool | Online status |
| `Properties` | TArray\<FArduinoPropertyMeta\> | Property metadata |

### FArduinoPropertyMeta

Metadata about a Thing property.

| Field | Type | Description |
|-------|------|-------------|
| `Id` | FString | Property ID |
| `Name` | FString | Property name/key |
| `DisplayName` | FString | Human-readable name |
| `Type` | EArduinoPropertyType | Value type |
| `bWritable` | bool | Can be written |
| `UpdatedAt` | FDateTime | Last update time |

### FArduinoValue

Container for property values.

| Field | Type | Description |
|-------|------|-------------|
| `BoolValue` | bool | Boolean data |
| `IntValue` | int32 | Integer data |
| `FloatValue` | float | Float data |
| `StringValue` | FString | String data |
| `ColorValue` | FLinearColor | Color data |
| `CloudLightHue` | float | CloudLight hue (0-360) |
| `CloudLightSaturation` | float | CloudLight saturation (0-100) |
| `CloudLightBrightness` | float | CloudLight brightness (0-100) |
| `bCloudLightSwitch` | bool | CloudLight on/off |
| `Type` | EArduinoPropertyType | Value type |
| `bIsValid` | bool | Has valid data |

### EArduinoPropertyType

Enumeration of property types.

| Value | Description |
|-------|-------------|
| `Boolean` | True/false |
| `Integer` | Whole number |
| `Float` | Decimal number |
| `String` | Text |
| `Color` | RGB color |
| `CloudLight` | HSB + switch |
| `Enum` | Enumerated value |
| `Unknown` | Unrecognized type |

### FArduinoPropertyBinding

Property binding for Device Actor.

| Field | Type | Description |
|-------|------|-------------|
| `PropertyKey` | FString | Cloud property name |
| `Type` | EArduinoPropertyType | Expected type |
| `bPullFromCloud` | bool | Receive updates |
| `bPushToCloud` | bool | Send changes |
| `BoolValue` | bool | Local bool storage |
| `IntValue` | int32 | Local int storage |
| `FloatValue` | float | Local float storage |
| `StringValue` | FString | Local string storage |
| `ColorValue` | FLinearColor | Local color storage |

---

## Events & Delegates

### Runtime Subsystem Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `OnDevicesUpdated` | — | Device list refreshed |
| `OnThingValuesUpdated` | ThingId (FString) | Properties updated |
| `OnRequestError` | Code (int32), Message (FString) | API error |
| `OnConnectionStatusChanged` | bSuccess, Code, Message | Connection state change |

### Device Component Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `OnValuesUpdated` | — | Values refreshed |
| `OnPropertyChanged` | PropertyKey (FString) | Single property changed |
| `OnRequestError` | Code, Message | API error |
| `OnConnectionStatusChanged` | bSuccess, Code, Message | Connection change |
| `OnSyncComplete` | bSuccess, Message | SyncToCloud finished |

### Editor Subsystem Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `OnDevicesUpdated` | — | Device list refreshed |
| `OnThingValuesUpdated` | ThingId | Properties updated |
| `OnRequestError` | Code, Message | API error |
| `OnConnectionStatusChanged` | bSuccess, Code, Message | Connection change |

---

## Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 0 | Success | — |
| 401 | Unauthorized | Check credentials |
| 403 | Forbidden | Check Organization ID |
| 404 | Not Found | Verify Thing/Property ID |
| 429 | Rate Limited | Reduce poll frequency |
| 500 | Server Error | Retry later |
| 502 | Bad Gateway | Arduino Cloud issue |
| 503 | Service Unavailable | Arduino Cloud maintenance |

---

*© 2026 Twinise. All rights reserved.*

# Changelog

All notable changes to Twinise | Arduino Cloud Bridge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-02-01

### Added

#### Core Features
- OAuth2 authentication with automatic token refresh
- Bidirectional property read/write with Arduino Cloud
- Automatic polling with configurable intervals and exponential backoff retry
- Multi-platform support: Win64, Mac, Linux, Android, iOS

#### Blueprint API
- `UArduinoCloudRuntimeSubsystem` - Central runtime access point
- `UArduinoCloudEditorSubsystem` - Editor-only operations
- `UArduinoCloudDeviceComponent` - Per-actor device linking
- `AArduinoCloudDeviceActor` - Pre-built actor with property bindings

#### Value Types
- Boolean, Integer, Float, String support
- Color values with hex string parsing
- Enum values (string or integer backing)
- CloudLight HSB + Switch control

#### Component System
- Property setters: `SetBoolProperty`, `SetIntProperty`, `SetFloatProperty`, `SetStringProperty`
- Property getters: `GetBoolProperty`, `GetIntProperty`, `GetFloatProperty`, `GetStringProperty`
- Queue-based writes with `SyncToCloud()`
- `HasPendingChanges()` and `ClearPendingChanges()` management

#### Error Handling
- `OnRequestError` delegate on all classes (Subsystem, Component, Actor)
- `OnConnectionStatusChanged` delegate for connection state
- `OnSyncComplete` delegate for sync feedback
- `GetErrorDescription()` static helper for human-readable errors
- `ValidateConfiguration()` on Component
- `ValidateCredentials()` on Subsystem
- `IsReady()` and `IsConnected()` diagnostics

#### Editor Tools
- Editor Window (Window → Arduino Cloud)
- Device Browser Widget (C++ Slate-based)
- Actor spawning: `SpawnDeviceActor`, `SpawnDeviceActorAtEditorCamera`
- Polling control: `StartPolling`, `StopPolling`, `IsPollingActive`

#### Property Bindings (Actor)
- Sequencer-compatible value fields
- Property key dropdown sourced from cached properties
- CloudLight color picker and switch toggle
- `PullFromCloud` and `PushToCloud` flags per binding

#### Project Settings
- Poll Rate (default 1.0s, min 0.5s)
- Cache Lifetime (default 60s)
- Auto Refresh On Init toggle
- Organization Id for org accounts
- Show Properties In Things List optimization
- Request Retry Count, Base Delay, Max Delay
- Editor Preview toggle
- Verbose Logging toggle

#### Testing
- Automation test framework integration
- Parser tests (all value types)
- Round-trip cache tests
- Error handling scenario tests
- Mock auth provider for isolated testing

#### Documentation
- Comprehensive README.md
- FAB Submission Guidelines
- Blueprint API reference
- Troubleshooting guide

---

## [Unreleased]

### Planned
- WebSocket support (pending Arduino Cloud API availability)
- Dashboard management integration
- Batch property operations
- Offline caching with sync-on-reconnect

---

*Twinise | Arduino Cloud Bridge*

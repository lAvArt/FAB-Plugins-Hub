# Arduino Cloud Bridge - User Guide

This guide will walk you through setting up and using the Arduino Cloud Bridge plugin in your Unreal Engine project.

## 1. Prerequisites

- **Unreal Engine**: Version 5.3 or newer.
- **Arduino Cloud Account**: An active account at [cloud.arduino.cc](https://cloud.arduino.cc).
- **API Keys**: You will need a Client ID and Client Secret.

## 2. Getting Started

### Generating API Keys
1.  Log in to the [Arduino IoT Cloud](https://create.arduino.cc/iot/things).
2.  Navigate to **Integrations** or go directly to the [API Keys page](https://cloud.arduino.cc/home/api-keys).
3.  Click **Create API Key**.
4.  **IMPORTANT**: Copy and save your **Client ID** and **Client Secret** immediately. They will not be shown again.

### Configuring the Plugin
1.  In Unreal Engine, go to **Window > Arduino Cloud**.
2.  Paste your **Client ID** and **Client Secret**.
3.  Click **Save Credentials**.
4.  Test the connection by clicking **List Devices**. If successful, your "Things" should appear in the log.

## 3. Blueprint Usage

### The Runtime Subsystem
The plugin uses a Game Instance Subsystem (`UArduinoCloudRuntimeSubsystem`) to manage API communication.

#### Initializing the Stream
Use the `Ensure Devices Loaded` node to trigger the initial fetch of your Arduino Things.

#### Receiving Updates
Bind to the `OnDeviceValuesUpdated` event to react when property values change on your devices.

#### Writing Values
Use the typed "Set Property" nodes:
- `Set Bool Property`
- `Set Int Property`
- `Set Float Property`
- `Set String Property`

## 4. Project Settings

Customize the behavior in **Project Settings > Game > Arduino Cloud Bridge**:
- **Poll Rate**: Frequency of API requests (suggested 1.0s or higher to avoid rate limits).
- **Auto Refresh**: Enable to automatically start polling on BeginPlay.
- **Verbose Logging**: Useful for debugging connection issues.

## 5. Troubleshooting

- **401 Unauthorized**: Double-check your API credentials.
- **429 Rate Limit**: Increase your Poll Rate in Project Settings.
- **No Devices Found**: Ensure your Arduino Things are correctly configured in the Arduino Cloud dashboard.

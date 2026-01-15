# Installation Guide

This guide covers the installation process for FAB plugins in Unreal Engine.

## Prerequisites

- Unreal Engine (see [Compatibility Information](../compatibility/README.md) for supported versions)
- Access to the Unreal Engine Marketplace (FAB)

## Installation Methods

### Method 1: Via Unreal Engine Marketplace (FAB)

This is the recommended installation method:

1. Open the Epic Games Launcher
2. Navigate to the Unreal Engine Marketplace (FAB)
3. Search for the plugin you want to install
4. Click "Install to Engine" or "Add to Project"
5. Select your target Unreal Engine version and project (if applicable)
6. Wait for the installation to complete

### Method 2: Manual Installation

If you have previously downloaded the plugin:

1. Locate your plugin files (.uplugin and associated folders)
2. Copy the plugin folder to one of these locations:
   - **Engine Plugins**: `[UE_Install_Directory]/Engine/Plugins/Marketplace/`
   - **Project Plugins**: `[Your_Project]/Plugins/`
3. Restart Unreal Engine
4. Open your project
5. Go to **Edit → Plugins**
6. Search for the plugin name
7. Enable the plugin
8. Restart the editor when prompted

## Post-Installation

### Verify Installation

1. Open Unreal Engine
2. Go to **Edit → Plugins**
3. Search for the plugin name
4. Verify it appears and is enabled

### First-Time Setup

Some plugins may require additional setup steps. Please refer to the specific plugin documentation in the `docs/` directory for detailed configuration instructions.

## Troubleshooting

### Plugin Not Appearing

- Verify the plugin is installed in the correct directory
- Check that your Unreal Engine version is compatible (see [Compatibility](../compatibility/README.md))
- Try restarting Unreal Engine
- Clear the `Intermediate` and `Saved` folders in your project

### Plugin Won't Enable

- Check the Output Log for error messages
- Verify all dependencies are met
- Ensure your project is compatible with the plugin version
- Review the [FAQ](faq.md) for common issues

### Build Errors

- Make sure your Unreal Engine version matches the plugin's compatible versions
- Try rebuilding your project
- Check the plugin's release notes for known issues

## Updating Plugins

1. Open the Epic Games Launcher
2. Navigate to your Library
3. Look for available updates in the "Marketplace" section
4. Click "Update" for the plugin
5. Restart Unreal Engine to use the updated version

**Note:** Always back up your project before updating plugins.

## Uninstalling Plugins

1. In Unreal Engine, go to **Edit → Plugins**
2. Search for the plugin
3. Uncheck "Enabled"
4. Restart the editor
5. (Optional) Delete the plugin folder from your installation directory

## Need Help?

If you encounter issues during installation, please:
- Review the [FAQ](faq.md)
- Check existing [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
- Create a new issue with details about your problem

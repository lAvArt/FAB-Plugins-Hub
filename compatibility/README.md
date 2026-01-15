# Compatibility Information

This directory contains compatibility information for all FAB plugins with different Unreal Engine versions.

## Supported Unreal Engine Versions

Compatibility information is organized by plugin. Please refer to the specific plugin documentation for detailed version support.

### General Compatibility Guidelines

- **Recommended**: The plugin is fully tested and recommended for use with this UE version
- **Supported**: The plugin works with this version but may have minor limitations
- **Experimental**: The plugin may work but is not fully tested
- **Not Supported**: The plugin is not compatible with this version

## Checking Compatibility

Before installing a plugin:

1. Check your Unreal Engine version (Help → About Unreal Engine)
2. Review the compatibility matrix for the specific plugin
3. Verify any dependencies or requirements
4. Check for known issues with your platform/engine version combination

## Platform Support

Platform compatibility varies by plugin. Common platforms include:
- Windows
- macOS
- Linux
- Android
- iOS
- PlayStation
- Xbox
- Nintendo Switch

Check individual plugin documentation for specific platform support details.

## Unreal Engine Version Matrix

Detailed compatibility matrices for each plugin will be maintained in plugin-specific subdirectories.

### Example Format

| Plugin | UE 5.5 | UE 5.4 | UE 5.3 | UE 5.2 | UE 5.1 | UE 4.27 |
|--------|--------|--------|--------|--------|--------|---------|
| Plugin A | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ |

**Legend:**
- ✅ Recommended/Supported
- ⚠️ Experimental or Limited Support
- ❌ Not Supported

## Dependencies

Some plugins may require:
- Specific Unreal Engine plugins to be enabled
- Certain engine versions for particular features
- Additional third-party plugins or libraries

All dependencies are documented in the individual plugin compatibility information.

## Upgrade Paths

When upgrading between Unreal Engine versions, please:
1. Check the compatibility information for the target version
2. Review release notes for migration notes
3. Test in a copy of your project before upgrading
4. Check for plugin updates that may be required

## Reporting Compatibility Issues

If you encounter compatibility issues:
1. Verify your engine and plugin versions
2. Check known issues in the release notes
3. Search existing [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
4. Report new issues with full version information

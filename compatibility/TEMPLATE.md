# Compatibility Matrix Template

Use this template when creating compatibility information for a specific plugin.

## Format

Create a file named `[plugin-name]-compatibility.md` in the `compatibility/` directory.

## Template

```markdown
# [Plugin Name] - Compatibility Matrix

Last Updated: YYYY-MM-DD

## Unreal Engine Version Support

| Plugin Version | UE 5.5 | UE 5.4 | UE 5.3 | UE 5.2 | UE 5.1 | UE 5.0 | UE 4.27 |
|----------------|--------|--------|--------|--------|--------|--------|---------|
| 2.0.x          | ✅     | ✅     | ✅     | ⚠️     | ❌     | ❌     | ❌      |
| 1.5.x          | ⚠️     | ✅     | ✅     | ✅     | ✅     | ⚠️     | ❌      |
| 1.0.x          | ❌     | ⚠️     | ✅     | ✅     | ✅     | ✅     | ✅      |

**Legend:**
- ✅ **Fully Supported** - Recommended and fully tested
- ⚠️ **Limited Support** - Works but may have limitations or experimental
- ❌ **Not Supported** - Not compatible or not tested

## Platform Compatibility

### Desktop Platforms

| Platform | Support Status | Notes |
|----------|---------------|-------|
| Windows  | ✅ Full       | All versions fully supported |
| macOS    | ✅ Full       | macOS 12.0+ required |
| Linux    | ⚠️ Experimental | Ubuntu 20.04+ tested |

### Mobile Platforms

| Platform | Support Status | Notes |
|----------|---------------|-------|
| Android  | ✅ Full       | Android 7.0+ required |
| iOS      | ✅ Full       | iOS 13.0+ required |

### Console Platforms

| Platform | Support Status | Notes |
|----------|---------------|-------|
| PlayStation 5 | ✅ Full | Requires PS5 SDK |
| PlayStation 4 | ⚠️ Limited | Performance limitations |
| Xbox Series X/S | ✅ Full | Requires Xbox GDK |
| Xbox One | ⚠️ Limited | Performance limitations |
| Nintendo Switch | ⚠️ Experimental | Contact for details |

## Build Configuration Support

| Configuration | Support Status |
|--------------|---------------|
| Development  | ✅ Supported  |
| DebugGame    | ✅ Supported  |
| Shipping     | ✅ Supported  |
| Debug        | ✅ Supported  |

## Dependencies

### Required Plugins

List any required Unreal Engine plugins:
- Enhanced Input (for UE5 projects using input features)
- [Other required plugins]

### Optional Plugins

List any optional plugins that enhance functionality:
- [Optional plugin 1]: Adds [feature]
- [Optional plugin 2]: Enables [capability]

### External Dependencies

List any external dependencies or SDKs:
- None / [List dependencies]

## Render Pipeline Support

| Render Pipeline | Support Status | Notes |
|----------------|---------------|-------|
| Deferred       | ✅ Full       | Default and recommended |
| Forward        | ✅ Full       | Fully supported |
| Mobile         | ⚠️ Limited    | Some features may be unavailable |

## Known Limitations

### By Unreal Engine Version

**UE 5.4+**
- [Any specific limitations for this version]

**UE 5.0-5.3**
- [Any specific limitations for these versions]

**UE 4.27**
- [Any specific limitations for this version]

### By Platform

**Mobile Platforms**
- [Mobile-specific limitations]

**Console Platforms**
- [Console-specific limitations]

## Feature Availability Matrix

| Feature | UE 5.x | UE 4.27 | Mobile | Consoles |
|---------|--------|---------|--------|----------|
| Feature 1 | ✅ | ✅ | ✅ | ✅ |
| Feature 2 | ✅ | ✅ | ⚠️ | ✅ |
| Feature 3 | ✅ | ❌ | ❌ | ⚠️ |

## Upgrade Notes

### Upgrading from UE 4.27 to UE 5.x

Important notes when migrating projects:
1. [Migration step 1]
2. [Migration step 2]
3. [Common issues and solutions]

### Upgrading Between UE 5.x Versions

Notes for upgrading between UE5 versions:
- [Compatibility notes]
- [Breaking changes]
- [Required updates]

## Testing Coverage

Platforms and versions we actively test:
- Windows 11 + UE 5.4
- macOS 14 + UE 5.4
- [Other tested configurations]

## Support Policy

- **Latest UE Release**: Full support within 2 weeks of release
- **Previous UE Release**: Full support maintained
- **Older Versions**: Critical bug fixes only
- **Deprecated Versions**: No support (marked as ❌)

## Getting Help

If you encounter compatibility issues:
1. Verify your versions match the compatibility matrix
2. Check [Known Issues](../releases/README.md)
3. Search [existing issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
4. Report new compatibility issues with:
   - Plugin version
   - Unreal Engine version
   - Platform details
   - Reproduction steps

## Changelog

Track when compatibility changes:

**2026-01-15**
- Added UE 5.5 support
- Deprecated UE 5.0 support

**2025-12-01**
- Initial compatibility matrix
```

## Best Practices

1. **Keep Updated**: Update the matrix with each plugin release
2. **Be Specific**: Include version numbers, not just "latest"
3. **Document Limitations**: Clearly state what doesn't work
4. **Test Coverage**: Only mark as supported what you've actually tested
5. **Update Dates**: Always include last updated date
6. **Migration Guides**: Provide upgrade paths for breaking changes

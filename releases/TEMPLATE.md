# Release Notes Template

Use this template when documenting a new plugin release.

## Format

Create a file named `[plugin-name]-v[version].md` in the `releases/` directory.

Example: `awesome-plugin-v1.2.0.md`

## Template

```markdown
# [Plugin Name] v[Version Number]

**Release Date:** YYYY-MM-DD

**Compatibility:** Unreal Engine [versions]

## Overview

Brief summary of this release. What are the highlights?

## Download

Available on [Unreal Engine Marketplace (FAB)](https://www.fab.com/)

## What's New

### ✨ New Features

#### Feature Name
Detailed description of the new feature, including:
- What it does
- How to use it
- Any configuration needed
- Screenshots or examples (if applicable)

#### Another Feature
[Same format as above]

### 🔧 Improvements

- **[Category]**: Description of improvement
- **[Category]**: Description of improvement
- **Performance**: Specific performance improvements and metrics
- **Usability**: User experience enhancements

### 🐛 Bug Fixes

- Fixed [specific issue] that caused [problem] ([Issue #123](link-to-issue))
- Resolved [bug description] in [component]
- Corrected [issue] when [conditions]

### 🔄 Changes

- **[Breaking]**: Description of breaking change and migration path
- **[Behavior Change]**: How behavior has changed
- Updated [component] to [new approach]

### 📦 Dependencies

- Added dependency on [package/plugin] v[version]
- Updated [dependency] from v[old] to v[new]
- Removed dependency on [package]

### 🗑️ Deprecated

- **[Feature/API]** is deprecated and will be removed in v[future-version]
  - Use [alternative] instead
  - Migration guide: [link or instructions]

### ❌ Removed

- Removed [feature/API] (deprecated in v[version])
- Removed support for [platform/version]

## Compatibility

### Unreal Engine Versions
- ✅ Fully Supported: UE [versions]
- ⚠️ Limited Support: UE [versions]
- ❌ Not Supported: UE [versions]

### Platform Support
- Windows: ✅
- macOS: ✅
- Linux: ⚠️
- Android: ✅
- iOS: ✅
- Consoles: [Status]

### Breaking Changes

If there are breaking changes, provide:

#### Change 1: [Description]

**Impact:** Who is affected and how

**Migration:**
```
// Old way
[old code example]

// New way
[new code example]
```

**Why:** Reason for the breaking change

## Known Issues

### Critical Issues
- **[Issue]**: Description, impact, and workaround (if available)

### Minor Issues
- [Issue]: Description and workaround

### Platform-Specific Issues
- **Windows**: [Issue]
- **macOS**: [Issue]
- **[Platform]**: [Issue]

## Installation

1. Open Epic Games Launcher
2. Navigate to your Library
3. Find [Plugin Name]
4. Click "Update" or "Install to Engine"
5. Restart Unreal Engine

For detailed instructions, see the [Installation Guide](../docs/installation.md).

## Upgrade Notes

### From v[previous-version]

Important notes when upgrading:
1. [Step or consideration]
2. [Step or consideration]
3. Backup your project before upgrading

### Configuration Changes

If you have custom configuration, you may need to:
- Update [setting] in [location]
- Migrate [old config] to [new config]

## Documentation

Updated documentation for this release:
- [Documentation page](link)
- [Tutorial](link)
- [API Reference](link)

## Performance Notes

### Improvements
- [Operation] is now [X]% faster
- Reduced memory usage by [amount] in [scenario]
- Optimized [system] for [use case]

### Benchmarks

| Operation | v[old] | v[new] | Improvement |
|-----------|--------|--------|-------------|
| [Task]    | 100ms  | 75ms   | 25% faster  |

## Community Contributions

Special thanks to:
- [Username] for reporting [Issue #123]
- [Username] for suggesting [Feature]
- All users who provided feedback on [topic]

## Technical Details

### Changed Files/Components
- Modified: [component list]
- Added: [new files]
- Removed: [removed files]

### API Changes

#### New APIs
```cpp
// Blueprint-callable
UFUNCTION(BlueprintCallable, Category="Category")
void NewFunction(FString Parameter);
```

#### Modified APIs
```cpp
// Old signature
void OldFunction(int32 Param);

// New signature  
void OldFunction(int32 Param, bool bNewParam = false);
```

#### Deprecated APIs
```cpp
// This function is deprecated
UE_DEPRECATED(5.4, "Use NewFunction instead")
void OldFunction();
```

## Support

Need help with this release?
- Review the [FAQ](../docs/faq.md)
- Check [Troubleshooting Guide](../docs/plugins/[plugin-name]/troubleshooting.md)
- Search [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
- Report new issues with the bug report template

## What's Next

Preview of what's coming in future releases:
- [Planned feature 1]
- [Planned feature 2]
- See the full [Roadmap](../ROADMAP.md)

## Previous Releases

- [v[version]](link) - Release date
- [v[version]](link) - Release date
- [View all releases](../releases/README.md)

---

**Full Changelog**: [v[old]...v[new]](link-if-applicable)
```

## Section Guidelines

### Overview
- Keep it concise (2-3 sentences)
- Highlight the most important changes
- Make it exciting for major releases

### What's New
- Group by type (Features, Improvements, Fixes)
- Use clear, user-focused language
- Include examples for complex features
- Add screenshots for visual changes

### Breaking Changes
- Always highlight breaking changes clearly
- Provide migration guides
- Explain the reason for the change
- Give examples of old vs. new code

### Known Issues
- Be transparent about problems
- Provide workarounds when available
- Link to tracking issues
- Set expectations for fixes

### Performance Notes
- Include specific metrics when possible
- Explain the context of improvements
- Note any trade-offs

## Best Practices

1. **Write for Users**: Focus on impact, not implementation
2. **Be Specific**: Use concrete examples and metrics
3. **Stay Organized**: Use consistent formatting
4. **Link Resources**: Connect to relevant documentation
5. **Update Regularly**: Keep information current
6. **Thank Contributors**: Acknowledge community input
7. **Set Expectations**: Be clear about support and known issues

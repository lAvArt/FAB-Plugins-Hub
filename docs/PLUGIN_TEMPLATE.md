# Plugin Documentation Template

This template should be used when adding documentation for a new plugin.

## Structure

Each plugin should have its own directory under `docs/plugins/[plugin-name]/` with the following structure:

```
docs/plugins/[plugin-name]/
├── README.md              # Plugin overview and quick start
├── installation.md        # Plugin-specific installation notes
├── user-guide.md         # Detailed usage instructions
├── api-reference.md      # Blueprint/C++ API documentation
├── examples.md           # Code examples and use cases
├── troubleshooting.md    # Common issues and solutions
└── changelog.md          # Plugin-specific changelog
```

## README.md Template

```markdown
# [Plugin Name]

Brief description of what the plugin does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Supported Versions

- Unreal Engine: 5.x, 4.27
- Platforms: Windows, Mac, Linux, etc.

## Quick Start

1. Install the plugin from FAB Marketplace
2. Enable it in your project
3. [First steps to use the plugin]

## Documentation

- [Installation](installation.md)
- [User Guide](user-guide.md)
- [API Reference](api-reference.md)
- [Examples](examples.md)
- [Troubleshooting](troubleshooting.md)

## Support

For issues and support, see the main [FAQ](../../faq.md) or create an [issue](https://github.com/lAvArt/FAB-Plugins-Hub/issues).
```

## Installation.md Template

```markdown
# [Plugin Name] - Installation

## Prerequisites

List any specific requirements for this plugin.

## Installation Steps

Follow the general [Installation Guide](../../installation.md) with these plugin-specific notes:

### Additional Configuration

Any plugin-specific configuration steps.

## Post-Installation

What to do after installing this plugin.

## Known Issues

Any known installation issues specific to this plugin.
```

## User Guide Template

```markdown
# [Plugin Name] - User Guide

## Overview

Detailed overview of the plugin's capabilities.

## Getting Started

### Basic Setup

Step-by-step setup instructions.

### Your First [Feature]

Tutorial for the primary use case.

## Core Features

### Feature 1

Detailed explanation with examples.

### Feature 2

Detailed explanation with examples.

## Advanced Usage

More complex scenarios and workflows.

## Best Practices

Recommended patterns and practices.

## Tips and Tricks

Helpful hints for power users.
```

## API Reference Template

```markdown
# [Plugin Name] - API Reference

## Blueprint Nodes

### Category 1

#### Node Name

**Description**: What this node does

**Inputs**:
- Input1 (Type): Description
- Input2 (Type): Description

**Outputs**:
- Output1 (Type): Description

**Example**: Brief usage example

## C++ Classes

### ClassName

**Header**: `PluginName/Public/ClassName.h`

**Description**: What this class does

#### Public Methods

##### MethodName

```cpp
ReturnType MethodName(ParamType Param1, ParamType Param2);
```

**Parameters**:
- `Param1`: Description
- `Param2`: Description

**Returns**: Description of return value

**Example**:
```cpp
// Code example
```
```

## Examples Template

```markdown
# [Plugin Name] - Examples

## Basic Examples

### Example 1: [Description]

**Use Case**: When to use this

**Blueprint**:
[Screenshot or description]

**C++**:
```cpp
// Code example
```

## Advanced Examples

### Example 2: [Description]

More complex example with detailed explanation.

## Sample Projects

Links to or descriptions of sample projects demonstrating the plugin.
```

## Troubleshooting Template

```markdown
# [Plugin Name] - Troubleshooting

## Common Issues

### Issue 1: [Description]

**Symptoms**: What the user sees

**Cause**: Why this happens

**Solution**: How to fix it

### Issue 2: [Description]

[Same format as above]

## Platform-Specific Issues

### Windows

Issues specific to Windows platform.

### Mac

Issues specific to Mac platform.

### Linux

Issues specific to Linux platform.

## Getting Help

If your issue isn't listed here:
1. Check the main [FAQ](../../faq.md)
2. Search [existing issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
3. Create a new issue with details
```

## Changelog Template

```markdown
# [Plugin Name] - Changelog

## [Version Number] - YYYY-MM-DD

### Added
- New feature descriptions

### Changed
- Modified functionality descriptions

### Fixed
- Bug fix descriptions

### Deprecated
- Features marked for removal

### Removed
- Removed features

### Security
- Security-related changes

## [Previous Version] - YYYY-MM-DD

[Same format as above]
```

## Guidelines

### Writing Style
- Be clear and concise
- Use active voice
- Include examples where helpful
- Use screenshots for UI elements
- Provide code samples for API usage

### Organization
- Start with most common use cases
- Progress from simple to complex
- Group related features together
- Use consistent terminology

### Maintenance
- Update documentation with each release
- Mark deprecated features clearly
- Add migration guides for breaking changes
- Keep examples up to date

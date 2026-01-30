# Frequently Asked Questions (FAQ)

## General Questions

### What is the FAB Plugins Hub?

The FAB Plugins Hub is a central repository for documentation, release notes, compatibility information, and updates for our Unreal Engine plugins. It does not contain source code.

### Where can I get the plugins?

All plugins are distributed through the Unreal Engine Marketplace (FAB). You can install them via the Epic Games Launcher.

### Is the source code available?

No, plugin source code is maintained privately. This repository only contains documentation and update information.

### How do I report a bug?

Please create an issue in the [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues) section using the bug report template.

### How do I request a feature?

You can submit feature requests through the [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues) section using the feature request template.

## Installation & Compatibility

### Which Unreal Engine versions are supported?

Please refer to the [Compatibility Information](../compatibility/README.md) for detailed version support information for each plugin.

### Can I use multiple plugins together?

Yes, our plugins are designed to work together. Check the compatibility information for any specific requirements or known interactions.

### The plugin won't enable in my project. What should I do?

1. Check the Output Log for specific error messages
2. Verify your Unreal Engine version is compatible
3. Ensure all dependencies are installed
4. Try creating a fresh project to test
5. Review the [Installation Guide](installation.md) troubleshooting section

### How do I update a plugin?

Updates are distributed through the Epic Games Launcher. Check your Library for available updates.

## Usage Questions

### Where can I find tutorials?

Tutorial content and usage guides are included in each plugin's specific documentation directory.

### Are there example projects?

Example projects and sample content may be included with plugins. Check the individual plugin documentation for details.

### Can I use these plugins in commercial projects?

Yes, all plugins purchased through the Unreal Engine Marketplace can be used in commercial projects according to the standard Epic Games Marketplace EULA.

## Technical Questions

### What platforms are supported?

Platform support varies by plugin. Check the individual plugin documentation for specific platform compatibility.

### Do the plugins support multiplayer/networking?

Multiplayer and networking support depends on the specific plugin. Refer to the plugin's documentation for details.

### Are Blueprint and C++ both supported?

Most plugins provide both Blueprint and C++ support. Check the specific plugin documentation for implementation details.

## Support & Community

### How can I get help?

1. Review this FAQ and plugin documentation
2. Search existing [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
3. Create a new issue if your question hasn't been answered

### Can I contribute to the documentation?

Yes! We welcome documentation contributions. Please see the [Contributing Guidelines](../CONTRIBUTING.md) for details.

### Where can I see what's planned for future updates?

Check the [Roadmap](../ROADMAP.md) for planned features and improvements.

## Troubleshooting

### My project crashes after installing a plugin

1. Check the compatibility information to ensure version compatibility
2. Review the crash log in `[Project]/Saved/Logs/`
3. Try disabling other plugins to identify conflicts
4. Report the issue with crash logs and reproduction steps

### The plugin is causing packaging errors

1. Verify all plugin dependencies are included
2. Check platform-specific requirements in the documentation
3. Review the Output Log during packaging
4. Ensure your project settings are configured correctly

### Performance issues after installing a plugin

1. Check the plugin documentation for performance considerations
2. Review your project's profiling data
3. Ensure you're using the latest plugin version
4. Report performance issues with specific metrics and reproduction steps

## Still Need Help?

If your question isn't answered here, please:
- Search the [Issues](https://github.com/lAvArt/FAB-Plugins-Hub/issues)
- Create a new issue with detailed information
- Include your Unreal Engine version, plugin version, and steps to reproduce

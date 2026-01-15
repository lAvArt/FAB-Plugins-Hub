# Repository Structure

This document explains the organization and purpose of each directory and file in the FAB Plugins Hub.

## Directory Overview

```
FAB-Plugins-Hub/
├── .github/              # GitHub configuration
│   └── ISSUE_TEMPLATE/   # Issue templates for bug reports, features, etc.
├── announcements/        # Official announcements and updates
├── compatibility/        # Unreal Engine version compatibility information
├── docs/                 # Main documentation directory
├── releases/            # Release notes and changelogs
├── CONTRIBUTING.md      # Guidelines for contributing
├── LICENSE              # Repository license (CC0 1.0)
├── README.md            # Main repository README
└── ROADMAP.md           # Development roadmap and planned features
```

## Directory Details

### `.github/`
Contains GitHub-specific configuration files.

**ISSUE_TEMPLATE/**
- `bug_report.md` - Template for bug reports
- `feature_request.md` - Template for feature requests
- `documentation.md` - Template for documentation issues
- `config.yml` - Issue template configuration with helpful links

### `announcements/`
Official announcements about plugins, updates, and events.

**Contents:**
- `README.md` - Overview and guide to announcements
- `YYYY-MM-DD-title.md` - Individual announcements (dated format)

**Purpose:** Keep users informed about major updates, changes, and news.

### `compatibility/`
Unreal Engine version and platform compatibility matrices.

**Contents:**
- `README.md` - General compatibility information
- `TEMPLATE.md` - Template for creating compatibility matrices
- `[plugin-name]-compatibility.md` - Plugin-specific compatibility info (future)

**Purpose:** Help users verify their setup is compatible before installation.

### `docs/`
Main documentation directory for all guides and references.

**Core Files:**
- `README.md` - Documentation hub and navigation
- `getting-started.md` - Introduction and quick start guide
- `installation.md` - Installation instructions
- `faq.md` - Frequently asked questions
- `PLUGIN_TEMPLATE.md` - Template for plugin-specific documentation

**Future Structure:**
```
docs/
├── plugins/
│   ├── [plugin-name]/
│   │   ├── README.md
│   │   ├── user-guide.md
│   │   ├── api-reference.md
│   │   ├── examples.md
│   │   └── troubleshooting.md
```

**Purpose:** Comprehensive documentation for all plugins and features.

### `releases/`
Release notes, changelogs, and version history.

**Contents:**
- `README.md` - Release notes overview and versioning info
- `TEMPLATE.md` - Template for creating release notes
- `[plugin-name]-v[version].md` - Individual release notes (future)

**Purpose:** Track changes, new features, and fixes for each release.

## Root Files

### `CONTRIBUTING.md`
Guidelines for contributing to the repository, including:
- How to report issues
- How to suggest features
- Documentation contribution guidelines
- Code of conduct

### `LICENSE`
Creative Commons CC0 1.0 Universal license for the documentation.

### `README.md`
Main repository introduction with:
- Repository purpose and overview
- Quick start guide
- Navigation to all sections
- Support information

### `ROADMAP.md`
Development roadmap showing:
- Features in progress
- Planned features
- Under consideration items
- Completed recent work

## File Naming Conventions

### Announcements
Format: `YYYY-MM-DD-descriptive-title.md`
Example: `2026-01-15-welcome.md`

### Release Notes
Format: `[plugin-name]-v[version].md`
Example: `awesome-plugin-v1.2.0.md`

### Compatibility Matrices
Format: `[plugin-name]-compatibility.md`
Example: `awesome-plugin-compatibility.md`

### Plugin Documentation
Format: `[plugin-name]/[document-type].md`
Example: `awesome-plugin/user-guide.md`

## Navigation Guide

### For New Users
1. Start with `README.md`
2. Read `docs/getting-started.md`
3. Follow `docs/installation.md`
4. Check `docs/faq.md` for common questions

### For Developers
1. Review `CONTRIBUTING.md`
2. Check `docs/PLUGIN_TEMPLATE.md` for documentation structure
3. Use `releases/TEMPLATE.md` for release notes format
4. Follow `compatibility/TEMPLATE.md` for compatibility info

### For Issue Reporters
1. Search existing issues first
2. Use appropriate template in `.github/ISSUE_TEMPLATE/`
3. Provide all requested information
4. Reference relevant documentation

### For Users Seeking Updates
1. Watch the repository for notifications
2. Check `announcements/` for news
3. Review `releases/` for changelogs
4. Follow `ROADMAP.md` for planned features

## Maintenance

### Adding New Plugin Documentation
1. Create directory: `docs/plugins/[plugin-name]/`
2. Use `docs/PLUGIN_TEMPLATE.md` as guide
3. Create compatibility matrix in `compatibility/`
4. Add initial release notes in `releases/`
5. Update main `docs/README.md` with links

### Creating New Release
1. Use `releases/TEMPLATE.md` as guide
2. Document all changes thoroughly
3. Update compatibility matrices if needed
4. Create announcement if major release
5. Update `ROADMAP.md` to mark completed items

### Adding Announcements
1. Create file: `announcements/YYYY-MM-DD-title.md`
2. Follow clear, informative format
3. Link to relevant documentation
4. Update `announcements/README.md` if needed

## Best Practices

### Documentation
- Keep it clear and concise
- Use examples where helpful
- Include screenshots for UI elements
- Link to related documentation
- Update with each release

### Organization
- Follow naming conventions
- Use templates for consistency
- Keep structure flat where possible
- Group related content together

### Maintenance
- Keep information current
- Archive outdated content
- Update links when files move
- Review and improve regularly

## Questions?

If you have questions about the repository structure:
- Check the [FAQ](docs/faq.md)
- Review [Contributing Guidelines](CONTRIBUTING.md)
- Create an issue for suggestions

---

*This structure is designed to be scalable as more plugins and documentation are added.*

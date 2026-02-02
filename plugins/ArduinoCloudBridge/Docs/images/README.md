# Documentation Images

This folder contains **SVG placeholder images** for the documentation. These are visual mockups showing what each screenshot should contain.

## Status: Replace with PNG Screenshots

Before publishing, replace each `placeholder-*.svg` with the actual `.png` screenshot.

---

## Placeholder Files (Current)

| SVG Placeholder | Replace With | Description |
|----------------|--------------|-------------|
| `placeholder-banner.svg` | `banner.png` | Marketing banner (1920×400) |
| `placeholder-arduino-cloud-menu.svg` | `arduino-cloud-menu.png` | Arduino Cloud menu (800×500) |
| `placeholder-project-settings.svg` | `project-settings.png` | Project Settings page (1000×600) |
| `placeholder-device-browser.svg` | `device-browser-euw.png` | Device Browser EUW (1200×700) |
| `placeholder-runtime-nodes.svg` | `runtime-subsystem-nodes.png` | Blueprint nodes (1400×900) |
| `placeholder-editor-nodes.svg` | `editor-subsystem-nodes.png` | Blueprint nodes (1400×800) |
| `placeholder-device-component.svg` | `device-component-details.png` | Details panel (500×600) |
| `placeholder-device-actor.svg` | `device-actor-details.png` | Details panel (500×750) |

---

## How to Capture Screenshots

### 1. Banner (`banner.png`)
- Use the AI-generated banner with your branding
- Dimensions: **1920 × 400 px**

### 2. Arduino Cloud Menu (`arduino-cloud-menu.png`)
- Open UE Editor → **Window → Arduino Cloud**
- Expand the menu to show all options
- Capture the full menu dropdown

### 3. Project Settings (`project-settings.png`)
- **Edit → Project Settings → Plugins → Arduino Cloud Bridge**
- Ensure all settings are visible
- Recommended: 1000×600 px

### 4. Device Browser EUW (`device-browser-euw.png`)
- Open the Device Browser via **Window → Arduino Cloud → Open Device Browser**
- Ensure at least one device is visible with properties expanded
- Show the Log and About panels (collapsed or expanded)
- Recommended: 1200×700 px

### 5. Runtime Subsystem Nodes (`runtime-subsystem-nodes.png`)
- Open a Level Blueprint or Actor Blueprint
- Right-click → search "Arduino Cloud Runtime Subsystem"
- Arrange key nodes: Get Devices, Get Value, Set Bool Property, Set Cloud Light Property
- Include event nodes: On Devices Updated, On Thing Values Updated
- Recommended: 1400×900 px

### 6. Editor Subsystem Nodes (`editor-subsystem-nodes.png`)
- Create/open an Editor Utility Widget or Editor Blueprint
- Right-click → search "Arduino Cloud Editor Subsystem"
- Arrange key nodes: Spawn Device Actor, Save Credentials, Start/Stop Polling
- Recommended: 1400×800 px

### 7. Device Component Details (`device-component-details.png`)
- Add `Arduino Cloud Device Component` to any actor
- Select the component, capture the Details panel
- Show: Thing Id, Enable Editor Preview, Local Poll Override
- Recommended: 500×600 px

### 8. Device Actor Details (`device-actor-details.png`)
- Place `Arduino Cloud Device Actor` in a level
- Select it and capture the Details panel
- Show: Thing Id, Property Bindings, Billboard settings, Cloud Light
- Recommended: 500×750 px

---

## After Capturing

1. Save as `.png` with the exact names above
2. Update `USER_GUIDE.md` to reference `.png` instead of `.svg`:
   - Find: `placeholder-*.svg`
   - Replace with corresponding `.png` filename
3. Delete the `.svg` placeholder files

Example update in USER_GUIDE.md:
```diff
- ![Device Browser EUW](images/placeholder-device-browser.svg)
+ ![Device Browser EUW](images/device-browser-euw.png)
```

---

*These placeholders were auto-generated to show the expected content and layout.*

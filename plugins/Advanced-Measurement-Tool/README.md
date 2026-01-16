# Advanced Measurement Tool (AMT)

A professional-grade measurement and analysis plugin for Unreal Engine 5, designed to give level designers, architects, and QA teams precise control over their spatial data.

![AMT Banner](https://via.placeholder.com/1200x300?text=Advanced+Measurement+Tool)

## Overview

The **Advanced Measurement Tool (AMT)** extends the Unreal Editor with a suite of precise measurement utilities. Whether you need to measure the distance between two vertices, calculate the surface area of a complex floor plan, or check the bounding volume of an asset, AMT provides the tools you need directly in the viewport.

**Current Version:** v1.0  
**Supported Engine Versions:** 5.0+

## Features

### 📏 Core Measurement Tools
*   **Distance**: Measure linear distance in 3D space. Includes ground projection (show horizontal distance) and slope angle display.
*   **Angle**: Measure the precise angle between any three points.
*   **Area**: Define complex polygons point-by-point to calculate surface area.
*   **Volume**: 
    *   **Bounds Mode**: Measure the Axis-Aligned Bounding Box (AABB) of any actor.
    *   **Geometry Mode**: Calculate the exact geometric volume of static meshes.

### 🧲 Advanced Snapping
Precision is key. AMT includes a robust snapping system:
*   **Grid Snap**: Accurately snap to the editor grid spacing.
*   **Vertex Snap**: Snap to the nearest vertex of any static mesh.
*   **Bounds Snap**: Snap to the corners and center points of actor bounds.

### 📊 Data Management
*   **Measurement History**: Automatically tracks your session's measurements.
*   **Import/Export**: Save your measurements to JSON or CSV for external reporting and analysis.
*   **Visual Customization**: Fully configurable colors, line thickness, and font sizes to match your workflow.

## Installation

1.  Close Unreal Editor.
2.  Download the `AdvancedMeasurementTool` folder.
3.  Copy it into your project's `Plugins` directory (e.g., `MyProject/Plugins/`).
4.  Launch Unreal Editor.
5.  Go to `Edit > Plugins` and ensure **Advanced Measurement Tool** is enabled.

## Usage Guide

### Activation
Open the AMT Dashboard by clicking the **Toolbar Button** (Ruler Icon) or using the shortcut (default `Shift + M`).

### Controls

| Tool | Shortcut | Action |
| :--- | :--- | :--- |
| **Distance** | `D` | Click Start -> Click End. Hold `Shift` to drag the end point. |
| **Angle** | `A` | Click Apex -> Click Start -> Click End. |
| **Area** | `R` | Click multiple points to define shape. Press `Enter` to close loop. |
| **Volume** | `V` | Hover over an actor and click to measure. |
| **Clear** | `Delete` | Remove the currently selected measurement. |
| **Exit Tool** | `Esc` | Stop the current measurement action. |

### Dashboard Overview
The main dashboard gives you quick access to:
*   **Tool Selection**: Switch between Distance, Angle, Area, and Volume modes.
*   **Snapping Toggles**: Quickly enable/disable Grid, Vertex, and Bounds snapping.
*   **History**: Review past measurements. Click the "Eye" icon to hide/show individual measurements.
*   **Settings**: Configure units (Metric/Imperial), colors, and more.

## Updates

This plugin includes an integrated **Update Checker**. It will automatically check for new versions on startup (configurable in Project Settings) and notify you if an update is available.

---

**Developed by lAvArt Studio**  
[www.lavartstudio.com](http://www.lavartstudio.com)  
[GitHub Repository](https://github.com/lAvArt/FAB-Plugins-Hub/tree/main/plugins/Advanced-Measurement-Tool)

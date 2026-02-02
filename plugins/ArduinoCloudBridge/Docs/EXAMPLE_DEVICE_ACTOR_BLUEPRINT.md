# Example: BP_CloudLight - Smart Light Actor

This guide walks you through creating `BP_CloudLight`, a Blueprint Actor derived from `AArduinoCloudDeviceActor` that responds to Arduino Cloud's **CloudLight** property type.

**Example Location:** `Plugins/ArduinoCloudBridge/Content/Blueprints/Examples/`

---

## Overview

The CloudLight property type in Arduino Cloud combines:
- **Hue** (0-360) - Color wheel position
- **Saturation** (0-100) - Color intensity  
- **Brightness** (0-100) - Light level
- **Switch** (on/off) - Power state

By deriving from `AArduinoCloudDeviceActor`, your Blueprint automatically inherits:
- ✅ Arduino Cloud connection management
- ✅ Property binding system (Sequencer-compatible)
- ✅ Automatic polling and synchronization
- ✅ Event delegates for value updates
- ✅ Built-in error handling

---

## Step 1: Create the Blueprint

1. In the Content Browser, navigate to `Plugins/ArduinoCloudBridge/Content/Blueprints/Examples/`
2. Right-click and select **Blueprint Class**
3. In the "Pick Parent Class" dialog, search for `ArduinoCloudDeviceActor`
4. Select **ArduinoCloudDeviceActor** and click **Select**
5. Name it `BP_CloudLight`

---

## Step 2: Add Components

1. Open `BP_CloudLight`
2. In the Components panel, add:
   - **Point Light**
   - **Box Collision** → For overlap interaction

Your component hierarchy:
```
DefaultSceneRoot
├── BillboardComponent (inherited - editor visualization)
├── PointLight
└── BoxCollision
```

---

## Step 3: Configure Property Binding

In the Details panel (Class Defaults):

1. Find **Arduino Cloud** category
2. Expand **Property Bindings**
3. Click **+** to add one binding:

| Property Key | Type | Pull From Cloud | Push To Cloud |
|-------------|------|-----------------|---------------|
| `light` | CloudLight | ✅ | ✅ |

> **Note:** The property key must match your Arduino Cloud variable name exactly.

---

## Step 4: Implement Event Graph

### BeginPlay

```
Event BeginPlay
│
└─→ Bind Event to OnPropertyChanged
      └─→ OnPropertyChanged_Event (Custom Event)
```

### OnPropertyChanged_Event

```
Custom Event: OnPropertyChanged_Event
│   Parameter: PropertyKey (String)
│
└─→ Get Cloud Light Property
      Target: self
      Property Key: PropertyKey
      │
      └─→ Branch (Return Value - success check)
            │
            ├─ True:
            │    → Set Light Color (PointLight, OutColor)
            │    → Select Float
            │        Pick A: OutSwitchOn
            │        A: 5000.0 (on)
            │        B: 0.0 (off)
            │        └─→ Set Intensity (PointLight)
            │
            └─ False:
                 → Print String ("Property Not Found!")
```

### On Component Begin Overlap (BoxCollision)

```
On Component Begin Overlap (BoxCollision)
│
├─→ Get Cloud Light Property ("light")
│     Returns: OutColor, OutSwitchOn
│
├─→ NOT Boolean (OutSwitchOn)
│     Returns: NewSwitchState
│
├─→ Set Cloud Light Property
│     Property Key: "light"
│     Color: OutColor (keep current color)
│     bSwitchOn: NewSwitchState
│
└─→ Push Local Changes To Cloud
```

---

## Step 5: Place in Level

1. Drag `BP_CloudLight` into your level
2. Select the actor
3. In Details panel → **Arduino Cloud**:
   - Set **Thing Id** (copy from Arduino Cloud dashboard)
4. Play the level!

---

## Key Nodes Reference

| Node | Category | Description |
|------|----------|-------------|
| `Get Cloud Light Property` | Arduino Cloud \| Read | Returns color, switch state, and success bool |
| `Set Cloud Light Property` | Arduino Cloud \| Write | Sets color and switch state |
| `Push Local Changes To Cloud` | Arduino Cloud | Syncs pending changes to cloud |
| `OnPropertyChanged` | Arduino Cloud \| Events | Fires when a property changes (with key) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Light not changing color | Verify `Thing Id` is set; check property key matches Arduino Cloud |
| Switch not working | Ensure `bPushToCloud` is enabled on the binding |
| "Property Not Found!" | Check that PropertyKey matches your Arduino Cloud variable name |
| No updates from cloud | Check connection in Window → Arduino Cloud |

---

*Twinise | Arduino Cloud Bridge © 2026*

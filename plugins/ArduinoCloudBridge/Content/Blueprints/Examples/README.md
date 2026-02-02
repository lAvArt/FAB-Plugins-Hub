# Arduino Cloud Bridge Examples

This folder contains example Blueprints derived from `AArduinoCloudDeviceActor`.

---

## BP_CloudLight

A smart light actor that responds to Arduino Cloud's **CloudLight** property type.

### Features
- Point Light with dynamic color from Arduino Cloud
- Intensity controlled by switch state (on/off)
- Toggle on overlap interaction

### Setup Instructions

1. **Create the Blueprint**
   - Right-click in this folder → Blueprint Class
   - Search for and select `ArduinoCloudDeviceActor`
   - Name it `BP_CloudLight`

2. **Add Components**
   ```
   DefaultSceneRoot
   ├── BillboardComponent (inherited)
   ├── PointLight
   └── BoxCollision (for overlap interaction)
   ```

3. **Configure Property Binding**
   - Select the actor (Class Defaults)
   - In **Arduino Cloud → Property Bindings**, add:
     | Property Key | Type | Pull | Push |
     |-------------|------|------|------|
     | `light` | CloudLight | ✅ | ✅ |

4. **Event Graph**

   ```
   ┌─────────────────────────────────────────────────────────────┐
   │ EVENT BEGINPLAY                                              │
   │ ────────────────                                             │
   │ BeginPlay → Bind Event to OnPropertyChanged                  │
   │               └─→ OnPropertyChanged_Event (Custom Event)     │
   │                                                              │
   ├─────────────────────────────────────────────────────────────┤
   │ CUSTOM EVENT: OnPropertyChanged_Event (PropertyKey: String)  │
   │ ───────────────────────────────────────────────────────────  │
   │                                                              │
   │ OnPropertyChanged_Event                                      │
   │   → Get Cloud Light Property (PropertyKey)                   │
   │       → Branch (Return Value - success check)                │
   │           │                                                  │
   │           ├─ True:                                           │
   │           │    → Set Light Color (PointLight, OutColor)      │
   │           │    → Select Float (OutSwitchOn)                  │
   │           │        A: 5000.0 (on)                            │
   │           │        B: 0.0 (off)                              │
   │           │        → Set Intensity (PointLight)              │
   │           │                                                  │
   │           └─ False:                                          │
   │                → Print String ("Property Not Found!")        │
   │                                                              │
   ├─────────────────────────────────────────────────────────────┤
   │ ON COMPONENT BEGIN OVERLAP (BoxCollision)                    │
   │ ─────────────────────────────────────────                    │
   │                                                              │
   │ OnComponentBeginOverlap                                      │
   │   → Get Cloud Light Property ("light")                       │
   │   → NOT Boolean (OutSwitchOn)                                │
   │   → Set Cloud Light Property ("light", OutColor, !SwitchOn)  │
   │   → Push Local Changes To Cloud                              │
   └─────────────────────────────────────────────────────────────┘
   ```

5. **Place in Level**
   - Drag `BP_CloudLight` into your level
   - Set the **Thing Id** in Details panel
   - Play!

---

*Twinise | Arduino Cloud Bridge © 2026*

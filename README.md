# Modifier Batch Apply

> A Blender addon that brings the full modifier workflow to multiple objects at once.

![Blender](https://img.shields.io/badge/Blender-4.2%2B-orange?logo=blender)
![License](https://img.shields.io/badge/License-GPL--3.0-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-green)

---

## Features

| Feature | Description |
|---|---|
| **15 Modifiers** | Mirror, Subsurf, Solidify, Bevel, Array, Triangulate, Decimate, Smooth, Weld, Cast, Displace, Screw, Simple Deform, Wireframe, Remesh |
| **Batch Target** | Apply to **selected objects** or **all mesh objects** in the scene |
| **Add / Sync / Apply / Remove** | Full modifier lifecycle from a single panel |
| **Stack Order** | Move any modifier up/down in the stack across all targets |
| **Copy from Active** | Duplicate all modifiers from the active object to selected ones |
| **Apply ALL** | One-click apply every modifier on every target (with confirmation) |
| **Remove ALL** | One-click remove everything (with confirmation) |
| **Live Values** | Panel values are wired with `update=` callbacks — changes reflect immediately on objects that already have the modifier |
| **Blender 4.2 / 5.0+** | Uses `context.temp_override`, `# type: ignore` annotations and runtime API guards |

---

## Installation

### Legacy Add-on (Blender 4.2 Preferences)

1. Download the latest `.zip` from [Releases](../../releases)
2. Open Blender → **Edit → Preferences → Add-ons → Install**
3. Select `modifier_batch_apply.zip` and click **Install Add-on**
4. Enable the checkbox next to **"Modifier Batch Apply"**

### From Source

```bash
git clone https://github.com/yourname/modifier-batch-apply.git
```

Copy the `modifier_batch_apply/` folder into your Blender addons directory:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Blender Foundation\Blender\4.x\scripts\addons\` |
| macOS | `~/Library/Application Support/Blender/4.x/scripts/addons/` |
| Linux | `~/.config/blender/4.x/scripts/addons/` |

---

## Usage

1. Open the **N Panel** in the 3D Viewport (`N` key)
2. Go to the **"Modifiers"** tab
3. Choose your target: **Selected Objects** or **All Objects**
4. Expand any modifier section (Mirror, Bevel, etc.)
5. Tweak the values — objects with that modifier already applied will update in real time
6. Click **Add** to add the modifier to targets, **Apply** to make it permanent, or **Remove** to discard it

### Button Reference

| Button | Action |
|---|---|
| **Add** | Adds the modifier with current panel values to targets that don't have it yet |
| **Sync** | Pushes current panel values to targets that **already** have the modifier |
| **Apply** | Applies (makes permanent) the modifier on all targets |
| **Remove** | Removes the modifier from all targets without applying |
| **↑ / ↓** | Moves the modifier up or down in the stack on all targets |
| **Apply ALL** | Applies every modifier on every target (confirmation required) |
| **Remove ALL** | Removes every modifier from every target (confirmation required) |
| **Copy from Active** | Copies all modifiers from the active object to other selected objects |

---

## Project Structure

```
modifier_batch_apply/
├── __init__.py        # bl_info, register/unregister wiring
├── core.py            # Target resolution, setup functions, apply helper
├── operators.py       # All bpy.types.Operator classes
├── panels.py          # All N-panel Panel classes
├── properties.py      # PropertyGroup with all modifier settings
└── ui.py              # Shared UI helpers (header_row, action_row)
```

---

## Compatibility

| Blender Version | Status |
|---|---|
| 4.2 LTS | ✅ Tested |
| 4.3 | ✅ Tested |
| 4.4+ / 5.0+ | ✅ Tested |
| 3.6 LTS | ⚠️ Use the [3.6 branch](../../tree/blender-3.6) |

---

## Contributing

Pull requests are welcome! Please open an issue first to discuss what you would like to change.

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
```

---

## License

[GPL-3.0](LICENSE) — same as Blender itself.

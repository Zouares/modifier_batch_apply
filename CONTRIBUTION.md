# Contributing to Modifier Batch Apply

Thank you for your interest in contributing! This document outlines how to get started, the project structure, and the conventions used throughout the codebase.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Coding Conventions](#coding-conventions)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Adding a New Modifier](#adding-a-new-modifier)

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/modifier_batch_apply.git
   ```
3. Create a **feature branch** from `master`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes, commit, and push:
   ```bash
   git commit -m "Add: short description of your change"
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request** against `master`.

> **Please open an issue first** to discuss larger changes before investing time in an implementation. This avoids duplicate work and ensures the change aligns with the project's direction.

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

| File | Responsibility |
|---|---|
| `__init__.py` | Entry point — defines `bl_info` and wires `register()`/`unregister()` |
| `core.py` | Pure logic — target resolution, modifier setup, apply helpers |
| `operators.py` | All `bpy.types.Operator` subclasses (Add, Sync, Apply, Remove, etc.) |
| `panels.py` | All `bpy.types.Panel` subclasses that build the N-panel UI |
| `properties.py` | The main `PropertyGroup` with every modifier parameter |
| `ui.py` | Reusable UI row builders (`header_row`, `action_row`) |

---

## Development Setup

### Requirements

- **Blender 4.2 LTS or later** (4.3, 4.4, 5.0+ are also tested)
- Python 3.11+ (bundled with Blender — no external interpreter needed)

### Installing from Source

Copy (or symlink) the `modifier_batch_apply/` folder into your Blender addons directory:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Blender Foundation\Blender\4.x\scripts\addons\` |
| macOS | `~/Library/Application Support/Blender/4.x/scripts/addons/` |
| Linux | `~/.config/blender/4.x/scripts/addons/` |

Then enable it under **Edit → Preferences → Add-ons**.

### Reloading During Development

Use Blender's **Reload Scripts** (`F3` → search "Reload Scripts") to pick up code changes without restarting Blender.

---

## Coding Conventions

- **Style:** Follow [PEP 8](https://peps.python.org/pep-0008/). Use 4-space indentation.
- **Type annotations:** Add `# type: ignore` where the Blender API stubs are incomplete — this keeps the codebase compatible with Blender 4.2+ without requiring external stub packages.
- **Operator naming:** Use the `modifier_batch_apply.` prefix for all `bl_idname` values (e.g. `modifier_batch_apply.add_mirror`).
- **Property updates:** Wire modifier properties with `update=` callbacks so changes reflect immediately on objects that already own the modifier.
- **Context overrides:** Use `context.temp_override(...)` for any operator that must run on a specific object — never manipulate `bpy.context` directly.
- **Commits:** Use an imperative prefix: `Add:`, `Fix:`, `Refactor:`, `Docs:`, `Chore:`.

---

## Submitting Changes

- Keep pull requests **focused** — one feature or fix per PR.
- Describe *what* changed and *why* in the PR description.
- If your PR closes an issue, include `Closes #<issue-number>` in the description.
- Make sure the addon registers and unregisters cleanly with no Python errors in the Blender console.
- Test against **Blender 4.2 LTS** as the minimum supported version.

---

## Reporting Issues

When filing a bug, please include:

1. **Blender version** (e.g. 4.3.2)
2. **OS and architecture** (e.g. Windows 11 x64)
3. **Steps to reproduce** — what you did, what you expected, what happened
4. **Error output** from the Blender system console (Window → Toggle System Console on Windows)
5. A minimal `.blend` file if applicable

---

## Adding a New Modifier

The codebase is structured so that new modifiers follow a clear, repeatable pattern:

1. **`properties.py`** — Add a new `PropertyGroup` subclass (or extend the main one) with all parameters for the modifier. Wire `update=` callbacks pointing to a sync function in `core.py`.
2. **`core.py`** — Add a `setup_<modifier>()` function that applies property values to a modifier instance, and register it in the target-resolution helpers.
3. **`operators.py`** — Reuse the generic `Add`, `Sync`, `Apply`, and `Remove` operator pattern, passing your modifier's type string.
4. **`panels.py`** — Add a collapsible section to the N-panel using the `header_row` / `action_row` helpers from `ui.py`.
5. **`__init__.py`** — Register any new classes.
6. Update **`README.md`** to list the new modifier in the Features table.

---

## License

By contributing, you agree that your contributions will be licensed under the [GPL-3.0 License](LICENSE) that covers this project.

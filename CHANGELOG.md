# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] - 2025-01-01

### Added
- Initial release
- 15 modifiers: Mirror, Subdivision Surface, Solidify, Bevel, Array, Triangulate, Decimate, Smooth, Weld, Cast, Displace, Screw, Simple Deform, Wireframe, Remesh
- Batch target: Selected Objects or All Objects in scene
- Add / Sync / Apply / Remove per modifier type
- Apply ALL and Remove ALL with confirmation dialog
- Copy modifiers from active object to selected objects
- Move modifier up/down in stack across all targets
- Live value update via `update=` callbacks
- Blender 4.2 / 5.0+ compatibility with `context.temp_override` and runtime API guards
- N Panel under "Modifiers" tab in the 3D Viewport

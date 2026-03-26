bl_info = {
    "name": "Modifier Batch Apply",
    "author": "Zouares",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "View3D > N Panel > Modifiers",
    "description": "Add, tweak and apply modifiers in batch across multiple objects",
    "doc_url": "https://github.com/Zouares/modifier_batch_apply",
    "tracker_url": "https://github.com/Zouares/modifier_batch_apply/issues",
    "category": "Object",
}

from . import properties, operators, panels

def register():
    properties.register()
    operators.register()
    panels.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()

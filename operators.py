import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty
from . import core


class MBA_OT_AddModifier(Operator):
    bl_idname      = "mba.add_modifier"
    bl_label       = "Add Modifier"
    bl_description = "Add this modifier to target objects (does not apply)"
    bl_options     = {'REGISTER', 'UNDO'}

    mod_type: StringProperty()  # type: ignore

    def execute(self, context):
        p       = context.scene.mba_props
        objs    = core.get_targets(context)
        setup   = core.MODIFIER_SETUP_MAP.get(self.mod_type)

        if not objs:
            self.report({'WARNING'}, "No valid mesh objects found.")
            return {'CANCELLED'}

        added = 0
        for obj in objs:
            if self.mod_type not in [m.type for m in obj.modifiers]:
                mod = obj.modifiers.new(
                    name=self.mod_type.replace('_', ' ').title(),
                    type=self.mod_type
                )
                if setup:
                    setup(mod, p)
                added += 1
            else:
                self.report({'INFO'}, f"{obj.name} already has {self.mod_type}")

        self.report({'INFO'}, f"Added {self.mod_type} to {added} object(s).")
        return {'FINISHED'}


class MBA_OT_ApplyModifier(Operator):
    bl_idname      = "mba.apply_modifier"
    bl_label       = "Apply Modifier"
    bl_description = "Apply (make permanent) this modifier on target objects"
    bl_options     = {'REGISTER', 'UNDO'}

    mod_type: StringProperty()  # type: ignore

    def execute(self, context):
        objs    = core.get_targets(context)
        applied = 0

        for obj in objs:
            names = [m.name for m in obj.modifiers if m.type == self.mod_type]
            for n in names:
                if core.apply_mod(context, obj, n):
                    applied += 1

        self.report({'INFO'}, f"Applied {self.mod_type} on {applied} modifier(s).")
        return {'FINISHED'}


class MBA_OT_RemoveModifier(Operator):
    bl_idname      = "mba.remove_modifier"
    bl_label       = "Remove Modifier"
    bl_description = "Remove this modifier from target objects without applying"
    bl_options     = {'REGISTER', 'UNDO'}

    mod_type: StringProperty()  # type: ignore

    def execute(self, context):
        objs    = core.get_targets(context)
        removed = 0

        for obj in objs:
            for m in [x for x in obj.modifiers if x.type == self.mod_type]:
                obj.modifiers.remove(m)
                removed += 1

        self.report({'INFO'}, f"Removed {removed} {self.mod_type} modifier(s).")
        return {'FINISHED'}


class MBA_OT_ApplyAll(Operator):
    bl_idname      = "mba.apply_all"
    bl_label       = "Apply ALL Modifiers"
    bl_description = "Apply every modifier on target objects"
    bl_options     = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        objs    = core.get_targets(context)
        applied = 0

        for obj in objs:
            names = [m.name for m in obj.modifiers]
            for n in names:
                if core.apply_mod(context, obj, n):
                    applied += 1

        self.report({'INFO'}, f"Applied {applied} modifier(s) total.")
        return {'FINISHED'}


class MBA_OT_RemoveAll(Operator):
    bl_idname      = "mba.remove_all"
    bl_label       = "Remove ALL Modifiers"
    bl_description = "Remove every modifier from target objects without applying"
    bl_options     = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        objs    = core.get_targets(context)
        removed = 0

        for obj in objs:
            for m in list(obj.modifiers):
                obj.modifiers.remove(m)
                removed += 1

        self.report({'INFO'}, f"Removed {removed} modifier(s) total.")
        return {'FINISHED'}


class MBA_OT_SyncModifier(Operator):
    bl_idname      = "mba.sync_modifier"
    bl_label       = "Sync Values"
    bl_description = "Push current panel values to existing modifiers on target objects"
    bl_options     = {'REGISTER', 'UNDO'}

    mod_type: StringProperty()  # type: ignore

    def execute(self, context):
        p     = context.scene.mba_props
        objs  = core.get_targets(context)
        setup = core.MODIFIER_SETUP_MAP.get(self.mod_type)

        if not setup:
            self.report({'WARNING'}, f"No setup function for {self.mod_type}")
            return {'CANCELLED'}

        synced = 0
        for obj in objs:
            for mod in [m for m in obj.modifiers if m.type == self.mod_type]:
                setup(mod, p)
                synced += 1

        self.report({'INFO'}, f"Synced {synced} {self.mod_type} modifier(s).")
        return {'FINISHED'}


class MBA_OT_CopyFromActive(Operator):
    bl_idname      = "mba.copy_from_active"
    bl_label       = "Copy Modifiers from Active"
    bl_description = "Copy all modifiers from the active object to selected objects"
    bl_options     = {'REGISTER', 'UNDO'}

    def execute(self, context):
        active = context.active_object
        if not active or active.type != 'MESH':
            self.report({'WARNING'}, "Active object must be a mesh.")
            return {'CANCELLED'}

        targets = [o for o in context.selected_objects if o.type == 'MESH' and o != active]
        if not targets:
            self.report({'WARNING'}, "Select at least one other mesh object.")
            return {'CANCELLED'}

        copied = 0
        for obj in targets:
            for src_mod in active.modifiers:
                if src_mod.type not in [m.type for m in obj.modifiers]:
                    new_mod = obj.modifiers.new(name=src_mod.name, type=src_mod.type)
                    for attr in src_mod.bl_rna.properties.keys():
                        if attr in ('rna_type', 'type', 'name'):
                            continue
                        try:
                            setattr(new_mod, attr, getattr(src_mod, attr))
                        except Exception:
                            pass
                    copied += 1

        self.report({'INFO'}, f"Copied {copied} modifier(s) to {len(targets)} object(s).")
        return {'FINISHED'}


class MBA_OT_MoveModifier(Operator):
    bl_idname      = "mba.move_modifier"
    bl_label       = "Move Modifier"
    bl_description = "Move modifier up or down in the stack on all target objects"
    bl_options     = {'REGISTER', 'UNDO'}

    mod_type:  StringProperty()   # type: ignore
    direction: StringProperty(default='UP')  # type: ignore

    def execute(self, context):
        objs  = core.get_targets(context)
        moved = 0

        for obj in objs:
            for mod in [m for m in obj.modifiers if m.type == self.mod_type]:
                with context.temp_override(object=obj, active_object=obj):
                    try:
                        bpy.ops.object.modifier_move_up(modifier=mod.name) \
                            if self.direction == 'UP' else \
                            bpy.ops.object.modifier_move_down(modifier=mod.name)
                        moved += 1
                    except Exception:
                        pass

        self.report({'INFO'}, f"Moved {moved} modifier(s) {self.direction.lower()}.")
        return {'FINISHED'}


CLASSES = [
    MBA_OT_AddModifier,
    MBA_OT_ApplyModifier,
    MBA_OT_RemoveModifier,
    MBA_OT_ApplyAll,
    MBA_OT_RemoveAll,
    MBA_OT_SyncModifier,
    MBA_OT_CopyFromActive,
    MBA_OT_MoveModifier,
]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)

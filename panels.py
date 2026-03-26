import bpy
from bpy.types import Panel
from . import ui

_S = 'VIEW_3D'
_R = 'UI'
_C = "Modifiers"
_P = "MBA_PT_main"
_CLOSED = {'DEFAULT_CLOSED'}


class MBA_PT_main(Panel):
    bl_label      = "Modifier Batch Apply"
    bl_idname     = "MBA_PT_main"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C

    def draw(self, context):
        layout = self.layout
        p      = context.scene.mba_props
        v      = bpy.app.version

        if p.show_info:
            box = layout.box()
            row = box.row()
            row.label(text=f"Blender {v[0]}.{v[1]}.{v[2]}", icon='INFO')
            objs = [o for o in context.selected_objects if o.type == 'MESH']
            row.label(text=f"{len(objs)} mesh selected")

        box = layout.box()
        box.label(text="Settings", icon='SETTINGS')
        box.prop(p, "target", expand=True)
        box.prop(p, "show_info")

        layout.separator()
        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mba.apply_all",   icon='CHECKMARK')
        col.operator("mba.remove_all",  icon='TRASH')

        layout.separator()
        layout.operator("mba.copy_from_active", icon='COPYDOWN')


class MBA_PT_mirror(Panel):
    bl_label = "Mirror"; bl_idname = "MBA_PT_mirror"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'MIRROR', "Mirror", 'MOD_MIRROR')
        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Axis:")
        row.prop(p, "mirror_x", toggle=True)
        row.prop(p, "mirror_y", toggle=True)
        row.prop(p, "mirror_z", toggle=True)
        row2 = col.row(align=True)
        row2.label(text="Bisect:")
        row2.prop(p, "mirror_bisect_x", toggle=True)
        row2.prop(p, "mirror_bisect_y", toggle=True)
        row2.prop(p, "mirror_bisect_z", toggle=True)
        col.separator()
        col.prop(p, "mirror_clipping")
        col.prop(p, "mirror_merge")
        layout.separator()
        ui.action_row(layout, 'MIRROR')


class MBA_PT_subsurf(Panel):
    bl_label = "Subdivision Surface"; bl_idname = "MBA_PT_subsurf"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'SUBSURF', "Subdivision Surface", 'MOD_SUBSURF')
        col = layout.column(align=True)
        col.prop(p, "subsurf_type")
        col.prop(p, "subsurf_levels")
        col.prop(p, "subsurf_render_levels")
        col.prop(p, "subsurf_optimal")
        layout.separator()
        ui.action_row(layout, 'SUBSURF')


class MBA_PT_solidify(Panel):
    bl_label = "Solidify"; bl_idname = "MBA_PT_solidify"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'SOLIDIFY', "Solidify", 'MOD_SOLIDIFY')
        col = layout.column(align=True)
        col.prop(p, "solidify_thickness")
        col.prop(p, "solidify_offset")
        col.prop(p, "solidify_fill_rim")
        layout.separator()
        ui.action_row(layout, 'SOLIDIFY')


class MBA_PT_bevel(Panel):
    bl_label = "Bevel"; bl_idname = "MBA_PT_bevel"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'BEVEL', "Bevel", 'MOD_BEVEL')
        col = layout.column(align=True)
        col.prop(p, "bevel_limit_method")
        col.prop(p, "bevel_width")
        col.prop(p, "bevel_segments")
        col.prop(p, "bevel_profile")
        if p.bevel_limit_method == 'ANGLE':
            col.prop(p, "bevel_angle_limit")
        layout.separator()
        ui.action_row(layout, 'BEVEL')


class MBA_PT_array(Panel):
    bl_label = "Array"; bl_idname = "MBA_PT_array"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'ARRAY', "Array", 'MOD_ARRAY')
        col = layout.column(align=True)
        col.prop(p, "array_count")
        col.separator()
        col.label(text="Relative Offset:")
        col.prop(p, "array_offset_x")
        col.prop(p, "array_offset_y")
        col.prop(p, "array_offset_z")
        col.separator()
        col.prop(p, "array_merge")
        if p.array_merge:
            col.prop(p, "array_merge_dist")
        layout.separator()
        ui.action_row(layout, 'ARRAY')


class MBA_PT_triangulate(Panel):
    bl_label = "Triangulate"; bl_idname = "MBA_PT_triangulate"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'TRIANGULATE', "Triangulate", 'MOD_TRIANGULATE')
        col = layout.column(align=True)
        col.prop(p, "tri_quad_method")
        col.prop(p, "tri_ngon_method")
        layout.separator()
        ui.action_row(layout, 'TRIANGULATE')


class MBA_PT_decimate(Panel):
    bl_label = "Decimate"; bl_idname = "MBA_PT_decimate"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'DECIMATE', "Decimate", 'MOD_DECIM')
        col = layout.column(align=True)
        col.prop(p, "decimate_ratio")
        col.prop(p, "decimate_use_symmetry")
        layout.separator()
        ui.action_row(layout, 'DECIMATE')


class MBA_PT_smooth(Panel):
    bl_label = "Smooth"; bl_idname = "MBA_PT_smooth"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'SMOOTH', "Smooth", 'MOD_SMOOTH')
        col = layout.column(align=True)
        col.prop(p, "smooth_factor")
        col.prop(p, "smooth_repeat")
        row = col.row(align=True)
        row.label(text="Axis:")
        row.prop(p, "smooth_x", toggle=True)
        row.prop(p, "smooth_y", toggle=True)
        row.prop(p, "smooth_z", toggle=True)
        layout.separator()
        ui.action_row(layout, 'SMOOTH')


class MBA_PT_weld(Panel):
    bl_label = "Weld"; bl_idname = "MBA_PT_weld"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'WELD', "Weld", 'AUTOMERGE_OFF')
        col = layout.column(align=True)
        col.prop(p, "weld_distance")
        col.prop(p, "weld_mode")
        layout.separator()
        ui.action_row(layout, 'WELD')


class MBA_PT_cast(Panel):
    bl_label = "Cast"; bl_idname = "MBA_PT_cast"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'CAST', "Cast", 'MOD_CAST')
        col = layout.column(align=True)
        col.prop(p, "cast_type")
        col.prop(p, "cast_factor")
        col.prop(p, "cast_radius")
        row = col.row(align=True)
        row.label(text="Axis:")
        row.prop(p, "cast_x", toggle=True)
        row.prop(p, "cast_y", toggle=True)
        row.prop(p, "cast_z", toggle=True)
        layout.separator()
        ui.action_row(layout, 'CAST')


class MBA_PT_displace(Panel):
    bl_label = "Displace"; bl_idname = "MBA_PT_displace"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'DISPLACE', "Displace", 'MOD_DISPLACE')
        col = layout.column(align=True)
        col.prop(p, "displace_direction")
        col.prop(p, "displace_strength")
        col.prop(p, "displace_mid_level")
        layout.separator()
        ui.action_row(layout, 'DISPLACE')


class MBA_PT_screw(Panel):
    bl_label = "Screw"; bl_idname = "MBA_PT_screw"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'SCREW', "Screw", 'MOD_SCREW')
        col = layout.column(align=True)
        col.prop(p, "screw_axis")
        col.prop(p, "screw_angle")
        col.prop(p, "screw_steps")
        col.prop(p, "screw_iter")
        layout.separator()
        ui.action_row(layout, 'SCREW')


class MBA_PT_simple_deform(Panel):
    bl_label = "Simple Deform"; bl_idname = "MBA_PT_simple_deform"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'SIMPLE_DEFORM', "Simple Deform", 'MOD_SIMPLEDEFORM')
        col = layout.column(align=True)
        col.prop(p, "simple_deform_method")
        col.prop(p, "simple_deform_axis")
        if p.simple_deform_method in ('TWIST', 'BEND'):
            col.prop(p, "simple_deform_angle")
        else:
            col.prop(p, "simple_deform_factor")
        layout.separator()
        ui.action_row(layout, 'SIMPLE_DEFORM')


class MBA_PT_wireframe(Panel):
    bl_label = "Wireframe"; bl_idname = "MBA_PT_wireframe"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'WIREFRAME', "Wireframe", 'MOD_WIREFRAME')
        col = layout.column(align=True)
        col.prop(p, "wireframe_thickness")
        col.prop(p, "wireframe_offset")
        col.prop(p, "wireframe_use_replace")
        col.prop(p, "wireframe_use_boundary")
        layout.separator()
        ui.action_row(layout, 'WIREFRAME')


class MBA_PT_remesh(Panel):
    bl_label = "Remesh"; bl_idname = "MBA_PT_remesh"
    bl_space_type = _S; bl_region_type = _R; bl_category = _C
    bl_parent_id = _P; bl_options = _CLOSED

    def draw(self, context):
        layout = self.layout
        p = context.scene.mba_props
        ui.header_row(layout, 'REMESH', "Remesh", 'MOD_REMESH')
        col = layout.column(align=True)
        col.prop(p, "remesh_mode")
        if p.remesh_mode == 'VOXEL':
            col.prop(p, "remesh_voxel_size")
        else:
            col.prop(p, "remesh_octree_depth")
        col.prop(p, "remesh_smooth_normals")
        layout.separator()
        ui.action_row(layout, 'REMESH')


CLASSES = [
    MBA_PT_main,
    MBA_PT_mirror,
    MBA_PT_subsurf,
    MBA_PT_solidify,
    MBA_PT_bevel,
    MBA_PT_array,
    MBA_PT_triangulate,
    MBA_PT_decimate,
    MBA_PT_smooth,
    MBA_PT_weld,
    MBA_PT_cast,
    MBA_PT_displace,
    MBA_PT_screw,
    MBA_PT_simple_deform,
    MBA_PT_wireframe,
    MBA_PT_remesh,
]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)

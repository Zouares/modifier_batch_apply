import bpy


def get_targets(context):
    p = context.scene.mba_props
    if p.target == 'ALL':
        return [o for o in context.scene.objects if o.type == 'MESH']
    return [o for o in context.selected_objects if o.type == 'MESH']


def get_or_create(obj, mod_type):
    for m in obj.modifiers:
        if m.type == mod_type:
            return m
    return obj.modifiers.new(name=mod_type.replace('_', ' ').title(), type=mod_type)


def sync(mod_type, setup_fn):
    ctx = bpy.context
    p   = ctx.scene.mba_props
    flag = f"active_{mod_type.lower()}"
    if not getattr(p, flag, False):
        return
    for obj in get_targets(ctx):
        mod = get_or_create(obj, mod_type)
        setup_fn(mod, p)


def apply_mod(context, obj, mod_name):
    if mod_name not in obj.modifiers:
        return False
    prev = context.view_layer.objects.active
    context.view_layer.objects.active = obj
    if obj.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    try:
        with context.temp_override(object=obj, active_object=obj):
            bpy.ops.object.modifier_apply(modifier=mod_name)
        return True
    except Exception as e:
        print(f"[MBA] apply error '{mod_name}' on '{obj.name}': {e}")
        return False
    finally:
        context.view_layer.objects.active = prev


def setup_mirror(mod, p):
    mod.use_axis[0] = p.mirror_x
    mod.use_axis[1] = p.mirror_y
    mod.use_axis[2] = p.mirror_z
    if hasattr(mod, 'use_bisect_axis'):
        mod.use_bisect_axis[0] = p.mirror_bisect_x
        mod.use_bisect_axis[1] = p.mirror_bisect_y
        mod.use_bisect_axis[2] = p.mirror_bisect_z
    for attr in ('use_clip', 'use_mirror_u'):
        pass
    if hasattr(mod, 'use_clip'):
        mod.use_clip = p.mirror_clipping
    if hasattr(mod, 'use_mirror_merge'):
        mod.use_mirror_merge = p.mirror_merge


def setup_subsurf(mod, p):
    mod.subdivision_type = p.subsurf_type
    mod.levels           = p.subsurf_levels
    mod.render_levels    = p.subsurf_render_levels
    if hasattr(mod, 'show_only_control_edges'):
        mod.show_only_control_edges = p.subsurf_optimal


def setup_solidify(mod, p):
    mod.thickness  = p.solidify_thickness
    mod.offset     = p.solidify_offset
    mod.use_rim    = p.solidify_fill_rim


def setup_bevel(mod, p):
    mod.width        = p.bevel_width
    mod.segments     = p.bevel_segments
    mod.profile      = p.bevel_profile
    mod.limit_method = p.bevel_limit_method
    if p.bevel_limit_method == 'ANGLE':
        mod.angle_limit = p.bevel_angle_limit


def setup_array(mod, p):
    mod.count = p.array_count
    mod.relative_offset_displace[0] = p.array_offset_x
    mod.relative_offset_displace[1] = p.array_offset_y
    mod.relative_offset_displace[2] = p.array_offset_z
    mod.use_merge_vertices = p.array_merge
    if p.array_merge:
        mod.merge_threshold = p.array_merge_dist


def setup_triangulate(mod, p):
    mod.quad_method = p.tri_quad_method
    mod.ngon_method = p.tri_ngon_method


def setup_decimate(mod, p):
    mod.ratio = p.decimate_ratio
    if hasattr(mod, 'use_symmetry'):
        mod.use_symmetry = p.decimate_use_symmetry


def setup_smooth(mod, p):
    mod.factor = p.smooth_factor
    mod.use_x  = p.smooth_x
    mod.use_y  = p.smooth_y
    mod.use_z  = p.smooth_z
    for attr in ('iterations', 'repeat'):
        if hasattr(mod, attr):
            try:
                setattr(mod, attr, p.smooth_repeat)
            except Exception:
                pass


def setup_weld(mod, p):
    mod.merge_threshold = p.weld_distance
    if hasattr(mod, 'mode'):
        mod.mode = p.weld_mode


def setup_cast(mod, p):
    mod.cast_type = p.cast_type
    mod.factor    = p.cast_factor
    mod.radius    = p.cast_radius
    mod.use_x     = p.cast_x
    mod.use_y     = p.cast_y
    mod.use_z     = p.cast_z


def setup_displace(mod, p):
    mod.strength  = p.displace_strength
    mod.mid_level = p.displace_mid_level
    mod.direction = p.displace_direction


def setup_screw(mod, p):
    mod.angle      = p.screw_angle
    mod.steps      = p.screw_steps
    mod.iterations = p.screw_iter
    mod.axis       = p.screw_axis


def setup_simple_deform(mod, p):
    mod.deform_method = p.simple_deform_method
    mod.deform_axis   = p.simple_deform_axis
    if p.simple_deform_method in ('TWIST', 'BEND'):
        mod.angle  = p.simple_deform_angle
    else:
        mod.factor = p.simple_deform_factor


def setup_wireframe(mod, p):
    mod.thickness              = p.wireframe_thickness
    mod.offset                 = p.wireframe_offset
    mod.use_replace            = p.wireframe_use_replace
    mod.use_boundary           = p.wireframe_use_boundary


def setup_remesh(mod, p):
    mod.mode = p.remesh_mode
    if p.remesh_mode == 'VOXEL':
        mod.voxel_size = p.remesh_voxel_size
    else:
        mod.octree_depth = p.remesh_octree_depth
    if hasattr(mod, 'use_smooth_shade'):
        mod.use_smooth_shade = p.remesh_smooth_normals


MODIFIER_SETUP_MAP = {
    'MIRROR':        setup_mirror,
    'SUBSURF':       setup_subsurf,
    'SOLIDIFY':      setup_solidify,
    'BEVEL':         setup_bevel,
    'ARRAY':         setup_array,
    'TRIANGULATE':   setup_triangulate,
    'DECIMATE':      setup_decimate,
    'SMOOTH':        setup_smooth,
    'WELD':          setup_weld,
    'CAST':          setup_cast,
    'DISPLACE':      setup_displace,
    'SCREW':         setup_screw,
    'SIMPLE_DEFORM': setup_simple_deform,
    'WIREFRAME':     setup_wireframe,
    'REMESH':        setup_remesh,
}

import bpy
from bpy.props import (
    EnumProperty, BoolProperty, FloatProperty,
    IntProperty, StringProperty, PointerProperty,
)
from bpy.types import PropertyGroup
from . import core


def _upd_mirror(self, ctx):      core.sync('MIRROR',      core.setup_mirror)
def _upd_subsurf(self, ctx):     core.sync('SUBSURF',     core.setup_subsurf)
def _upd_solidify(self, ctx):    core.sync('SOLIDIFY',    core.setup_solidify)
def _upd_bevel(self, ctx):       core.sync('BEVEL',       core.setup_bevel)
def _upd_array(self, ctx):       core.sync('ARRAY',       core.setup_array)
def _upd_tri(self, ctx):         core.sync('TRIANGULATE', core.setup_triangulate)
def _upd_decimate(self, ctx):    core.sync('DECIMATE',    core.setup_decimate)
def _upd_smooth(self, ctx):      core.sync('SMOOTH',      core.setup_smooth)
def _upd_weld(self, ctx):        core.sync('WELD',        core.setup_weld)
def _upd_cast(self, ctx):        core.sync('CAST',        core.setup_cast)
def _upd_displace(self, ctx):    core.sync('DISPLACE',    core.setup_displace)
def _upd_screw(self, ctx):       core.sync('SCREW',       core.setup_screw)
def _upd_simple_deform(self, ctx): core.sync('SIMPLE_DEFORM', core.setup_simple_deform)
def _upd_wireframe(self, ctx):   core.sync('WIREFRAME',   core.setup_wireframe)
def _upd_remesh(self, ctx):      core.sync('REMESH',      core.setup_remesh)


class MBA_Props(PropertyGroup):

    target: EnumProperty(
        name="Target",
        items=[
            ('SELECTED', "Selected Objects", "Apply to selected mesh objects only"),
            ('ALL',      "All Objects",      "Apply to all mesh objects in the scene"),
        ],
        default='SELECTED',
    )  # type: ignore

    only_mesh: BoolProperty(
        name="Mesh Only",
        description="Skip non-mesh objects",
        default=True,
    )  # type: ignore

    show_info: BoolProperty(
        name="Show Info Bar",
        description="Show Blender version and object count in the panel",
        default=True,
    )  # type: ignore

    mirror_x:        BoolProperty(name="X", default=True,  update=_upd_mirror)  # type: ignore
    mirror_y:        BoolProperty(name="Y", default=False, update=_upd_mirror)  # type: ignore
    mirror_z:        BoolProperty(name="Z", default=False, update=_upd_mirror)  # type: ignore
    mirror_clipping: BoolProperty(name="Clipping", default=True,  update=_upd_mirror)  # type: ignore
    mirror_merge:    BoolProperty(name="Merge",    default=True,  update=_upd_mirror)  # type: ignore
    mirror_bisect_x: BoolProperty(name="Bisect X", default=False, update=_upd_mirror)  # type: ignore
    mirror_bisect_y: BoolProperty(name="Bisect Y", default=False, update=_upd_mirror)  # type: ignore
    mirror_bisect_z: BoolProperty(name="Bisect Z", default=False, update=_upd_mirror)  # type: ignore

    subsurf_type: EnumProperty(
        name="Type",
        items=[('CATMULL_CLARK', "Catmull-Clark", ""), ('SIMPLE', "Simple", "")],
        default='CATMULL_CLARK', update=_upd_subsurf,
    )  # type: ignore
    subsurf_levels:        IntProperty(name="Viewport", default=2, min=0, max=6, update=_upd_subsurf)  # type: ignore
    subsurf_render_levels: IntProperty(name="Render",   default=2, min=0, max=6, update=_upd_subsurf)  # type: ignore
    subsurf_optimal:       BoolProperty(name="Optimal Display", default=False, update=_upd_subsurf)    # type: ignore

    solidify_thickness: FloatProperty(name="Thickness", default=0.05,  min=0.0001, max=10.0,  update=_upd_solidify)  # type: ignore
    solidify_offset:    FloatProperty(name="Offset",    default=-1.0,  min=-1.0,   max=1.0,   update=_upd_solidify)  # type: ignore
    solidify_fill_rim:  BoolProperty(name="Fill Rim",   default=True,              update=_upd_solidify)             # type: ignore

    bevel_width:       FloatProperty(name="Width",    default=0.1,      min=0.0001, max=10.0,     update=_upd_bevel)  # type: ignore
    bevel_segments:    IntProperty  (name="Segments", default=2,        min=1,      max=100,      update=_upd_bevel)  # type: ignore
    bevel_angle_limit: FloatProperty(name="Angle",    default=0.523599, min=0.0,    max=3.14159,
                                     subtype='ANGLE', update=_upd_bevel)  # type: ignore
    bevel_profile:     FloatProperty(name="Profile",  default=0.5,      min=0.0,    max=1.0,      update=_upd_bevel)  # type: ignore
    bevel_limit_method: EnumProperty(
        name="Limit Method",
        items=[
            ('NONE',   "None",   ""),
            ('ANGLE',  "Angle",  ""),
            ('WEIGHT', "Weight", ""),
            ('VGROUP', "Vertex Group", ""),
        ],
        default='ANGLE', update=_upd_bevel,
    )  # type: ignore

    array_count:       IntProperty  (name="Count",    default=3,   min=2,   max=100, update=_upd_array)  # type: ignore
    array_offset_x:    FloatProperty(name="Offset X", default=1.0,                  update=_upd_array)  # type: ignore
    array_offset_y:    FloatProperty(name="Offset Y", default=0.0,                  update=_upd_array)  # type: ignore
    array_offset_z:    FloatProperty(name="Offset Z", default=0.0,                  update=_upd_array)  # type: ignore
    array_merge:       BoolProperty(name="Merge",     default=False,                update=_upd_array)  # type: ignore
    array_merge_dist:  FloatProperty(name="Merge Distance", default=0.001, min=0.0, update=_upd_array)  # type: ignore

    tri_quad_method: EnumProperty(
        name="Quad Method",
        items=[
            ('BEAUTY',            "Beauty",         ""),
            ('FIXED',             "Fixed",          ""),
            ('FIXED_ALTERNATE',   "Fixed Alternate",""),
            ('SHORTEST_DIAGONAL', "Shortest Diag.", ""),
        ],
        default='BEAUTY', update=_upd_tri,
    )  # type: ignore
    tri_ngon_method: EnumProperty(
        name="Ngon Method",
        items=[
            ('BEAUTY',  "Beauty",  ""),
            ('CLIP',    "Clip",    ""),
        ],
        default='BEAUTY', update=_upd_tri,
    )  # type: ignore

    decimate_ratio:      FloatProperty(name="Ratio",       default=0.5, min=0.0, max=1.0, update=_upd_decimate)   # type: ignore
    decimate_use_symmetry: BoolProperty(name="Symmetry",   default=False,                 update=_upd_decimate)   # type: ignore

    smooth_factor:  FloatProperty(name="Factor",     default=0.5, min=0.0, max=1.0, update=_upd_smooth)  # type: ignore
    smooth_repeat:  IntProperty  (name="Repeat",     default=1,   min=1,   max=100, update=_upd_smooth)  # type: ignore
    smooth_x:       BoolProperty (name="X",          default=True,          update=_upd_smooth)          # type: ignore
    smooth_y:       BoolProperty (name="Y",          default=True,          update=_upd_smooth)          # type: ignore
    smooth_z:       BoolProperty (name="Z",          default=True,          update=_upd_smooth)          # type: ignore

    weld_distance:  FloatProperty(name="Distance",   default=0.001, min=0.0, max=1.0, update=_upd_weld)  # type: ignore
    weld_mode: EnumProperty(
        name="Mode",
        items=[('ALL', "All", ""), ('CONNECTED', "Connected", "")],
        default='ALL', update=_upd_weld,
    )  # type: ignore

    cast_type: EnumProperty(
        name="Cast Type",
        items=[('SPHERE', "Sphere", ""), ('CYLINDER', "Cylinder", ""), ('CUBOID', "Cuboid", "")],
        default='SPHERE', update=_upd_cast,
    )  # type: ignore
    cast_factor:  FloatProperty(name="Factor",  default=1.0, min=-10.0, max=10.0, update=_upd_cast)  # type: ignore
    cast_radius:  FloatProperty(name="Radius",  default=0.0, min=0.0,             update=_upd_cast)  # type: ignore
    cast_x:       BoolProperty (name="X",       default=True,  update=_upd_cast)                     # type: ignore
    cast_y:       BoolProperty (name="Y",       default=True,  update=_upd_cast)                     # type: ignore
    cast_z:       BoolProperty (name="Z",       default=True,  update=_upd_cast)                     # type: ignore

    displace_strength:  FloatProperty(name="Strength",   default=1.0,   update=_upd_displace)  # type: ignore
    displace_mid_level: FloatProperty(name="Mid Level",  default=0.5,   update=_upd_displace)  # type: ignore
    displace_direction: EnumProperty(
        name="Direction",
        items=[
            ('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", ""),
            ('NORMAL', "Normal", ""), ('CUSTOM_NORMAL', "Custom Normal", ""),
            ('RGB_TO_XYZ', "RGB to XYZ", ""),
        ],
        default='NORMAL', update=_upd_displace,
    )  # type: ignore

    screw_angle:    FloatProperty(name="Angle",    default=6.2831853, subtype='ANGLE', update=_upd_screw)  # type: ignore
    screw_steps:    IntProperty  (name="Steps",    default=16, min=2, max=256,         update=_upd_screw)  # type: ignore
    screw_iter:     IntProperty  (name="Iterations", default=1, min=1, max=100,        update=_upd_screw)  # type: ignore
    screw_axis: EnumProperty(
        name="Axis",
        items=[('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", "")],
        default='Z', update=_upd_screw,
    )  # type: ignore

    simple_deform_method: EnumProperty(
        name="Mode",
        items=[
            ('TWIST',   "Twist",   ""),
            ('BEND',    "Bend",    ""),
            ('TAPER',   "Taper",   ""),
            ('STRETCH', "Stretch", ""),
        ],
        default='TWIST', update=_upd_simple_deform,
    )  # type: ignore
    simple_deform_angle:  FloatProperty(name="Angle",  default=0.785398, subtype='ANGLE', update=_upd_simple_deform)  # type: ignore
    simple_deform_factor: FloatProperty(name="Factor", default=0.5,                       update=_upd_simple_deform)  # type: ignore
    simple_deform_axis: EnumProperty(
        name="Axis",
        items=[('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", "")],
        default='Z', update=_upd_simple_deform,
    )  # type: ignore

    wireframe_thickness:   FloatProperty(name="Thickness",    default=0.02, min=0.0001, update=_upd_wireframe)  # type: ignore
    wireframe_offset:      FloatProperty(name="Offset",       default=0.0,  min=-1.0, max=1.0, update=_upd_wireframe)  # type: ignore
    wireframe_use_replace: BoolProperty (name="Replace Original", default=True, update=_upd_wireframe)          # type: ignore
    wireframe_use_boundary: BoolProperty(name="Boundary",     default=True, update=_upd_wireframe)              # type: ignore

    remesh_mode: EnumProperty(
        name="Mode",
        items=[
            ('VOXEL', "Voxel", ""),
            ('SHARP', "Sharp", ""),
            ('SMOOTH',"Smooth",""),
            ('BLOCKS',"Blocks",""),
        ],
        default='VOXEL', update=_upd_remesh,
    )  # type: ignore
    remesh_voxel_size:  FloatProperty(name="Voxel Size",  default=0.1, min=0.001, max=2.0, update=_upd_remesh)  # type: ignore
    remesh_octree_depth: IntProperty (name="Octree Depth",default=4,   min=1,     max=12,  update=_upd_remesh)  # type: ignore
    remesh_smooth_normals: BoolProperty(name="Smooth Shading", default=False, update=_upd_remesh)               # type: ignore


def register():
    bpy.utils.register_class(MBA_Props)
    bpy.types.Scene.mba_props = PointerProperty(type=MBA_Props)

def unregister():
    del bpy.types.Scene.mba_props
    bpy.utils.unregister_class(MBA_Props)

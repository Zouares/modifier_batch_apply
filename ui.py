import bpy


def header_row(layout, mod_type, label, icon):
    row = layout.row(align=True)
    row.label(text=label, icon=icon)
    sub = row.row(align=True)
    sub.alignment = 'RIGHT'

    up = sub.operator("mba.move_modifier", text="", icon='TRIA_UP')
    up.mod_type  = mod_type
    up.direction = 'UP'

    dn = sub.operator("mba.move_modifier", text="", icon='TRIA_DOWN')
    dn.mod_type  = mod_type
    dn.direction = 'DOWN'


def action_row(layout, mod_type):
    row = layout.row(align=True)
    row.scale_y = 1.2

    add = row.operator("mba.add_modifier",   icon='ADD',       text="Add")
    add.mod_type = mod_type

    syn = row.operator("mba.sync_modifier",  icon='FILE_REFRESH', text="Sync")
    syn.mod_type = mod_type

    apl = row.operator("mba.apply_modifier", icon='CHECKMARK', text="Apply")
    apl.mod_type = mod_type

    rem = row.operator("mba.remove_modifier",icon='X',         text="Remove")
    rem.mod_type = mod_type

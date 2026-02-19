# ============================================================================
#  Armature Tools — Blender Add-on
# ============================================================================
#
#  Stick display + In Front for all armatures.
#
#  Copyright (C) 2026 .Staples.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ============================================================================

bl_info = {
    "name": "Armature Tools",
    "author": ".Staples.",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Armature Tools",
    "description": "Set all armatures to Stick display with In Front enabled",
    "category": "3D View",
}

import bpy
from bpy.props import BoolProperty
from bpy.types import Panel, Operator

# Sidebar tab name — overridden by __init__.py when used as part of a package
PANEL_CATEGORY = "Armature Tools"


def apply_to_armatures(context, include_hidden=True):
    count = 0
    for obj in bpy.data.objects:
        if obj.type != "ARMATURE":
            continue

        if not include_hidden:
            if obj.hide_viewport:
                continue

        # Set Display type to Stick
        if obj.data is not None:
            obj.data.display_type = 'STICK'

        # Set Display Setting to In Front
        obj.show_in_front = True

        count += 1

    return count


class ARMATURETOOLS_OT_apply_stick_infront(Operator):
    bl_idname = "armaturetools.apply_stick_infront"
    bl_label = "Apply Stick + In Front"
    bl_description = "Set all armatures to Stick display and enable In Front"
    bl_options = {'REGISTER', 'UNDO'}

    include_hidden: BoolProperty(
        name="Include Hidden",
        description="Also apply to armatures hidden in the viewport",
        default=True,
    )

    def execute(self, context):
        count = apply_to_armatures(context, include_hidden=self.include_hidden)
        self.report({'INFO'}, f"Updated {count} armature(s).")
        return {'FINISHED'}


# -- Panel --

class SVRC_PT_armature_tools(Panel):
    bl_label = "Armature Tools"
    bl_idname = "SVRC_PT_armature_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = PANEL_CATEGORY
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        op = layout.operator("armaturetools.apply_stick_infront", icon='ARMATURE_DATA')
        op.include_hidden = True


# ============================================================================
#  REGISTRATION
# ============================================================================

_classes = (
    ARMATURETOOLS_OT_apply_stick_infront,
    SVRC_PT_armature_tools,
)


def register():
    for c in _classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(_classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()

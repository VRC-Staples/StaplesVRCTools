# ============================================================================
#  Staples VRC Tools — Blender Add-on
# ============================================================================
#
#  Combined toolset for VRC avatar workflow:
#    - Armature Tools: Stick display + In Front for all armatures
#    - Elastic Clothing Fit: Proxy-based clothing fitting with UV preservation
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
    "name": "Staples VRC Tools",
    "author": ".Staples.",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > StaplesVRCTools",
    "description": "Misc Tools for VRC Avatar Workflow",
    "category": "3D View",
}

from . import armature_tools
from . import elastic_fit

# Override sidebar tab so both modules share one "StaplesVRCTools" tab
_SHARED_CATEGORY = "StaplesVRCTools"


def register():
    armature_tools.PANEL_CATEGORY = _SHARED_CATEGORY
    armature_tools.SVRC_PT_armature_tools.bl_category = _SHARED_CATEGORY
    elastic_fit.PANEL_CATEGORY = _SHARED_CATEGORY
    elastic_fit.SVRC_PT_elastic_fit.bl_category = _SHARED_CATEGORY

    armature_tools.register()
    elastic_fit.register()


def unregister():
    elastic_fit.unregister()
    armature_tools.unregister()

import bpy
from bpy.props import IntProperty, FloatProperty
from mathutils import Vector

from sverchok_redux.node_tree import SvRxTreeNode


class SvRxMathVector(bpy.types.Node, SvRxTreeNode):
    ''' Scalar Vector '''

    bl_idname = 'SvRxMathVector'
    bl_label = 'Vector'

    dummy = IntProperty(default=3)

    def draw_buttons(self, context, layout):
        pass


def register():
    bpy.utils.register_class(SvRxMathVector)


def unregister():
    bpy.utils.unregister_class(SvRxMathVector)

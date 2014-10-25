bl_info = {
    "name": "Moth3r Snap Toggle",
    "author": "Ivan Santic, Stanislav Blinov",
    "version": (1, 0),
    "blender": (2, 72, 0),
    "location": "",
    "description": "Toggle Vertex/Face Snapping",
    "warning": "",
    "wiki_url": "",
    "category": ""
}

import bpy


def main(context):
    context.scene.tool_settings.use_mesh_automerge = True
    if context.scene.tool_settings.snap_element != 'VERTEX':
        context.scene.tool_settings.snap_element = 'VERTEX'
        if context.active_object and context.active_object.mode == 'EDIT':
            bpy.ops.mesh.select_mode(use_extend=False, type='VERT')
    else:
        context.scene.tool_settings.snap_element = 'FACE'
        if context.active_object and context.active_object.mode == 'EDIT':
            bpy.ops.mesh.select_mode(use_extend=False, type='VERT')
            bpy.ops.mesh.select_mode(use_extend=True, type='EDGE')
            bpy.ops.mesh.select_mode(use_extend=True, type='FACE')

class VertexFaceSnapToggle(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "moth3r.snap_toggle"
    bl_label = "Toggle Vertex/Face Snapping"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VertexFaceSnapToggle)


def unregister():
    bpy.utils.unregister_class(VertexFaceSnapToggle)


if __name__ == "__main__":
    register()
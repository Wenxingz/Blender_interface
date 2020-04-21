
bl_info = {
    "name": "Speed Tools",
    "author": "Wenxingz",
    "version": (0, 1 , 1),
    "blender": (2, 80, 0),
    "location": "INFO > TOPBAR",
    "description": "Speed Button Tools",
    "doc_url": "https://github.com/Wenxingz/Blender_interface",
    "category": "Interface",
}

import bpy
from bpy.types import NodeTree, Node, NodeSocket, Operator, Object
from bpy.types import Header


class Speed_Button(bpy.types.Header):
    bl_idname = "IM_EXport"
    bl_space_type = "INFO"
    bl_region_type = "HEADER"        

    def draw(self, context,):
        layout = self.layout
        
        row = layout.row()
        row.operator("wm.read_homefile",text = "New", icon = "FILE_NEW")
        row.operator("wm.open_mainfile",icon = "FILEBROWSER")
        row.operator("wm.save_mainfile",text = "Save",icon = "FILE_TICK")
        row.operator("wm.link",icon = "LINKED")
        row.operator("import_scene.fbx", text = "Im_fbx", icon = "IMPORT")
        row.operator("export_scene.fbx", text = "Ex_fbx", icon = "EXPORT")
        row.operator("import_scene.obj", text = "Im_obj", icon = "IMPORT")
        row.operator("export_scene.obj", text = "Ex_obj", icon = "EXPORT")
        
        row.operator("screen.userpref_show", text = "Preferences...", icon = "PREFERENCES")

        prefs = context.preferences
        view = prefs.view
        layout.prop(view,"use_translate_interface", text = "Language")
        
        row = layout.row()
        row.operator("mesh.primitive_plane_add", text = "Plane", icon = "MESH_PLANE")
        row.operator("mesh.primitive_cube_add", text = "Cube", icon = "CUBE")
        row.operator("mesh.primitive_uv_sphere_add", text = "UV Sphere", icon = "MESH_UVSPHERE")
        row.operator("mesh.primitive_cylinder_add", text = "Cylinder", icon = "MESH_CYLINDER")
        row.operator("curve.primitive_bezier_curve_add", text = "Bezier", icon = "CURVE_BEZCURVE")
        row.operator("object.armature_add", text = "Armature", icon = "BONE_DATA")
        row.operator("object.empty_add", text = "Empty", icon = "EMPTY_AXIS")
        row.operator("object.camera_add", text = "Camera", icon = "CAMERA_DATA")


def register():
    bpy.utils.register_class(Speed_Button)


def unregister():
    bpy.utils.unregister_class(Speed_Button)


if __name__ == "__main__":
    register()


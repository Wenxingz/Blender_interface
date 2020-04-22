
bl_info = {
    "name": "Speed Tools",
    "author": "Wenxingz",
    "version": (0, 2 , 0),
    "blender": (2, 80, 0),
    "location": "INFO > TOPBAR",
    "description": "Speed Button Tools",
    "doc_url": "https://github.com/Wenxingz/Blender_interface",
    "category": "Interface",
}

import bpy
from bpy.types import NodeTree, Node, NodeSocket, Operator, Object
from bpy.types import Header, Panel


class ST_Add_PLAIN_AXES_Obje(bpy.types.Operator):#定义空物体
    bl_idname = "obje.ts_plain_axes"
    bl_label = "obje.ts_node_PLAIN_AXES"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        return {'FINISHED'}


class Info_Speed_Button(bpy.types.Header):
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
        row.operator("obje.ts_plain_axes",text = "Empty", icon = "EMPTY_AXIS")
        row.operator("object.camera_add", text = "Camera", icon = "CAMERA_DATA")

######################################################################################


class ShaderEditor_Add_Search(bpy.types.Panel): 
    bl_label = "Search"            
    bl_idname = "Shader_Search"
    bl_space_type = "NODE_EDITOR"  
    bl_region_type = "UI"         
    bl_category = "Shader Node"  

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("node.add_search", text="Search...", icon = "VIEWZOOM")


#############################################输入节点
class ST_Add_AO_Node(bpy.types.Operator):
    bl_idname = "node.ts_add_ao_node"
    bl_label = "Node.ts_node_AO"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeAmbientOcclusion", use_transform=True)
        return {'FINISHED'}

class ST_Add_Attribute_Node(bpy.types.Operator):
    bl_idname = "node.ts_add_attribute_node"
    bl_label = "Node.ts_node_Attribute"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeAttribute", use_transform=True)
        return {'FINISHED'}

class ST_Add_Bevel_Node(bpy.types.Operator):
    bl_idname = "node.ts_add_bevel_node"
    bl_label = "Node.ts_node_Bevel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBevel", use_transform=True,)
        return {'FINISHED'}

class ST_Add_CameraData_Node(bpy.types.Operator):
    bl_idname = "node.ts_camera_data_node"
    bl_label = "Node.ts_node_Camera_data"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeCameraData", use_transform=True)
        return {'FINISHED'}

class ST_Add_Fresnel_Node(bpy.types.Operator):
    bl_idname = "node.ts_fresnel_node"
    bl_label = "Node.ts_node_Fresnel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeFresnel", use_transform=True)
        return {'FINISHED'}

class ST_Add_Geometry_Node(bpy.types.Operator):
    bl_idname = "node.ts_geometry_node"
    bl_label = "Node.ts_node_Geometry"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeNewGeometry", use_transform=True)
        return {'FINISHED'}

class ST_Add_HairInfo_Node(bpy.types.Operator):
    bl_idname = "node.ts_hairinfo_node"
    bl_label = "Node.ts_node_HairInfo"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeHairInfo", use_transform=True)
        return {'FINISHED'}

class ST_Add_LayerWeight_Node(bpy.types.Operator):
    bl_idname = "node.ts_layerweight_node"
    bl_label = "Node.ts_node_LayerWeight"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeLayerWeight", use_transform=True)
        return {'FINISHED'}

class ST_Add_LightPath_Node(bpy.types.Operator):
    bl_idname = "node.ts_lightpath_node"
    bl_label = "Node.ts_node_LightPath"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeLightPath", use_transform=True)
        return {'FINISHED'}

class ST_Add_ObjectInfo_Node(bpy.types.Operator):
    bl_idname = "node.ts_objectinfo_node"
    bl_label = "Node.ts_node_ObjectInfo"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', ype="ShaderNodeObjectInfo", use_transform=True)
        return {'FINISHED'}

class ST_Add_ParticleInfo_Node(bpy.types.Operator):
    bl_idname = "node.ts_particleinfo_node"
    bl_label = "Node.ts_node_ParticleInfo"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeParticleInfo", use_transform=True)
        return {'FINISHED'}

class ST_Add_RGB_Node(bpy.types.Operator):
    bl_idname = "node.ts_rgb_node"
    bl_label = "Node.ts_node_RGB"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeRGB", use_transform=True)
        return {'FINISHED'}

class ST_Add_Tangent_Node(bpy.types.Operator):
    bl_idname = "node.ts_tangent_node"
    bl_label = "Node.ts_node_Tangent"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTangent", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexCoord_Node(bpy.types.Operator):
    bl_idname = "node.ts_texcoord_node"
    bl_label = "Node.ts_node_TexCoord"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexCoord", use_transform=True)
        return {'FINISHED'}

class ST_Add_UVMap_Node(bpy.types.Operator):
    bl_idname = "node.ts_uvmap_node"
    bl_label = "Node.ts_node_UVMap"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeUVMap", use_transform=True)
        return {'FINISHED'}

class ST_Add_Value_Node(bpy.types.Operator):
    bl_idname = "node.ts_value_node"
    bl_label = "Node.ts_node_Value"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeValue", use_transform=True)
        return {'FINISHED'}

class ST_Add_VertexColor_Node(bpy.types.Operator):
    bl_idname = "node.ts_vertexcolor_node"
    bl_label = "Node.ts_node_VertexColor"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVertexColor", use_transform=True)
        return {'FINISHED'}

class ST_Add_VolumeInfo_Node(bpy.types.Operator):
    bl_idname = "node.ts_volumeinfo_node"
    bl_label = "Node.ts_node_VolumeInfo"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVolumeInfo", use_transform=True)
        return {'FINISHED'}

class ST_Add_Wireframe_Node(bpy.types.Operator):
    bl_idname = "node.ts_wireframe_node"
    bl_label = "Node.ts_node_Wireframe"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeWireframe", use_transform=True)
        return {'FINISHED'}



class ShaderEditor_Add_Input(bpy.types.Panel): 
    bl_label = "Input"            
    bl_idname = "Shader_Input"
    bl_space_type = "NODE_EDITOR"  
    bl_region_type = "UI"          
    bl_category = "Shader Node"  

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_add_ao_node", text= "Ambient Occlusion 环境光遮蔽")
        props = layout.operator("node.ts_add_attribute_node", text= "Attribute 属性") 
        props = layout.operator("node.ts_add_bevel_node", text = "Bevel")
        props = layout.operator("node.ts_camera_data_node", text = "Camera Data 相机数据") 
        props = layout.operator("node.ts_fresnel_node", text= "Fresnel 菲涅尔")
        props = layout.operator("node.ts_geometry_node", text= "Geometry 几何数据")
        props = layout.operator("node.ts_hairinfo_node", text= "HairInfo 毛发信息")
        props = layout.operator("node.ts_layerweight_node", text= "Layerweight 层权重")
        props = layout.operator("node.ts_lightpath_node", text= "Lightpath 光程")
        props = layout.operator("node.ts_objectinfo_node", text= "ObjectInfo 物体信息")
        props = layout.operator("node.ts_particleinfo_node", text= "ParticleInfo 粒子信息")
        props = layout.operator("node.ts_rgb_node", text= "RGB")
        props = layout.operator("node.ts_tangent_node", text= "Tangent 切向（正切）")
        props = layout.operator("node.ts_texcoord_node", text= "Texcoord 纹理坐标")
        props = layout.operator("node.ts_uvmap_node", text= "UVMap UV 贴图")
        props = layout.operator("node.ts_value_node", text= "Value 值（明度）")
        props = layout.operator("node.ts_vertexcolor_node", text= "VertexColor 顶点颜色")
        props = layout.operator("node.ts_volumeinfo_node", text= "VolumeInfo 体积信息")
        props = layout.operator("node.ts_wireframe_node", text= "Wireframe 线框")
#########################################################

###########################################################输出节点
class ST_Add_OutputAOV_Node(bpy.types.Operator):
    bl_idname = "node.ts_outputaov"
    bl_label = "Node.ts_node_OutputAOV"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeOutputAOV", use_transform=True)
        return {'FINISHED'}

class ST_Add_OutputLight_Node(bpy.types.Operator):
    bl_idname = "node.ts_outputlight"
    bl_label = "Node.ts_node_OutputLight"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeOutputLight", use_transform=True)
        return {'FINISHED'}

class ST_Add_OutputMaterial_Node(bpy.types.Operator):
    bl_idname = "node.ts_outputmaterial"
    bl_label = "Node.ts_node_OutputMaterial"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeOutputMaterial", use_transform=True)
        return {'FINISHED'}




class ShaderEditor_Add_Output(bpy.types.Panel):
    bl_label = "Output"
    bl_idname = "Shader_Output"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_outputaov", text="AOV 输出")
        props = layout.operator("node.ts_outputlight", text="OutputLight 光输出")
        props = layout.operator("node.ts_outputmaterial", text="OutputMaterial 材质输出")
              
############################################################材质节点

class ST_Add_AddShader_Node(bpy.types.Operator):
    bl_idname = "node.ts_addshader"
    bl_label = "Node.ts_node_AddShader"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeAddShader", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfAnisotropic_Node(bpy.types.Operator):  #CYCLES专属材质
    bl_idname = "node.ts_bsdfanisotropic"
    bl_label = "Node.ts_node_BsdfAnisotropic"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfAnisotropic", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfDiffuse_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdfdiffuse"
    bl_label = "Node.ts_node_BsdfDiffuse"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfDiffuse", use_transform=True)
        return {'FINISHED'}

class ST_Add_Emission_Node(bpy.types.Operator):
    bl_idname = "node.ts_emission"
    bl_label = "Node.ts_node_Emission"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeEmission", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfGlass_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdfglass"
    bl_label = "Node.ts_node_BsdfGlass"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfGlass", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfGlossy_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdfglossy"
    bl_label = "Node.ts_node_BsdfGlossy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfGlossy", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfHair_Node(bpy.types.Operator):  #CYCLES专属材质
    bl_idname = "node.ts_bsdfhair"
    bl_label = "Node.ts_node_BsdfHair"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfHair", use_transform=True)
        return {'FINISHED'}

class ST_Add_Holdout_Node(bpy.types.Operator):
    bl_idname = "node.ts_holdout"
    bl_label = "Node.ts_node_Holdout"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeHoldout", use_transform=True)
        return {'FINISHED'}

class ST_Add_MixShader_Node(bpy.types.Operator):
    bl_idname = "node.ts_mixshader"
    bl_label = "Node.ts_node_MixShader"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeMixShader", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfPrincipled_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdfprincipled"
    bl_label = "Node.ts_node_BsdfPrincipled"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfPrincipled", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfHairPrincipled_Node(bpy.types.Operator): #CYCLES专属材质
    bl_idname = "node.ts_bsdfhairprincipled"
    bl_label = "Node.ts_node_BsdfHairPrincipled"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfHairPrincipled", use_transform=True)
        return {'FINISHED'}

class ST_Add_VolumePrincipled_Node(bpy.types.Operator):
    bl_idname = "node.ts_volumeprincipled"
    bl_label = "Node.ts_node_VolumePrincipled"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVolumePrincipled", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfRefraction_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdfrefraction"
    bl_label = "Node.ts_node_BsdfRefraction"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfRefraction", use_transform=True)
        return {'FINISHED'}

class ST_Add_Specular_Node(bpy.types.Operator): #EEVEE专属材质
    bl_idname = "node.ts_specular"
    bl_label = "Node.ts_node_Specular"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine != 'CYCLES'
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeEeveeSpecular", use_transform=True)
        return {'FINISHED'}

class ST_Add_SubsurfaceScattering_Node(bpy.types.Operator):
    bl_idname = "node.ts_subsurfacescattering"
    bl_label = "Node.ts_node_SubsurfaceScattering"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeSubsurfaceScattering", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfToon_Node(bpy.types.Operator):  #CYCLES专属材质
    bl_idname = "node.ts_bsdftoon"
    bl_label = "Node.ts_node_BsdfToon"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfToon", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfTranslucent_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdftranslucent"
    bl_label = "Node.ts_node_BsdfTranslucent"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfTranslucent", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfTransparent_Node(bpy.types.Operator):
    bl_idname = "node.ts_bsdftransparent"
    bl_label = "Node.ts_node_BsdfTransparent"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfTransparent", use_transform=True)
        return {'FINISHED'}

class ST_Add_BsdfVelvet_Node(bpy.types.Operator):  #CYCLES专属材质
    bl_idname = "node.ts_bsdfvelvet"
    bl_label = "Node.ts_node_BsdfVelvet"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBsdfVelvet", use_transform=True)
        return {'FINISHED'}

class ST_Add_VolumeAbsorption_Node(bpy.types.Operator):
    bl_idname = "node.ts_volumeabsorption"
    bl_label = "Node.ts_node_VolumeAbsorption"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVolumeAbsorption", use_transform=True)
        return {'FINISHED'}

class ST_Add_VolumeScatter_Node(bpy.types.Operator):
    bl_idname = "node.ts_volumescatter"
    bl_label = "Node.ts_node_VolumeScatter"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVolumeScatter", use_transform=True)
        return {'FINISHED'}




class ShaderEditor_Add_Shader(bpy.types.Panel):
    bl_label = "Shader"
    bl_idname = "Shader_Shader"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_addshader", text="AddShader 相加着色器")
        props = layout.operator("node.ts_bsdfanisotropic", text="Anisotropic BSDF 各向异性")  #CYCLES专属材质
        props = layout.operator("node.ts_bsdfdiffuse", text="Diffuse BSDF 漫射")
        props = layout.operator("node.ts_emission", text="Emission 自发光")
        props = layout.operator("node.ts_bsdfglass", text="Glass BSDF 玻璃")
        props = layout.operator("node.ts_bsdfglossy", text="Glossy BSDF 光泽")
        props = layout.operator("node.ts_bsdfhair", text="Hair BSDF 毛发")  #CYCLES专属材质
        props = layout.operator("node.ts_holdout", text="Holdout 阻隔")
        props = layout.operator("node.ts_mixshader", text="Mix Shader 混合着色器")
        props = layout.operator("node.ts_bsdfprincipled", text="Principled BSDF 原理化BSDF")
        props = layout.operator("node.ts_bsdfhairprincipled", text="Principled Hair 原理化毛发")  #CYCLES专属材质
        props = layout.operator("node.ts_volumeprincipled", text="Principled Volume 原理化体积")
        props = layout.operator("node.ts_specular", text="Specular 高光")  #EEVEE专属材质
        props = layout.operator("node.ts_bsdfrefraction", text="Refraction 折射")        
        props = layout.operator("node.ts_subsurfacescattering", text="Subsurface Scattering 次表面散射")
        props = layout.operator("node.ts_bsdftoon", text="Toon BSDF 卡通")
        props = layout.operator("node.ts_bsdftranslucent", text="Translucent BSDF 半透")
        props = layout.operator("node.ts_bsdftransparent", text="Transparent BSDF 透明")
        props = layout.operator("node.ts_bsdfvelvet", text="Velevt BSDF 丝绒")  #CYCLES专属材质
        props = layout.operator("node.ts_volumeabsorption", text="Volume Absorption 体积吸收")
        props = layout.operator("node.ts_volumescatter", text="Solume Scatter 体积散射")
        
##########################################################################################纹理节点
class ST_Add_TexBrick_Node(bpy.types.Operator):
    bl_idname = "node.ts_texbrick"
    bl_label = "Node.ts_node_TexBrick"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexBrick", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexChecker_Node(bpy.types.Operator):
    bl_idname = "node.ts_texchecker"
    bl_label = "Node.ts_node_TexChecker"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexChecker", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexEnvironment_Node(bpy.types.Operator):
    bl_idname = "node.ts_texenvironment"
    bl_label = "Node.ts_node_TexEnvironment"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexEnvironment", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexGradient_Node(bpy.types.Operator):
    bl_idname = "node.ts_texgradient"
    bl_label = "Node.ts_node_TexGradient"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexGradient", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexIES_Node(bpy.types.Operator):
    bl_idname = "node.ts_texies"
    bl_label = "Node.ts_node_TexIES"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexIES", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexImage_Node(bpy.types.Operator):
    bl_idname = "node.ts_teximage"
    bl_label = "Node.ts_node_TexImage"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexImage", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexMagic_Node(bpy.types.Operator):
    bl_idname = "node.ts_texmagic"
    bl_label = "Node.ts_node_TexMagic"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexMagic", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexMusgrave_Node(bpy.types.Operator):
    bl_idname = "node.ts_texmusgrave"
    bl_label = "Node.ts_node_TexMusgrave"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexMusgrave", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexNoise_Node(bpy.types.Operator):
    bl_idname = "node.ts_texnoise"
    bl_label = "Node.ts_node_TexNoise"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexNoise", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexPointDensity_Node(bpy.types.Operator):
    bl_idname = "node.ts_texpointdensity"
    bl_label = "Node.ts_node_TexPointDensity"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexPointDensity", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexSky_Node(bpy.types.Operator):
    bl_idname = "node.ts_texsky"
    bl_label = "Node.ts_node_TexSky"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexSky", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexVoronoi_Node(bpy.types.Operator):
    bl_idname = "node.ts_texvoronoi"
    bl_label = "Node.ts_node_TexVoronoi"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexVoronoi", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexWave_Node(bpy.types.Operator):
    bl_idname = "node.ts_texwave"
    bl_label = "Node.ts_node_TexWave"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexWave", use_transform=True)
        return {'FINISHED'}

class ST_Add_TexWhiteNoise_Node(bpy.types.Operator):
    bl_idname = "node.ts_texwhitenoise"
    bl_label = "Node.ts_node_TexWhiteNoise"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeTexWhiteNoise", use_transform=True)
        return {'FINISHED'}


class ShaderEditor_Add_Texture(bpy.types.Panel):
    bl_label = "Texture"
    bl_idname = "Shader_Texture"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_texbrick", text="Brick Texture 砖墙纹理")
        props = layout.operator("node.ts_texchecker", text="Checker Texture 棋盘格纹理")
        props = layout.operator("node.ts_texenvironment", text="Environment Texture 环境纹理")
        props = layout.operator("node.ts_texgradient", text="Gradient Texture 渐变纹理")
        props = layout.operator("node.ts_texies", text="IES Texture IES纹理")
        props = layout.operator("node.ts_teximage", text="Image Texture 图像纹理")
        props = layout.operator("node.ts_texmagic", text="Magic Texture 迷幻纹理")
        props = layout.operator("node.ts_texmusgrave", text="Musgrave Texture 马氏分形纹理")
        props = layout.operator("node.ts_texnoise", text="Noise Texture 噪波纹理")
        props = layout.operator("node.ts_texpointdensity", text="Point Density 点密度")
        props = layout.operator("node.ts_texsky", text="Sky Texture 天空纹理")
        props = layout.operator("node.ts_texvoronoi", text="Voronoi Texture 沃洛诺伊纹理")
        props = layout.operator("node.ts_texwave", text="Wave Texture 波浪纹理")
        props = layout.operator("node.ts_texwhitenoise", text="White Noise 白噪波")

##################################################################################颜色节点
class ST_Add_BrightContrast_Node(bpy.types.Operator):
    bl_idname = "node.ts_brightcontrast"
    bl_label = "Node.ts_node_BrightContrast"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBrightContrast", use_transform=True)
        return {'FINISHED'}

class ST_Add_Gamma_Node(bpy.types.Operator):
    bl_idname = "node.ts_gamma"
    bl_label = "Node.ts_node_Gamma"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeGamma", use_transform=True)
        return {'FINISHED'}

class ST_Add_HueSaturation_Node(bpy.types.Operator):
    bl_idname = "node.ts_huesaturation"
    bl_label = "Node.ts_node_HueSaturation"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeHueSaturation", use_transform=True)
        return {'FINISHED'}

class ST_Add_Invert_Node(bpy.types.Operator):
    bl_idname = "node.ts_invert"
    bl_label = "Node.ts_node_Invert"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeInvert", use_transform=True)
        return {'FINISHED'}

class ST_Add_LightFalloff_Node(bpy.types.Operator):
    bl_idname = "node.ts_lightfalloff"
    bl_label = "Node.ts_node_LightFalloff"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeLightFalloff", use_transform=True)
        return {'FINISHED'}

class ST_Add_MixRGB_Node(bpy.types.Operator):
    bl_idname = "node.ts_mixrgb"
    bl_label = "Node.ts_node_MixRGB"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeMixRGB", use_transform=True)
        return {'FINISHED'}

class ST_Add_RGBCurve_Node(bpy.types.Operator):
    bl_idname = "node.ts_rgbcurve"
    bl_label = "Node.ts_node_RGBCurve"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeRGBCurve", use_transform=True)
        return {'FINISHED'}





class ShaderEditor_Add_Color(bpy.types.Panel):
    bl_label = "Color"
    bl_idname = "Shader_Textur"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_brightcontrast", text="Bright Contrast 亮度对比度")
        props = layout.operator("node.ts_Gamma", text="Gamma 伽马")
        props = layout.operator("node.ts_huesaturation", text="HUE/Saturation 色相/饱和度")
        props = layout.operator("node.ts_invert", text="Invert 反转")
        props = layout.operator("node.ts_lightfalloff", text="Light Falloff 光线衰减")
        props = layout.operator("node.ts_mixrgb", text="Mix RGB 混合RGB")
        props = layout.operator("node.ts_rgbcurve", text="RGB Curve RGB曲线")

##########################################################################################矢量节点
class ST_Add_Bump_Node(bpy.types.Operator):
    bl_idname = "node.ts_bump"
    bl_label = "Node.ts_node_Bump"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBump", use_transform=True)
        return {'FINISHED'}

class ST_Add_Displacement_Node(bpy.types.Operator):
    bl_idname = "node.ts_displacement"
    bl_label = "Node.ts_node_Displacement"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeDisplacement", use_transform=True)
        return {'FINISHED'}

class ST_Add_Mapping_Node(bpy.types.Operator):
    bl_idname = "node.ts_mapping"
    bl_label = "Node.ts_node_Mapping"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeMapping", use_transform=True)
        return {'FINISHED'}

class ST_Add_Normal_Node(bpy.types.Operator):
    bl_idname = "node.ts_normal"
    bl_label = "Node.ts_node_Normal"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeNormal", use_transform=True)
        return {'FINISHED'}

class ST_Add_NormalMap_Node(bpy.types.Operator):
    bl_idname = "node.ts_normalmap"
    bl_label = "Node.ts_node_NormalMap"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeNormalMap", use_transform=True)
        return {'FINISHED'}

class ST_Add_VectorCurve_Node(bpy.types.Operator):
    bl_idname = "node.ts_vectorcurve"
    bl_label = "Node.ts_node_VectorCurve"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVectorCurve", use_transform=True)
        return {'FINISHED'}

class ST_Add_VectorDisplacement_Node(bpy.types.Operator):
    bl_idname = "node.ts_vectordisplacement"
    bl_label = "Node.ts_node_VectorDisplacement"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVectorDisplacement", use_transform=True)
        return {'FINISHED'}

class ST_Add_VectorRotate_Node(bpy.types.Operator):
    bl_idname = "node.ts_vectorrotate"
    bl_label = "Node.ts_node_VectorRotate"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVectorRotate", use_transform=True)
        return {'FINISHED'}

class ST_Add_VectorTransform_Node(bpy.types.Operator):
    bl_idname = "node.ts_vectortransform"
    bl_label = "Node.ts_node_VectorTransform"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVectorTransform", use_transform=True)
        return {'FINISHED'}




class ShaderEditor_Add_Vector(bpy.types.Panel):
    bl_label = "Vector"
    bl_idname = "Shader_Vector"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_bump", text="Bump 凹凸")
        props = layout.operator("node.ts_displacement", text="Displacement 置换")
        props = layout.operator("node.ts_mapping", text="Mapping 映射")
        props = layout.operator("node.ts_normal", text="Normal 法向")
        props = layout.operator("node.ts_normalmap", text="Normal Map 法线贴图")
        props = layout.operator("node.ts_vectorcurve", text="Vector Curve 矢量曲线")
        props = layout.operator("node.ts_vectordisplacement", text="Vector Displacement 矢量置换")
        props = layout.operator("node.ts_vectorrotate", text="Vector Rotate 矢量旋转")
        props = layout.operator("node.ts_vectortransform", text="Vector Transform 矢量变换")

#########################################################################################转换节点
class ST_Add_Blackbody_Node(bpy.types.Operator):
    bl_idname = "node.ts_blackbody"
    bl_label = "Node.ts_node_Blackbody"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeBlackbody", use_transform=True)
        return {'FINISHED'}

class ST_Add_Clamp_Node(bpy.types.Operator):
    bl_idname = "node.ts_clamp"
    bl_label = "Node.ts_node_Clamp"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeClamp", use_transform=True)
        return {'FINISHED'}

class ST_Add_ValToRGB_Node(bpy.types.Operator):
    bl_idname = "node.ts_valtorgb"
    bl_label = "Node.ts_node_ValToRGB"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeValToRGB", use_transform=True)
        return {'FINISHED'}

class ST_Add_CombineHSV_Node(bpy.types.Operator):
    bl_idname = "node.ts_combinehsv"
    bl_label = "Node.ts_node_CombineHSV"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeCombineHSV", use_transform=True)
        return {'FINISHED'}

class ST_Add_CombineRGB_Node(bpy.types.Operator):
    bl_idname = "node.ts_combinergb"
    bl_label = "Node.ts_node_CombineRGB"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeCombineRGB", use_transform=True)
        return {'FINISHED'}

class ST_Add_CombineXYZ_Node(bpy.types.Operator):
    bl_idname = "node.ts_combinexyz"
    bl_label = "Node.ts_node_CombineXYZ"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeCombineXYZ", use_transform=True)
        return {'FINISHED'}

class ST_Add_MapRange_Node(bpy.types.Operator):
    bl_idname = "node.ts_maprange"
    bl_label = "Node.ts_node_MapRange"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeMapRange", use_transform=True)
        return {'FINISHED'}

class ST_Add_Math_Node(bpy.types.Operator):
    bl_idname = "node.ts_math"
    bl_label = "Node.ts_node_Math"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeMath", use_transform=True)
        return {'FINISHED'}

class ST_Add_RGBToBW_Node(bpy.types.Operator):
    bl_idname = "node.ts_rgbtobw"
    bl_label = "Node.ts_node_RGBToBW"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeRGBToBW", use_transform=True)
        return {'FINISHED'}

class ST_Add_SeparateHSV_Node(bpy.types.Operator):
    bl_idname = "node.ts_separatehsv"
    bl_label = "Node.ts_node_SeparateHSV"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeSeparateHSV", use_transform=True)
        return {'FINISHED'}

class ST_Add_SeparateRGB_Node(bpy.types.Operator):
    bl_idname = "node.ts_separatergb"
    bl_label = "Node.ts_node_SeparateRGB"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeSeparateRGB", use_transform=True)
        return {'FINISHED'}

class ST_Add_SeparateXYZ_Node(bpy.types.Operator):
    bl_idname = "node.ts_separatexyz"
    bl_label = "Node.ts_node_SeparateXYZ"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeSeparateXYZ", use_transform=True)
        return {'FINISHED'}

class ST_Add_VectorMath_Node(bpy.types.Operator):
    bl_idname = "node.ts_vectormath"
    bl_label = "Node.ts_node_VectorMath"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeVectorMath", use_transform=True)
        return {'FINISHED'}

class ST_Add_Wavelength_Node(bpy.types.Operator):
    bl_idname = "node.ts_wavelength"
    bl_label = "Node.ts_node_Wavelength"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeWavelength", use_transform=True)
        return {'FINISHED'}




class ShaderEditor_Add_Converter(bpy.types.Panel):
    bl_label = "Converter"
    bl_idname = "Shader_Converter"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_blackbody", text="Blackbody 黑体")
        props = layout.operator("node.ts_clamp", text="Clamp 钳制")
        props = layout.operator("node.ts_valtorgb", text="Color Ramp 颜色渐变")
        props = layout.operator("node.ts_combinehsv", text="Combine HSV 合并HSV")
        props = layout.operator("node.ts_combinergb", text="Combine RGB 合并RGN")
        props = layout.operator("node.ts_combinexyz", text="Combine XYZ 合并XYZ")
        props = layout.operator("node.ts_maprange", text="Map Range 范围映射")
        props = layout.operator("node.ts_math", text="Math 运算")
        props = layout.operator("node.ts_rgbtobw", text="RGB To BW")
        props = layout.operator("node.ts_separatehsv", text="Separate HSV 分离HSV")
        props = layout.operator("node.ts_separatergb", text="Separate RGB 分离RGB")
        props = layout.operator("node.ts_separatexyz", text="Separate XYZ 分离XYZ")
        props = layout.operator("node.ts_vectormath", text="Vector Math 矢量运算")
        props = layout.operator("node.ts_wavelength", text="Wavelength 波长")

############################################################################################脚本节点
class ST_Add_Script_Node(bpy.types.Operator):
    bl_idname = "node.ts_script"
    bl_label = "Node.ts_node_Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="ShaderNodeScript", use_transform=True)
        return {'FINISHED'}



class ShaderEditor_Add_Script(bpy.types.Panel):
    bl_label = "Script"
    bl_idname = "Shader_Script"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_script", text="Script 脚本")


##############################################################################################组节点
class ShaderEditor_Add_Group(bpy.types.Panel):
    bl_label = "Group"
    bl_idname = "Shader_Group"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.group_make", text="Make Group")
        props = layout.operator("node.group_ungroup", text="Ungroup")



###############################################################################################布局节点
class ST_Add_NodeFrame_Node(bpy.types.Operator):
    bl_idname = "node.ts_nodeframe"
    bl_label = "Node.ts_node_NodeFrame"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="NodeFrame", use_transform=True)
        return {'FINISHED'}

class ST_Add_NodeReroute_Node(bpy.types.Operator):
    bl_idname = "node.ts_nodereroute"
    bl_label = "Node.ts_node_NodeReroute"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.node.add_node('INVOKE_DEFAULT', type="NodeReroute", use_transform=True)
        return {'FINISHED'}



class ShaderEditor_Add_Layout(bpy.types.Panel):
    bl_label = "Layout"
    bl_idname = "Shader_Layout"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Shader Node"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        props = layout.operator("node.ts_nodeframe", text="Frame 框")
        props = layout.operator("node.ts_nodereroute", text="Reroute 转接点")

##################################################################################################




#新注册插件函数 
classes = [Info_Speed_Button, ST_Add_PLAIN_AXES_Obje,

           ShaderEditor_Add_Search, 

           ST_Add_AO_Node, ST_Add_Attribute_Node, ST_Add_Bevel_Node, ST_Add_CameraData_Node, 
           ST_Add_Fresnel_Node, ST_Add_Geometry_Node, ST_Add_HairInfo_Node,  ST_Add_LayerWeight_Node,
           ST_Add_LightPath_Node, ST_Add_ObjectInfo_Node, ST_Add_ParticleInfo_Node, ST_Add_RGB_Node,
           ST_Add_Tangent_Node, ST_Add_TexCoord_Node, ST_Add_UVMap_Node, ST_Add_Value_Node,
           ST_Add_VertexColor_Node, ST_Add_VolumeInfo_Node, ST_Add_Wireframe_Node,
           ShaderEditor_Add_Input,

           ST_Add_OutputAOV_Node, ST_Add_OutputLight_Node, ST_Add_OutputMaterial_Node,
           ShaderEditor_Add_Output,

           ST_Add_AddShader_Node, ST_Add_BsdfAnisotropic_Node, ST_Add_BsdfDiffuse_Node, ST_Add_Emission_Node, 
           ST_Add_BsdfGlass_Node, ST_Add_BsdfGlossy_Node, ST_Add_BsdfHair_Node, ST_Add_Holdout_Node, ST_Add_MixShader_Node, ST_Add_BsdfPrincipled_Node,
           ST_Add_BsdfHairPrincipled_Node, ST_Add_VolumePrincipled_Node, ST_Add_BsdfRefraction_Node, ST_Add_Specular_Node, 
           ST_Add_SubsurfaceScattering_Node, ST_Add_BsdfToon_Node, ST_Add_BsdfTranslucent_Node, ST_Add_BsdfTransparent_Node,
           ST_Add_BsdfVelvet_Node, ST_Add_VolumeAbsorption_Node, ST_Add_VolumeScatter_Node,
           ShaderEditor_Add_Shader, 
           
           ST_Add_TexBrick_Node, ST_Add_TexChecker_Node, ST_Add_TexEnvironment_Node, ST_Add_TexGradient_Node,
           ST_Add_TexIES_Node, ST_Add_TexImage_Node, ST_Add_TexMagic_Node, ST_Add_TexMusgrave_Node, 
           ST_Add_TexNoise_Node, ST_Add_TexPointDensity_Node, ST_Add_TexSky_Node, ST_Add_TexVoronoi_Node,
           ST_Add_TexWave_Node, ST_Add_TexWhiteNoise_Node,
           ShaderEditor_Add_Texture,
           
           ST_Add_BrightContrast_Node, ST_Add_Gamma_Node, ST_Add_HueSaturation_Node, ST_Add_Invert_Node,
           ST_Add_LightFalloff_Node, ST_Add_MixRGB_Node, ST_Add_RGBCurve_Node, 
           ShaderEditor_Add_Color, 

           ST_Add_Bump_Node, ST_Add_Displacement_Node, ST_Add_Mapping_Node, ST_Add_Normal_Node, ST_Add_NormalMap_Node,
           ST_Add_VectorCurve_Node, ST_Add_VectorDisplacement_Node, ST_Add_VectorRotate_Node, ST_Add_VectorTransform_Node,
           ShaderEditor_Add_Vector, 

           ST_Add_Blackbody_Node, ST_Add_Clamp_Node, ST_Add_ValToRGB_Node, ST_Add_CombineHSV_Node, ST_Add_CombineRGB_Node,
           ST_Add_CombineXYZ_Node, ST_Add_MapRange_Node, ST_Add_Math_Node, ST_Add_RGBToBW_Node, ST_Add_SeparateHSV_Node,
           ST_Add_SeparateRGB_Node, ST_Add_SeparateXYZ_Node, ST_Add_VectorMath_Node, ST_Add_Wavelength_Node,
           ShaderEditor_Add_Converter,

           ST_Add_Script_Node, ShaderEditor_Add_Script, 

           ST_Add_NodeFrame_Node, ST_Add_NodeReroute_Node, ShaderEditor_Add_Group, 
           ShaderEditor_Add_Layout ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()



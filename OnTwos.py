
import bpy 
from bpy.props import IntProperty

bl_info = {
    'name': 'OnTwos-fy',
    'description': 'A plugin to turn animations into 2D animation-like on twos.',
    'author': 'KripC',
    'version': (0, 1, 0),
    "blender": (3, 1, 0),
    'location': 'View3D > Tools > OnTwos-fy',
    'link': '',
    'category': 'Animate'
}

class OTProperty(bpy.types.PropertyGroup):
    key_str : IntProperty(
        name = "Start Frame",
        description = "value for the start frame of the breakdown animation",
        default = 1,
    )
    
    key_end : IntProperty(
        name = "End Frame",
        description = "value for the end frame of the breakdown animation",
        default = 120,
    )

class OT_Process(bpy.types.Operator):
    bl_idname = "otfy.proces"
    bl_label = "OnTwos-fy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        on_two = False 
        scene = context.scene
        my_twol = scene.OTfy_tools
        
        return {'FINISHED'}
        
        
        

class OnTwos(bpy.types.Panel):
    bl_label = "ontwos-fy"
    bl_idname = "OTfy.id"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OnTwos-fy"
    bl_label = "OnTwos-fy"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytwol = scene.OTfy_tools
        
        layout.operator(OT_Process.bl_idname, text="OnTwos-fy!", icon="SORT_ASC")
        layout.prop(mytwol, "key_str")
        layout.prop(mytwol, "key_end")
        
classes = (
    OTProperty,
    OT_Process,
    OnTwos,
)
    
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.OTfy_tools = bpy.props.PointerProperty(type=OTProperty)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.OTfy_tools
        
if __name__ == "__main__":
    register()
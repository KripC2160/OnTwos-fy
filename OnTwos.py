
import bpy 
from bpy.props import IntProperty, BoolProperty

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
    
    custom_keyframe: BoolProperty(
        name = "Custom Keyframe",
        description = "set custom keyframe to apply the OnTwo-fy to",
        default = False,
    )
    
    key_str : IntProperty(
        name = "Start Frame",
        description = "value for the start frame of the breakdown animation",
        default = 0,
    )
    
    key_end : IntProperty(
        name = "End Frame",
        description = "value for the end frame of the breakdown animation",
        default = 0,
    )
    

class OT_Process(bpy.types.Operator):
    bl_idname = "otfy.process"
    bl_label = "OnTwos-fy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        on_two = False 
        scene = context.scene
        my_twol = scene.OTfy_tools
        bonecount = 0 

        if my_twol.custom_keyframe == False:
            if context.active_object.type == "ARMATURE":
                for bone in bpy.data.objects[context.active_object.name].data.bones:
                    bone.select = True
                    for f in range(scene.frame_start, scene.frame_end+1):
                        bpy.context.scene.frame_set(f)
                        if on_two == False:
                            bpy.context.selected_objects[0].pose.bones[bonecount].keyframe_insert(data_path="location", frame=f)
                            bpy.context.selected_objects[0].pose.bones[bonecount].keyframe_insert(data_path="rotation", frame=f)
                            bpy.context.selected_objects[0].pose.bones[bonecount].keyframe_insert(data_path="scale", frame=f)
                            on_two = True
                        elif on_two == True:
                            on_two = False 
                    bonecount += 1
            for f in range(scene.frame_start, scene.frame_end+1):
                bpy.context.scene.frame_set(f)
                context.active_object.type.keyframe_insert(data_path="location", frame=f)
                context.active_object.type.keyframe_insert(data_path="rotation", frame=f)
                context.active_object.type.keyframe_insert(data_path="scale", frame=f)
        else:
            x = mytwol.key_str
            
            for x in range(mytwol.key_end):
                pass
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
        
        layout.operator(OT_Process.bl_idname, text="OnTwos-fy!", icon="POSE_HLT")
        layout.prop(mytwol, "custom_keyframe")
        layout = layout.row(align=True)
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
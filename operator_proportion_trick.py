bl_info = {
    "name": "Proportion Trick",
    "author": "Β L Λ Ζ Ξ",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "View3D > Tool Shelf > Β L Λ Ζ Ξ",
    "description": "Automatically align the bones so you don't have to spend too much time doing it manually",
    "warning": "",
    "wiki_url": "",
    "category": "Scene",
    }
    
import bpy
from collections import OrderedDict

def main(context):
    obj = bpy.data.objects

    try:
        armature = obj['gg']
    except:
        raise Exception('gg skeleton not found. You must rename imported skeleton to gg. Watch the video again carefully.')

    if armature.type != 'ARMATURE': raise Exception('gg must be an ARMATURE not '+armature.type)

    valvebipeds = [
        'ValveBiped.Bip01_Pelvis',
        'ValveBiped.Bip01_Spine',
        'ValveBiped.Bip01_Spine1',
        'ValveBiped.Bip01_Spine2',
        'ValveBiped.Bip01_Spine4',
        'ValveBiped.Bip01_Neck1',
        'ValveBiped.Bip01_Head1',
        'ValveBiped.Bip01_R_Clavicle',
        'ValveBiped.Bip01_R_UpperArm',
        'ValveBiped.Bip01_R_Forearm',
        'ValveBiped.Bip01_R_Hand',
        'ValveBiped.Bip01_R_Finger0',
        'ValveBiped.Bip01_R_Finger01',
        'ValveBiped.Bip01_R_Finger02',
        'ValveBiped.Bip01_R_Finger1',
        'ValveBiped.Bip01_R_Finger11',
        'ValveBiped.Bip01_R_Finger12',
        'ValveBiped.Bip01_R_Finger2',
        'ValveBiped.Bip01_R_Finger21',
        'ValveBiped.Bip01_R_Finger22',
        'ValveBiped.Bip01_R_Finger3',
        'ValveBiped.Bip01_R_Finger31',
        'ValveBiped.Bip01_R_Finger32',
        'ValveBiped.Bip01_R_Finger4',
        'ValveBiped.Bip01_R_Finger41',
        'ValveBiped.Bip01_R_Finger42',
        'ValveBiped.Bip01_L_Clavicle',
        'ValveBiped.Bip01_L_UpperArm',
        'ValveBiped.Bip01_L_Forearm',
        'ValveBiped.Bip01_L_Hand',
        'ValveBiped.Bip01_L_Finger0',
        'ValveBiped.Bip01_L_Finger01',
        'ValveBiped.Bip01_L_Finger02',
        'ValveBiped.Bip01_L_Finger1',
        'ValveBiped.Bip01_L_Finger11',
        'ValveBiped.Bip01_L_Finger12',
        'ValveBiped.Bip01_L_Finger2',
        'ValveBiped.Bip01_L_Finger21',
        'ValveBiped.Bip01_L_Finger22',
        'ValveBiped.Bip01_L_Finger3',
        'ValveBiped.Bip01_L_Finger31',
        'ValveBiped.Bip01_L_Finger32',
        'ValveBiped.Bip01_L_Finger4',
        'ValveBiped.Bip01_L_Finger41',
        'ValveBiped.Bip01_L_Finger42',
        'ValveBiped.Bip01_R_Thigh',
        'ValveBiped.Bip01_R_Calf',
        'ValveBiped.Bip01_R_Foot',
        'ValveBiped.Bip01_R_Toe0',
        'ValveBiped.Bip01_L_Thigh',
        'ValveBiped.Bip01_L_Calf',
        'ValveBiped.Bip01_L_Foot',
        'ValveBiped.Bip01_L_Toe0',
        ]
        
    valvebipeds2 = [
        'ValveBiped.Bip01_L_Thigh',
        'ValveBiped.Bip01_L_Calf',
        'ValveBiped.Bip01_L_Calf',
        'ValveBiped.Bip01_L_Foot',
        'ValveBiped.Bip01_R_Thigh',
        'ValveBiped.Bip01_R_Calf',
        'ValveBiped.Bip01_R_Calf',
        'ValveBiped.Bip01_R_Foot',
        'ValveBiped.Bip01_L_UpperArm',
        'ValveBiped.Bip01_L_Forearm',
        'ValveBiped.Bip01_L_Forearm',
        'ValveBiped.Bip01_L_Hand',
        'ValveBiped.Bip01_R_UpperArm',
        'ValveBiped.Bip01_R_Forearm',
        'ValveBiped.Bip01_R_Forearm',
        'ValveBiped.Bip01_R_Hand',
        'ValveBiped.Bip01_L_Finger0',
        'ValveBiped.Bip01_L_Finger01',
        'ValveBiped.Bip01_L_Finger01',
        'ValveBiped.Bip01_L_Finger02',
        'ValveBiped.Bip01_L_Finger1',
        'ValveBiped.Bip01_L_Finger11',
        'ValveBiped.Bip01_L_Finger11',
        'ValveBiped.Bip01_L_Finger12',
        'ValveBiped.Bip01_L_Finger2',
        'ValveBiped.Bip01_L_Finger21',
        'ValveBiped.Bip01_L_Finger21',
        'ValveBiped.Bip01_L_Finger22',
        'ValveBiped.Bip01_L_Finger3',
        'ValveBiped.Bip01_L_Finger31',
        'ValveBiped.Bip01_L_Finger31',
        'ValveBiped.Bip01_L_Finger32',
        'ValveBiped.Bip01_L_Finger4',
        'ValveBiped.Bip01_L_Finger41',
        'ValveBiped.Bip01_L_Finger41',
        'ValveBiped.Bip01_L_Finger42',
        'ValveBiped.Bip01_R_Finger0',
        'ValveBiped.Bip01_R_Finger01',
        'ValveBiped.Bip01_R_Finger01',
        'ValveBiped.Bip01_R_Finger02',
        'ValveBiped.Bip01_R_Finger1',
        'ValveBiped.Bip01_R_Finger11',
        'ValveBiped.Bip01_R_Finger11',
        'ValveBiped.Bip01_R_Finger12',
        'ValveBiped.Bip01_R_Finger2',
        'ValveBiped.Bip01_R_Finger21',
        'ValveBiped.Bip01_R_Finger21',
        'ValveBiped.Bip01_R_Finger22',
        'ValveBiped.Bip01_R_Finger3',
        'ValveBiped.Bip01_R_Finger31',
        'ValveBiped.Bip01_R_Finger31',
        'ValveBiped.Bip01_R_Finger32',
        'ValveBiped.Bip01_R_Finger4',
        'ValveBiped.Bip01_R_Finger41',
        'ValveBiped.Bip01_R_Finger41',
        'ValveBiped.Bip01_R_Finger42',
        ]
        
    target = valvebipeds2[::2]
    sub = valvebipeds2[1::2]

    d = OrderedDict()
    for idx, value in enumerate(sub):
        key = 'var' + str(idx)
        d[key] = value 
        
    for i in valvebipeds:
        objbone = bpy.data.objects['proportions'].pose.bones[i].constraints
        
        if armature.pose.bones.get(i) is not None:
            objbone.new('COPY_LOCATION')
            objbone['Copy Location'].target = armature
            objbone['Copy Location'].subtarget = i

    for j, k in enumerate(target):
        objbone2 = bpy.data.objects['proportions'].pose.bones[k].constraints
        
        if armature.pose.bones.get(k) is not None:
            objbone2.new('LOCKED_TRACK')
            objbone2['Locked Track'].target = armature
            objbone2['Locked Track'].subtarget = d["var"+str(j)]
            objbone2['Locked Track'].track_axis = 'TRACK_X'
            objbone2['Locked Track'].lock_axis = 'LOCK_Z'
            objbone2.new('LOCKED_TRACK')
            objbone2['Locked Track.001'].target = armature
            objbone2['Locked Track.001'].subtarget = d["var"+str(j)]
            objbone2['Locked Track.001'].track_axis = 'TRACK_X'
            objbone2['Locked Track.001'].lock_axis = 'LOCK_Y'

    #added on Feb 2021
    #this part removes LOCKED_TRACK on parent if child constraint is empty			
    for l in valvebipeds:
        objbone3 = bpy.data.objects['proportions'].pose.bones[l]
            
        for child in objbone3.children:    
            objbone4 = bpy.data.objects['proportions'].pose.bones[child.name].constraints
            
            if not objbone4.keys():
                if objbone3.parent is not None:
                    objbone5 = bpy.data.objects['proportions'].pose.bones[l].constraints
                    
                    for constraint in objbone5:
                        if constraint.name != 'Copy Location':
                            objbone5.remove(constraint)
        
            print(l+' is a parent of '+child.name+' with constraint: ',objbone3.constraints.keys())
            
    bpy.context.scene.layers[1] = True
    bpy.context.scene.layers[0] = False
    bpy.context.scene.objects.active = bpy.data.objects["proportions"]
    bpy.data.objects['proportions'].select = True
    bpy.ops.object.mode_set(mode='POSE')

class ProportionTrick(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "blz.proportion_trick"
    bl_label = "1. Proportion Trick"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
class MergeSkeleton(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "blz.merge_skeleton"
    bl_label = "2. Merge Skeleton"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        arm = bpy.data.objects['gg']
        arm2 = bpy.data.objects['proportions']
        objects = bpy.context.scene.objects

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.duplicate()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')

        valvebipeds = [
        	'ValveBiped.Bip01_Pelvis',
        	'ValveBiped.Bip01_Spine',
        	'ValveBiped.Bip01_Spine1',
        	'ValveBiped.Bip01_Spine2',
        	'ValveBiped.Bip01_Spine4',
        	'ValveBiped.Bip01_Neck1',
        	'ValveBiped.Bip01_Head1',
        	'ValveBiped.Bip01_R_Clavicle',
        	'ValveBiped.Bip01_R_UpperArm',
        	'ValveBiped.Bip01_R_Forearm',
        	'ValveBiped.Bip01_R_Hand',
        	'ValveBiped.Bip01_R_Finger0',
        	'ValveBiped.Bip01_R_Finger01',
        	'ValveBiped.Bip01_R_Finger02',
        	'ValveBiped.Bip01_R_Finger1',
        	'ValveBiped.Bip01_R_Finger11',
        	'ValveBiped.Bip01_R_Finger12',
        	'ValveBiped.Bip01_R_Finger2',
        	'ValveBiped.Bip01_R_Finger21',
        	'ValveBiped.Bip01_R_Finger22',
        	'ValveBiped.Bip01_R_Finger3',
        	'ValveBiped.Bip01_R_Finger31',
        	'ValveBiped.Bip01_R_Finger32',
        	'ValveBiped.Bip01_R_Finger4',
        	'ValveBiped.Bip01_R_Finger41',
        	'ValveBiped.Bip01_R_Finger42',
        	'ValveBiped.Bip01_L_Clavicle',
        	'ValveBiped.Bip01_L_UpperArm',
        	'ValveBiped.Bip01_L_Forearm',
        	'ValveBiped.Bip01_L_Hand',
        	'ValveBiped.Bip01_L_Finger0',
        	'ValveBiped.Bip01_L_Finger01',
        	'ValveBiped.Bip01_L_Finger02',
        	'ValveBiped.Bip01_L_Finger1',
        	'ValveBiped.Bip01_L_Finger11',
        	'ValveBiped.Bip01_L_Finger12',
        	'ValveBiped.Bip01_L_Finger2',
        	'ValveBiped.Bip01_L_Finger21',
        	'ValveBiped.Bip01_L_Finger22',
        	'ValveBiped.Bip01_L_Finger3',
        	'ValveBiped.Bip01_L_Finger31',
        	'ValveBiped.Bip01_L_Finger32',
        	'ValveBiped.Bip01_L_Finger4',
        	'ValveBiped.Bip01_L_Finger41',
        	'ValveBiped.Bip01_L_Finger42',
        	'ValveBiped.Bip01_R_Thigh',
        	'ValveBiped.Bip01_R_Calf',
        	'ValveBiped.Bip01_R_Foot',
        	'ValveBiped.Bip01_R_Toe0',
        	'ValveBiped.Bip01_L_Thigh',
        	'ValveBiped.Bip01_L_Calf',
        	'ValveBiped.Bip01_L_Foot',
        	'ValveBiped.Bip01_L_Toe0',
        	]

        bn = []
        pr = []

        for bone in bpy.context.object.data.edit_bones:
        	if bone.name in valvebipeds:
        		bone.select = True
        		bone.select_head = True
        		bone.select_tail = True

        bpy.ops.armature.delete()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.move_to_layer(layers=(False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.scene.layers[1] = True
        bpy.context.scene.layers[0] = False
        bpy.context.scene.objects.active = bpy.data.objects["proportions"]
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.join()
        bpy.ops.object.mode_set(mode='EDIT')

        for bone in arm.data.bones:
        	if bone.name not in valvebipeds:
        	   bn.append(bone.name)

        for bone in arm.data.bones:
        	if bone.name not in valvebipeds:
        	   pr.append(getattr(bone.parent, "name", "ValveBiped.Bip01_Pelvis"))

        for bone in bpy.context.object.data.edit_bones:
            j = 0    
            i = 0
            while j < len(bn) and i < len(pr):
            	   arm2.data.edit_bones[bn[i]].parent = arm2.data.edit_bones[pr[j]]
            	   j += 1        
            	   i += 1
        		
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.scene.layers[0] = True
        bpy.context.scene.layers[1] = False

        #add armature modifier
        for ob in objects:
            if ob.type == 'MESH':
                if ob.modifiers.values() == []:
                    ob.modifiers.new('Armature', 'ARMATURE')
                    ob.modifiers['Armature'].object = bpy.data.objects['proportions']
                else:
                    for mods in ob.modifiers.values():
                        if mods.name == 'Armature':
                            ob.modifiers['Armature'].object = bpy.data.objects['proportions']
                        else:
                            ob.modifiers.new('Armature', 'ARMATURE')
                            ob.modifiers['Armature'].object = bpy.data.objects['proportions']
                            
        bpy.context.scene.objects.active = bpy.data.objects["gg"]
        bpy.data.objects['gg'].select = True
        bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False))
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.move_to_layer(layers=(False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.scene.layers[1] = True
        bpy.context.scene.layers[0] = False
        return {'FINISHED'}

class ProportionTrickPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Proportion Trick"
    bl_idname = "OBJECT_PT_proportion"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Β L Λ Ζ Ξ"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("blz.proportion_trick")
                
        row = layout.row()
        row.operator("blz.merge_skeleton")

def register():
    bpy.utils.register_class(ProportionTrick)
    bpy.utils.register_class(MergeSkeleton)
    bpy.utils.register_class(ProportionTrickPanel)

def unregister():
    bpy.utils.unregister_class(ProportionTrick)
    bpy.utils.unregister_class(MergeSkeleton)
    bpy.utils.unregister_class(ProportionTrickPanel)

if __name__ == "__main__":
    register()
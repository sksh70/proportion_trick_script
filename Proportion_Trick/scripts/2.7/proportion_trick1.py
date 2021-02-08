#Proportion Trick script by Β L Λ Ζ Ξ
#Blender version: 2.79
#Aligns proportion to imported skeleton.
#Video (2.79): https://www.youtube.com/watch?v=MSWirIyobb4
#Video (2.8+): https://www.youtube.com/watch?v=n9lmxpjSv0I

import bpy

obj = bpy.data.objects

armature = obj['gg']

objbone = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Pelvis'].constraints

objbone2 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Thigh'].constraints
objbone3 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Calf'].constraints
objbone4 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Foot'].constraints
objbone5 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Toe0'].constraints

objbone6 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Thigh'].constraints
objbone7 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Calf'].constraints
objbone8 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Foot'].constraints
objbone9 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Toe0'].constraints

objbone10 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Spine'].constraints
objbone11 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Spine1'].constraints
objbone12 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Spine2'].constraints
objbone13 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Spine4'].constraints
objbone14 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Neck1'].constraints
objbone15 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_Head1'].constraints

objbone16 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Clavicle'].constraints
objbone17 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_UpperArm'].constraints
objbone18 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Forearm'].constraints

objbone19 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Clavicle'].constraints
objbone20 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_UpperArm'].constraints
objbone21 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Forearm'].constraints

objbone22 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Hand'].constraints
objbone23 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger0'].constraints
objbone24 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger01'].constraints
objbone25 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger02'].constraints
objbone26 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger1'].constraints
objbone27 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger11'].constraints
objbone28 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger12'].constraints
objbone29 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger2'].constraints
objbone30 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger21'].constraints
objbone31 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger22'].constraints
objbone32 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger3'].constraints
objbone33 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger31'].constraints
objbone34 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger32'].constraints
objbone35 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger4'].constraints
objbone36 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger41'].constraints
objbone37 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_L_Finger42'].constraints

objbone38 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Hand'].constraints
objbone39 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger0'].constraints
objbone40 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger01'].constraints
objbone41 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger02'].constraints
objbone42 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger1'].constraints
objbone43 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger11'].constraints
objbone44 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger12'].constraints
objbone45 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger2'].constraints
objbone46 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger21'].constraints
objbone47 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger22'].constraints
objbone48 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger3'].constraints
objbone49 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger31'].constraints
objbone50 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger32'].constraints
objbone51 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger4'].constraints
objbone52 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger41'].constraints
objbone53 = bpy.data.objects['proportions'].pose.bones['ValveBiped.Bip01_R_Finger42'].constraints

if armature.pose.bones.get('ValveBiped.Bip01_Pelvis') is not None:
    objbone.new('COPY_LOCATION')
    objbone['Copy Location'].target = armature
    objbone['Copy Location'].subtarget = 'ValveBiped.Bip01_Pelvis'

if armature.pose.bones.get('ValveBiped.Bip01_L_Thigh') is not None:
    objbone2.new('COPY_LOCATION')
    objbone2['Copy Location'].target = armature
    objbone2['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Thigh'
if armature.pose.bones.get('ValveBiped.Bip01_L_Calf') is not None:
    objbone2.new('LOCKED_TRACK')
    objbone2['Locked Track'].target = armature
    objbone2['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Calf'
    objbone2['Locked Track'].track_axis = 'TRACK_X'
    objbone2['Locked Track'].lock_axis = 'LOCK_Z'
    objbone2.new('LOCKED_TRACK')
    objbone2['Locked Track.001'].target = armature
    objbone2['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Calf'
    objbone2['Locked Track.001'].track_axis = 'TRACK_X'
    objbone2['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Calf') is not None:
    objbone3.new('COPY_LOCATION')
    objbone3['Copy Location'].target = armature
    objbone3['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Calf'
if armature.pose.bones.get('ValveBiped.Bip01_L_Foot') is not None:
    objbone3.new('LOCKED_TRACK')
    objbone3['Locked Track'].target = armature
    objbone3['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Foot'
    objbone3['Locked Track'].track_axis = 'TRACK_X'
    objbone3['Locked Track'].lock_axis = 'LOCK_Z'
    objbone3.new('LOCKED_TRACK')
    objbone3['Locked Track.001'].target = armature
    objbone3['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Foot'
    objbone3['Locked Track.001'].track_axis = 'TRACK_X'
    objbone3['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Foot') is not None:
    objbone4.new('COPY_LOCATION')
    objbone4['Copy Location'].target = armature
    objbone4['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Foot'

if armature.pose.bones.get('ValveBiped.Bip01_L_Toe0') is not None:
    objbone5.new('COPY_LOCATION')
    objbone5['Copy Location'].target = armature
    objbone5['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Toe0'

if armature.pose.bones.get('ValveBiped.Bip01_R_Thigh') is not None:
    objbone6.new('COPY_LOCATION')
    objbone6['Copy Location'].target = armature
    objbone6['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Thigh'
if armature.pose.bones.get('ValveBiped.Bip01_R_Calf') is not None:
    objbone6.new('LOCKED_TRACK')
    objbone6['Locked Track'].target = armature
    objbone6['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Calf'
    objbone6['Locked Track'].track_axis = 'TRACK_X'
    objbone6['Locked Track'].lock_axis = 'LOCK_Z'
    objbone6.new('LOCKED_TRACK')
    objbone6['Locked Track.001'].target = armature
    objbone6['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Calf'
    objbone6['Locked Track.001'].track_axis = 'TRACK_X'
    objbone6['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Calf') is not None:
    objbone7.new('COPY_LOCATION')
    objbone7['Copy Location'].target = armature
    objbone7['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Calf'
if armature.pose.bones.get('ValveBiped.Bip01_R_Foot') is not None:
    objbone7.new('LOCKED_TRACK')
    objbone7['Locked Track'].target = armature
    objbone7['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Foot'
    objbone7['Locked Track'].track_axis = 'TRACK_X'
    objbone7['Locked Track'].lock_axis = 'LOCK_Z'
    objbone7.new('LOCKED_TRACK')
    objbone7['Locked Track.001'].target = armature
    objbone7['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Foot'
    objbone7['Locked Track.001'].track_axis = 'TRACK_X'
    objbone7['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Foot') is not None:
    objbone8.new('COPY_LOCATION')
    objbone8['Copy Location'].target = armature
    objbone8['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Foot'

if armature.pose.bones.get('ValveBiped.Bip01_R_Toe0') is not None:
    objbone9.new('COPY_LOCATION')
    objbone9['Copy Location'].target = armature
    objbone9['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Toe0'

if armature.pose.bones.get('ValveBiped.Bip01_Spine') is not None:
    objbone10.new('COPY_LOCATION')
    objbone10['Copy Location'].target = armature
    objbone10['Copy Location'].subtarget = 'ValveBiped.Bip01_Spine'

if armature.pose.bones.get('ValveBiped.Bip01_Spine1') is not None:
    objbone11.new('COPY_LOCATION')
    objbone11['Copy Location'].target = armature
    objbone11['Copy Location'].subtarget = 'ValveBiped.Bip01_Spine1'

if armature.pose.bones.get('ValveBiped.Bip01_Spine2') is not None:
    objbone12.new('COPY_LOCATION')
    objbone12['Copy Location'].target = armature
    objbone12['Copy Location'].subtarget = 'ValveBiped.Bip01_Spine2'

if armature.pose.bones.get('ValveBiped.Bip01_Spine4') is not None:
    objbone13.new('COPY_LOCATION')
    objbone13['Copy Location'].target = armature
    objbone13['Copy Location'].subtarget = 'ValveBiped.Bip01_Spine4'

if armature.pose.bones.get('ValveBiped.Bip01_Neck1') is not None:
    objbone14.new('COPY_LOCATION')
    objbone14['Copy Location'].target = armature
    objbone14['Copy Location'].subtarget = 'ValveBiped.Bip01_Neck1'

if armature.pose.bones.get('ValveBiped.Bip01_Head1') is not None:
    objbone15.new('COPY_LOCATION')
    objbone15['Copy Location'].target = armature
    objbone15['Copy Location'].subtarget = 'ValveBiped.Bip01_Head1'

if armature.pose.bones.get('ValveBiped.Bip01_L_Clavicle') is not None:
    objbone16.new('COPY_LOCATION')
    objbone16['Copy Location'].target = armature
    objbone16['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Clavicle'

if armature.pose.bones.get('ValveBiped.Bip01_L_UpperArm') is not None:
    objbone17.new('COPY_LOCATION')
    objbone17['Copy Location'].target = armature
    objbone17['Copy Location'].subtarget = 'ValveBiped.Bip01_L_UpperArm'
if armature.pose.bones.get('ValveBiped.Bip01_L_Forearm') is not None:
    objbone17.new('LOCKED_TRACK')
    objbone17['Locked Track'].target = armature
    objbone17['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Forearm'
    objbone17['Locked Track'].track_axis = 'TRACK_X'
    objbone17['Locked Track'].lock_axis = 'LOCK_Z'
    objbone17.new('LOCKED_TRACK')
    objbone17['Locked Track.001'].target = armature
    objbone17['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Forearm'
    objbone17['Locked Track.001'].track_axis = 'TRACK_X'
    objbone17['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Forearm') is not None:
    objbone18.new('COPY_LOCATION')
    objbone18['Copy Location'].target = armature
    objbone18['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Forearm'
if armature.pose.bones.get('ValveBiped.Bip01_L_Hand') is not None:
    objbone18.new('LOCKED_TRACK')
    objbone18['Locked Track'].target = armature
    objbone18['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Hand'
    objbone18['Locked Track'].track_axis = 'TRACK_X'
    objbone18['Locked Track'].lock_axis = 'LOCK_Z'
    objbone18.new('LOCKED_TRACK')
    objbone18['Locked Track.001'].target = armature
    objbone18['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Hand'
    objbone18['Locked Track.001'].track_axis = 'TRACK_X'
    objbone18['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Clavicle') is not None:
    objbone19.new('COPY_LOCATION')
    objbone19['Copy Location'].target = armature
    objbone19['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Clavicle'

if armature.pose.bones.get('ValveBiped.Bip01_R_UpperArm') is not None:
    objbone20.new('COPY_LOCATION')
    objbone20['Copy Location'].target = armature
    objbone20['Copy Location'].subtarget = 'ValveBiped.Bip01_R_UpperArm'
if armature.pose.bones.get('ValveBiped.Bip01_R_Forearm') is not None:
    objbone20.new('LOCKED_TRACK')
    objbone20['Locked Track'].target = armature
    objbone20['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Forearm'
    objbone20['Locked Track'].track_axis = 'TRACK_X'
    objbone20['Locked Track'].lock_axis = 'LOCK_Z'
    objbone20.new('LOCKED_TRACK')
    objbone20['Locked Track.001'].target = armature
    objbone20['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Forearm'
    objbone20['Locked Track.001'].track_axis = 'TRACK_X'
    objbone20['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Forearm') is not None:
    objbone21.new('COPY_LOCATION')
    objbone21['Copy Location'].target = armature
    objbone21['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Forearm'
if armature.pose.bones.get('ValveBiped.Bip01_R_Hand') is not None:
    objbone21.new('LOCKED_TRACK')
    objbone21['Locked Track'].target = armature
    objbone21['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Hand'
    objbone21['Locked Track'].track_axis = 'TRACK_X'
    objbone21['Locked Track'].lock_axis = 'LOCK_Z'
    objbone21.new('LOCKED_TRACK')
    objbone21['Locked Track.001'].target = armature
    objbone21['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Hand'
    objbone21['Locked Track.001'].track_axis = 'TRACK_X'
    objbone21['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Hand') is not None:
    objbone22.new('COPY_LOCATION')
    objbone22['Copy Location'].target = armature
    objbone22['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Hand'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger0') is not None:
    objbone23.new('COPY_LOCATION')
    objbone23['Copy Location'].target = armature
    objbone23['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger0'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger01') is not None:
    objbone23.new('LOCKED_TRACK')
    objbone23['Locked Track'].target = armature
    objbone23['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger01'
    objbone23['Locked Track'].track_axis = 'TRACK_X'
    objbone23['Locked Track'].lock_axis = 'LOCK_Z'
    objbone23.new('LOCKED_TRACK')
    objbone23['Locked Track.001'].target = armature
    objbone23['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger01'
    objbone23['Locked Track.001'].track_axis = 'TRACK_X'
    objbone23['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger01') is not None:
    objbone24.new('COPY_LOCATION')
    objbone24['Copy Location'].target = armature
    objbone24['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger01'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger02') is not None:
    objbone24.new('LOCKED_TRACK')
    objbone24['Locked Track'].target = armature
    objbone24['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger02'
    objbone24['Locked Track'].track_axis = 'TRACK_X'
    objbone24['Locked Track'].lock_axis = 'LOCK_Z'
    objbone24.new('LOCKED_TRACK')
    objbone24['Locked Track.001'].target = armature
    objbone24['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger02'
    objbone24['Locked Track.001'].track_axis = 'TRACK_X'
    objbone24['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger02') is not None:
    objbone25.new('COPY_LOCATION')
    objbone25['Copy Location'].target = armature
    objbone25['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger02'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger1') is not None:
    objbone26.new('COPY_LOCATION')
    objbone26['Copy Location'].target = armature
    objbone26['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger1'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger11') is not None:
    objbone26.new('LOCKED_TRACK')
    objbone26['Locked Track'].target = armature
    objbone26['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger11'
    objbone26['Locked Track'].track_axis = 'TRACK_X'
    objbone26['Locked Track'].lock_axis = 'LOCK_Z'
    objbone26.new('LOCKED_TRACK')
    objbone26['Locked Track.001'].target = armature
    objbone26['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger11'
    objbone26['Locked Track.001'].track_axis = 'TRACK_X'
    objbone26['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger11') is not None:
    objbone27.new('COPY_LOCATION')
    objbone27['Copy Location'].target = armature
    objbone27['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger11'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger12') is not None:
    objbone27.new('LOCKED_TRACK')
    objbone27['Locked Track'].target = armature
    objbone27['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger12'
    objbone27['Locked Track'].track_axis = 'TRACK_X'
    objbone27['Locked Track'].lock_axis = 'LOCK_Z'
    objbone27.new('LOCKED_TRACK')
    objbone27['Locked Track.001'].target = armature
    objbone27['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger12'
    objbone27['Locked Track.001'].track_axis = 'TRACK_X'
    objbone27['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger12') is not None:
    objbone28.new('COPY_LOCATION')
    objbone28['Copy Location'].target = armature
    objbone28['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger12'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger2') is not None:
    objbone29.new('COPY_LOCATION')
    objbone29['Copy Location'].target = armature
    objbone29['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger2'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger21') is not None:
    objbone29.new('LOCKED_TRACK')
    objbone29['Locked Track'].target = armature
    objbone29['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger21'
    objbone29['Locked Track'].track_axis = 'TRACK_X'
    objbone29['Locked Track'].lock_axis = 'LOCK_Z'
    objbone29.new('LOCKED_TRACK')
    objbone29['Locked Track.001'].target = armature
    objbone29['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger21'
    objbone29['Locked Track.001'].track_axis = 'TRACK_X'
    objbone29['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger21') is not None:
    objbone30.new('COPY_LOCATION')
    objbone30['Copy Location'].target = armature
    objbone30['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger21'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger22') is not None:
    objbone30.new('LOCKED_TRACK')
    objbone30['Locked Track'].target = armature
    objbone30['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger22'
    objbone30['Locked Track'].track_axis = 'TRACK_X'
    objbone30['Locked Track'].lock_axis = 'LOCK_Z'
    objbone30.new('LOCKED_TRACK')
    objbone30['Locked Track.001'].target = armature
    objbone30['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger22'
    objbone30['Locked Track.001'].track_axis = 'TRACK_X'
    objbone30['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger22') is not None:
    objbone31.new('COPY_LOCATION')
    objbone31['Copy Location'].target = armature
    objbone31['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger22'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger3') is not None:
    objbone32.new('COPY_LOCATION')
    objbone32['Copy Location'].target = armature
    objbone32['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger3'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger31') is not None:
    objbone32.new('LOCKED_TRACK')
    objbone32['Locked Track'].target = armature
    objbone32['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger31'
    objbone32['Locked Track'].track_axis = 'TRACK_X'
    objbone32['Locked Track'].lock_axis = 'LOCK_Z'
    objbone32.new('LOCKED_TRACK')
    objbone32['Locked Track.001'].target = armature
    objbone32['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger31'
    objbone32['Locked Track.001'].track_axis = 'TRACK_X'
    objbone32['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger31') is not None:
    objbone33.new('COPY_LOCATION')
    objbone33['Copy Location'].target = armature
    objbone33['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger31'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger32') is not None:
    objbone33.new('LOCKED_TRACK')
    objbone33['Locked Track'].target = armature
    objbone33['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger32'
    objbone33['Locked Track'].track_axis = 'TRACK_X'
    objbone33['Locked Track'].lock_axis = 'LOCK_Z'
    objbone33.new('LOCKED_TRACK')
    objbone33['Locked Track.001'].target = armature
    objbone33['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger32'
    objbone33['Locked Track.001'].track_axis = 'TRACK_X'
    objbone33['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger32') is not None:
    objbone34.new('COPY_LOCATION')
    objbone34['Copy Location'].target = armature
    objbone34['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger32'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger4') is not None:
    objbone35.new('COPY_LOCATION')
    objbone35['Copy Location'].target = armature
    objbone35['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger4'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger41') is not None:
    objbone35.new('LOCKED_TRACK')
    objbone35['Locked Track'].target = armature
    objbone35['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger41'
    objbone35['Locked Track'].track_axis = 'TRACK_X'
    objbone35['Locked Track'].lock_axis = 'LOCK_Z'
    objbone35.new('LOCKED_TRACK')
    objbone35['Locked Track.001'].target = armature
    objbone35['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger41'
    objbone35['Locked Track.001'].track_axis = 'TRACK_X'
    objbone35['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger41') is not None:
    objbone36.new('COPY_LOCATION')
    objbone36['Copy Location'].target = armature
    objbone36['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger41'
if armature.pose.bones.get('ValveBiped.Bip01_L_Finger42') is not None:
    objbone36.new('LOCKED_TRACK')
    objbone36['Locked Track'].target = armature
    objbone36['Locked Track'].subtarget = 'ValveBiped.Bip01_L_Finger42'
    objbone36['Locked Track'].track_axis = 'TRACK_X'
    objbone36['Locked Track'].lock_axis = 'LOCK_Z'
    objbone36.new('LOCKED_TRACK')
    objbone36['Locked Track.001'].target = armature
    objbone36['Locked Track.001'].subtarget = 'ValveBiped.Bip01_L_Finger42'
    objbone36['Locked Track.001'].track_axis = 'TRACK_X'
    objbone36['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_L_Finger42') is not None:
    objbone37.new('COPY_LOCATION')
    objbone37['Copy Location'].target = armature
    objbone37['Copy Location'].subtarget = 'ValveBiped.Bip01_L_Finger42'

if armature.pose.bones.get('ValveBiped.Bip01_R_Hand') is not None:
    objbone38.new('COPY_LOCATION')
    objbone38['Copy Location'].target = armature
    objbone38['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Hand'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger0') is not None:
    objbone39.new('COPY_LOCATION')
    objbone39['Copy Location'].target = armature
    objbone39['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger0'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger01') is not None:
    objbone39.new('LOCKED_TRACK')
    objbone39['Locked Track'].target = armature
    objbone39['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger01'
    objbone39['Locked Track'].track_axis = 'TRACK_X'
    objbone39['Locked Track'].lock_axis = 'LOCK_Z'
    objbone39.new('LOCKED_TRACK')
    objbone39['Locked Track.001'].target = armature
    objbone39['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger01'
    objbone39['Locked Track.001'].track_axis = 'TRACK_X'
    objbone39['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger01') is not None:
    objbone40.new('COPY_LOCATION')
    objbone40['Copy Location'].target = armature
    objbone40['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger01'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger02') is not None:
    objbone40.new('LOCKED_TRACK')
    objbone40['Locked Track'].target = armature
    objbone40['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger02'
    objbone40['Locked Track'].track_axis = 'TRACK_X'
    objbone40['Locked Track'].lock_axis = 'LOCK_Z'
    objbone40.new('LOCKED_TRACK')
    objbone40['Locked Track.001'].target = armature
    objbone40['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger02'
    objbone40['Locked Track.001'].track_axis = 'TRACK_X'
    objbone40['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger02') is not None:
    objbone41.new('COPY_LOCATION')
    objbone41['Copy Location'].target = armature
    objbone41['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger02'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger1') is not None:
    objbone42.new('COPY_LOCATION')
    objbone42['Copy Location'].target = armature
    objbone42['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger1'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger11') is not None:
    objbone42.new('LOCKED_TRACK')
    objbone42['Locked Track'].target = armature
    objbone42['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger11'
    objbone42['Locked Track'].track_axis = 'TRACK_X'
    objbone42['Locked Track'].lock_axis = 'LOCK_Z'
    objbone42.new('LOCKED_TRACK')
    objbone42['Locked Track.001'].target = armature
    objbone42['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger11'
    objbone42['Locked Track.001'].track_axis = 'TRACK_X'
    objbone42['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger11') is not None:
    objbone43.new('COPY_LOCATION')
    objbone43['Copy Location'].target = armature
    objbone43['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger11'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger12') is not None:
    objbone43.new('LOCKED_TRACK')
    objbone43['Locked Track'].target = armature
    objbone43['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger12'
    objbone43['Locked Track'].track_axis = 'TRACK_X'
    objbone43['Locked Track'].lock_axis = 'LOCK_Z'
    objbone43.new('LOCKED_TRACK')
    objbone43['Locked Track.001'].target = armature
    objbone43['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger12'
    objbone43['Locked Track.001'].track_axis = 'TRACK_X'
    objbone43['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger12') is not None:
    objbone44.new('COPY_LOCATION')
    objbone44['Copy Location'].target = armature
    objbone44['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger12'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger2') is not None:
    objbone45.new('COPY_LOCATION')
    objbone45['Copy Location'].target = armature
    objbone45['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger2'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger21') is not None:
    objbone45.new('LOCKED_TRACK')
    objbone45['Locked Track'].target = armature
    objbone45['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger21'
    objbone45['Locked Track'].track_axis = 'TRACK_X'
    objbone45['Locked Track'].lock_axis = 'LOCK_Z'
    objbone45.new('LOCKED_TRACK')
    objbone45['Locked Track.001'].target = armature
    objbone45['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger21'
    objbone45['Locked Track.001'].track_axis = 'TRACK_X'
    objbone45['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger21') is not None:
    objbone46.new('COPY_LOCATION')
    objbone46['Copy Location'].target = armature
    objbone46['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger21'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger22') is not None:
    objbone46.new('LOCKED_TRACK')
    objbone46['Locked Track'].target = armature
    objbone46['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger22'
    objbone46['Locked Track'].track_axis = 'TRACK_X'
    objbone46['Locked Track'].lock_axis = 'LOCK_Z'
    objbone46.new('LOCKED_TRACK')
    objbone46['Locked Track.001'].target = armature
    objbone46['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger22'
    objbone46['Locked Track.001'].track_axis = 'TRACK_X'
    objbone46['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger22') is not None:
    objbone47.new('COPY_LOCATION')
    objbone47['Copy Location'].target = armature
    objbone47['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger22'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger3') is not None:
    objbone48.new('COPY_LOCATION')
    objbone48['Copy Location'].target = armature
    objbone48['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger3'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger31') is not None:
    objbone48.new('LOCKED_TRACK')
    objbone48['Locked Track'].target = armature
    objbone48['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger31'
    objbone48['Locked Track'].track_axis = 'TRACK_X'
    objbone48['Locked Track'].lock_axis = 'LOCK_Z'
    objbone48.new('LOCKED_TRACK')
    objbone48['Locked Track.001'].target = armature
    objbone48['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger31'
    objbone48['Locked Track.001'].track_axis = 'TRACK_X'
    objbone48['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger31') is not None:
    objbone49.new('COPY_LOCATION')
    objbone49['Copy Location'].target = armature
    objbone49['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger31'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger32') is not None:
    objbone49.new('LOCKED_TRACK')
    objbone49['Locked Track'].target = armature
    objbone49['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger32'
    objbone49['Locked Track'].track_axis = 'TRACK_X'
    objbone49['Locked Track'].lock_axis = 'LOCK_Z'
    objbone49.new('LOCKED_TRACK')
    objbone49['Locked Track.001'].target = armature
    objbone49['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger32'
    objbone49['Locked Track.001'].track_axis = 'TRACK_X'
    objbone49['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger32') is not None:
    objbone50.new('COPY_LOCATION')
    objbone50['Copy Location'].target = armature
    objbone50['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger32'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger4') is not None:
    objbone51.new('COPY_LOCATION')
    objbone51['Copy Location'].target = armature
    objbone51['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger4'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger41') is not None:
    objbone51.new('LOCKED_TRACK')
    objbone51['Locked Track'].target = armature
    objbone51['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger41'
    objbone51['Locked Track'].track_axis = 'TRACK_X'
    objbone51['Locked Track'].lock_axis = 'LOCK_Z'
    objbone51.new('LOCKED_TRACK')
    objbone51['Locked Track.001'].target = armature
    objbone51['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger41'
    objbone51['Locked Track.001'].track_axis = 'TRACK_X'
    objbone51['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger41') is not None:
    objbone52.new('COPY_LOCATION')
    objbone52['Copy Location'].target = armature
    objbone52['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger41'
if armature.pose.bones.get('ValveBiped.Bip01_R_Finger42') is not None:
    objbone52.new('LOCKED_TRACK')
    objbone52['Locked Track'].target = armature
    objbone52['Locked Track'].subtarget = 'ValveBiped.Bip01_R_Finger42'
    objbone52['Locked Track'].track_axis = 'TRACK_X'
    objbone52['Locked Track'].lock_axis = 'LOCK_Z'
    objbone52.new('LOCKED_TRACK')
    objbone52['Locked Track.001'].target = armature
    objbone52['Locked Track.001'].subtarget = 'ValveBiped.Bip01_R_Finger42'
    objbone52['Locked Track.001'].track_axis = 'TRACK_X'
    objbone52['Locked Track.001'].lock_axis = 'LOCK_Y'

if armature.pose.bones.get('ValveBiped.Bip01_R_Finger42') is not None:
    objbone53.new('COPY_LOCATION')
    objbone53['Copy Location'].target = armature
    objbone53['Copy Location'].subtarget = 'ValveBiped.Bip01_R_Finger42'
import bpy
import os

os.chdir('C:\\Users\\jackp\\OneDrive\\FRACTAL SALES\\NFT\\Periodic table\\Blender\\SVG')
#set working directory

frac_no = 15
svg_name = str(frac_no) + ".svg"

bpy.ops.import_curve.svg (filepath=svg_name) #load svg

bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = bpy.data.objects['path22'] #prevents error
bpy.ops.object.select_by_type(type='CURVE')    #select all the curves
bpy.ops.object.join()                         #join to one object

bpy.ops.transform.resize(value=(6, 6, 6))   #scale

bpy.ops.object.convert(target='MESH')


for o in bpy.context.scene.objects:
    if o.name == "Cube":
        bpy.data.objects['Cube'].select_set(True)
        bpy.ops.object.delete()     #delete the cube

#apply modifiers and extrusion
object_1 = bpy.data.objects['path22']
solidify_1 = object_1.modifiers.new(name="Solidify", type='SOLIDIFY')
solidify_1.offset = -1.5
solidify_1.thickness = 0.01 #0.01 to 0.02
bpy.ops.object.mode_set( mode   = 'EDIT'   )
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )
bpy.ops.mesh.extrude_region_move(
    TRANSFORM_OT_translate={"value":(0, 0.2, 0.2)} #last 0.2 - 0.5    
)     #EXTRUDE
bpy.ops.object.mode_set( mode = 'OBJECT' )
#screw_1 = object_1.modifiers.new(name="Screw", type='SCREW')
#screw_1.angle = 0.03   #use this or no screw mod
#wave_1 = object_1.modifiers.new(name="Wave", type='WAVE')
#wave_1.height = 0.2   #0.1 - 0.2
#build_1 = object_1.modifiers.new(name="Build", type='BUILD')
#build_1.length = 144


# colour
mat = bpy.data.materials.new("PKHG")
#mat.diffuse_color = (1, 0, 0.1, 1) #red
mat.diffuse_color = (0.2, 0.2, 1, 1) #blue
#mat.diffuse_color = (1, 1, 1, 0.6) #glass
#mat.diffuse_color = (1, 0.96, 0, 1) #gold
object_1 = bpy.data.objects['path22']
object_1.active_material = mat

#animate:
scene = bpy.context.scene
object_1 = bpy.data.objects['path22']
scene.frame_set(0)
object_1.rotation_euler = (3.2, 3.6, 0)
object_1.keyframe_insert(data_path="rotation_euler", index=-1)
#scene.frame_set(144)
#object_1.rotation_euler = (0, 0, 6.25)
#object_1.keyframe_insert(data_path="rotation_euler", index=-1)
#bpy.data.scenes[0].frame_start = 1
#bpy.data.scenes[0].frame_end = 144

#add text
font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
#load csv with element names:  ................
#neither numpy nor pandas works for this




#element_name = element_data[1, frac_no+1]
font_curve.body = str(frac_no) + '\r\nIsotope' #+ element_name
font_obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
bpy.context.scene.collection.objects.link(font_obj)


#export
#bpy.context.scene.render.filepath = '//my_video.avi'
#bpy.ops.render.render(animation=True)

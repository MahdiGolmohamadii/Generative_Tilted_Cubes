import bpy
import random
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)



#settings
scaling = 3/4
x = 5
y = 5
z = 6

def make_stack(x,y):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))
    cube = bpy.context.active_object
    cube.scale=(1,1,0.2)
    rnd = random.randint(0,3)

    x_to_be_or_not = random.randint(0,1)
    y_to_be_or_not = random.randint(0,1)

    x_minus_or_add = random.randint(0,1)
    y_minus_or_add = random.randint(0,1)

    for i in range(1,z):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
        bpy.context.object.modifiers["Bevel"].width_pct = 2
        bpy.context.object.modifiers["Bevel"].segments = 4



        cube = bpy.context.active_object
        cube.scale=(scaling**i, scaling**i,0.2)

        cube.location.z = i * 0.2
        if x_minus_or_add == 0: 
            cube.location.x += ((1-(scaling**i))/2) * x_to_be_or_not
        else:
            cube.location.x -= ((1-(scaling**i))/2) * x_to_be_or_not
        if y_minus_or_add == 0:
            cube.location.y += ((1-(scaling**i))/2) * y_to_be_or_not
        else:
            cube.location.y -= ((1-(scaling**i))/2) * y_to_be_or_not





for i in range(0,x):
    for j in range(0,y):
        make_stack(i,j)






        

from Montys_FreeCAD import *

a = rotate(axis = "Z", angle = 90) (cube(1))
export(name = "rotation around the origin I") (a)

a = translate([10, 0, 0]) (cube(1))
b = rotate(axis = "Z", angle = 90) (a)
export(name = "rotation around the origin II") (a + b)

a = rotate(axis = "Z", angle = 60, axis_pos = [10, 0, 0]) (a)
export(name = "rotation around an arbitrary point") (a)

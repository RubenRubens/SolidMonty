from SolidMonty_FreeCAD import *

A = rotate(axis = "Z", angle = 90) (cube(4))
export(name = "rotation around the origin I") (A)

A = translate([10, 0, 0]) (cube(4))
B = rotate(axis = "Z", angle = 90) (A)
export(name = "rotation around the origin II") (A + B)

B = rotate(axis = "Z", angle = 60, axis_pos = [10, 0, 0]) (A)
export(name = "rotation around an arbitrary point") (B)

from SolidMonty_FreeCAD import *

a = cube(20)
export_STL(a, name = "cube first octant")

b = cube(20, center = True)
export_STL(b, name = "cube center")

c = cube([65, 30, 10])
export_STL(c, "diferent sides cube")
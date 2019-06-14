from Montys_FreeCAD import *

a = cube(20)
export_STL(a, name = "cube first octant")

b = cube(20, center = True)
export_STL(a, name = "cube center")
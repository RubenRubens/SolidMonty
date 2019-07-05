from SolidMonty_FreeCAD import *

a = cylinder(r = 23, h = 12)
export_STL(a, "cylinder")

b = cylinder(r = 23, h = 12, center = True)
export_STL(b, "center cylinder")
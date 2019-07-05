from SolidMonty_FreeCAD import *

a = cone(h = 30, r1 = 25)
export_STL(a, "cone1")

b = cone(h = 30, r1 = 25, r2 = 18)
export_STL(b, "cone2")
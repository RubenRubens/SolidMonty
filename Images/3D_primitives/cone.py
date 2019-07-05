from SolidMonty_FreeCAD import *

a = cone(h = 30, r1 = 25)
export(name="cone1")(a)

b = cone(h = 30, r1 = 25, r2 = 18)
export(name="cone2")(b)
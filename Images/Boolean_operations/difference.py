from SolidMonty_FreeCAD import *

a = cube(30, center = True) - sphere(d = 34)

export(name="difference")(a)
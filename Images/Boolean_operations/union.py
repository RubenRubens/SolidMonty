from SolidMonty_FreeCAD import *

a = cube([5, 5, 1]) + cone(h = 2, r1 = 5, r2 = 4)

export(name="union") (a)
from SolidMonty_FreeCAD import *

A = circle(9)
B = translate([0, 1, 10]) (circle(13))
C = translate([0, 0, 20]) (circle(7))
S = [A, B, C]

F = loft(S)

export(name="loft") (F)
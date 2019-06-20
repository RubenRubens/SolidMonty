from Montys_FreeCAD import *

A = translate([24, 0, 0]) (circle(9))
B = revolve("Y") (A)

export(name = "revolve") (B)
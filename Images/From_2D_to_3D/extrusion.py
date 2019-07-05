from SolidMonty_FreeCAD import *

a = extrude(h = 20) (circle(r = 50))

export(name="extrusion") (a)
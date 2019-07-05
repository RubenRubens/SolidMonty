from SolidMonty_FreeCAD import *

A = rotate("Y", angle = 90) (circle(10))
path = spline(points = [[0, 0], [30, 50], [40, 59]], closed = False)

F = sweep(A, path)

export(name="sweep") (F)
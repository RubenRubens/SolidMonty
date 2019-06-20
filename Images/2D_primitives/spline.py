from Montys_FreeCAD import *

# Open
spline([[0, 0], [3, 1], [5, 9]], closed = False)

# Closed but not rounded
spline([[0, 0], [3, 1], [5, 9]], closed = True)

# Closed and rounded
spline([[0, 0], [3, 1], [5, 9]], closed = True, rounded = True)

save_FreeCAD("spline")
from SolidMonty_FreeCAD import *

# Open
polyline([[0, 0], [3, 1], [5, 9]], closed = False)

# Closed
polyline([[0, 0], [3, 1], [5, 9]])

save_FreeCAD("polyline")
from visuel import Point, Vector, findWithAngle, set_lines

#   Example 1

V = Vector(Point(160, 111), Point(160, 0))

for a in range(0, 360, 90):
  set_lines([findWithAngle(V, a, 100)], "red")

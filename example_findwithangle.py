from visuel import Point, Vector, findWithAngle, set_lines

#   Example 1
A = Point(160, 111)
V = Vector(A, Point(160, 0))

dist = 100

for a in range(0, 360, 90):
  B = findWithAngle(A, V, a, dist)
  round(B)
  set_lines([(A,B)], "red")

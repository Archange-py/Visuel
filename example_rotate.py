from visuel import Point, Vector, set_lines

A, B = Point(160, 111), Point(250, 111)
V = Vector(A, B)

set_lines([(A, B)], "red")

for a in range(8):
    V = V.rotate(45)
    round(V)
    set_lines([(A, V + A)], "red")
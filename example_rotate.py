from visuel import Point, Vector, draw_lines, set_pixel

A, B = Point(50, 50), Point(100, 50)
V = Vector(A, B)

draw_lines([(A, B)], "red")

for a in range(8):
    V = V.rotate(45) ; round(V)
    draw_lines([(A, V + A)], "red")
from visuel_5 import Point, Vecteur, rotate, draw_lines, set_pixel

A, B = Point(50, 50), Point(100, 50)
U = Vecteur(A, B)

draw_lines([(A, B)], "red")

for a in range(180):
    V = rotate(U, a)
    set_pixel(V.P2, "black")
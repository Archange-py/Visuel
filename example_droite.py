from visuel_5 import Point, Droite, draw_droites

A = Point(120, 70, "A")
B = Point(180, 30, "B")
C = Point(100, 150, "C")
D = Point(230, 140, "D")

A = Point(100, 50, "A")
B = Point(200, 50, "B")
C = Point(100, 150, "C")
D = Point(200, 150, "D")

D1 = Droite(A, B, "D1")
D2 = Droite(A, C, "D2")
D3 = Droite(C, D, "D3")
D4 = Droite(B, D, "D4")

draw_droites([D1, D2, D3, D4], 'green')
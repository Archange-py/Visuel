from Visuel import Point, draw_lines, draw_lines_AA

A = Point(50, 50)
B = Point(160, 111)
C = Point(270, 50)

D = Point(50, 100)
E = Point(160, 161)
F = Point(270, 100)

draw_lines([(A, B), (B, C)], 'black')

draw_lines_AA([(D, E), (E, F)])

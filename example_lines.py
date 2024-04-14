from visuel import Point, draw_lines, set_lines

A, B, C = Point(20, 10), Point(160, 35), Point(300, 10)
D, E, F = Point(20, 50), Point(160, 75), Point(300, 50)
G, H, I = Point(20, 90), Point(160, 115), Point(300, 90)
J, K, L = Point(20, 130), Point(160, 155), Point(300, 130)
M, N, O = Point(20, 170), Point(160, 195), Point(300, 170)

#   Exemple 1
set_lines([(A, B), (B, C)], 'black')

#   Exemple 2
yellow, red = (255, 255, 0), (255, 0, 0)
draw_lines([(D, E), (E, F)], [(yellow, red), (red, yellow)], taille=1, alpha=0.5)

#   Exemple 2
yellow, red = (255, 255, 0), (255, 0, 0)
draw_lines([(G, H), (H, I)], [(yellow, red), (red, yellow)], taille=2)

#   Exemple 3
draw_lines([(J, K), (K, L)], style="AA")

#   Exemple 4
blue, orange, yellow = (0, 0, 255), (255, 134, 24), (255, 255, 0)
draw_lines([(M, N), (N, O)], [(blue, orange), (orange, yellow)], taille=10)

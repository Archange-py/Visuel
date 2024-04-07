from Visuel import alpha_pixel, Point
from Visuel import fill_rect

def draw_rect(x, y, w, h, color, alpha=1):
  for i in range(w):
    for j in range(h):
      alpha_pixel(x + i, y + j, color, alpha)

def fill_cercle(P, r, color, alpha=0):
  r = abs(int(r))
  for x in range(-r, r): 
    l = round((r**2 - x**2)**0.5)
    for y in range(P.y - l, P.y + l): alpha_pixel(P.x + x, y, color, alpha)

#   Exemple 1
down_color = "red"
up_color = "blue"

fill_rect(15, 50, 70, 80, down_color)
draw_rect(30, 80, 70, 80, up_color, 0)
fill_rect(15+100, 50, 70, 80, down_color)
draw_rect(30+100, 80, 70, 80, up_color, 0.5)
fill_rect(15+200, 50, 70, 80, down_color)
draw_rect(30+200, 80, 70, 80, up_color, 0.9)

# Exemple 2
#alpha = 0.2

#C1, C2, C3 = Point(100,100), Point(130,100), Point(115,130)
#fill_cercle(C1, 30, "magenta", alpha)
#fill_cercle(C2, 30, "yellow", alpha)
#fill_cercle(C3, 30, "cyan", alpha)

#C1, C2, C3 = Point(200,100), Point(230,100), Point(215,130)
#fill_cercle(C3, 30, "blue", alpha)
#fill_cercle(C1, 30, "red", alpha)
#fill_cercle(C2, 30, "green", alpha)
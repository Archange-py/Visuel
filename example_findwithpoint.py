from Visuel import Point, findWithPoint, draw_lines, set_pixel
from ion import keydown, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

center = Point(160, 111)
x, y = 250, 111
r = 30
V = findWithPoint(center, r, Point(x, y))

def clear():
    global V
    set_pixel(x, y, "white")
    draw_lines([(center, V.P2)], "white")
    V = findWithPoint(center, r, Point(x, y))

def update():
    set_pixel(x, y, "black")
    draw_lines([(center, V.P2)], "red")

while True:
    if keydown(KEY_UP): clear() ; y -= 1 ; update()
    if keydown(KEY_DOWN): clear() ; y += 1 ; update()
    if keydown(KEY_LEFT): clear() ; x -= 1 ; update()
    if keydown(KEY_RIGHT): clear() ; x += 1 ; update()
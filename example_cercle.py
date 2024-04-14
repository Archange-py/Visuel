from visuel import Point, draw_circle, fill_circle

#   Exemple 1
O = Point(160, 111)

fill_circle(O, 110, "red", alpha=0.0)
draw_circle(O, 100, "black")

#   Exemple 2
def CD(center, rayon, color):
    fill_circle(center, rayon/1.75, color)
    _rayon = rayon
    for _ in range(rayon):
        _rayon -= 1
        draw_circle(center, _rayon, "black")
    fill_circle(center, rayon/3.8, "white")

O = Point(160, 111)

#CD(O, 100, "red")
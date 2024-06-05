from visuel import Point, Screen, draw_points

#   Example 1
print(list(Screen.style.keys()))

def exemple(P: Point, color: tuple | str):
  for s in Screen.style.keys(): 
    draw_points([P], color, style=s)
    P.x += 20

exemple(Point(85,80),"green")
exemple(Point(85,110),"red")
exemple(Point(85,140),"blue")
from visuel import Point, Screen, draw_points, set_pixel

print(Screen.style.keys())

A, B, C = Point(50, 50), Point(100, 100), Point(200, 80)

def exemple(x,y,color):
  for s in Screen.style.keys(): 
    draw_points([Point(x,y)],color,style=s)
    x += 20

exemple(100,60,"green")
exemple(100,90,"red")
exemple(100,120,"blue")
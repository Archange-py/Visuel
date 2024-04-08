from Visuel import Point, Screen, draw_points, set_pixel

print(Screen.style.keys())

A, B, C = Point(50, 50), Point(100, 100), Point(200, 80)

#draw_points([A, B, C], 'black', True)

def exemple(x,y,color):
  for s in Screen.style.keys(): 
    draw_points([Point(x,y)],color,style=s)
    set_pixel(x,y,"black")
    x += 20

exemple(100,60,"green")
exemple(100,90,"red")
exemple(100,120,"blue")

#exemple(100,60,"yellow")
#exemple(100,90,"magenta")
#exemple(100,120,"cyan")
from ion import keydown, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from visuel import Point, Vector, draw_arrows, fill_rect

#   Example 1
A = Point(20, 25)
B = Point(150, 200)
C = Point(120, 25)
D = Point(250, 200)

AB = Vector(A, B)
CD = Vector(C, D)

draw_arrows([(A,AB)], 'orange', fill=False)
draw_arrows([(C,CD)], 'blue', fill=True)

#   Example 2
def animation():
  x, y = 0, 0
  p = 1
  def update():
    fill_rect(0,0,320,222,"w")
    draw_arrows([(Point(50, 50), Vector(x=x,y=y))],"red",6,45,True)
  while True: 
    if keydown(KEY_UP): y -= p ; update()
    if keydown(KEY_DOWN): y += p ; update()
    if keydown(KEY_RIGHT): x += p ; update()
    if keydown(KEY_LEFT): x -= p ; update()

#animation()
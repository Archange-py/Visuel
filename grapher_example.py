from grapher import *
from random import *
from time import *
from visuel import *

#axes()
G_no_text = Grapher(text=False)
#scatter([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "red", "+", grapher=G_no_text)
#scatter([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "blue", "*", grapher=G_no_text)

#for x, style in enumerate([s for s in Screen.style.keys()]): scatter([x+1],[1],"red",style, grapher=G_no_text)

#show(G_no_text)

#DefaultGrapher = Grapher(Lxg=50, Lxd=100, Lyh=50, Lyb=100, pas=1)
#DefaultGrapher = Grapher(text=False)

r =  1
while True:
  fill_rect(0,0,320,222,"w")
#  draw_circle(Point(160,111),r,"red")
  fill_circle(Point(160+15,111),r,"red",0.5)
  r += 1
  sleep(1)

draw_circle(Point(160,111),30,"blue")
fill_circle(Point(160,111),3,"red",0.5)

#fill_circle(Point(160+33,111),3,(255,0,0),1)
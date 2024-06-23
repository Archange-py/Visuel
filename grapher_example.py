from ext_grapher import *
from random import *
from time import *
from visuel import *
import ext_grapher as graph

#axes()
G_no_text = graph.Grapher(text=False)
#scatter([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "red", "+", grapher=G_no_text)
#scatter([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "blue", "*", grapher=G_no_text)
#for x, style in enumerate([s for s in Screen.style.keys()]): graph.scatter([x+1],[1],"red",style, grapher=G_no_text)

show(G_no_text)

#DefaultGrapher = Grapher(Lxg=50, Lxd=100, Lyh=50, Lyb=100, pas=1)
#DefaultGrapher = Grapher(text=False)

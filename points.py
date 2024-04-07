from Visuel import *

class Screen:
  style = ["O","(O)","[]","([])","*","+","."]

def draw_points(points,color,style="O"):
  for P in points:
    if style == "O": fill_circle(P,3,color)
    elif style == "(O)": fill_circle(P,3,color) ; draw_circle(P,7,color)
    elif style == "[]": fill_rect(P.x-3,P.y-3,7,7,color)
    elif style == "([])":
      fill_rect(P.x-3,P.y-3,7,7,color)
      draw_lines([(Point(P.x-7,P.y-7),Point(P.x+7,P.y-7)),(Point(P.x+7,P.y-7),Point(P.x+7,P.y+7)),(Point(P.x+7,P.y+7),Point(P.x-7,P.y+7)),(Point(P.x-7,P.y+7),Point(P.x-7,P.y-7))],color)
    elif style == "*": draw_croix(P,45,4,color)
    elif style == "+": draw_croix(P,0,4,color)
    elif style == ".": set_pixel(P.x,P.y,color)

def exemple(x,y,color):
  for s in Screen.style: 
    draw_points([Point(x,y)],color,s)
    set_pixel(x,y,"black")
    x += 20

exemple(100,60,"green")
exemple(100,90,"red")
exemple(100,120,"blue")

#exemple(100,60,"yellow")
#exemple(100,90,"magenta")
#exemple(100,120,"cyan")
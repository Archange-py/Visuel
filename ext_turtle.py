from visuel import Point, Vector, Screen, dot, findWithAngle, fill_rect, set_lines, draw_lines, draw_vectors, draw_string
from math import acos, degrees

class Turtle:
  def __init__(self, position: Point = Screen.center, color: str | tuple = Screen.palette["PrimaryColor"], angle: int = 90, pensize: int = 1):
    self.color,self.penup,self.pendown,self.pensize,self.position,self.angle = color,True,False,pensize,position,angle

  @staticmethod
  def _lines(lines, color, pensize): set_lines(lines, color) if pensize == 1 else draw_lines(lines, color, pensize)
  def __forward__(self, l: int): V = findWithAngle(self.position,Vector(x=0, y=-l),self.angle,abs(l));round(V);Turtle._lines([(self.position,V)], self.color, self.pensize) if self.pendown else None;self.position = V
  def __backward__(self, l: int): V = findWithAngle(self.position,-Vector(x=0, y=-l),self.angle,abs(l));round(V);Turtle._lines([(self.position,V)], self.color, self.pensize) if self.pendown else None;self.position = V
  def __goto__(self, x: int, y: int): 
    if self.position != Point(x,y): Turtle._lines([(self.position,Point(round(x),round(y)))],self.color,self.pensize) if self.pendown else None;V2 = Vector(self.position,Point(x,y));N2 = (V2.x**2+V2.y**2)**0.5;angle = degrees(acos((N2*V2.y)/(N2**2)));self.angle = 180-angle if -V2.x < 0 else 180+angle;self.position.x,self.position.y = round(x),round(y)

  def __circle__(self, r):
    for a in range(360):
      V = findWithAngle(self.position, Vector(x=0,y=r), a, 10) ; round(V)
      Turtle._lines([(self.position,V)], self.color, self.pensize) if self.pendown else None
      self.position = V
  
  def __write__(self, text, color=Screen.palette["PrimaryText"], background=Screen.palette["SecondaryText"]): draw_string(text, self.position.x, self.position.y, color, background)

DefaultTurtle = Turtle()
def forward(*args, turtle: Turtle = DefaultTurtle, **kwds): turtle.__forward__(*args, **kwds)
def backward(*args, turtle: Turtle = DefaultTurtle, **kwds): turtle.__backward__(*args, **kwds)
def goto(*args, turtle: Turtle = DefaultTurtle, **kwds): turtle.__goto__(*args, **kwds)
def circle(*args, turtle: Turtle = DefaultTurtle, **kwds): turtle.__circle__(*args, **kwds)
def write(*args, turtle: Turtle = DefaultTurtle, **kwds): turtle.__write__(*args, **kwds)

def right(a: int, turtle: Turtle = DefaultTurtle): turtle.angle += a
def left(a: int, turtle: Turtle = DefaultTurtle): turtle.angle -= a
def setheading(a: int, turtle: Turtle = DefaultTurtle): turtle.angle = a
def pensize(t: int, turtle: Turtle = DefaultTurtle): turtle.pensize = abs(int(t))
def color(color: str | tuple, turtle: Turtle = DefaultTurtle): turtle.color = color

def reset(turtle: Turtle = DefaultTurtle): fill_rect(0, 0, 320, 222, Screen.palette['Background']) ; turtle.position = Point(160, 111)
def pendown(turtle: Turtle = DefaultTurtle): turtle.pendown, turtle.penup = True, False
def penup(turtle: Turtle = DefaultTurtle): turtle.penup, turtle.pendown = True, False
def position(turtle: Turtle = DefaultTurtle) -> tuple[int,int]: return turtle.position.x, turtle.position.y
def heading(turtle: Turtle = DefaultTurtle) -> int: return turtle.angle
def isdown(turtle: Turtle = DefaultTurtle) -> bool: return (turtle.pendown == True)
def isup(turtle: Turtle = DefaultTurtle) -> bool: return (turtle.penup == True)

def clear(): fill_rect(0, 0, 320, 222, Screen.palette['Background'])

pendown()
for i in range(6):
	for col in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):
		color(col)
		circle(100)
		left(10)
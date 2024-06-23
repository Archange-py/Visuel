from visuel import Screen,Point,a,b,fill_rect,draw_string,draw_points,set_lines,expend,plot,connect_points
from ion import keydown,KEY_UP,KEY_DOWN,KEY_RIGHT,KEY_LEFT,KEY_MINUS,KEY_PLUS,KEY_BACKSPACE,KEY_ZERO
from time import sleep

Screen.palette["PrimaryColor"],Screen.palette["SecondaryColor"],Screen.palette["ThirdColor"] = (0,0,0),(200,200,200),(235,235,235)
Screen.center,Screen.width,Screen.height = Point(160, 111),320,222

class Grapher:
  def __init__(self, p: int = 45, Lxg: int = round(Screen.width/2), Lxd: int = round(Screen.width/2), Lyh: int = round(Screen.height/2), Lyb: int = round(Screen.height/2), C: Point = Screen.center, text: bool = True, background: bool = True, color1 : str | tuple = Screen.palette["PrimaryColor"], color2 : str | tuple = Screen.palette["SecondaryColor"], color3 : str | tuple = Screen.palette["ThirdColor"], pas: int = None):
    Screen.palette["PrimaryColor"],Screen.palette["SecondaryColor"],Screen.palette["ThirdColor"] = color1,color2,color3
    self.p,self.Lxg,self.Lxd,self.Lyh,self.Lyb,self._Lxg,self._Lxd,self._Lyh,self._Lyb,self.C,self._C,self.text,self.background,self.pas = p,Lxg,Lxd,Lyh,Lyb,Lxg,Lxd,Lyh,Lyb,Point(C.x,C.y),Point(C.x,C.y),text,background,round(p/5) if pas == None else pas
    self._liste_scatter,self._liste_plot,self._liste_point,self._liste_droite,self._liste_vector,self.liste_scatter,self.liste_plot,self.liste_point,self.liste_droite,self.liste_vector = [],[],[],[],[],[],[],[],[],[]

  def check(self, x: int, y: int) -> bool: return round(self._C.x+x*self.p) > self.C.x-self.Lxg and round(self._C.x+x*self.p) < self.C.x+self.Lxd-3 and round(self._C.y-y*self.p) > self.C.y-self.Lyh and round(self._C.y-y*self.p) < self.C.y+self.Lyb-3

  def intersec(self, A: Point, B: Point) -> Point:
    if A.x == B.x: return Point(A.x,A.y-self.Lyh) if B.y < A.y else Point(A.x,A.y+self.Lyb)
    elif A.y == B.y: return Point(A.x-self.Lxg,A.y) if B.x < A.x else Point(A.x+self.Lxd,A.y)
    else:
      _a,_a2 = a(A,B),a(Point(A.x-self.Lxg,A.y-self.Lyh),A);_b,_b2 = b(_a,A),b(_a2,A)
      if B.y-(_a2*B.x+_b2) == 0: I = Point(A.x-self.Lxg,A.y-self.Lyh) if B.x < A.x else Point(A.x+self.Lxd,A.y+self.Lyb)
      elif B.y-(_a2*B.x+_b2) > 0:  I = Point(((A.y+self.Lyb)-_b)/_a,A.y+self.Lyb) if abs(B.x-A.x) < abs(B.y-A.y) else Point(A.x-self.Lxg,_a*(A.x-self.Lxg)+_b) 
      else: I = Point(((A.y-self.Lyh)-_b)/_a,A.y-self.Lyh) if abs(B.x-A.x) < abs(B.y-A.y) else Point(A.x+self.Lxd,_a*(A.x+self.Lxd)+_b)
      round(I) ; return I

  def scatter(self, X: list[Point], Y: list[Point], color: str | tuple = Screen.palette["PrimaryColor"], style: str = "O"):
    if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
    if not {"X":X,"Y":Y,"color":color,"style":style} in self.liste_scatter: self._liste_scatter.append({"X":X,"Y":Y,"color":color,"style":style});self.liste_scatter.append({"X":X,"Y":Y,"color":color,"style":style})
    else: draw_points([Point(round(self._C.x+x*self.p), round(self._C.y-y*self.p)) for x, y in zip(X, Y) if self.check(x,y)], color, False, style)

  def plot(self, X: list[Point], Y: list[Point], color: str | tuple = Screen.palette["PrimaryColor"]):
    if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
    if not {"X":X,"Y":Y,"color":color} in self.liste_plot: self._liste_plot.append({"X":X,"Y":Y,"color":color});self.liste_plot.append({"X":X,"Y":Y,"color":color})
#    else: set_lines(connect_points([Point(round(self._C.x+x*self.p), round(self._C.y-y*self.p)) for x, y in zip(X, Y) if round(self._C.x+x*self.p) > self.C.x-self.Lxg and round(self._C.x+x*self.p) < self.C.x+self.Lxd-3 and round(self._C.y-y*self.p) > self.C.y-self.Lyh and round(self._C.y-y*self.p) < self.C.y+self.Lyb-3]), color)
    else:
      liste,pts = [],[Point(x,y) for x,y in zip(X, Y)]
      for n,(x,y) in enumerate(pts):
        if self.check(x,y): liste.append(Point(round(self._C.x+x*self.p),round(self._C.y-y*self.p)))
#if round(self._C.x+x*self.p) < self.C.x+self.Lxd-3
        else: I = self.intersec(pts[n+1 if n != len(pts)-1 else 1],Point(x,y));liste.append(Point(round(self._C.x+I.x*self.p),round(self._C.y-I.y*self.p)))
      set_lines(connect_points(liste), color)

  def set_points(self, liste: list[Point], color: str | tuple = Screen.palette["PrimaryColor"]): pass

  def set_vectors(self, liste: list[tuple[Point,Point]], color: str | tuple = Screen.palette["PrimaryColor"]): pass

  def set_lines(self, liste: list[tuple[Point,Point]], color: str | tuple = Screen.palette["PrimaryColor"]): pass

  def clean(self): self._liste_scatter,self._liste_plot,self._liste_point,self._liste_droite,self._liste_vector,self.liste_scatter,self.liste_plot,self.liste_point,self.liste_droite,self.liste_vector = [],[],[],[],[],[],[],[],[],[] ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

  def set_axes(self):
    if self.background:
      for i in range(self._Lyh,0,-self.p): fill_rect(self.C.x-self.Lxg,self._C.y-self._Lyh+round(i-self.p/2),self.Lxg+self.Lxd,1,Screen.palette["ThirdColor"]) if self.C.y-self._Lyh+round(i-self.p/2) > self.C.y-self._Lyh and self.C.y-self._Lyh+round(i-self.p/2) < self.C.y+self._Lyb else None
      for j in range(0,self._Lyb,self.p): fill_rect(self.C.x-self.Lxg,self._C.y+round(j+self.p/2),self.Lxg+self.Lxd,1,Screen.palette["ThirdColor"]) if self.C.y+round(j+self.p/2) > self.C.y-self._Lyh and self.C.y+round(j+self.p/2) < self.C.y+self._Lyb else None
      for i in range(self._Lxg,0,-self.p): fill_rect(self._C.x-self._Lxg+round(i-self.p/2),self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["ThirdColor"]) if self.C.x-self._Lxg+round(i-self.p/2) > self.C.x-self._Lxg and self.C.x-self._Lxg+round(i-self.p/2) < self.C.x+self._Lxd else None
      for j in range(0,self._Lxd,self.p): fill_rect(self._C.x+round(j+self.p/2),self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["ThirdColor"]) if self.C.x+round(j+self.p/2) > self.C.x-self._Lxg and self.C.x+round(j+self.p/2) < self.C.x+self._Lxd else None
    for n,i in enumerate(range(self._Lxg,0,-self.p)):
      if self.background and self.C.x-self._Lxg+i < self.C.x+self._Lxd: fill_rect(self.C.x-self.Lxg+i,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["SecondaryColor"])
      if self._C.x-self._Lxg+i < self.C.x+self.Lxd and self._C.y-2 > self.C.y-self.Lyh and self._C.y+2 < self.C.y+self.Lyb: fill_rect(self.C.x-self.Lxg+i,self._C.y-2,1,5,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(-n),self.C.x-self.Lxg+i-5,self._C.y+10)
    for n,j in enumerate(range(0,self._Lxd,self.p)):
      if self.background and self._C.x+j < self.C.x+self.Lxd and self._C.x+j > self.C.x-self.Lxg: fill_rect(self._C.x+j,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["SecondaryColor"])
      if self._C.x+j < self.C.x+self.Lxd and self._C.x+j > self.C.x-self.Lxg and self._C.y-2 > self.C.y-self.Lyh and self._C.y+2 < self.C.y+self.Lyb: fill_rect(self._C.x+j,self._C.y-2,1,5,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(n),self._C.x+j-5,self._C.y+10)
    for n,i in enumerate(range(self._Lyh,0,-self.p)):
      if self.background and self.C.y-self._Lyh+i < self.C.y+self._Lyb: fill_rect(self.C.x-self.Lxg,self._C.y-self._Lyh+i,self.Lxg+self.Lxd,1,Screen.palette["SecondaryColor"])
      if self._C.y-self._Lyh+i > self.C.y-self.Lyh and self._C.x-2 > self.C.x-self.Lxg and self._C.x+2 < self.C.x+self.Lxd and self._C.y-self._Lyh+i < self.C.y+self.Lyb: fill_rect(self._C.x-2,self.C.y-self.Lyh+i,5,1,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(n),self._C.x+10,self.C.y-self.Lyh+i-5)
    for n,j in enumerate(range(0,self._Lyb,self.p)):
      if self.background and self.C.y+j > self.C.y-self._Lyh and self.C.y+j < self.C.y+self._Lyb: fill_rect(self.C.x-self.Lxg,self._C.y+j,self.Lxg+self.Lxd,1,Screen.palette["SecondaryColor"])
      if self._C.y+j < self.C.y+self.Lyb and self._C.x-2 > self.C.x-self.Lxg and self._C.x+2 < self.C.x+self.Lxd and self._C.y+j > self.C.y-self.Lyh: fill_rect(self._C.x-2,self._C.y+j,5,1,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(-n),self._C.x+10,self._C.y+j-5)
    fill_rect(self._C.x,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["PrimaryColor"]) if self._C.x >= self.C.x-self.Lxg and self._C.x < self.C.x+self.Lxd else None;fill_rect(self.C.x-self.Lxg,self._C.y,self.Lxg+self.Lxd,1,Screen.palette["PrimaryColor"]) if self._C.y >= self.C.y-self.Lyh and self._C.y < self.C.y+self.Lyb else None
    for dico in self.liste_scatter: self.scatter(X=dico["X"],Y=dico["Y"],color=dico["color"],style=dico["style"])
    for dico in self.liste_plot: self.plot(X=dico["X"],Y=dico["Y"],color=dico["color"])

  def zoom(self):
    if keydown(KEY_PLUS):
      for dico in self.liste_scatter: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], -(self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] ; dico["Y"] = [P.y for P in liste]
      for dico in self.liste_plot: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], -(self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] ; dico["Y"] = [P.y for P in liste]
      self.p += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_MINUS):
      for dico in self.liste_scatter: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], (self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] if self.p-self.pas > 1 else dico["X"] ; dico["Y"] = [P.y for P in liste] if self.p-self.pas > 1 else dico["Y"]
      for dico in self.liste_plot: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], (self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] if self.p-self.pas > 1 else dico["X"] ; dico["Y"] = [P.y for P in liste] if self.p-self.pas > 1 else dico["Y"]
      self.p -= self.pas if self.p-self.pas > 1 else 0 ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

  def scroll(self):
    if keydown(KEY_UP):
      for dico in self._liste_scatter: dico["Y"] = [y+self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_plot: dico["Y"] = [y+self.pas/self.p for y in dico["Y"]]
      self._C.y += self.pas ; self._Lyh += self.pas ; self._Lyb -= self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_DOWN):
      for dico in self._liste_scatter: dico["Y"] = [y-self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_plot: dico["Y"] = [y-self.pas/self.p for y in dico["Y"]]
      self._C.y -= self.pas ; self._Lyh -= self.pas ; self._Lyb += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_LEFT):
      for dico in self._liste_scatter: dico["X"] = [x+self.pas/self.p for x in dico["X"]]
      for dico in self._liste_plot: dico["X"] = [x+self.pas/self.p for x in dico["X"]]
      self._C.x += self.pas ; self._Lxg += self.pas ; self._Lxd -= self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_RIGHT):
      for dico in self._liste_scatter: dico["X"] = [x-self.pas/self.p for x in dico["X"]]
      for dico in self._liste_plot: dico["X"] = [x-self.pas/self.p for x in dico["X"]]
      self._C.x -= self.pas ; self._Lxg -= self.pas ; self._Lxd += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

  def main(self):
    self.set_axes()
    while True: 
      self.zoom() ; self.scroll()
      if keydown(KEY_BACKSPACE): sleep(0.1) ; break
      if keydown(KEY_ZERO):
        for dico,dico_copy in zip(self._liste_scatter,self.liste_scatter): dico["X"] = dico_copy["X"].copy() ; dico["Y"] = dico_copy["Y"].copy()
        for dico,dico_copy in zip(self._liste_plot,self.liste_plot): dico["X"] = dico_copy["X"].copy() ; dico["Y"] = dico_copy["Y"].copy()
        self._Lxg,self._Lxd,self._Lyh,self._Lyb = self.Lxg,self.Lxd,self.Lyh,self.Lyb ; self._C = Point(self.C.x,self.C.y) ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

DefaultGrapher = Grapher(text=True)
DefaultGrapher = Grapher(Lxg=100, Lxd=100, Lyh=100, Lyb=100, text=False)
def axes(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_axes(*args, **kwds)
def show(grapher: Grapher = DefaultGrapher): grapher.main()
def scatter(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.scatter(*args, **kwds)
def plot(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.plot(*args, **kwds)
def points(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_points(*args, **kwds)
def lines(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_lines(*args, **kwds)
def vectors(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_vectors(*args, **kwds)
def clean(grapher: Grapher = DefaultGrapher): grapher.clean()

from random import *
#axes()
#plot([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "red")
plot([-3,1,4],[1,-2,4],"blue")
#scatter([randint(-3, 3) for x in range(4)], [randint(-3, 3) for y in range(4)], "red", "+")
show()

#points([Point(1,1), Point(5,-3), Point(-2,4)], "red")

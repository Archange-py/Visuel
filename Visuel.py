from kandinsky import set_pixel, get_pixel, fill_rect, draw_string
from math import pi, cos, sin, radians, ceil
import kandinsky as kd

dot = lambda V1, V2: V1.x * V2.y - V2.x * V1.y
a,b = lambda P1, P2: (P2.y-P1.y)/(P2.x-P1.x),lambda a, P1: -(a*P1.x-P1.y)
linear = lambda t,A,B: Point((1-t)*A.x+t*B.x,(1-t)*A.y+t*B.y)
quadratic = lambda t,A,B,C: Point((1-t)**2*A.x+2*(1-t)*t*B.x+t**2*C.x,(1-t)**2*A.y+2*(1-t)*t*B.y+t**2*C.y)
quadratic_derivative = lambda t,A,B,C: Point(-2*(1-t)*A.x+2*B.x*(1-2*t)+2*t*C.x,-2*(1-t)*A.y+2*B.y*(1-2*t)+2*t*C.y)
cubic = lambda t,A,B,C,D: Point(A.x*(1-t)**3+3*B.x*t*(1-t)**2+3*C.x*t**2*(1-t)+D.x*t**3,A.y*(1-t)**3+3*B.y*t*(1-t)**2+3*C.y*t**2*(1-t)+D.y*t**3)
distance,milieu = lambda P1, P2: ((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5,lambda P1, P2, p=2: Point((P1.x+P2.x)/p,(P1.y+P2.y)/p)
mean,mean_point = lambda liste: sum(liste) / len(liste),lambda liste: Point(round(mean([P.x for P in liste])),round(mean([P.y for P in liste])))

class Point:
  def __init__(self, x: int, y: int, name=''): self.x, self.y, self.name = x, y, name
  def __str__(self) -> str: return str(self.name)
  def __repr__(self) -> str: return "Point({}, {})".format(self.x, self.y)
  def __eq__(self, other) -> bool: return (self.x == other.x) and (self.y == other.y) if isinstance(other, Point) else False
  def __iter__(self): return iter([self.x, self.y])
  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)
  def __round__(self): self.x, self.y = round(self.x), round(self.y)
  def copy(self): return Point(self.x,self.y,self.name)

class Vector:
  def __init__(self, P1: Point = None, P2: Point = None, x: int = None, y: int = None, name: str = ''): cond = (P1 != None and P2 != None) ; self.x, self.y,self.name = P2.x-P1.x if cond else x, P2.y-P1.y if cond else y,name
  def __str__(self) -> str: return str(self.name)
  def __repr__(self) -> str: return "Vector({}, {})".format(self.x,self.y)
  def __eq__(self, other) -> bool: return (self.x == other.x) and (self.y == other.y) if isinstance(other, Vector) else False
  def __iter__(self): return iter([self.x, self.y])
  def __pos__(self): return self
  def __neg__(self): return Vector(x=-self.x, y=-self.y, name=self.name)
  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)
  def __round__(self): self.x = round(self.x) ; self.y = round(self.y)
  def __add__(self, other): return Vector(x=self.x+other.x, y=self.y+other.y) if isinstance(other, Vector) else Point(other.x+self.x, other.y+self.y) if isinstance(other, Point) else None
  def __sub__(self, other): return Vector(x=self.x-other.x, y=self.y-other.y) if isinstance(other, Vector) else Point(other.x-self.x, other.y-self.y) if isinstance(other, Point) else None
  def __mul__(self, other): return Vector(x=self.x*other.x, y=self.y*other.y) if isinstance(other, Vector) else Vector(x=self.x*other, y=self.y*other) if isinstance(other, int) else None
  def __truediv__(self, other): return Vector(x=self.x/other.x, y=self.y/other.y) if isinstance(other, Vector) else Vector(x=self.x/other, y=self.y/other) if isinstance(other, int) else None
  __radd__, __rsub__, __rmul__, __rtruediv__ = __add__, __sub__, __mul__, __truediv__
  def rotate(self, angle: int): angle = radians(angle) ; return Vector(x=self.x*cos(angle)-self.y*sin(angle), y=self.x*sin(angle)+self.y*cos(angle), name=self.name)
  def copy(self): return Vector(x=self.x,y=self.y,name=self.name)

class Screen:
  width, height, p = 320, 222, 2 ; center = Point(int(width/2), int(height/2))
  def style_circle_curs(P,color): fill_circle(P,Screen.p,color) ; draw_circle(P,Screen.p+2,color)
  def style_rect_curs(P,color): fill_rect(P.x-Screen.p,P.y-Screen.p,Screen.p*2+1,Screen.p*2+1,color);fill_rect(P.x-Screen.p-2,P.y-Screen.p-2,Screen.p*4-2,1,color);fill_rect(P.x-Screen.p-2+Screen.p*4-2,P.y-Screen.p-2,1,Screen.p*4-1,color);fill_rect(P.x-Screen.p-2+Screen.p*4-2,P.y-Screen.p-2+Screen.p*4-2,-Screen.p*4+2,1,color);fill_rect(P.x-Screen.p-2,P.y-Screen.p-2,1,Screen.p*4-2,color)
  def style_rhombus(P,color): fill_triangles([(Point(P.x,P.y-Screen.p),Point(P.x-Screen.p,P.y),Point(P.x+Screen.p,P.y)),(Point(P.x,P.y+Screen.p),Point(P.x-Screen.p,P.y),Point(P.x+Screen.p,P.y))], color)
  def style_rhombus_curs(P, color): fill_triangles([(Point(P.x,P.y-Screen.p),Point(P.x-Screen.p,P.y),Point(P.x+Screen.p,P.y)),(Point(P.x,P.y+Screen.p),Point(P.x-Screen.p,P.y),Point(P.x+Screen.p,P.y))], color) ; set_lines([(Point(P.x,P.y-Screen.p-3),Point(P.x-Screen.p-3,P.y)),(Point(P.x-Screen.p-3,P.y),Point(P.x,P.y+Screen.p+3)),(Point(P.x,P.y+Screen.p+3),Point(P.x+Screen.p+3,P.y)),(Point(P.x+Screen.p+3,P.y),Point(P.x,P.y-Screen.p-3))],color)
  palette = {"Background" : (248, 252, 248), "PrimaryColor" : (0, 0, 0), "SecondaryColor" : (200, 200, 200), "PrimaryText" : (0, 0, 0), "SecondaryText" : (248, 252, 248)}
  style = {"[]":"fill_rect(P.x-Screen.p,P.y-Screen.p,Screen.p*2+1,Screen.p*2+1,color)","([])":"Screen.style_rect_curs(P,color)","<>":"Screen.style_rhombus(P,color)","(<>)":"Screen.style_rhombus_curs(P,color)","O":"fill_circle(P,Screen.p,color)","(O)":"Screen.style_circle_curs(P,color)","*":"draw_croix(P,4,45,color)","+":"draw_croix(P,Screen.p,0,color)",".":"set_pixel(P.x,P.y,color)"}

def expend(liste: list[Point], d: float, M: Point = None) -> list[Point]: M = mean_point(liste) if M == None else M ; return [Point(round(P.x+(P.x-M.x)*d),round(P.y+(P.y-M.y)*d)) if d != 0 else P for n, P in enumerate(liste)]
def connect_points(liste: list[Point], ending: bool = False) -> list[tuple[Point, Point]]: line = [(liste[p], liste[p+1]) for p in range(len(liste)) if p < len(liste)-1] ; line.append((liste[-1], liste[0])) if ending else None ; return line
def findWithPoint(P1: Point, P2: Point, length: int) -> Point: N = ((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5 ; return Point(P1.x+((P2.x-P1.x)*length)/N,P1.y+((P2.y-P1.y)*length)/N)
def findWithAngle(P: Point, V: Vector, angle: int, rayon: int) -> Point: _V = V.rotate(angle) ; return findWithPoint(P, P+_V, rayon)
def scatter(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor'], style: str = None): draw_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)], color, False, style)
def plot(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor']): set_lines(connect_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)]), color)
def alpha_pixel(x: int, y: int, color: tuple | str, alpha: float = 1.0): set_pixel(x,y,tuple(C1*alpha-C2*alpha+C2 for C1, C2 in zip(kd.color(color), get_pixel(x,y))))
def interpolate(C1: tuple | str, C2: tuple | str, N: int = 100) -> list[tuple[float, float, float]]: C1,C2 = kd.color(C1),kd.color(C2);interpolated_colors = [(C1[0]+(C2[0]-C1[0])*i/(N+1),C1[1]+(C2[1]-C1[1])*i/(N+1),C1[2]+(C2[2]-C1[2])*i/(N+1)) for i in range(N + 2)];return interpolated_colors[1:-1]

def draw_points(liste: list[Point], color: tuple | str = Screen.palette['PrimaryColor'], text: bool = True, style: str = "O"):
  for P in liste: eval(Screen.style[style]) ; draw_string(str(P.name),P.x+6,P.y+6,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) if text else None

def draw_croix(center: Point, r: int, angle: int = 90, color: tuple | str = Screen.palette['PrimaryColor']):
  R = Vector(center, Point(center.x+r, center.y)) ; R = R.rotate(angle)
  for _ in range(4): R = R.rotate(90) ; round(R) ; set_lines([(center, center+R)], color)

def set_lines(line: list[tuple[Point, Point]], color: tuple | str = Screen.palette['PrimaryColor']):
  for P1,P2 in line: 
    up,right = True if P2.y > P1.y else False,True if P2.x > P1.x else False;h,b = P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n = True if h <= b else False;set_pixel(P2.x,P2.y,color)
    if b != 0 or h != 0: e = h/b if n else b/h
    for i in range(b if n else h):set_pixel(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i)),color)

def draw_lines(line: list[tuple[Point, Point]], color: list[str | tuple[int]] | tuple | str = Screen.palette['PrimaryColor'], thickness: int = 1):
  if isinstance(color, list):
    for (P1,P2),(C1,C2) in zip(line,color):
      up,right = True if P2.y > P1.y else False,True if P2.x > P1.x else False;h,b = P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n = True if h <= b else False;e = h/b if n and (b != 0 or h != 0) else b/h;colors = interpolate(C1,C2,round(distance(P1,P2)))
      for i in range(b if n else h): fill_circle(Point(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i))),thickness,colors[i])
  else:
    for (P1,P2) in line:
      up,right = True if P2.y > P1.y else False,True if P2.x > P1.x else False;h,b = P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n = True if h <= b else False;e = h/b if n and (b != 0 or h != 0) else b/h
      for i in range(b if n else h): fill_circle(Point(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i))),thickness,color)

def draw_lines_AA(line: list[tuple[Point, Point]]):
    for (x0, y0), (x1, y1) in line:
      dx,dy,sx,sy = abs(x1-x0),abs(y1-y0), 1 if x0 < x1 else -1, 1 if y0 < y1 else -1;err,e2,x2,ed = dx-dy,0,0,1 if dx + dy == 0 else (dx*dx+dy*dy)**0.5
      while True:
        set_pixel(x0,y0,tuple(int(255*abs(err-dx+dy)/ed) for _ in range(3)));e2,x2 = err,x0
        if 2 * e2 >= -dx:
          if x0 == x1: break
          if e2 + dy < ed: set_pixel(x0,y0+sy,tuple(int(255*(e2+dy)/ed) for _ in range(3)))
          err -= dy ; x0 += sx
        if 2 * e2 <= dy:
          if y0 == y1: break
          if dx - e2 < ed: set_pixel(x2+sx,y0,tuple(int(255*(dx-e2)/ed) for _ in range(3)))
          err += dx ; y0 += sy

def draw_arrows(liste: list[tuple[Point, Vector]], color: tuple | str = Screen.palette['PrimaryColor'], length: int = 10, angle: int = 45, fill: bool = False):
  for A, V in liste: B = A+V;V1 = -Vector(findWithPoint(B,A,length),B) if A != B else V;V2,V3 = V1.rotate(angle), V1.rotate(-angle);round(V2);round(V3);set_lines([(A,B)],color);set_lines([(B,B+V2),(B,B+V3)],color) if not fill else fill_triangles([(B+V2,B,B+V3)],color)

def draw_vector(P: Point, V: Vector, color: tuple | str = Screen.palette['PrimaryColor']): x,y = milieu(P,P+V) ; draw_string(str(V.name),round(x-6),round(y-6),Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) ; draw_arrows([(P,V)],color,fill=False)

def draw_droite(P1: Point, P2: Point, color: tuple | str = Screen.palette['PrimaryColor'], name: str = None):
  if P1.x == P2.x: set_lines([(Point(P1.x,0),Point(P1.x,222))],color)
  elif P1.y == P2.y: set_lines([(Point(0,P1.y),Point(320,P1.y))],color)
  else: _a = a(P1,P2);_b = b(_a,P1);P0,P3 = Point(round((222-_b)/_a),222) if abs(P2.x-P1.x) < abs(P2.y-P1.y) else Point(0,round(_a*0+_b)),Point(round((-1-_b)/_a),-1) if abs(P2.x-P1.x) < abs(P2.y-P1.y) else Point(320,round(_a*320+_b));set_lines([(P0,P3)],color)
  if name != None: M = milieu(P1, P2) ; draw_string(str(name),round(M.x-6),round(M.y-6),Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])

def fill_triangles(liste: list[tuple[Point,Point,Point]], color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  eq = lambda p, a, b: (a.x-p.x)*(b.y-p.y)-(a.y-p.y)*(b.x-p.x)
  for P1,P2,P3 in liste:
    xmin,xmax,ymin,ymax = min(P1.x,P2.x,P3.x),max(P1.x,P2.x,P3.x)+1,min(P1.y,P2.y,P3.y),max(P1.y,P2.y,P3.y)+1 ; width, height = abs(xmax+xmin), abs(ymax+ymin)
    for y in range(ymin, ymax):
      if 0 <= y < height:
        for x in range(xmin, xmax):
          pos = Point(x,y) ; w1,w2,w3 = eq(pos,P3,P1),eq(pos,P1,P2),eq(pos,P2,P3)
          if 0 <= x < width and ((w1 >= 0 and w2 >= 0 and w3 >= 0) or (-w1 >= 0 and -w2 >= 0 and -w3 >= 0)): set_pixel(x,y,color) if int(alpha) == 1 else alpha_pixel(x,y,color,alpha)

def draw_polygone(n: int, rayon: int, coord: Point, color: tuple | str = Screen.palette['PrimaryColor']): alpha = 2*pi/n;draw_lines(connect_points([Point(round(coord.x+rayon*cos(k*alpha)),round(coord.y+rayon*sin(k*alpha))) for k in range(1, n+1)],True),color)

def fill_polygone(n: int, rayon: int, coord: Point, color: tuple | str = Screen.palette['PrimaryColor'], c_map: list[tuple | str] = None, alpha: float = 1.0):
  _alpha = 2*pi/n;points = [Point(round(coord.x+rayon*cos(k*_alpha)),round(coord.y+rayon*sin(k*_alpha))) for k in range(1, n+1)]
  for p,c in zip(connect_points(points,True),[color for _ in range(len(points))] if not isinstance(c_map, list) else c_map): fill_triangles([([coord,p[0],p[1]])],c,alpha)

def draw_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor']): fill_rect(P1.x,P1.y,P4.x-P1.x,1,color);fill_rect(P4.x,P1.y,1,P4.y-P1.y+1,color);fill_rect(P1.x,P4.y,P4.x-P1.x,1,color);fill_rect(P1.x,P1.y,1,P4.y-P1.y,color)

def fill_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  for x,y in [(x, y) for x in range(P4.x-P1.x if P4.x > P1.x else P1.x-P4.x) for y in range(P4.y-P1.y if P4.y > P1.y else P1.y-P4.y)]: alpha_pixel(P1.x+x, P1.y+y, color, alpha)

def draw_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor']):
  for x in range(-abs(rayon), abs(rayon)):
    l = round((abs(rayon)**2-x**2)**0.5)
    if abs(x) <= l: set_pixel(center.x+l,center.y+x,color);set_pixel(center.x-l,center.y-x,color);set_pixel(center.x-x,center.y-l,color);set_pixel(center.x+x,center.y+l,color)

def fill_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  for x,y in [(x,y) for x in range(-round(rayon), round(rayon)+1) for y in range(-round(rayon), round(rayon)+1)]:
    if round(distance(center,Point(center.x+x,center.y+y))) <= rayon: alpha_pixel(center.x+x,center.y+y,color,alpha) if int(alpha) != 1 else set_pixel(center.x+x,center.y+y,color)

def draw_ellipses(P1: Point, P2: Point, color: tuple | str = Screen.palette['PrimaryColor']):
    (x0,y0),(x1,y1) = P1, P2;a,b = abs(x1-x0),abs(y1-y0);b1 = b&1;dx,dy = 4*(1-a)*b*b,4*(b1+1)*a*a;err = dx+dy+b1*a*a
    if x0 > x1: x0,x1 = x1,x0+a
    if y0 > y1: y0 = y1
    y0 += (b+1)//2;y1 = y0-b1;a *= 8*a ; b1 = 8*b*b
    while x0 <= x1:
      set_pixel(x1,y0,color);set_pixel(x0,y0,color);set_pixel(x0,y1,color);set_pixel(x1,y1,color);e2 = 2*err
      if e2 <= dy: y0 += 1 ; y1 -= 1 ; err += dy ; dy += a
      if e2 >= dx or 2 * err > dy: x0 += 1 ; x1 -= 1 ; err += dx ; dx += b1
    while y0 - y1 < b: set_pixel(x0-1,y0,color);set_pixel(x1+1,y0,color);set_pixel(x0-1,y1,color);set_pixel(x1+1,y1,color);y0 += 1;y1 -= 1

def fill_ellipses(P1: Point, P2: Point, color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  a, b = abs(P2.x - P1.x) // 2, abs(P2.y - P1.y) // 2
  C = Point((P1.x + P2.x) // 2, (P1.y + P2.y) // 2)
  for x in range(-a, a + 1):
    for y in range(-b, b + 1):
      if (x**2 / a**2) + (y**2 / b**2) <= 1: alpha_pixel(C.x + x, C.y + y, color, alpha)

def draw_quadratic(P1: Point, P2: Point, P3: Point, color: tuple | str = Screen.palette['PrimaryColor'], thickness: int = 1):
# D = quadratic_derivative(t,P1,P2,P3) ; V = (D.x**2+D.y**2)**0.5 ; U = Vector(P,Point(P.x+(D.x/V)*40, P.y+(D.y/V)*40))
  t = 0
  while t <= 1: P = quadratic(t,P1,P2,P3);round(P);set_pixel(P.x,P.y,color) if thickness == 1 else fill_circle(P,thickness,color,1);t += 0.001

def draw_cubic(P1: Point, P2: Point, P3: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor'], thickness: int = 1):
  t = 0
  while t <= 1: P = cubic(t,P1,P2,P3,P4);round(P);set_pixel(P.x,P.y,color) if thickness == 1 else fill_circle(P,thickness,color,1);t += 0.001

def bezier_curve(liste: list[Point], color: tuple | str = Screen.palette['PrimaryColor'], thickness: int = 1, extrem: bool = False):
  list_connect, list_milieu, L = connect_points(liste), [milieu(P1,P2) for P1,P2 in connect_points(liste)], [] ; _liste = [((list_connect[n][0],M),(M,list_connect[n][1])) for n,M in enumerate(list_milieu)]
  for line in _liste: L.extend(line)
  if extrem: round(L[0][0]);round(L[0][1]);set_lines([(L[0])],color)
  for n,T in enumerate(L): draw_quadratic(T[0],T[1],L[n+1][1],color,thickness) if n != 0 and n < len(L)-2 and n%2 != 0 else None
  if extrem: round(L[-1][0]);round(L[-1][1]);set_lines([(L[-1])],color)

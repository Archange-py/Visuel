from kandinsky import set_pixel, get_pixel, fill_rect, draw_string
from math import pi, cos, sin, atan2, radians

a,b = lambda P1, P2: (P2.y-P1.y)/(P2.x-P1.x),lambda a, P1: -(a*P1.x-P1.y)
distance,milieu = lambda P1, P2: ((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5,lambda P1, P2, p=2: Point((P1.x+P2.x)/p,(P1.y+P2.y)/p)
linear = lambda t,A,B: Point((1-t)*A.x+t*B.x,(1-t)*A.y+t*B.y)
quadratic = lambda t,A,B,C: Point(round((1-t)**2*A.x+2*(1-t)*t*B.x+t**2*C.x),round((1-t)**2*A.y+2*(1-t)*t*B.y+t**2*C.y))
#cubique = lambda t,A,B,C,D:
mean,mean_point = lambda liste: sum(liste) / len(liste),lambda liste: Point(round(mean([P.x for P in liste])),round(mean([P.y for P in liste])))
dot = lambda V1, V2: V1.x * V2.y - V2.x * V1.y
#toScreen = lambda *args: [Point(((P.x+1)/2)*320,((P.y+1)/2)*222) for P in list(args)]
#toStandard = lambda *args: [Point(((P.x/320)*2)-1,((P.y/222)*2)-1) for P in list(args)]

class Point:
  def __init__(self, x: int, y: int, name=''): self.x, self.y, self.name = x, y, name
  def __str__(self) -> str: return str(self.name)
  def __repr__(self) -> str: return "Point({}, {})".format(self.x, self.y)
  def __eq__(self, other) -> bool: return (self.x == other.x) and (self.y == other.y) if isinstance(other, Point) else False
  def __iter__(self): return iter([self.x, self.y])
  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)
  def __round__(self): self.x, self.y = round(self.x), round(self.y)
  def copy(self): return Point(self.x, self.y, self.name)

class Vector:
  def __init__(self, P1: Point, P2: Point, name: str = ''): self.P1, self.P2, self.name = P1, P2, name ; self.x, self.y  = P2.x-P1.x, P2.y-P1.y ; self.norme = (self.x**2 + self.y**2)**0.5
  def __str__(self) -> str: return "({}, {})".format(self.P1,self.P2)
  def __repr__(self) -> str: return "Vector({}, {})".format(repr(self.P1),repr(self.P2))
  def __eq__(self, other) -> bool: return (self.x == other.x) and (self.y == other.y) if isinstance(other, Vector) else False
  def __iter__(self): return iter([self.P1, self.P2])
  def __pos__(self): return self
  def __neg__(self): return Vector(self.P2, self.P1)
  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)
  def __round__(self): self.P1.round() ; self.P2.round()
  def copy(self): V = Vector(self.P1, self.P2, self.name) ; V.x, V.y = self.x, self.y ; return V
  def __add__(self, other): return Vector(self.P1, other.P2) if self.P2 == other.P1 else None
  __radd__ = __add__

  def rotate(self, angle: int, anchor: str = "first"):
    angle = radians(angle) ; P = self.P1 if anchor == "first" else self.P2
    return Vector(P, Point(P.x+self.x*cos(angle)-self.y*sin(angle), P.y+self.x*sin(angle)+self.y*cos(angle)))

class Screen:
  palette = {"Background" : (248, 252, 248), "PrimaryColor" : (0, 0, 0), "PrimaryText" : (0, 0, 0), "SecondaryText" : (248, 252, 248)}
  style = {"O":"fill_circle(P,3,color)","(O)":"","*":"draw_croix(P,4,45,color)","+":"draw_croix(P,4,0,color)",".":"set_pixel(P.x,P.y,color)"}
  width, height = 320, 222 ; center = Point(int(width/2), int(height/2))

def expend(liste: list[Point], d: float) -> list[Point]: M = mean_point(liste) ; return [Point(round(P.x+(P.x-M.x)*d),round(P.y+(P.y-M.y)*d)) if d != 0 else P for n, P in enumerate(liste)]

def interpolate(C1: tuple | str, C2: tuple | str, N: int = 100) -> list[tuple[float, float, float]]:
  new = [C1] ; C1 = list(C1)
  for _ in range(N-2):
    if C1[0] < C2[0]: C1[0] += abs(C2[0]-C1[0])/(N-2)
    elif C1[0] > C2[0]: C1[0] -= abs(C2[0]-C1[0])/(N-2)
    if C1[1] < C2[1]: C1[1] += abs(C2[1]-C1[1])/(N-2)
    elif C1[1] > C2[1]: C1[1] -= abs(C2[1]-C1[1])/(N-2)
    if C1[2] < C2[2]: C1[2] += abs(C2[2]-C1[2])/(N-2)
    elif C1[2] > C2[2]: C1[2] -= abs(C2[2]-C1[2])/(N-2)
    new.append(tuple(C1))
  new.append(C2) ; return new

def alpha_pixel(x: int, y: int, color: tuple | str, alpha: float = 1.0):
  if alpha == 0.0 or alpha == 1.0: set_pixel(x, y, color if alpha == 1 else get_pixel(x,y))
  else: set_pixel(x, y, tuple(C1*a-C2*a+C2 for C1, C2 in zip(color, get_pixel(x, y))))

def connect_points(liste: list[Point], ending: bool = False) -> list[tuple[Point, Point]]: line = [(liste[p], liste[p+1]) for p in range(len(liste)) if p < len(liste)-1] ; line.append((liste[-1], liste[0])) if ending else None ; return line

def findWithPoint(center: Point, point: Point, r: int) -> Vector:
  if center.x == point.x: return Vector(center, Point(center.x, center.y + r if point.y > center.y else center.y - r))
  elif center.y == point.y: return Vector(center, Point(center.x + r if point.x > center.x else center.x - r, center.y))
  else: _b, _h, = point.x - center.x, point.y - center.y ; h = (_b**2 + _h**2)**0.5 ; return Vector(center, Point(round(center.x+((r*_b)/h)), round(center.y+(r*_h)/h)))

def findWithAngle(R: Vector, angle: int, rayon: int) -> Vector: pass
#  _a = 180-(90+radians(-angle+207)) ; b, h = cos(-_a)*abs(r), sin(-_a)*abs(r)
#  return Vecteur(center, Point(round(center.x+b), round(center.y+h)))
#  V = rotate(R, angle) ; return findWithPoint(V.P1, V.P2, rayon)

def scatter(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor'], style=None):
  if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
  draw_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)], color, False, style)

def plot(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor']):
  if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
  set_lines(connect_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)]), color)

def draw_points(liste: list[Point], color: tuple | str = Screen.palette['PrimaryColor'], text: bool = True, style: str = "O"):
  for P in liste:
    if text: draw_string(str(P.name), P.x+6, P.y+6, Screen.palette["PrimaryText"], Screen.palette["SecondaryText"])
    if style == "(O)": fill_circle(P,3,color) ; draw_circle(P,7,color)
    else: eval(Screen.style[style])

def draw_croix(center: Point, r: int, a: int = 90, color: tuple | str = Screen.palette['PrimaryColor']):
  R = Vector(center, Point(center.x, center.y-r)).rotate(a, "first")
  for _ in range(4): R = R.rotate(90, "first") ; R.round() ; set_lines([(center, R.P2)], color)

def set_lines(line: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor']):
  for P1,P2 in line: 
    up,right = True if P2.y > P1.y else False,True if P2.x > P1.x else False;h,b = P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n = True if h <= b else False
    if b != 0 or h != 0: e = h/b if n else b/h
    for i in range(b if n else h):set_pixel(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i)),color)

def draw_lines(line: list[(Point, Point)], color: list[tuple] | tuple | str = Screen.palette['PrimaryColor'], taille: int = 1, alpha: float = 1.0, style: str = None):
  if style is None:
    degrad = isinstance(color, list)
    if degrad and len(line) != len(color): raise TypeError
    for P, col in zip(line,color) if degrad else line:
      if degrad: P1,P2 = P ; C1, C2 = col
      else: P1 = P ; P2 = col
      right, up = True if P1.x < P2.x else False, True if P2.y > P1.y else False ; b, h = P2.x-P1.x if right else P1.x-P2.x, P2.y-P1.y if up else P1.y-P2.y
      if h < b:
        if degrad: N = P2.x-P1.x if right else P1.x-P2.x ; colors = interpolate(C1,C2,N)
        for p in range(b):
          if degrad: color = colors[p]
          fill_circle(Point(round(P1.x+p) if right else round(P1.x-p),round(P1.y+(h*p)/b) if up else round(P1.y-(h*p)/b)),taille,color,alpha)
      else:
        if degrad: N = P2.y-P1.y if up else P1.y-P2.y ; colors = interpolate(C1,C2,N)
        for p in range(h):
          if degrad: color = colors[p]
          fill_circle(Point(round(P1.x+(b*p)/h) if right else round(P1.x-(b*p)/h),P1.y+p if up else round(P1.y-p)),taille,color,alpha)
  elif style == "AA":
    for (x0, y0), (x1, y1) in line:
      dx, dy, sx, sy = abs(x1 - x0), abs(y1 - y0), 1 if x0 < x1 else -1, 1 if y0 < y1 else -1
      err, e2, x2, ed = dx - dy, 0, 0, 1 if dx + dy == 0 else (dx * dx + dy * dy)**0.5
      while True:
        set_pixel(x0, y0, tuple(int(255 * abs(err - dx + dy) / ed) for i in range(3))) ; e2, x2 = err, x0
        if 2 * e2 >= -dx:
          if x0 == x1: break
          if e2 + dy < ed: set_pixel(x0, y0 + sy, tuple(int(255 * (e2 + dy) / ed) for i in range(3)))
          err -= dy ; x0 += sx
        if 2 * e2 <= dy:
          if y0 == y1: break
          if dx - e2 < ed: set_pixel(x2 + sx, y0, tuple(int(255 * (dx - e2) / ed) for i in range(3)))
          err += dx ; y0 += sy

def draw_arrows(vecteurs: list[Vector] = None, color: tuple | str = Screen.palette['PrimaryColor'], fill: bool = False):
  for V in vecteurs:
    A, B = V.P1, V.P2 ; set_lines([(A,B)], color=color) ; x0, y0, x1, y1 = A.x, A.y, B.x, B.y ; xb = 0.95*(x1-x0)+x0 ; yb = 0.95*(y1-y0)+y0
    if x0==x1: vtx0 = Point(int(xb-5), int(yb)) ; vtx1 = Point(int(xb+5), int(yb))
    elif y0==y1: vtx0 = Point(int(xb), int(yb+5)) ; vtx1 = Point(int(xb), int(yb-5))
    else: alpha = atan2(y1-y0,x1-x0)-90*pi/180 ;  a, b = 8*cos(alpha), 8*sin(alpha) ; vtx0, vtx1 = Point(int(xb+a), int(yb+b)), Point(int(xb-a), int(yb-b))
#    if fill: draw_triangles([Triangle([vtx0, vtx1, B], col_int=color, col_ligne=color, fill=True)])
#    else: draw_lines([(vtx0,B),(vtx1,B)], color)
    set_lines([(vtx0,B),(vtx1,B)], color)

def draw_vecteurs(vecteurs: list[Vector] = None, color: tuple | str = Screen.palette['PrimaryColor'], text: bool = False):
  for V in vecteurs:
    if text: x, y = milieu(V.P1, V.P2) ; draw_string(str(V.name), round(x-6), round(y-6))
    draw_arrows([V], color=color)

def draw_droites(droite: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor'], text: bool = True):
  y = lambda a, b, x: round((a*x + b))
  for D in droite:
#    _a = a(D.P1, D.P2) ; _b = b(_a, D.P1) ; draw_lines([(Point(0, y(_a, _b, 0)), Point(320, y(_a, _b, 320)))], color)
    set_lines([(Point(0, y(D.a, D.b, 0)), Point(320, y(D.a, D.b, 320)))], color)
    if text: M = milieu(D.P1, D.P2) ; draw_string(str(D.name), round(M.x-6), round(M.y-6), Screen.palette["PrimaryText"], Screen.palette["SecondaryText"])

def draw_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor']): 
  fill_rect(P1.x,P1.y,P4.x-P1.x,1,color);fill_rect(P4.x,P1.y,1,P4.y-P1.y+1,color);fill_rect(P1.x,P4.y,P4.x-P1.x,1,color);fill_rect(P1.x,P1.y,1,P4.y-P1.y,color)

def fill_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  for i in range(P4.x-P1.x):
    for j in range(P4.y-P1.y): alpha_pixel(P1.x+i, P1.y+j, color, alpha)

def draw_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor']):
  for x in range(-abs(int(rayon)), abs(int(rayon))):
    l = round((abs(int(rayon))**2-x**2)**0.5)
    if abs(x) <= l: set_pixel(center.x+l,center.y+x,color) ; set_pixel(center.x-l,center.y-x,color) ; set_pixel(center.x-x,center.y-l,color) ; set_pixel(center.x+x,center.y+l,color)
    
def fill_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  if rayon != 1: 
    for x in range(center.x-abs(int(rayon)), center.x+abs(int(rayon))): l = round((abs(int(rayon))**2-(center.x-x)**2)**0.5) ; fill_rectangle(Point(x, center.y-l), Point(x+1, (center.y-l)+l*2), color, alpha)
  else: alpha_pixel(center.x, center.y, color, alpha)

def draw_ellipses(rect: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor']):
  for (x0, y0), (x1, y1) in rect:
    a, b = abs(x1 - x0), abs(y1 - y0) ; b1 = b & 1 ; dx, dy = 4 * (1 - a) * b * b, 4 * (b1 + 1) * a * a ; err = dx + dy + b1 * a * a
    if x0 > x1: x0, x1 = x1, x0 + a
    if y0 > y1: y0 = y1
    y0 += (b + 1) // 2 ; y1 = y0 - b1 ; a *= 8 * a ; b1 = 8 * b * b
    while x0 <= x1:
      set_pixel(x1, y0, color) ; set_pixel(x0, y0, color) ; set_pixel(x0, y1, color) ; set_pixel(x1, y1, color) ; e2 = 2 * err
      if e2 <= dy: y0 += 1 ; y1 -= 1 ; err += dy ; dy += a
      if e2 >= dx or 2 * err > dy: x0 += 1 ; x1 -= 1 ; err += dx ; dx += b1
    while y0 - y1 < b:
      set_pixel(x0 - 1, y0, color) ; set_pixel(x1 + 1, y0, color) ; set_pixel(x0 - 1, y1, color) ; set_pixel(x1 + 1, y1, color) ; y0 += 1 ; y1 -= 1

def fill_ellipses(rect: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor'], alpha: float = 1.0):
  pass

def draw_quadratic(P1: Point, P2: Point, P3: Point, color: tuple | str = Screen.palette['PrimaryColor']):
  t = 0
  while t <= 1: P = quadratic(t,P1,P2,P3) ; set_pixel(P.x,P.y,color) ; t += 0.001

def draw_cubic(P1: Point, P2: Point, P3: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor']):
  pass

def bezier_curve(liste: list[Point], color: tuple | str = Screen.palette['PrimaryColor'], extrem: bool = False):
  list_connect, list_milieu, L = connect_points(liste), [milieu(P1,P2) for P1,P2 in connect_points(liste)], [] ; _liste = [((list_connect[n][0],M),(M,list_connect[n][1])) for n,M in enumerate(list_milieu)]
  for line in _liste: L.extend(line)
  if extrem: round(L[0][0]);round(L[0][1]);set_lines([(L[0])],color)
  for n,T in enumerate(L): draw_quadratic(T[0],T[1],L[n+1][1],color) if n != 0 and n < len(L)-2 and n%2 != 0 else None
  if extrem: round(L[-1][0]);round(L[-1][1]);set_lines([(L[-1])],color)
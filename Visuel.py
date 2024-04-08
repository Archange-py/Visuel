from math import pi, cos, sin, atan2, radians
from kandinsky import set_pixel, get_pixel, fill_rect, draw_string
from mathforvisuel import a, b, distance, milieu, Point, Vecteur, Droite, Vector, rotate
import kandinsky as kd

class Screen:
  palette = {"Background" : (248, 252, 248), "PrimaryColor" : (0, 0, 0), "PrimaryText" : (0, 0, 0), "SecondaryText" : (248, 252, 248)}
  style = {"O":"fill_circle(P,3,color)","(O)":"","*":"draw_croix(P,4,45,color)","+":"draw_croix(P,4,0,color)",".":"set_pixel(P.x,P.y,color)"}
  width, height = 320, 222 ; center = Point(int(width/2), int(height/2))

def interpolate(C1: tuple | str, C2: tuple | str, N: int = 100) -> list[tuple[float, float, float]]:
  d1, d2, d3 = abs(C2[0]-C1[0])/(N-2), abs(C2[1]-C1[1])/(N-2), abs(C2[2]-C1[2])/(N-2) ; new = [C1] ; C1 = list(C1)
  for _ in range(N-2):
    if C1[0] < C2[0]: C1[0] += d1
    elif C1[0] > C2[0]: C1[0] -= d1
    if C1[1] < C2[1]: C1[1] += d2
    elif C1[1] > C2[1]: C1[1] -= d2
    if C1[2] < C2[2]: C1[2] += d3
    elif C1[2] > C2[2]: C1[2] -= d3
    new.append(tuple(C1))
  new.append(C2) ; return new

def alpha_pixel(x: int, y: int, color: tuple | str, alpha: int = 0):
  if alpha == 0: set_pixel(x, y, color)
  elif alpha == 1: set_pixel(x, y, get_pixel(x,y))
  else: col_alpha = interpolate(kd.color(color), kd.color(get_pixel(x, y)), 12)[int(alpha*10)] ; set_pixel(x, y, kd.color(col_alpha))

def connect_points(liste: list[Point], ending: bool = False) -> list[tuple[Point, Point]]:
  line = [(liste[p], liste[p+1]) for p in range(len(liste)) if p < len(liste)-1]
  if ending: line.append((liste[-1], liste[0]))
  return line

def scatter(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor'], style=None):
  if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
  draw_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)], color, False, style)

def plot(X: list[int], Y: list[int], color: tuple | str = Screen.palette['PrimaryColor']):
  if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
  draw_lines(connect_points([Point(round(Screen.center.x+x), round(Screen.center.y-y)) for x, y in zip(X, Y)]), color)

def draw_points(liste: list[Point], color: tuple | str = Screen.palette['PrimaryColor'], text: bool = True, style: str = "O"):
  for P in liste:
    if text: draw_string(str(P.name), P.x+6, P.y+6, Screen.palette["PrimaryText"], Screen.palette["SecondaryText"])
    if style == "(O)": fill_circle(P,3,color) ; draw_circle(P,7,color)
    else: eval(Screen.style[style])

def findWithPoint(center: Point, point: Point, r: int) -> Vecteur:
  if center.x == point.x: return Vecteur(center, Point(center.x, center.y + r if point.y > center.y else center.y - r))
  elif center.y == point.y: return Vecteur(center, Point(center.x + r if point.x > center.x else center.x - r, center.y))
  else: _b, _h, = point.x - center.x, point.y - center.y ; h = (_b**2 + _h**2)**0.5 ; return Vecteur(center, Point(round(center.x+((r*_b)/h)), round(center.y+(r*_h)/h)))

def findWithAngle(R: Vecteur, angle: int, rayon: int) -> Vecteur:
#  _a = 180-(90+radians(-angle+207)) ; b, h = cos(-_a)*abs(r), sin(-_a)*abs(r)
#  return Vecteur(center, Point(round(center.x+b), round(center.y+h)))
  V = rotate(R, angle) ; return findWithPoint(V.P1, V.P2, rayon)

def draw_croix(center: Point, r: int, a: int = 90, color: tuple | str = Screen.palette['PrimaryColor']):
  R = Vector(center, Point(center.x, center.y-r)).rotate(a, "first")
  for _ in range(4): R = R.rotate(90, "first") ; R.round() ; draw_lines([(center, R.P2)], color)

def draw_lines(line: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor']):
  for P1,P2 in line:
    right, up = True if P1.x < P2.x else False, True if P2.y > P1.y else False ; b, h = P2.x-P1.x if right else P1.x-P2.x, P2.y-P1.y if up else P1.y-P2.y
    set_pixel(P1.x, P1.y, color) ; set_pixel(P2.x, P2.y, color)
    if h < b:
      for p in range(int(b)): set_pixel(round(P1.x+p) if right else round(P1.x-p),round(P1.y+(h*p)/b) if up else round(P1.y-(h*p)/b),color)
    else:
      for p in range(int(h)): set_pixel(round(P1.x+(b*p)/h) if right else round(P1.x-(b*p)/h),P1.y+p if up else round(P1.y-p),color)

def draw_lines_AA(line: list[(Point, Point)]):
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

def draw_arrows(vecteurs: list[Vecteur] = None, color: tuple | str = Screen.palette['PrimaryColor'], fill: bool = False):
  for V in vecteurs:
    A, B = V.P1, V.P2 ; draw_lines([(A,B)], color=color) ; x0, y0, x1, y1 = A.x, A.y, B.x, B.y ; xb = 0.95*(x1-x0)+x0 ; yb = 0.95*(y1-y0)+y0
    if x0==x1: vtx0 = Point(int(xb-5), int(yb)) ; vtx1 = Point(int(xb+5), int(yb))
    elif y0==y1: vtx0 = Point(int(xb), int(yb+5)) ; vtx1 = Point(int(xb), int(yb-5))
    else: alpha = atan2(y1-y0,x1-x0)-90*pi/180 ;  a, b = 8*cos(alpha), 8*sin(alpha) ; vtx0, vtx1 = Point(int(xb+a), int(yb+b)), Point(int(xb-a), int(yb-b))
#    if fill: draw_triangles([Triangle([vtx0, vtx1, B], col_int=color, col_ligne=color, fill=True)])
#    else: draw_lines([(vtx0,B),(vtx1,B)], color)
    draw_lines([(vtx0,B),(vtx1,B)], color)

def draw_vecteurs(vecteurs: list[Vecteur] = None, color: tuple | str = Screen.palette['PrimaryColor'], text: bool = False):
  for V in vecteurs:
    if text: x, y = milieu(V.P1, V.P2) ; draw_string(str(V.name), round(x-6), round(y-6))
    draw_arrows([V], color=color)

def draw_droites(droite: list[(Point, Point)] | list[Droite], color: tuple | str = Screen.palette['PrimaryColor'], text: bool = True):
  y = lambda a, b, x: round((a*x + b))
  for D in droite:
#    _a = a(D.P1, D.P2) ; _b = b(_a, D.P1) ; draw_lines([(Point(0, y(_a, _b, 0)), Point(320, y(_a, _b, 320)))], color)
    draw_lines([(Point(0, y(D.a, D.b, 0)), Point(320, y(D.a, D.b, 320)))], color)
    if text: M = milieu(D.P1, D.P2) ; draw_string(str(D.name), round(M.x-6), round(M.y-6), Screen.palette["PrimaryText"], Screen.palette["SecondaryText"])

def draw_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor']): draw_lines([(Point(P4.x,P1.y), P4),(Point(P1.x,P4.y), P4),(P1, Point(P4.x,P1.y)),(P1, Point(P1.x,P4.y))], color)

def fill_rectangle(P1: Point, P4: Point, color: tuple | str = Screen.palette['PrimaryColor']): fill_rect(P1.x, P1.y, P4.x-P1.x, P4.y-P1.y, color)

def draw_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor']):
  for x in range(-abs(int(rayon)), abs(int(rayon))):
    l = round((abs(int(rayon))**2-x**2)**0.5)
    if abs(x) <= l:
      set_pixel(center.x+l,center.y+x,color) ; set_pixel(center.x-l,center.y-x,color) ; set_pixel(center.x-x,center.y-l,color) ; set_pixel(center.x+x,center.y+l,color)

def fill_circle(center: Point, rayon: int, color: tuple | str = Screen.palette['PrimaryColor']):
  for x in range(center.x-abs(int(rayon)), center.x+abs(int(rayon))): l = round((abs(int(rayon))**2-(center.x-x)**2)**0.5) ; fill_rect(x, center.y-l, 1, l*2, color)

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

def fill_ellipses(rect: list[(Point, Point)], color: tuple | str = Screen.palette['PrimaryColor']):
  pass
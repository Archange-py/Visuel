from math import cos, sin, radians

a = lambda P1, P2: (P2.y-P1.y)/(P2.x-P1.x)
b = lambda a, P1: -(a*P1.x-P1.y)
distance = lambda P1, P2: ((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5
milieu = lambda P1, P2, p=2: Point((P1.x+P2.x)/p,(P1.y+P2.y)/p)

class Point:
  def __init__(self, x: int, y: int, name=''): self.x, self.y, self.name = x, y, name

  def __str__(self) -> str: return str(self.name)

  def __repr__(self) -> str: return "Point({}, {})".format(self.x, self.y)

  def __eq__(self, other) -> bool:
    if isinstance(other, Point): return (self.x == other.x) and (self.y == other.y)
    else: return False

  def __iter__(self): return iter([self.x, self.y])

  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)
  
  def copy(self): return Point(self.x, self.y, self.name)
  
  def round(self): self.x, self.y = round(self.x), round(self.y)

class Vector:
  def __init__(self, P1: Point, P2: Point, name: str = ''):
    self.P1, self.P2, self.name = P1, P2, name
    self.x, self.y  = P2.x-P1.x, P2.y-P1.y
    self.norme = (self.x**2 + self.y**2)**0.5

  def __str__(self) -> str: return "({}, {})".format(self.x,self.y)
  
  def __repr__(self) -> str: return "Vector({}, {})".format(self.x,self.y)

  def __iter__(self): return iter([self.x, self.y])

  def __add__(self, other):
    if isinstance(other, Vector): return Vector(self.x+other.x, self.y+other.y)
    elif isinstance(other, int): return Vector(self.x+other, self.y+other)

  __radd__ = __add__

  def __sub__(self, other):
    if isinstance(other, Vector): return Vector(self.x-other.x, self.y-other.y)
    elif isinstance(other, int): return Vector(self.x-other, self.y-other)

  __rsub__ = __sub__

  def __mul__(self, other):
    if isinstance(other, Vector): return Vector(self.x*other.x, self.y*other.y)
    elif isinstance(other, int): return Vector(self.x*other, self.y*other)

  __rmul__ = __mul__

  def __eq__(self, other) -> bool: 
    if isinstance(other, Vector): return (self.x == other.x) and (self.y == other.y)
    else: return False

  def __pos__(self): return self

  def __neg__(self): return Vector(-self.x, -self.y)

  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)

  def rotate(self, angle: int, anchor: str = "first"):
    angle = radians(angle) ; P = self.P1 if anchor == "first" else self.P2
    return Vector(P, Point(P.x+self.x*cos(angle)-self.y*sin(angle), P.y+self.x*sin(angle)+self.y*cos(angle)))

  def copy(self): return Vector(self.x, self.y, self.name)
  
  def round(self): self.P1.round() ; self.P2.round()

class Line:
  def __init__(self, P1: Point, P2: Point, name: str = ''):
    self.P1, self.P2, self.name = P1, P2, name
    if not P1.x == P2.x and not P1.y == P2.y: self.a = a(self.P1, self.P2) ; self.b = b(self.a, self.P1)
    else: self.a, self.b = 0, 0

  def __str__(self) -> str:
    if self.b <= 0: end = ' - {}' . format(abs(self.b))
    elif self.b >= 0: end = ' + {}' . format(self.b)
    else: end = ''
    return 'y = {}x'.format(self.a) + end

  def __repr__(self) -> str:
    return 'Droite({}, {})'.format(repr(self.P1), repr(self.P2))

  def __eq__(self, other) -> bool:
    if isinstance(other, Line): return self.a == other.a and self.b == other.b
    else: return False

  def __hash__(self) -> int: return hash(self.a) ^ hash(self.b)



class Droite:
  def __init__(self, P1: Point, P2: Point, name: str = ''):
    self.P1, self.P2, self.name = P1, P2, name
    if not P1.x == P2.x and not P1.y == P2.y: self.a = a(self.P1, self.P2) ; self.b = b(self.a, self.P1)
    else: self.a, self.b = 0, 0

  def __str__(self) -> str:
    if self.b < 0: end = ' - {}' . format(abs(self.b))
    elif self.b > 0: end = ' + {}' . format(self.b)
    else: end = ''
    return 'y = {}x'.format(self.a) + end

  def __repr__(self) -> str:
    return 'Droite({}, {})'.format(self.P1, self.P2)

  def __eq__(self, other) -> bool:
    if isinstance(other, type(self)):
      if self.a == other.a and self.b == other.b: return True
      else: return False

  def __hash__(self) -> int: return hash(self.a) ^ hash(self.b)

class Vecteur:
  def __init__(self, P1: Point, P2: Point, name: str = ''):
    self.P1, self.P2, self.name = P1, P2, name
    self.x, self.y = P2.x - P1.x, P2.y - P1.y
    self.norme = (self.x**2 + self.y**2)**0.5

  def __add__(self,other):
    if isinstance(other, type(self)):
      return Vecteur(Point(self.P1.x,self.P1.y,self.P1.name),Point(self.P2.x+other.x,self.P2.y+other.y,self.P2.name))

  def __sub__(self,other):
    if isinstance(other, type(self)):
      return Vecteur(Point(self.P1.x,self.P1.y,self.P1.name),Point(self.P2.x-other.x,self.P2.y-other.y,self.P2.name))

  def __mul__(self,other):
    if isinstance(other, type(self)):
      return Vecteur(self.x*other.x, self.y*other.y)
    elif isinstance(other, int):
      return Vecteur(self.x*other, self.y*other)

  def __eq__(self, other) -> bool:
    if isinstance(other, type(self)):
       return (self.x == other.x) and (self.y == other.y)

  def __str__(self) -> str: return "({} ; {})".format(self.P1,self.P2)
  
  def __repr__(self) -> str: return "Vecteur({}, {})".format(self.P1.__repr__(),self.P2.__repr__())

  def __iter__(self): return iter([self.P1, self.P2])
  
  def __pos__(self): return self

  def __neg__(self): return Vecteur(self.P2, self.P1, self.name)

  def __hash__(self) -> int: return hash(self.x) ^ hash(self.y)

def dot(V1: Vecteur, V2: Vecteur) -> int: return V1.x * V2.y - V2.x * V1.y

def rotate(V: Vecteur, angle: float | int) -> Vecteur:
  angle = radians(angle) ; return Vecteur(V.P2, Point(V.P2.x+V.x*cos(angle)-V.y*sin(angle), V.P2.y+V.x*sin(angle)+V.y*cos(angle)))

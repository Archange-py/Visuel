from visuel import *
from time import *
from ion import *

xg,xd,yh,yb = 50,50,80,80
C = Point(160,111)
pas = 0

def intersec(A,B):
  if A.x == B.x: return Point(A.x,A.y-yh) if B.y < A.y else Point(A.x,A.y+yb)
  elif A.y == B.y: return Point(A.x-xg,A.y) if B.x < A.x else Point(A.x+xd,A.y)
  else:
    _a,_a2 = a(A,B),a(Point(A.x-xg,A.y-yh),A);_b,_b2 = b(_a,A),b(_a2,A)
    if B.y-(_a2*B.x+_b2) == 0: I = Point(A.x-xg,A.y-yh) if B.x < A.x else Point(A.x+xd,A.y+yb)
    elif B.y-(_a2*B.x+_b2) > 0:  I = Point(((A.y+yb)-_b)/_a,A.y+yb) if abs(B.x-A.x) < abs(B.y-A.y) else Point(A.x-xg,_a*(A.x-xg)+_b) 
    else: I = Point(((A.y-yh)-_b)/_a,A.y-yh) if abs(B.x-A.x) < abs(B.y-A.y) else Point(A.x+xd,_a*(A.x+xd)+_b)
    round(I) ; return I

A,x,y,t=Point(160,111),0,111,5
def update():
  fill_rect(0,0,320,222,"w")
  fill_rect(C.x-xg-1,C.y-yh-1,xg+xd+2,yh+yb+2,"black")
  fill_rect(C.x-xg,C.y-yh,xg+xd,yh+yb,"w")
#  set_lines([(A,Point(x,y))],"r")
#  set_lines([intersec(A,Point(x,y))],"orange")
  set_lines([(Point(x,y),intersec(A,Point(x,y)))],"r")

update()
while True:
  if keydown(KEY_UP): y -= t;update()
  if keydown(KEY_DOWN): y += t;update()
  if keydown(KEY_RIGHT): x += t;update()
  if keydown(KEY_LEFT): x -= t;update()
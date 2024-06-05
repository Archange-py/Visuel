from visuel import *
from time import *
from ion import *

xg,xd,yh,yb = 50,50,50,50
C = Point(160,111)
pas = 0

def intersec(A,B):
  if B.x < C.x-xg:#or B.y < C.y-yh: 
    p = (abs(B.y-A.y)*xg/abs(B.x-A.x))
    y = C.y-p if A.y > B.y else C.y+p;x = C.x-xg
  if B.y < C.y-yh:#and B.x > C.x-xg:
    p = (abs(A.x-B.x)*yh/abs(A.y-B.y))
    x = C.x-p if A.x > B.x else C.x+p;y = C.y-yh
  if B.x > C.x+xd:#or B.y < C.y-yh: 
    p = (abs(B.y-A.y)*xd/abs(B.x-A.x))
    y = C.y-p if A.y > B.y else C.y+p;x = C.x+xd
  if B.y > C.y+yb:#and B.x > C.x-xg:
    p = (abs(A.x-B.x)*yb/abs(A.y-B.y))
    x = C.x-p if A.x > B.x else C.x+p;y = C.y+yb
  return (A,Point(round(x),round(y)))

A,x,y,t=Point(160,111),0,0,5
def update():
  fill_rect(0,0,320,222,"w")
  fill_rect(C.x-xg-1,C.y-yh-1,xg+xd+2,yh+yb+2,"black")
  fill_rect(C.x-xg,C.y-yh,xg+xd,yh+yb,"w")
#  set_lines([(A,Point(x,y))],"r")
#  set_lines([intersec(A,Point(x,y))],"orange")
  set_lines([(Point(x,y),intersec(A,Point(x,y))[1])],"r")

update()
while True:
  if keydown(KEY_UP): y -= t;update()
  if keydown(KEY_DOWN): y += t;update()
  if keydown(KEY_RIGHT): x += t;update()
  if keydown(KEY_LEFT): x -= t;update()
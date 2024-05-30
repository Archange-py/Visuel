from ext_turtle import *
from math import *

def poly_cart(n, a, b, r):
    penup() ; goto(a+r, b) ; pendown()
    alpha = 2*pi / n
    for k in range(1, n+1):
        goto(a+r*cos(k*alpha), b+r*sin(k*alpha))

def poly_pol(n ,c):
    a = 360/n
    for i in range(n+1):
        forward(c)
        left(a)

def von_koch(n,L):
    if n == 0 :
        forward(L)
    else :
        von_koch(n-1,L/3)
        left(60)
        von_koch(n-1,L/3)
        right(120)
        von_koch(n-1,L/3)
        left(60)
        von_koch(n-1,L/3)

#pendown()
#poly_cart(10, 160, 111, 50)
#poly_pol(7, 20)
from time import *
setheading(0)
sleep(3)
for i in range(10): clear() ; penup() ; goto(0, 111) ; pendown() ; von_koch(i, 320) ; print(i) ; sleep(1)
#forward(100)
#color("pink")
#left(90)
#forward(100)
#penup()
#goto(160,111)
#pendown()
#forward(100)
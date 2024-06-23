from visuel_ import Point, draw_quadratic, draw_cubic, bezier_curve, fill_rect
from random import randint
from time import sleep

#   Example 1
A,B,C,D,E = Point(50,50),Point(100,200),Point(150,50),Point(200,200),Point(250,50)

#draw_quadratic(A, B, C, "red", thickness=1)

#   Example 2

#draw_cubic(A,B,C,D,"red", thickness=1)

#   Example 3

#bezier_curve([A,B,C,D,E], "red", 1, True)

#   Example 4

def random_curves(N, color, thickness, extrem=False):
  bezier_curve([Point(randint(10, 310), randint(10, 202)) for _ in range(N)], color, thickness, extrem)

def animation(N, color, thickness, extrem=False):
  while True:
    fill_rect(0, 0, 320, 222, "white")
    random_curves(N, color, thickness, extrem)
    sleep(0.5)

#animation(15, "purple", 1, False)
from visuel import Point, bezier_curve, draw_quadratic, fill_rect
from random import randint
from time import sleep

#   Example 1

A,B,C = Point(50,50),Point(130,200),Point(210,50)

def animation_1(color):
  draw_quadratic(A, B, C, color)
  draw_quadratic(A, C, B, color)
  draw_quadratic(B, A, C, color)

#animation_1("purple")

# Example 2

A,B,C,D,E = Point(50,50),Point(100,200),Point(150,50),Point(200,200),Point(250,50)

def animation_2(color):
  bezier_curve([A,B,C,D,E], color, True)

#animation_2("purple")

# Example 3

def random_curves(N, color, extrem=False):
  bezier_curve([Point(randint(10, 310), randint(10, 202)) for _ in range(N)], color, extrem)

def animation_3(N, color, extrem=False):
  while True:
    fill_rect(0, 0, 320, 222, "white")
    random_curves(N, color, extrem)
    sleep(0.5)

#animation_3(15, "purple", False)
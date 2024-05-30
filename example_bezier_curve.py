from visuel import Point, bezier_curve, draw_quadratic, draw_cubic, fill_rect
from random import randint
from time import sleep

#   Example 3

A,B,C,D,E = Point(50,50),Point(100,200),Point(150,50),Point(200,200),Point(250,50)

def animation_3(color, thickness):
  bezier_curve([A,B,C,D,E], color, thickness, True)

#animation_3("purple", 1)

#   Example 4

def random_curves(N, color, thickness, extrem=False):
  bezier_curve([Point(randint(10, 310), randint(10, 202)) for _ in range(N)], color, thickness, extrem)

def animation_4(N, color, thickness, extrem=False):
  while True:
    fill_rect(0, 0, 320, 222, "white")
    random_curves(N, color, thickness, extrem)
    sleep(0.5)

animation_4(15, "purple", 1, False)
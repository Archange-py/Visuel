from visuel import Point, draw_quadratic

#   Example 1
A,B,C = Point(50,50),Point(130,200),Point(210,50)

def animation_1(color, thickness):
  draw_quadratic(A, B, C, color, thickness)
  draw_quadratic(A, C, B, color, thickness)
  draw_quadratic(B, A, C, color, thickness)

animation_1("purple", 1)
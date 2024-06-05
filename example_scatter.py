from random import randint
from visuel import *
from math import sin

print(list(Screen.style.keys()))

#   Example 1
Screen.center = Point(50,200)

X = [3, 29, 55, 81, 108, 133, 160]
Y = [109, 144, 160, 161, 148, 122, 78]

scatter(X, Y, "red", "O")

#   Example 2
Screen.center = Point(160,111)

X = [x for x in range(-100, 100, 5)]
Y = [sin(y*25)*30 for y in range(-100, 100, 5)]

#scatter(X, Y, "red", "*")

#   Example 3
Screen.center = Point(160,111)

X = [randint(-100, 80) for x in range(-100, 100, 10)]
Y = [randint(-100, 80) for y in range(-100, 100, 10)]

#scatter(X, Y, "red", "+")

#   Example 4
Screen.center = Point(160,111)

X = [x for x in range(-100, 100, 3)]
Y = [sin(y*25)*30 for y in range(-100, 100, 3)]

#scatter(X, Y, "red", ".")
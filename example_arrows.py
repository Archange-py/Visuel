from visuel_5 import Point, Vecteur, draw_arrows

A = Point(20, 25)
B = Point(150, 200)
C = Point(120, 25)
D = Point(250, 200)

AB = Vecteur(A, B)
CD = Vecteur(C, D)

draw_arrows([AB], 'orange', fill=False)

draw_arrows([CD], 'blue', fill=True)
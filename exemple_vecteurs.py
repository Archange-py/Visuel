from visuel_5 import Point, Vecteur, draw_vecteurs

A = Point(50,50,"A")
B = Point(150,50,"B")
C = Point(250,50,"C")
D = Point(50,120,"D")
E = Point(150,120,"E")
F = Point(250,120,"F")
G = Point(50,185,"G")

BA = Vecteur(B,A,"BA")
DE = Vecteur(D,E,"DE")
CF = Vecteur(C,F,"CF")
GD = Vecteur(G,D,"GD")
AE = Vecteur(A,E,"AE")

EB = BA + AE
EB.name = "EB"

draw_vecteurs([BA, DE, CF, GD, AE, EB], color='purple', text=True)
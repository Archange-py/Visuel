from visuel import *

A,B,C,D,E = Point(20,20),Point(160,111),Point(20,202),Point(300,20),Point(300,202);F = milieu(D,E);round(F)
V,W,Y,X = Vector(A,B,name="V"),Vector(B,C,name="W"),Vector(F,D,name="Y"),Vector(F,E,name="X");U = V+W;U.name = "U"

def example():
  draw_points([A,B,C,D,E,F],"r",style=".")
  draw_rectangle(A,E)
  draw_croix(B,320)
  bezier_curve([A,C,D,E,A,C],"orange")
  draw_circle(B,50,"r")
  fill_circle(B,10,"r")
  draw_droite(D,E,"cyan","d'");draw_droite(D,B,"cyan","d''");draw_droite(E,B,"cyan","d'''")
  draw_vector(A,V,"g");draw_vector(B,W,"g");draw_vector(A,U,"g")
  draw_arrows([(F,Y)],"blue",fill=True);draw_arrows([(F,X)],"blue",fill=True)
  draw_polygone(6,50,B)
  fill_polygone(6,50,B,"yellow",alpha=0.5)

example()
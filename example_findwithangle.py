from Visuel import Point, Vecteur, findWithAngle, draw_lines, draw_circle, draw_vecteurs, draw_lines_AA

R = Vecteur(Point(160,111),Point(160,0))

for a in range(0,360,90):
  V = findWithAngle(R,a,111,"first")
  draw_lines([(R.P1,R.P2),(V.P1,V.P2)],"red")

#A = Point(160,111)

#for a in range(0,360):
#  V = findWithAngle(A,a,0.2)
#  draw_line([(V.P1,V.P2)],"red")
#  set_pixel(round(V.P2.x),round(V.P2.y),"black")
#  A = V.P2
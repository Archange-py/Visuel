from Visuel import interpolate, fill_rect
from kandinsky import color

def draw_interpolate(C1, C2, N, position=(0, 0), taille=1):
  colors_interpolate = interpolate(C1, C2, N)
  for n, col in enumerate(colors_interpolate):
    fill_rect(position[0]+n*taille, position[1], taille, taille, color(col))
  del colors_interpolate

#   Exemple 1
for y in range(222):
  draw_interpolate((255,255,0), (255,0,0), N=320, position=(0, y), taille=1)

#   Exemple 2
#for y in range(222):
#  draw_interpolate((255,255,0), (0,255,255), N=320, position=(0, y), taille=1)

#   Exemple 3
#for y in range(0, 111):
#  draw_interpolate((255,255,255), (0,255,255), N=320, position=(0, y), taille=1)
#for y in range(111, 222):
#  draw_interpolate((0,255,255), (255,255,255), N=320, position=(0, y), taille=1)

#   Exemple 4
#for y in range(222):
#  C1 = (255 - y, 255 - y, 255 - y)
#  C2 = (255 - y, 0 + y, 0 + y)
#  draw_interpolate(C1, C2, N=320, position=(0, y), taille=1)
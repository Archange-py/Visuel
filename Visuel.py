from kandinsky import set_pixel,get_pixel,fill_rect,draw_string
from math import pi,cos,sin,radians
import builtins as blt
import kandinsky as kd
dot,distance,milieu,average,round,neg=lambda V1,V2:V1.x*V2.y-V2.x*V1.y,lambda P1,P2:((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5,lambda P1,P2,p=2:Point((P1.x+P2.x)/p,(P1.y+P2.y)/p),lambda liste:sum(liste)/len(liste),lambda cls:cls.__round__(),lambda cls:cls.__neg__()
class Point:
  def __init__(self,x,y,name=''):self.x,self.y,self.name=x,y,name
  def __str__(self):return str(self.name)
  def __repr__(self):return "Point({}, {})".format(self.x, self.y)
  def __eq__(self,other):return (self.x==other.x)and(self.y==other.y) if isinstance(other,Point) else False
  def __iter__(self):return iter([self.x,self.y])
  def __hash__(self):return hash(self.x)^hash(self.y)
  def __round__(self):self.x,self.y=blt.round(self.x),blt.round(self.y)
  def copy(self):return Point(self.x,self.y,self.name)
class Vector:
  def __init__(self,P1=None,P2=None,x=None,y=None,name=''):cond=(P1!=None and P2!=None);self.x,self.y,self.name=P2.x-P1.x if cond else x,P2.y-P1.y if cond else y,name
  def __str__(self):return str(self.name)
  def __repr__(self):return "Vector({}, {})".format(self.x,self.y)
  def __eq__(self,other):return (self.x==other.x)and(self.y==other.y) if isinstance(other,Vector) else False
  def __iter__(self):return iter([self.x,self.y])
  def __pos__(self):return self
  def __neg__(self):return Vector(x=-self.x,y=-self.y,name=self.name)
  def __hash__(self):return hash(self.x)^hash(self.y)
  def __round__(self):self.x=blt.round(self.x);self.y=blt.round(self.y)
  def __add__(self,other):return Vector(x=self.x+other.x,y=self.y+other.y) if isinstance(other,Vector) else Point(other.x+self.x,other.y+self.y) if isinstance(other,Point) else None
  def __sub__(self,other):return Vector(x=self.x-other.x,y=self.y-other.y) if isinstance(other,Vector) else Point(other.x-self.x,other.y-self.y) if isinstance(other,Point) else None
  def __mul__(self,other):return Vector(x=self.x*other.x,y=self.y*other.y) if isinstance(other,Vector) else Vector(x=self.x*other,y=self.y*other) if isinstance(other,int) else None
  def __truediv__(self,other):return Vector(x=self.x/other.x,y=self.y/other.y) if isinstance(other,Vector) else Vector(x=self.x/other,y=self.y/other) if isinstance(other,int) else None
  def rotate(self,angle):angle=radians(angle);return Vector(x=self.x*cos(angle)-self.y*sin(angle),y=self.x*sin(angle)+self.y*cos(angle),name=self.name)
  def copy(self):return Vector(x=self.x,y=self.y,name=self.name)
class Screen:
  width,height,p=320,222,3;center=Point(int(width/2),int(height/2))
  palette={"Background":(248,252,248),"PrimaryColor":(0,0,0),"SecondaryColor":(200,200,200),"PrimaryText":(0,0,0),"SecondaryText":(248,252,248)}
def expend(liste,d,M=None):M=Point(blt.round(average([P.x for P in liste])),blt.round(average([P.y for P in liste]))) if M==None else M;return [Point(blt.round(P.x+(P.x-M.x)*d),blt.round(P.y+(P.y-M.y)*d)) if d!=0 else P for P in liste]
def connect_points(liste,ending=False):line=[(liste[p],liste[p+1]) for p in range(len(liste)) if p<len(liste)-1] ; line.append((liste[-1],liste[0])) if ending else None;return line
def findWithPoint(P1,P2,length):N=((P2.x-P1.x)**2+(P2.y-P1.y)**2)**0.5;return Point(P1.x+((P2.x-P1.x)*length)/N,P1.y+((P2.y-P1.y)*length)/N)
def findWithAngle(P,V,angle,rayon):_V=V.rotate(angle);return findWithPoint(P,P+_V,rayon)
def alpha_pixel(x,y,color,alpha=1.0):set_pixel(x,y,tuple(C1*alpha-C2*alpha+C2 for C1,C2 in zip(kd.color(color),get_pixel(x,y))))
def interpolate(C1,C2,N=100):C1,C2=kd.color(C1),kd.color(C2);interpolated_colors=[(C1[0]+(C2[0]-C1[0])*i/(N+1),C1[1]+(C2[1]-C1[1])*i/(N+1),C1[2]+(C2[2]-C1[2])*i/(N+1)) for i in range(N+2)];return interpolated_colors[1:-1]
def draw_points(liste,color=Screen.palette['PrimaryColor'],text=True,style="O"):
  for P in liste:
    if style == "O":fill_circle(P,Screen.p,color)
    elif style == "+":draw_croix(P,Screen.p,0,color)
    elif style == "*":draw_croix(P,4,45,color)
    elif style == ".":set_pixel(P.x,P.y,color)
    if text:draw_string(str(P.name),P.x+6,P.y+6,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
def draw_croix(center,r,angle=90,color=Screen.palette['PrimaryColor']):
  R=Vector(center,Point(center.x+r,center.y));R=R.rotate(angle)
  for _ in range(4):R=R.rotate(90);round(R);set_lines([(center,R+center)],color)
def set_lines(line,color=Screen.palette['PrimaryColor']):
  for P1,P2 in line:
    up,right=True if P2.y>P1.y else False,True if P2.x>P1.x else False;h,b=P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n=True if h<=b else False;set_pixel(P2.x,P2.y,color)
    if b!=0 or h!=0:e=h/b if n else b/h
    for i in range(b if n else h):set_pixel(int(blt.round(P1.x+i) if right else blt.round(P1.x-i))if n else int(blt.round(P1.x+e*i) if right else blt.round(P1.x-e*i)),int(blt.round(P1.y+e*i) if up else blt.round(P1.y-e*i))if n else int(blt.round(P1.y+i) if up else blt.round(P1.y-i)),color)
def draw_arrows(liste,color=Screen.palette['PrimaryColor'],length=10,angle=45,fill=False):
  for A,V in liste:B=V+A;V1=neg(Vector(findWithPoint(B,A,length),B)) if A!=B else V;V2,V3=V1.rotate(angle),V1.rotate(-angle);round(V2);round(V3);set_lines([(A,B)],color);set_lines([(B,V2+B),(B,V3+B)],color) if not fill else fill_triangles([(V2+B,B,V3+B)],color)
def draw_vector(P,V,color=Screen.palette['PrimaryColor']):x,y=milieu(P,V+P);draw_string(str(V.name),blt.round(x-6),blt.round(y-6),Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]);draw_arrows([(P,V)],color,fill=False)
def draw_droite(P1,P2,color=Screen.palette['PrimaryColor'],name=None):
  if P1.x==P2.x:set_lines([(Point(P1.x,0),Point(P1.x,222))],color)
  elif P1.y==P2.y:set_lines([(Point(0,P1.y),Point(320,P1.y))],color)
  else: _a=(P2.y-P1.y)/(P2.x-P1.x);_b=-(_a*P1.x-P1.y);P0,P3=Point(blt.round((222-_b)/_a),222) if abs(P2.x-P1.x)<abs(P2.y-P1.y) else Point(0,blt.round(_a*0+_b)),Point(blt.round((-1-_b)/_a),-1) if abs(P2.x-P1.x)<abs(P2.y-P1.y) else Point(320,blt.round(_a*320+_b));set_lines([(P0,P3)],color)
  if name!=None:M=milieu(P1,P2);draw_string(str(name),blt.round(M.x-6),blt.round(M.y-6),Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
def fill_triangles(liste,color=Screen.palette['PrimaryColor'],alpha=1.0):
  eq=lambda p,a,b:(a.x-p.x)*(b.y-p.y)-(a.y-p.y)*(b.x-p.x)
  for P1,P2,P3 in liste:
    xmin,xmax,ymin,ymax=min(P1.x,P2.x,P3.x),max(P1.x,P2.x,P3.x)+1,min(P1.y,P2.y,P3.y),max(P1.y,P2.y,P3.y)+1;width,height=abs(xmax+xmin),abs(ymax+ymin)
    for y in range(ymin,ymax):
      if 0<=y<height:
        for x in range(xmin,xmax):
          pos=Point(x,y);w1,w2,w3=eq(pos,P3,P1),eq(pos,P1,P2),eq(pos,P2,P3)
          if 0<=x<width and ((w1>=0 and w2>=0 and w3>=0) or (-w1>=0 and -w2>=0 and -w3>=0)):set_pixel(x,y,color) if int(alpha)==1 else alpha_pixel(x,y,color,alpha)
def draw_polygone(n,rayon,coord,color=Screen.palette['PrimaryColor']):alpha=2*pi/n;set_lines(connect_points([Point(blt.round(coord.x+rayon*cos(k*alpha)),blt.round(coord.y+rayon*sin(k*alpha)),color) for k in range(1,n+1)],True),color)
def fill_polygone(n,rayon,coord,color=Screen.palette['PrimaryColor'],c_map=None,alpha=1.0):
  _alpha=2*pi/n;points=[Point(blt.round(coord.x+rayon*cos(k*_alpha)),blt.round(coord.y+rayon*sin(k*_alpha))) for k in range(1,n+1)]
  for p,c in zip(connect_points(points,True),[color for _ in range(len(points))] if not isinstance(c_map,list) else c_map):fill_triangles([([coord,p[0],p[1]])],c,alpha)
def draw_rectangle(P1,P4,color=Screen.palette['PrimaryColor']):fill_rect(P1.x,P1.y,P4.x-P1.x,1,color);fill_rect(P4.x,P1.y,1,P4.y-P1.y+1,color);fill_rect(P1.x,P4.y,P4.x-P1.x,1,color);fill_rect(P1.x,P1.y,1,P4.y-P1.y,color)
def fill_rectangle(P1,P4,color=Screen.palette['PrimaryColor'],alpha=1.0):
  for x,y in [(x,y) for x in range(P4.x-P1.x if P4.x>P1.x else P1.x-P4.x) for y in range(P4.y-P1.y if P4.y>P1.y else P1.y-P4.y)]:alpha_pixel(P1.x+x,P1.y+y,color,alpha)
def draw_circle(center,rayon,color=Screen.palette['PrimaryColor']):
  for x in range(-abs(rayon),abs(rayon)):
    l=blt.round((abs(rayon)**2-x**2)**0.5)
    if abs(x)<=l:set_pixel(center.x+l,center.y+x,color);set_pixel(center.x-l,center.y-x,color);set_pixel(center.x-x,center.y-l,color);set_pixel(center.x+x,center.y+l,color)
def fill_circle(center,rayon,color=Screen.palette['PrimaryColor'],alpha=1.0):
  for x,y in [(x,y) for x in range(-blt.round(rayon),blt.round(rayon)+1) for y in range(-blt.round(rayon),blt.round(rayon)+1)]:
    if blt.round(distance(center,Point(center.x+x,center.y+y)))<=rayon:alpha_pixel(center.x+x,center.y+y,color,alpha) if int(alpha)!=1 else set_pixel(center.x+x,center.y+y,color)
def bezier_curve(liste,color=Screen.palette['PrimaryColor'],thickness=1,extrem=False):
  list_connect,list_milieu,L=connect_points(liste),[milieu(P1,P2) for P1,P2 in connect_points(liste)],[];_liste=[((list_connect[n][0],M),(M,list_connect[n][1])) for n,M in enumerate(list_milieu)]
  for line in _liste:L.extend(line)
  if extrem:round(L[0][0]);round(L[0][1]);set_lines([(L[0])],color)
  for n,T in enumerate(L):
    if n!=0 and n<len(L)-2 and n%2!=0:
      t=0
      while t<=1:P=Point((1-t)**2*T[0].x+2*(1-t)*t*T[1].x+t**2*L[n+1][1].x,(1-t)**2*T[0].y+2*(1-t)*t*T[1].y+t**2*L[n+1][1].y);round(P);set_pixel(P.x,P.y,color) if thickness==1 else fill_circle(P,thickness,color,1);t+=0.001
  if extrem: round(L[-1][0]);round(L[-1][1]);set_lines([(L[-1])],color)
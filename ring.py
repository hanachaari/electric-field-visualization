from vpython import*
from time import*
k=9e9
Q=10e-9
R=0.01

#cring=ring(pos=vector(0,0,0),axis=vector(1,0,0), radius=R,thickness=R/10,color=color.red)

N=200
theta=0
dtheta=2*pi/N
dq=Q/N

points=[]
##drawing the ring

while theta<2*pi:
  points=points+[sphere(pos=R*vector(0,cos(theta),sin(theta)),radius=R/15,color=color.red)]
  theta=theta+dtheta
  
  
##drawing one observational point 
stepx = 0.8*R
stepy = 0.8*R
stepz = 0.8*R
ro=vector(-R,-2*R,-2*R)
while ro.y<4*R:
  while ro.z<4*R:
    while ro.x<R:
      obs=sphere(pos=ro, radius=R/25,color=color.cyan)
      E=vector(0,0,0)
      for p in points:
        r=obs.pos-p.pos
        dE=k*dq*norm(r)/mag(r)**2
        E=E+dE
      Escale=0.005/mag(E)
      Earrow=arrow(pos=obs.pos,axis=Escale*E,color=color.cyan)
      sleep(0.001)
      Earrow.color=color.yellow
      ro.x+=stepx
    ro.x=-R
    ro.z+=stepz
  ro.z=-2*R 
  ro.y+=stepy




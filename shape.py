import numpy as np
import scipy as sp
from scipy.integrate import quad
import matplotlib.pyplot as plt
import sympy as smp
import plotly.graph_objects as go
from IPython.display import HTML

# define the variable where to calculate the electric field on the charged shape
t = smp.symbols('t', positive=True)
# define our variables
x, y, z = smp.symbols('x y z')
# define the vector position where you are 
r = smp.Matrix([x, y, z])
# define where the charged shape is located
print('Enter the coordinates of the location where is the charged shape')
xpos = input("enter the coeficient of x position\n")
ypos = input("enter the coeficient of y position\n")
zpos = input("enter the coeficient of z position\n")

cos = input("does the x position use the cos or sin ?\n")
if cos =="cos":
    xpos1 = smp.cos(float(xpos)*t)
elif cos =="sin":
    xpos1 = smp.sin(float(xpos)*t)
else:
    xpos1 = float(xpos)*t

cos = input("does the y position use the cos or sin ?\n")
if cos =="cos":
    ypos1 = smp.cos(float(ypos)*t)
elif cos =="sin":
    ypos1 = smp.sin(float(ypos)*t)
else:
    ypos1 = float(ypos)*t

cos = input("does the z position use the cos or sin ?\n")
if cos =="cos":
    zpos1 = smp.cos(float(zpos)*t)
elif cos =="sin":
    zpos1 = smp.sin(float(zpos)*t)
else:
    zpos1 = float(zpos)*t

# initialize the vector of the charged shape location
r_p = smp.Matrix([xpos1, ypos1, zpos1])
# calculate the distance and initilaize it in a vector
sep = r - r_p

# get the total charge
q = input("Enter the total charge of the shape")
Q = float(q)

# diiferntiate the r' over t 
dr_pdt = smp.diff(r_p, t).norm().simplify()
# calculate the total charge Q over the distance
lam1 = Q / dr_pdt
# calculate the charge density lamda 
lam = smp.integrate(lam1, (t, 0, 2*smp.pi))
print("charge density = " + str(lam))


integrand = lam * sep/sep.norm()**3 * dr_pdt
dExdt = smp.lambdify([t, x, y, z], integrand[0])
dEydt = smp.lambdify([t, x, y, z], integrand[1])
dEzdt = smp.lambdify([t, x, y, z], integrand[2])
def E(x, y, z):
    return np.array([quad(dExdt, 0, 2*np.pi, args=(x, y, z))[0],
                     quad(dEydt, 0, 2*np.pi, args=(x, y, z))[0],
                     quad(dEzdt, 0, 2*np.pi, args=(x, y, z))[0]])

x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(0, 2*np.pi, 10)
xv, yv, zv = np.meshgrid(x, y, z)

E_field = np.vectorize(E, signature='(),(),()->(n)')(xv, yv, zv)
Ex = E_field[:,:,:,0]
Ey = E_field[:,:,:,1]
Ez = E_field[:,:,:,2]

E_max = 150
Ex[Ex>E_max] = E_max
Ey[Ey>E_max] = E_max
Ez[Ez>E_max] = E_max

Ex[Ex<-E_max] = -E_max
Ey[Ey<-E_max] = -E_max
Ez[Ez<-E_max] = -E_max
tt = np.linspace(0, 2*np.pi, 1000)
lx, ly, lz = np.cos(4*tt), np.sin(4*tt), tt
data = go.Cone(x=xv.ravel(), y=yv.ravel(), z=zv.ravel(),
               u=Ex.ravel(), v=Ey.ravel(), w=Ez.ravel(),
               colorscale='Inferno', colorbar=dict(title='$x^2$'),
               sizemode="scaled", sizeref=0.5)

layout = go.Layout(title=r'Plot Title',
                     scene=dict(xaxis_title=r'x',
                                yaxis_title=r'y',
                                zaxis_title=r'z',
                                aspectratio=dict(x=1, y=1, z=1),
                                camera_eye=dict(x=1.2, y=1.2, z=1.2)))

fig = go.Figure(data = data, layout=layout)
fig.add_scatter3d(x=lx, y=ly, z=lz, mode='lines',
                  line = dict(color='green', width=10))


HTML(fig.to_html(default_width=1000, default_height=600))

fig.show()
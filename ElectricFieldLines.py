from vpython import *
import random

Efl = int(input("Enter the electric field lines:"))
i = 0
shape = int(input("Enter the shape that you want to make: "
                 "1- Sphere"
                 "2- Box "))

if(shape == 1):
    sphere = sphere(vector=(0, 0, 0), color=color.red, radius=20, opacity=0.5)
if(shape == 2):
    square = box(vector=(0, 0, 0), width=20, length=20, height=20, color=color.red, opacity=0.5)

while i < Efl:
    Arrow = arrow(pos=vector(0, 0, 0), color=color.yellow, length=5)
    Arrow.pos = vector(random.randrange(-100, 100, 2), random.randrange(-20, 20, 5), random.randrange(-20, 20, 5))
    i = i+1

while True:
    pass
#! /usr/bin/env python3
"""
Dakota Bosch

Lorenz Equations
"""
from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title


#Lorenz Equations
def fx(x,y):
    return s*(y-x)

def fy(x,y,z):
    return r*x-y-x*z

def fz(x,y,z):
    return x*y-b*z
#constants
s=10
r=28
b=8/3

N=100000
#time interval
ti=0
tf=50
#step size
h=(tf-ti)/N

tpoints = arange(ti,tf,h)
xpoints = []
ypoints =[]
zpoints = []

#initial values
x = 0.0
y= 1.0
z = 0.0

#Runge-Kutta 4th order
for t in tpoints:
    xpoints.append(x)
    ypoints.append(y)
    zpoints.append(z)
    k1 = h*fx(x,y)
    k2 = h*fx(x+0.5*k1,y+0.5*h)
    k3 = h*fx(x+0.5*k2,y+0.5*h)
    k4 = h*fx(x+k3,y+h)
    x += (k1+2*k2+2*k3+k4)/6

    k1 = h*fy(x,y,z)
    k2 = h*fy(x+0.5*k1,y+0.5*h,z)
    k3 = h*fy(x+0.5*k2,y+0.5*h,z)
    k4 = h*fy(x+k3,y+h,z)
    y += (k1+2*k2+2*k3+k4)/6

    k1 = h*fz(x,y,z)
    k2 = h*fz(x+0.5*k1,y+0.5*h,z)
    k3 = h*fz(x+0.5*k2,y+0.5*h,z)
    k4 = h*fz(x+k3,y+h,z)
    z += (k1+2*k2+2*k3+k4)/6



plot(tpoints,ypoints, label = 'y vs t')
legend()
xlabel("z")
ylabel("x")
title("Lorenz Equation")
show()

plot(xpoints,zpoints, label = 'z vs x')
xlabel("z")
ylabel("x")
title("Lorenz Equation")
show()
#! /usr/bin/env python3
"""
Dakota Bosch

Short Spring
"""

import numpy as np
from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title

#dx/dt rabbit population
def fx(x,y):
    return y
#dy/dt fox population
def fy(y,x,t):
    return b*(-y)-A*x**3+B*np.cos(w*t)

#constants
B=7
b=0.01
A=1
w=1
#number of data points
N=1000
#initial and final time
ti=0
tf=25
#calculating step size
h=(tf-ti)/N

tpoints = arange(ti,tf,h)
xpoints = []
ypoints =[]
#initial value for each population
x = 3.0
y= 0.0

#Runge-Kutta 4th order
for t in tpoints:
    xpoints.append(x)
    ypoints.append(y)
    k1 = h*fx(x,y)
    k2 = h*fx(x+0.5*k1,y+0.5*h)
    k3 = h*fx(x+0.5*k2,y+0.5*h)
    k4 = h*fx(x+k3,y+h)
    x += (k1+2*k2+2*k3+k4)/6

    k1 = h*fy(y,x,t)
    k2 = h*fy(y+0.5*k1,x+0.5*h,t)
    k3 = h*fy(y+0.5*k2,x+0.5*h,t)
    k4 = h*fy(y+k3,x+h,t)
    y += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
legend()
xlabel("t")
ylabel("x(t)")
title("Character of a Short Spring")
show()

plot(xpoints,ypoints)
xlabel("x")
ylabel("dx/dt")
title("Character of a Short Spring")
show()
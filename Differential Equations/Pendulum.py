#! /usr/bin/env python3
"""
Dakota Bosch

Nonlinear Pendulum
"""
import numpy as np
from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title
import sys

#dx/dt rabbit population
def fx(x,y):
    return y
#dy/dt fox population
def fy(y,x):
    return -g/L*np.sin(x)

#constants
L=0.1 # pendulum length in m
g = 9.81 #acceleration in m/s^2

#number of data points
N=1000
#initial and final time
ti=0
tf=10
#calculating step size
h=(tf-ti)/N

tpoints = arange(ti,tf,h)
xpoints = []
ypoints =[]
#initial value for each population
x = float(sys.argv[1])
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

    k1 = h*fy(y,x)
    k2 = h*fy(y+0.5*k1,x+0.5*h)
    k3 = h*fy(y+0.5*k2,x+0.5*h)
    k4 = h*fy(y+k3,x+h)
    y += (k1+2*k2+2*k3+k4)/6


plot(tpoints,xpoints)
legend()
xlabel("t")
ylabel("theta")
title("Nonlinear Pendulum")
show()

plot(xpoints,ypoints)
legend()
xlabel("theta")
ylabel("dtheta/dt")
title("Nonlinear Pendulum")
show()
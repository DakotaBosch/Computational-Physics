#! /usr/bin/env python3
"""
Dakota Bosch

Lotka-Volterra equations

solves the interactions between two species over time
"""

from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title

#dx/dt rabbit population
def fx(x,y):
    return a*x-b*x*y
#dy/dt fox population
def fy(y,x):
    return g*x*y-d*y

#constants
a=1
b=0.5
g=0.5
d=2
#number of data points
N=1000
#initial and final time
ti=0
tf=30
#calculating step size
h=(tf-ti)/N

tpoints = arange(ti,tf,h)
xpoints = []
ypoints =[]
#initial value for each population
x = 2.0
y= 2.0

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

plot(tpoints,xpoints, label = 'Bunny')
plot(tpoints,ypoints, label = 'Fox')
legend()
xlabel("t")
ylabel("f(t)")
title("Fox and Rabbit Population")
show()
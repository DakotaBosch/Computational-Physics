#! /usr/bin/env python3
"""
Dakota Bosch

Schrodinger Equation Solutions

using units where hbar/m =1
-0.5 * W" + V * W = E * W

let x = W, y = W'
x' = W' = y
y' = W" = -2*W*(E-V) = -2*x*(E-V)

I.C. for even parity, W(0) = 1, W'(0)=0
=>  x(0) = 1
    y(0) = W'(0) = 0


"""

import numpy as np
from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title

def V(t):
    return np.abs(t)

#even parity solution
def fx(x,y):
    return y
#odd parity solution
def fy(y,x,t):
    return -2*x*(E-V(t))

#initial conditions for a symmetric potential
x = 1
y= 0

E=0.7071067786848986
ti=-4
tf=4
N=10000
xpoints=[]
x2points=[]
h=(tf-ti)/N

tpoints = arange(ti,tf,h)
#Runge-Kutta 4th order
for t in tpoints:
    xpoints.append(x)
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


plot(tpoints,xpoints,label='E=0.706')


x = 1
y= 0.0


E=0.707

#Runge-Kutta 4th order
for t in tpoints:
    x2points.append(x)
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

#plot(tpoints,x2points,label='E=0.707')
legend()
xlabel('x')
ylabel('Wavefunction')
show()
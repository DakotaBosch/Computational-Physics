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

Implements secant method to find E

"""

import numpy as np
from math import sin
from numpy import arange
from pylab import plot, xlabel,ylabel,show,legend,title
import sys

def V(t):
    return t**2

#even parity solution
def fx(x,y):
    return y
#odd parity solution
def fy(y,x,t,E):
    return -2*x*(E-V(t))

#initial conditions for a symmetric potential
#x = 1.0
y = 0.0

E=0.7
ti=0
tf=20
xpoints=[]
ypoints=[]
#Runge-Kutta 4th order
#where x = W and t = x
def Runge(z):
    xpoints=[]
    ypoints=[]
    x=1.0
    y=0.0
    t=0
    E=z
    ti=-20  
    tf=20
    N=100000
    h = (tf-ti)/N
    tpoints = arange(ti,tf+h,h)   
    for t in tpoints:
        xpoints.append(x)
        ypoints.append(y)
        k1 = h*fx(x,y)
        k2 = h*fx(x+0.5*k1,y+0.5*h)
        k3 = h*fx(x+0.5*k2,y+0.5*h)
        k4 = h*fx(x+k3,y+h)
        x += (k1+2*k2+2*k3+k4)/6
        k1 = h*fy(y,x,t,E)
        k2 = h*fy(y+0.5*k1,x+0.5*h,t,E)
        k3 = h*fy(y+0.5*k2,x+0.5*h,t,E)
        k4 = h*fy(y+k3,x+h,t,E)
        y += (k1+2*k2+2*k3+k4)/6
    i = len(xpoints)
    #print(tpoints[i-1],xpoints[i-1])
    return xpoints[i-1]
    

def f(x):
    #print('looking for x = ',x)
    return Runge(x)

def slope(y,x1,x2):    
    return (y(x2)-y(x1))/(x2-x1)



#command line v   
target = 1e-20
xa = float( sys.argv[1] ) 
xb = float( sys.argv[2] )
i=0
#secant method to find roots of wave function
while np.abs( xa-xb ) > target:    
    x = xb - f(xb) / slope(f, xa, xb)    
    xa, xb = xb, x
    i+=1
root=x
print('root =',x, 'total iterations:',i)


#trapezoid approx
def trap(a,b,N,h,root):
    xp=[]
    xpoints=[]
    ypoints=[]
    x=1.0
    y=0.0
    t=0
    E=root
    ti=a
    tf=b
    h = (tf-ti)/N
    tpoints = arange(ti,tf,h)   
    for t in tpoints:
        xp.append(x)
        xpoints.append(x**2)
        ypoints.append(y**2)
        k1 = h*fx(x,y)
        k2 = h*fx(x+0.5*k1,y+0.5*h)
        k3 = h*fx(x+0.5*k2,y+0.5*h)
        k4 = h*fx(x+k3,y+h)
        x += (k1+2*k2+2*k3+k4)/6
        k1 = h*fy(y,x,t,E)
        k2 = h*fy(y+0.5*k1,x+0.5*h,t,E)
        k3 = h*fy(y+0.5*k2,x+0.5*h,t,E)
        k4 = h*fy(y+k3,x+h,t,E)
        y += (k1+2*k2+2*k3+k4)/6

    print(N,len(xpoints))

    s = .5 *(xpoints[0]+xpoints[N-1])

    for k in range(1,N-1):
        s += xpoints[k]
    

    nconst = h*s
    print('Normalization constant=', 1/np.sqrt(nconst))

    for i in range(N):
        xpoints[i]=xpoints[i]/nconst
    plot(tpoints,xpoints)
    title('Normalized Wavefunction')
    xlabel('x')
    ylabel('Wavefunction')
    show()

    print('Expectation=',np.average(xpoints))
    
(trap(-4,4,10000,0,root))


"""
plot(tpoints,xpoints)
xlabel('x')
ylabel('Wavefunction')
show()
"""
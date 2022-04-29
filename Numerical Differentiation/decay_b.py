#! /usr/bin/env python3
"""
Dakota Bosch

Radioactive Decays Part B
"""

import numpy as np
from matplotlib.pylab import plot,show,xlabel,ylabel,title,legend
from decay import N,analytic

N0=100      #initial number (fraction)
h=0.01      #step size


n=int(16/h)     #total number of slices
x=[0]*(n)
y=[0]*(n)
z=[0]*(n)
e=[0]*(n)
x=np.linspace(0,15,int(n))
r = len(x)

T = [5,3,1,.1,.01]
for j in range(0,5):
    for i in range(r):
        y[i] = -(N(x[i]+h,T[j],N0)-N(x[i],T[j],N0))*T[j]/h #numerical solution
        z[i] = -T[j]*analytic(x[i])        #analytic solution  
        e[i] = (z[i]-y[i]) / z[i]       #%error of numerical soln
    
    y[0]=N0            
    plot(x,y,label=("T=",T[j]))
title('Numerical Solution With Varying T')
legend()
xlabel("Time (s)")
ylabel("N")
show()
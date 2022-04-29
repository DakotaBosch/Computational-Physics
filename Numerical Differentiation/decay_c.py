#! /usr/bin/env python3
"""
Dakota Bosch

Radioactive Decays Part C
"""

import numpy as np
from matplotlib.pylab import plot,show,legend,xlabel,ylabel
from decay import N,analytic

N0=100      #initial number (fraction)
h=0.01      #step size


n=int(16/h)     #total number of slices
x=[0]*(n)
y=[0]*(n)
z=[0]*(n)
e=[0]*(n)
w=[0]*n
x=np.linspace(0,15,int(n))
r = len(x)

T=2

for i in range(r):
    y[i] = -(N(x[i]+h,T,N0)-N(x[i],T,N0))*T/h #parent soln
    z[i] = -T*analytic(x[i])        #analytic solution  
    e[i] = (z[i]-y[i]) / z[i]       #%error of numerical soln

#plot(x,z,label=('Analytic'))  
plot(x,y,label=('Parent w/ T=',T))

N0=0
T= [200,2,.02]
for j in range(0,3):
    for i in range(r):
        w[i] = -T[j]*((N(x[i]+h,T[j],N0)-N(x[i],T[j],N0))/h-y[i]/2)      #daughter soln
    w[0]=N0
    plot(x,w,label=('Daughter w/ T=',T[j]))


legend()
xlabel("Time (s)")
ylabel("N")
show()

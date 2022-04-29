#! /usr/bin/env python3
"""
Dakota Bosch

Radioactive Decays
"""

import numpy as np
from matplotlib.pylab import plot,show,xlabel,ylabel,title,legend

N0=100      #initial number (fraction)
T=2         #seconds


def N(t,T,N0):     #function 
    return N0*np.exp(-t/T)
def analytic(t):    #analytic function
    return N0*(-1.0/T)*np.exp(-t/T)


if __name__ == "__main__": 
    h=[1,0.1,0.01]      #step size
    for j in range(0,3):
        n=int(16/h[j])     #total number of slices
        x=[0]*(n)
        y=[0]*(n)
        z=[0]*(n)
        e=[0]*(n)
        x=np.linspace(0,15,int(n))
        r = len(x)

        for i in range(r):
            y[i] = -(N(x[i]+h[j],T,N0)-N(x[i],T,N0))*T/h[j] #numerical solution
            z[i] = -T*analytic(x[i])        #analytic solution  
            e[i] = (z[i]-y[i]) / z[i]       #%error of numerical soln
        
        title('Numerical and Analytic differentiation')
        #plot(x,e,label=('Step Size',h[j])) 

        plot(x,y,label=("Step Size:",h[j]))
    plot(x,z,label=("Analytic"))

    xlabel("Time (s)")
    ylabel("Number")
    legend()
    show()

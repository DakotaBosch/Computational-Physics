#! /usr/bin/env python3
"""
Dakota Bosch

Differential calculator

Creates class with init and call constructors
Uses central difference to calculate the derivative of a give function f(x)
"""

import numpy as np
from matplotlib.pylab import *

#derivative class
class der(object):
    """
    blueprint for 
    """
    def __init__(self, f):  #constructor that assigns step size h and function f
        self.h = 1e-8
        self.f=f
    def __call__(self,x):   #constructor that returns the numerical derivative at x
        return (self.f(x+self.h/2)-self.f(x-self.h/2))/self.h



def main():
    def f(x):
        return 1+ .5*np.tanh(2*x) 

    #defines analytic derivative of f(x)
    def analytic(x):
        return 1.0/(np.cosh(2*x))**2

    num = der(f)    #creates object of calls type der
    
    n=100   #number of slices
    x= np.linspace(-2,2,n)  #x range
    y=[0]*n
    z=[0]*(n-1)

    #loop to solve using central difference
    for i in range(0,n):
        y[i]=num(x[i])

    plot(x,y, 'bs',label='Numerical Soln')
    x= np.linspace(-2,2,n-1)  #x range

    #loop to solve using analytic derivative
    for i in range(0,n-1):
        z[i]=analytic(x[i])

    plot(x,z,'g^',label='Analytic Soln')
    title('Derivative of 1+.5*tanh(2x)')
    xlabel('X')
    ylabel('Y')
    legend()
    show()

if __name__ == '__main__':
    main()

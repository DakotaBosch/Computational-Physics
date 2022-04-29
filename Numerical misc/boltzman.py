#! /usr/bin/env/ python3

"""
Dakota Bosch
Exam 1, Question 4

Evaluates the total energy per unit area radiated by a black body
Also calculates the Stefan-Boltzmann constant
"""
import numpy as np
from matplotlib.pylab import plot,show
from int import monte,simp
import math

"""
using the substitution z = x / (x+3), where x=3 is near the maximum
dz = dx*3/(x+3)^2
x = 3z/(1-z)

also using the substitution x^3 = e^(3lnx) to avoid overflow 
and (x+3)**2 = e^(2ln(x+3))
and using taylor series expansion of e^x
"""


def f(z):
    x=3*z/(1-z)
    t=0
    for j in range(0,30):
        t += x**j/math.factorial(j)
    return np.exp(3*np.log(x)+2*np.log(x+3))/(t-1)/3


result = monte(f,0,1,10000,1)
print('The evaluated integrand is', '%.3f' % result)

k=1.38064852e-23 #boltzmann const in units of m^2*kg*s^-2*K^-2
c=299792458      #speed of light in m/s
h=1.0545718e-34  # hbar in m^2*kg/s

sigma = result*k**4/(4*np.pi**2*c**2*h**3)
print ('The Stefan-Boltzmann constant is','%.3E' % sigma, 'in units of W*m^-2*K^-4')
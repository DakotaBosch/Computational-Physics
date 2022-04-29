#! /usr/bin/env python3
"""
Dakota Bosch

"""
import numpy as np
import scipy.constants as sc
import sys

M = 5.974e24    #mass of sun in kg
m = 7.348e22    #mass of moon in kg
R = 3.844e8     #distance between earth and moon in m
w= 2.662e-6       #angular speed of moon/L1 in s^-1
def f(x):    
    return sc.G*M/x**2-sc.G*m/(R-x)**2 - w**2*x

def dfdx(x):    
    return -2*sc.G*M/x**3-2*sc.G*m/(R-x)**3 - w**2

target = 1e-10
x = float( sys.argv[1] )
xlast = float("inf")

while np.abs(x - xlast) > target:    
    xlast = x    
    x = xlast - f(xlast)/dfdx(xlast)
print("Distance from Earth to L1:", '%.4E' % x, 'm')
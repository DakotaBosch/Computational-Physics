#! /usr/bin/env python3
"""
Dakota Bosch

Wien's Displacement Constant
"""
import numpy as np
import scipy.constants as sc
import sys

def f(x):
    return 5*np.exp(-x)+x-5

#define error target and use command line arguments for range
target = 1e-6
xa = float(sys.argv[1])
xb = float(sys.argv[2])

#binary search method
while np.abs(xa-xb)> target:
    x = (xa+xb)/2
    if f(x)*f(xa) > 0:
        xa=x
    else:
        xb=x

b = sc.h*sc.c/sc.k/x    #Wien displacement constant
print("Wein's Constant: ", '%.05E' % b)

lam = 502*1e-9  #wavelength of suns emitted radiation in m
T = b / lam     #equation for temp
print("Sun's Temperature: ", '%.02f' % T, 'K')
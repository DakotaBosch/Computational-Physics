#! /usr/bin/env python3
"""
Dakota Bosch

"""
import numpy as np
import sys

def f(x):
    return np.tan(x)-np.sin(x)-m*g/2/k/L0

def df(x):
    return 1/np.cos(x)**2-np.cos(x)

def slope(y,x1,x2):    
    return (y(x2)-y(x1))/(x2-x1)

m = 5   #mass in kg
L0 = 0.3 #half the distance between the two supports and spring rest length (meters)
k = 1000 #spring constant in N/m
g = 9.81 #gravitational acceleration in m/s^2
target = 1e-10   #define error target
xa = float(sys.argv[1])
xb = float(sys.argv[2])
xc = float(sys.argv[3])

#binary search method
def bisec(target,xa,xb):   
    counter=0 
    while np.abs(xa-xb)> target:
        x = (xa+xb)/2
        if f(x)*f(xa) > 0:
            xa=x
        else:
            xb=x
        counter+=1
    return ['%.2f' % x,counter]
    
#secant method
def secant(target,xa,xb):
    counter=0 
    while np.abs( xa-xb ) > target:    
        x = xb - f(xb) / slope(f, xa, xb)    
        xa, xb = xb, x  
        counter+=1
    return ['%.2f' % x,counter]  

def newton(target,x):
    xlast = float("inf")
    counter = 0
    while np.abs(x - xlast) > target:    
        xlast = x    
        x = xlast - f(xlast)/df(xlast)
        counter+=1
    return ['%.2f' % x,counter]

def false(target,xa,xb):
    xInt,xIntOld = xa,float("inf")
    counter = 0
    while np.abs(xInt - xIntOld) > target:    
        xIntOld = xInt    
        m = (f(xb) - f(xa)) / (xb - xa)    
        yInt = f(xa) - m*xa    
        xInt = -yInt/m    
        if f(xInt)*f(xa) > 0:        
            xa = xInt    
        else:        
            xb = xInt
        counter +=1
    return ['%.2f' % xInt,counter]

print("newton",newton(target,xc))
print("secant",secant(target,xa,xb))
print("bisection",bisec(target,xa,xb))
print("false",false(target,xa,xb))
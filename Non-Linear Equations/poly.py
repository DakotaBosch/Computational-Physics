#! /usr/bin/env python3
"""
Dakota Bosch

"""
import numpy as np
import sys
from matplotlib.pylab import plot,show,xlabel,ylabel,title

def f(x):  
    sum=0 
    for i in range(n+1):
        sum += F[i]*x**i
    return sum

def df(x):  
    sum=0 
    for i in range(n):
        sum += dF[i]*x**i
    return sum

print("Hello user, Welcome to polynomial root finder")


F = []
dF = [] 
temps = str()  
dtemps = str()

#highest order of x
n = int(input("What is the highest power of x? ")) 

print("input the coefficients of the polynomial in ascending order, starting with x^0") 
# iterating till x^n
for i in range(n+1): 
    temp = int(input()) 
    F.append(temp)
    temps = temps + str(temp) + "*x^" + str(i) + " + "


print("input the coefficients of the derivative of the polynomial in the same format") 
# iterating till x^n
for i in range(n): 
    temp = int(input()) 
    dF.append(temp)
    dtemps = dtemps + str(temp) + "*x^" + str(i) + " + "

print (F,dF, n,temps[:-2], dtemps[:-2])


print("Please input a plotting range\n")
a = float(input("lower bound? "))
b = float(input ("upper bound? "))

N=100
X = np.linspace(a,b,N)

y=[]

for i in range(len(X)):
    y.append(f(X[i]))


plot(X,y)
xlabel("x")
ylabel("f(x)")
show()

switch = 'y'

while switch == 'y' :
    temp = input("Please give an initial value ")

    target = 1e-5
    x = float( temp )
    xlast = float("inf")

    while np.abs(x - xlast) > target:    
        xlast = x    
        x = xlast - f(xlast)/df(xlast)

    print('%.10f' % x)
    show()
    temp = input("Continue finding more roots?(y or n) ")
    switch = temp



"""
a = np.array([1,-42,420,-1680,3150,-2772,924])
b = np.array([2,2,-4])
print(np.roots(a))
print(np.roots(b))
"""
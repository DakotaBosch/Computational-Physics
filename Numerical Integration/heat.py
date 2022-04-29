"""
Dakota Bosch 2/3/20

Heat capacity of a solid
"""


#! /usr/bin/env python3

import numpy as np
from gaussxw import gaussxw
import matplotlib
import matplotlib.pyplot as plt

#function inside integral of heat capacity equation
def f(x):
    return x**4+np.exp(x)/(np.exp(x)-1)**2

#full definition of the heat capacity equation
def cv(T):       #heat capacity of a solid @ T w/ volume 1e9cm
    V = 10**3
    d = 6.022e28   #number density (m^-3)
    D = 428     #Debye temp (K)
    N = 50      #sample number
    k = 1.38064852e-23  #Boltzman SI
    a=0
    b= D/T
    x,w = gaussxw(N)	#calling gaussian quadrature program
    xp = .5*(b-a)*x+.5*(b+a)
    wp = .5*(b-a)*w

    s= 0.0
    for k in range(N):
        s+=wp[k]*f(xp[k])
    
    y= (9*V*d*k*(T**3)/(D**3)*s)
    print (y)
    return y

t = [0]*495
c = [0]*495

#storing data for temp & heat capacity in arrays
for i in range(5,500):
    j = i-5
    t[j] = i
    c[j] = cv(i)


#plotting temp v heat capacity
fig, ax = plt.subplots()
ax.set(xlabel='Temp(K)', ylabel='Heat capacity',
       title='Heat Capacity of a Solid')
ax.plot(t,c)
plt.show()

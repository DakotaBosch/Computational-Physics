#! usr/bin/env python3
"""
Dakota Bosch 2/18/20

Sun photon using brownie
"""
import numpy as np
from numpy import random
from matplotlib.pylab import plot,show,ylim,xlim
from brownie import brownie

p=1000
n=100000
k= 10000

S = 0
X=Y=0


#calls brownie function p times(# of particles)
for j in range(0,p):
    x,y = brownie(n,k)
    X += x[n-1]
    Y += y[n-1]
    S += (x[n-1]**2+y[n-1]**2)
    

print('Mean Distance Squared:', S/p,'cm', '\nAverage distance', int((X**2+Y**2)**(1.0/2))/p,'cm')

plot(x,y)
ylim(-k/10,k/10)
xlim(-k/10,k/10)
show()

#! /usr/bin/env python3
"""
Dakota Bosch

Gamma Function
"""

from matplotlib.pylab import plot,show
import numpy as np
from int import monte
import math 

if __name__ == "__main__":

    for a in range (2,5):
        i=[0]*6
        j=[0]*6
        for x in range(0,6):
            i[x]=x
            j[x]= x**(a-1)*np.exp(-x)
        plot(i,j)
    #show()

    def gamma(z):
        x=z*(a[i]-1)/(1-z)
        e=(a[i]-1)*np.log(x)
        q=(a[i]-1)*np.exp(e)*np.exp(-x)/(1-z)**2    
        return q
    
    a=[3,6,10]
    for i in range(0,3):
            print('%.03f' % monte(gamma,0,1,20000,1))
            print(math.factorial(a[i]-1))
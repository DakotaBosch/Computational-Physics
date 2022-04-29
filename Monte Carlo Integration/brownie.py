#! usr/bin/env python3
"""
Dakota Bosch 2/18/20

Brownie 
"""
import numpy as np
from numpy import random
from matplotlib.pylab import plot,show,ylim,xlim

def brownie(n,b):
    k= b/2

    d = 0
    S = 0
    x = [0]*n
    y = [0]*n
    #Loop for each step
    for i in range(1,n):
        #copies position from previous element of array                                                                                                                                               
        x[i] = x[i-1]
        y[i] = y[i-1]

        #randomizes direction and moves in corresponding direction                                                                                                                                    
        d = np.random.randint(4)
        if d == 0:
            y[i] += 1
        elif d ==1:
            x[i] += 1
        elif d == 2:
            y[i] -= 1
        else:
            x[i] -= 1

        #checks that particle stays within 101x101 region, otherwise subtracts and restarts iteration of i                                                                                            
        if abs(y[i]) == k or abs(x[i]) == k:
            if y[i] == k:
                y[i] -= 1
            elif y[i] == -k:
                y[i] +=1
            elif x[i] == k:
                x[i] -=1
            else:
                x[i] += 1
                
            i-=1
    return x,y

if __name__ == "__main__":
    for c in range(0,5):
        x,y = brownie(2000,100)   
        plot(x,y)
        ylim(-50,50)
        xlim(-50,50)
        show()


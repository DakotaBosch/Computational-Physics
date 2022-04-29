#! usr/bin/env python3
"""
Dakota Bosch 2/18/20

Dice
"""

import numpy as np
from numpy import random

j=l=0
k=1000000

print('\n~~ LETS ROLL SOME DICE ~~\n')
#rolls 2 dice 1million times and stores into arrays d1,d2
d1 = np.random.randint(1,7,k)
d2 = np.random.randint(1,7,k)
for i in range(0,1000000):
    #prints the dice rolls until the first occurance of two 6
    if l ==0:
        print(d1[i],d2[i])
    #uses j as a counter for each time two sixes are rolled, l acts as an off switch for stopping the print of the dice after the first double six is rolled
    if d1[i]+d2[i] == 12:
        j+=1
        l+=1 

print('Total Dice Rolls: ', k, '\nNumber of Double 6: ',j)
print ('Double 6 had a frequency of ', "%.2f%%" % (100*j/k))
print('Average number of throws per double 6: ', "%.1f" % (k/j))

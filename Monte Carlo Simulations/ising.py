#! /usr/bin/env python3
"""
 ising.py is a program which performs an MCMC calculation
 of the 2D Ising model. Monte carlo simulations are used
 Plotting function and specific heat calculation included

 Dakota Bosch
 PHZ4151C
 20 March 2020
"""

from math import exp
import numpy as np
from random import random,randrange,randint
import datetime
from matplotlib.pyplot import plot,show,xlabel,ylabel,title

# constants
L = 20       # lattice size, LxL
N = 1000000  # number of MC steps
J = 1.0      # interaction strength
T = 3.0      # temperature factor, actually k_B*T
M=0


def energy(s):
	"""calculates total energy of spins on lattice based on
       nearest-neighbor interactions"""
	return -J*(np.sum(s[0:L-1,:]*s[1:L,:]) + np.sum(s[:,0:L-1]*s[:,1:L]) )
	
	
## initialize lattice with random spins
s = np.empty([L,L],int)
for i in range(L):
	for j in range(L):
		if random() < 0.5:
			s[i,j] = +1
		else:
			s[i,j] = -1

# initialize some values
E = energy(s)
M = np.sum(s)
print("Initial lattice energy = %6.2f and magnetization = %d"%(float(E),int(M)))


#arrays for plotting
x =[]
y=[]
#initializing time before monte carlo begins
ti = 0
t=datetime.datetime.now()
ti = t.second*1000 + t.microsecond/1000
e=[]

#monte carlo style runs of individually flipping one spin
for i in range(200000):
	a = randint(0,L-1)
	b = randint(0,L-1)
	Ei = energy(s)
	s[a,b] = s[a,b]*-1	#flipping the spin
	Ef = energy(s)
	#Metropolis acceptance formula
	if Ef > Ei:
		if random() > np.exp(-1/T*(Ef-Ei)):
			s[a,b] = s[a,b]*-1
	
	M=np.sum(s)
	t=datetime.datetime.now()
	x.append((t.second*1000 + t.microsecond/1000-ti))#time array
	y.append(M)	#magnetization array
	e.append(energy(s))	#array of energies over all changes

plot(x,y)
xlabel('Time(ms)')
ylabel('Total Magnetization')	
title('Magnetization vs time')
show()

#specific heat
C = 1/T**2*np.var(e)
print ('The specific heat is ',C)

		

## Run some Monte Carlo!


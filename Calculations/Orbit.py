"""
v2^2 - 2GMv2/(v1l1) - (v1^2 -2GM/l1) = 0        #Quadratic equation
v2 = ((2*G*M/v1/l1) -((2*G*M/v1/l1)**2+4*(v1**2-2*G*M/l1) )**(1.0/2))  /2   #smaller root

((2*G*M/v1/l1) -((2*G*M/v1/l1)**2+4*(v1**2-2*G*M/l1) )**(1.0/2))**2/2 - 2GM(((2*G*M/v1/l1) -((2*G*M/v1/l1)**2+4*(v1**2-2*G*M/l1) )**(1.0/2))/2)/(v1l1) -(v1^2 -2GM/l1) = 0  #plugging smaller root into quadratic 

0 = 0 # wow simplification


"""

import numpy as np

G = 6.6738e-11       #gravitational constant
M = 1.9891e30       #mass of sun in kg

temp = input("Hello bruv, please enter the distance to the sun at the perhilion:")
l1 = float(temp)
temp = input('Now enter the corresponding velocity:')
v1 = float(temp)

v2 = ((2*G*M/v1/l1) -((2*G*M/v1/l1)**2+4*(v1**2-2*G*M/l1) )**(1.0/2))  /2

l2 = l1*v1/v2
a = (1.0/2)*(l1 + l2)
b = (l1*l2)**(1.0/2)
T = 2*np.pi*a*b/l1/v1
e = (l2-l1)/(l2+l1)

y = T/365/3600/24

print('Semi-major axis(m):' , '{:.2e}'.format(a), 'Semi-minor axis(m):','{:.2e}'.format(b),'Orbital period(yrs):','{:.3}'.format(y),'Orbital eccentricity:','{:.4}'.format(e))

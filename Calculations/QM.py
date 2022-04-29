import numpy as np
from scipy import constants

m = 9.11e-31
E=10 
V=9
J = 1.602176565e-19            #conversion from EV to J
E=E*J
V=V*J


k1= (2*m*E)**(1.0/2)/constants.hbar

k2 = (2*m*(E-V))**(1.0/2) / constants.hbar


T = 4*k1*k2/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print('The probability for transmission is', '%.2f' % T,'and the probability for reflection is','%.2f' % R)


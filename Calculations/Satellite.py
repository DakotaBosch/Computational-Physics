import numpy as np

G = 6.67e-11       #gravitational constant
M = 5.97e24        #mass of earth in kg
R = 6.371e6        #radius of earth in m

temp = input('Hello user, please enter a desired period in seconds:')
t = int(temp)

h = (G*M*t**2 / (4*np.pi**2))**(1.0/3) - R
print('The desired altitude of a satellite with period',t,'seconds is :','{:.2e}'.format(h), 'meters')


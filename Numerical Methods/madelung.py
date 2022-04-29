import numpy as np
from scipy import constants as cs

a = 0.563e-9
l=0
s=0
M=0

temp = input('Hello user, give me an L value: ')
l = int(temp)
for i in range (-l,l+1):
    for j in range (-l,l+1):
        for k in range(-l,l+1):
            if (i==j==k==0):
                M=M
            elif (i+j+k)%2 == 0:
                M += 1.0/(i**2 +j**2+k**2)**(1.0/2)
            else:
                M -= 1.0/(i**2 +j**2+k**2)**(1.0/2)

#v = cs.elementary_charge / (4*np.pi*cs.epsilon_0*a*s)
#m = v*4*np.pi*cs.epsilon_0*a/ cs.elementary_charge

print('The calculated Madelung constant is: ' "%.5f" % abs(M))
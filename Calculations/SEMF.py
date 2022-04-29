a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

temp = input('Hello Welcome to the Semi-Emperical Mass Formula, please enter an atomic number:')
Z = int(temp)
temp = input('Now enter the mass number:')
A = int(temp)

if A - Z == 0:
    a5 = 0
elif A - Z & 2 ==0:
    a5 = 12
else:
    a5 = -12


B = a1*A - a2*A**(2.0/3)-a3*Z**2/A**(1.0/3)-a4*(A-2*Z)**2/A + a5/A**(1.0/2)
n = B/A

print('The binding energy is:','%.2f' % B, 'MeV', 'The binding energy per nucleon is;','%.2f' % n)
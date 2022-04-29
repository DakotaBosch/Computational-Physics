#! usr/bin/env python3
"""
Dakota Bosch 2/3/20

Gaussian error function
"""



import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = 0
b = 3
h = 0.1
N = int((b-a)/h)
s=0

#function for integration
def f(x):
    return np.exp(-1*(x**2))

#using trap rule to approx integral
s = .5 *(f(a) + f(b))

x = [0]*50
y = [0]*50
for k in range(0,N):
    print(f(a+k*h))
    s+= f(a+k*h)
print(h*s)

#solving for E(x) over (0,100)

h = .01
for q in range(0,50,1):
    N = int(( (q/10)-a)/h)
    s=0
    for k in range(0,N):
        s+= f(a+k*h)

    l = .5*(f(a)+f(q/10))
    print(N, s,l)
    x[q]=q/10
    y[q]= h*(l+s)


fig, ax = plt.subplots()
ax.set(title='E(x)')
ax.plot(x,y)
plt.show()
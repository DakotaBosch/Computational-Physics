#! /usr/bin/env/ python3

"""
Dakota Bosch
Exam 1, Question 3

Function H(n,x) calculates any hermite polynomial
program then plots the wave function vs x for desired range of n
"""
import numpy as np
import math
from matplotlib.pyplot import plot,show,legend,title,xlabel,ylabel,figure
from gaussxw import gaussxwab
#takes in n and returns evaluated hermite polynomial at x
def H(n,x):
    h =[1,2*x]
    for i in range(0,n-1):
        h.append(2*x*h[i+1] - 2*(i+1)*h[i])
    return h[n]

n=3
x=4
k=200  #number of steps to evaluate
X=np.linspace(-4,4,k)

for i in range(0,n+1):  #loop to evaluate multiple hermite polynomials
    h=[]
    wave=[]
    for j in range(0,k): #loop to evaluate hermite polynomials and wave function over x 
        h.append(H(i,X[j]))
        wave.append(h[j]/(2**n*math.factorial(n)*np.pi**.5)**.5*np.exp(-(X[j])**2/2)) 
    plot(X,wave,label=('n=',i))

legend()
title('Wave Function vs x')
xlabel('x')
ylabel('Wave Function')


## part B, makes a plot of wavefunction w/ n=30 with x range (-10,10)
figure(2)
n=30
x=10
h=[]
wave=[]
X=np.linspace(-10,10,k)

for j in range(0,k): #loop to evaluate hermite polynomials and wave function over x 
    h.append(H(n,X[j]))
    wave.append(h[j]/(2**n*math.factorial(n)*np.pi**.5)**.5*np.exp(-(X[j])**2/2))
   
plot(X,wave,label=('n=',n))
legend()
title('Wave Function vs x')
xlabel('x')
ylabel('Wave Function')
show()





#evaluates quantum uncertainty at n=5 using 100 points
#using substitutions x=tanz, dx= dz/cosz^2
#or z=x/(1+x), x=z/(1-z), dx = dz/(1-z)^2
a=0
b=1
n=5
s=0.0
h=0
y,w = gaussxwab(100,a,b)	#calling gaussian quadrature program

def f(z):
    x=z/(1-z)
    h=(H(n,x))
    wave = h/ (2**n*math.factorial(n)*np.pi**.5)**.5 *np.exp(-(x)**2/2)
    return x**2 * wave**2 / (1-z)**2

for k in range(100):
    s+=w[k]*f(y[k])

print(np.sqrt(s*2))
#! /usr/bin/env python3
"""
Dakota Bosch

Integration module
monte carlo, trapezoid, simpsons, adaptive trapezoid, adaptive simpsons

Parameters:
f = function
a = lower bound
b = upper bound
N = number of slices
d = dimensions
h = slice size
"""

import math
import random

def monte(f,a,b,N,d,h=0):
    N=N*100   #sets number of simulations
    v=0       #sum over all simulations 
    for i in range(0,N):    #each loop is a simulation
        x = random.uniform(a,b) 
        v += f(x)   #sums all sims
    return (b-a)**d*v/N 
   

#trapezoidal integration with f=function,a=starting point,b=endpoint,Nslices,h=width of slices
def trap(f,a,b,N=0,h=0):
    if h == 0:  #initializes slice size if not passed in
        h = (b-a)/N
    if N == 0:  #initializes slice count if not passed in
        N = (b-a)/h
    s = .5 *(f(a)+f(b))

    for k in range(0,N):
        s += f(a+k*h)

    return(h*s)

#simpson integration with f=function,a=starting point,b=endpoint,Nslices,h=width of slices       
def simp(f,a,b,N,h=0):
    if h == 0:  #initializes slice size if not passed in
        h = (b-a)/N 
    if N == 0:  #initializes slice count if not passed in
        N = (b-a)/h
    s = (f(a)+f(b))

    for k in range(1,N):
        if k % 2 == 0:
            s+= 2*f(a+k*h)
        else:
            s+= 4*f(a+k*h)

    return(h*s*(1.0/3))

#adap trap integration w/ f=function,a=starting point,b=endpoint,Nslices,h=width of slices
def atrap(f,a,b,N,h=0):
    if h == 0:
        h = (b-a)/N #initializes slice size if not passed in
    i=1
    j=0
    #compute first step of approximation
    I = [0]*N
    I[j] = (h*(.5*(f(a)+f(b))))

    #loop to iterate approximation until desired error is reached
    while i < (N/2):
        j+=1
        i=2*i  #doubles each loop, the pattern of adaptive integration
        s=0    
        h=(b-a)/i
        for k in range (1,i,2):
            s += h*f(a+k*h)    #series sum for adaptive intergration
    
        I[j] = .5*I[j-1] + s   #the final adaptive step

        #e = (1.0/3*(I[i]-I[i-1]))   #error on the ith step
        #print('Number of slices = ',N,' error = ',"%.02E" % abs(e),' I = ',"%.04f" % I[i])
    return I[j]


def asimp(f,a,b,N,h=0):
    if h == 0:  #initializes slice size if not passed in
        h = (b-a)/N
    i=1
    j=0
    t=0
    S= [0]*N
    S[j] = ( (1.0/6) * (f(a)+f(b)+4*f(a+0.5)) )
    #print(S[j])

    #loop to iterate approximation until desired error is reached
    while i < (N/2):
        j+=1
        i=2*i   #doubles each loop, the pattern of adaptive integration
        h=(b-a)/i   
        t=0
        for k in range (1,i,2):
            t -= (h*1.0/3*f(a+k*h)) #series sum component w/ odd K
            q=0
            for p in range(0,i):
                q += (h*2.0/3*f(a+h*(p+.5)))  #series sum component
            S[j] = .5*S[j-1]+t+q    #adaptive integration sum
            #es = (1.0/15*(S[i]-S[i-1])) #simpsons rule error   
    return S[j]                                       
    
if __name__ == "__main__":  
    def f(x):   #function to integrate
        return x**3+x-1
    a=0     #lower bound   
    b=2     #upperbound
    N=1000  #number of slices
    d=1     #dimensions
    print('trap: ',trap(f,a,b,N))
    print("simp: ", simp(f,a,b,N))
    print("atrap: ", atrap(f,a,b,N))
    print("asimp: ", asimp(f,a,b,N))
    print("monte: ", monte(f,a,b,N,d))

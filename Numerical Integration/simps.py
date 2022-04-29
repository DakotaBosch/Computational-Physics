#! /usr/bin/env python3
"""
Dakota Bosch 2/3/20

Simpson's approx
"""

#function defintion
def f(x):
    return x**4 -2*x +1

#trapezoid approx
def trap(a,b,N,h):
    if h == 0:
        h = (b-a)/N
    if N == 0:
        N = (b-a)/h
    s = .5 *(f(a)+f(b))

    for k in range(0,N):
        s += f(a+k*h)
    
    return(h*s)

#simpsons approx
def simp(a,b,N,h):
    if h == 0:
        h = (b-a)/N
    if N == 0:
        N = (b-a)/h
    s = (f(a)+f(b))

    for k in range(1,N):
        if k % 2 == 0:
            s+= 2*f(a+k*h)
        else:
            s+= 4*f(a+k*h)
    
    return(h*s*(1.0/3))

#running function for steps of 10,100,1000
if __name__ == "__main__":
    print('Slices = 10, I = ', simp(0.0,2.0,10,0))
    print('Slices = 100, I = ',simp(0.0,2.0,1000,0))
    print('Slices = 1000, I = ',simp(0.0,2.0,1000,0))


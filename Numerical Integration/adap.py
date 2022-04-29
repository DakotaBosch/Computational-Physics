#! usr/bin/env python3
"""
Dakota Bosch
2/10/20
Adaptive Integration, Trapezoidal and Simpsons method
"""
import math

N=es=e=h=1
a=i=0
b=1.0

def f(x):
    y = math.sin((100*x)**(1.0/2))**2
    return y


print(' ~~Trapezoidal Adaptive Integration~~ \n\n')

#compute first step of approximation
I = [0]*100
I[i] = (h*(.5*(f(a)+f(b))))

#loop to iterate approximation until desired error is reached
while abs(e) > 10e-6:
    i+=1
    N=2*N  #intervals doubling each iteration
    s=0    
    h=(b-a)/N
    for k in range (1,N,2):
        s += h*f(a+k*h)    #series sum for adaptive intergration
    
    I[i] = .5*I[i-1] + s   #the final adaptive step

    e = (1.0/3*(I[i]-I[i-1]))   #error on the ith step
    print('Number of slices = ',N,' error = ',"%.02E" % abs(e),' I = ',"%.04f" % I[i])


print('\n\n ~~Simpsons Adaptive Integration~~ \n\n')

#compute first step of approximation
i=t=0
S= [0]*50
S[i] = ( (1.0/6) * (f(a)+f(b)+4*f(a+0.5)) )
print(S[i])
# (w/6.0) * (f(a) + f(b) + 4*(a + w*(k+(1/2) ) ) )

#loop to iterate approximation until desired error is reached
N=1
while abs(es) > 10e-6:
    i+=1
    N=2*N
    h=(b-a)/N
    t=q=0
    for k in range (1,N,2):
        t -= (h*1.0/3*f(a+k*h)) #series sum component w/ odd K
    for p in range(0,N):
        q += (h*2.0/3*f(a+h*(p+.5)))  #series sum component
    #s[i] = s[i-1] + t
    S[i] = .5*S[i-1]+t+q    #adaptive integration sum
    es = (1.0/15*(S[i]-S[i-1])) #simpsons rule error                                          
    print('Number of slices = ',N,' error = ',"%.02E" % abs(es),' I = ',"%.04f" % S[i])





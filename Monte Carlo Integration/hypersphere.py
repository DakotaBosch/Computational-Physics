#! usr/bin/env python3
"""
Dakota Bosch 2/19/20

Hypersphere
"""



from matplotlib.pyplot import plot,show,title,xlabel,ylabel
import random
import numpy as np

#function to calculate the volume with parameters steps and dimensions
def montesphere(N,d):
   if d < 2:
      return d+1
   s=0
   q=0
   i=0
   x=[0]*d
   while i < N+1 :
      v=0
      for j in range(0,d):
         x[j] = random.uniform(-1,1)
         v += x[j]**2
      if v < 1 or v ==1:
         s += 1
      i+=1
   return s/N

if __name__ == "__main__":            
   #calls upon montesphere for dimensions 0-12
   d=12
   N=1000000
   I = [0]*(d+1)
   z= np.linspace(0,d,d+1)
   for k in range(0,d+1):
      I[k]= montesphere(N,k)*2**d
      print('A',k,'Dimension Unit Circle has volume','%0.3f' % I[k])

   plot(z,I)
   title('Volume of N Dimension Unit Circle')
   xlabel('Dimensions')
   ylabel('Volume')
   show()

   #Error Calculation
   q=np.linspace(20000,1000000,50) #creates array for N
   I = [0]*50
   for t in range(0,50):
      f= montesphere(int(q[t]),10)
      I[t] = (f/int(q[t])-f**2)**(1.0/2) #error formula
      print(t)
   plot(q,I)
   title('Error of N trails')
   xlabel('N')
   ylabel('Error')
   show()

#! /usr/bin/env/ python3
"""
Dakota Bosch
Exam 1, Question 2

Program efficiently checks for prime number up to n
"""
prime =[2]  #array to store prime numbers, starts with first prime
i=3
n=10000  #range of numbers to check
while i<n+1: #loop to check each number up to n
    j=0
    s=0 #switch variable
    while prime[j] <= i**.5 and s==0:   #only tests prime factors up to sqrt(n)
        if i%prime[j]==0:   #switches s if number is divisible
            s=1 
        j+=1
    if s==0:    #if number was never divisible then add to string
        prime.append(i)
    i+=1
print(prime)


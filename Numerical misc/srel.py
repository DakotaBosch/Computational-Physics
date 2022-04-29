#! /usr/bin/env python3
"""
Dakota Bosch
Exam 1, Question 1
"""

x = float(input("Hello buddy, we're going camping...\n\nHow many light years away is our camp ground? "))
v = float(input("\nHow fast should we drive? (enter speed as a fraction of the speed of light) "))
c=299792458           #speed of light m/s
gamma = 1.0 / (1-v**2)**.5  #gamma where v is in units of fraction of speed of light
t1=x/v         #time 
t2=gamma*(t1-v*x)   #

print("An observer on Earth would perceive the trip to take",'%.2f' % t1,"years", "\nFrom our point of view, it would take us",'%.2f' % t2,"years")
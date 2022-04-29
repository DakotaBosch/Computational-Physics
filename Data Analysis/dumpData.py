#! /usr/bin/env python3
"""
DumpData.py is a program which read in a simple ascii data file 
containing particle physics event Four-Vector information.  The program
prints the particle energies for the event and then print out a total event count.

Paul Eugenio
PHZ4151C
Florida State University
April 2, 2019
Updated: Sean Dobbs, March 30, 2020

"""

#
nEvents = 0
nPiPlus = 0
#
with open("n3pi.dat", "r") as dataFile:
	# open file and read in ascii events line-by-line
	# the line will contain either the number of particles which indicates start of an event
	# or the line contains particle information: id charge Px Py Pz E
	# 
	for line in dataFile:
		word = line.split() # split line into a list of words
		value = int(word[0])
		if value == 4:
			print("New event Information")
			nPiPlus = 0
			nEvents += 1
		elif value == 1:
			print("\tPhoton Beam with Energy: %f"%(float(word[5]) ) )
		elif value == 8:
			# piPlus meson
			print("\tPiPlus[%d] meson with Energy: %f"%(nPiPlus, float(word[5])) ) 
			nPiPlus += 1	
		elif value == 9:
			print("\tPiMinus meson with Energy: %f"%(float(word[5])) )
			

# Done reading all events from data file
print("\nTotal events read:", nEvents)










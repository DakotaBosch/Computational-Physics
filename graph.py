import pyaudio
import sys
import struct
import numpy
from pylab import *
import numpy

#temp = raw_input('File name? ')
#temp += ".txt"
#rint(temp)

file = open(str(sys.argv[1]), "rb")
snddata = file.read()
#snddatab = bytes(snddata, encoding = 'utf-8')

N = int(len(snddata)/2)
data = numpy.zeros(N,dtype=float)

for i in range(N) :
    data[i] = struct.unpack('h',snddata[2*i:2*(i+1)])[0]


dataft = numpy.fft.fft(data)

powerspectrum = abs(dataft)**2


figure()
plot(range(N),data)


figure()
plot(range(N),powerspectrum)



show()

import pyaudio
import sys
import struct
import numpy
import datetime
from pylab import *


chunk = 1024
FORMAT = pyaudio.paInt16  # 16-bit integers
CHANNELS = 1
RATE = 44100
temp = input('Enter desired recording duration(s): ')
RECORD_SECONDS = int(temp)
tune = str(input('Tuning?'))
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                output=True,
                frames_per_buffer=chunk)

print ("* recording")

snddata = stream.read(RATE * RECORD_SECONDS)
stream.stop_stream()
stream.close()
print ("* done")



now = datetime.datetime.now()
date = str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "." + str(now.minute) + "_" + tune + ".txt"
f = open(date, "w")

print('File saved as: ', date)

for q in range(0,len(snddata)):
               f.write( str(snddata[q]))



f.close()



print ("* playing")
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=chunk)

stream.write(snddata)
stream.stop_stream()
stream.close()
print ("* done")

p.terminate()


# Convert to pair of bytes to numerical datatype 
N = int(len(snddata)/2)
data = numpy.zeros(N)
for i in range(N) :
    data[i] = struct.unpack('h',snddata[2*i:2*(i+1)])[0]


dataft = numpy.fft.fft(data)

powerspectrum = abs(dataft)**2


figure()
plot(range(N),data)


figure()
plot(range(N),powerspectrum)



show()




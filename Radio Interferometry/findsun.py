from pysolar.solar import *
import datetime

lat = 30.446
lon = -84.301

date = datetime.datetime.now()
print(date)
date = date.replace(tzinfo=datetime.timezone.utc)
date = date.replace(hour = date.hour+4)

print("Altitude:","%.2f" % get_altitude(lat, lon, date),"  Azimuth:","%.2f" % get_azimuth(lat, lon,date))

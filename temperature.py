#!/usr/bin/env python

# pip install numpy
# pip install matplotlib

import matplotlib.pyplot as plt
#import datetime
from datetime import datetime, date, time
#import numpy as np

import re
from dateutil import tz
import fileinput


# curl "http://beehive1.mcs.anl.gov/api/1/nodes/0000001e06102bea/export?date=2016-04-12" > 2016-04-12.txt
# grep ";TMP112" 2016-04-12.txt > 2016-04-12_TMP112.txt


# pipe into script
# curl "http://beehive1.mcs.anl.gov/api/1/nodes/0000001e06102bea/export?date=2016-04-12" | grep ";TMP112"  | ./temperature.py
# cat 2016-04-12_TMP112.txt | ./temperature.py

# download all
# for i in 01 02 03 04 05 06 07 08 09 10 11 12 ; do curl "http://beehive1.mcs.anl.gov/api/1/nodes/0000001e06102bea/export?date=2016-04-${i}" > 2016-04-${i}.txt ; done

# extract TMP112
# for i in 01 02 03 04 05 06 07 08 09 10 11 12 ; do grep ";TMP112" 2016-04-${i}.txt > 2016-04-${i}_TMP112.txt ; done

# merge TMP112
# for i in 01 02 03 04 05 06 07 08 09 10 11 12 ; do cat 2016-04-${i}_TMP112.txt >> TMP112.txt ; done

# cat TMP112.txt | ./temperature.py



from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Chicago')


#file = open('2016-04-12_TMP112.txt')
dates=[]
values=[]
for line in fileinput.input():
    #print line
    array = line.split(';')
    date_str = array[5]
    value_str = array[8]
    #print date_str, value_str
    # example: 2016-04-12 23:59:50.874000
    #date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    try:
        date_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    except:
        date_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    
    date_object = date_object.replace(tzinfo=from_zone)
    #print "utc: ", str(date_object)
    # convert to local timezone
    date_object = date_object.astimezone(to_zone)
    #print "local: ", str(date_object)
    #print "value_str: ", value_str
    value = float(re.findall("[-+]?\d*\.\d+|\d+", value_str)[0])
    
    #print value
    dates.append(date_object)
    values.append(value)


#x = np.array(dates)
#y = np.random.randint(100, size=x.shape)

plt.plot(dates,values)
plt.savefig('testplot.png')
#plt.show()
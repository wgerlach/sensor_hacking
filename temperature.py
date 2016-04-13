#!/usr/bin/env python

# pip install numpy
# pip install matplotlib

import matplotlib.pyplot as plt
#import datetime
from datetime import datetime, date, time
import numpy as np

import re


file = open('2016-04-12_TMP112.txt')
dates=[]
values=[]
for line in file:
    #print line
    array = line.split(';')
    date_str = array[5]
    value_str = array[8]
    print date_str, value_str
    # example: 2016-04-12 23:59:50.874000
    #date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    try:
        date_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    except:
        date_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    
    print str(date_object)
    #print "value_str: ", value_str
    value = float(re.findall("[-+]?\d*\.\d+|\d+", value_str)[0])
    
    print value
    dates.append(date_object)
    values.append(value)


#x = np.array(dates)
#y = np.random.randint(100, size=x.shape)

plt.plot(dates,values)
plt.show()
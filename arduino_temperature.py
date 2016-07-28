#!/usr/bin/env python3

from serial import Serial


import time
from datetime import datetime, timezone
import json

#line = '17/Dec/2011:09:48:49 -0600'
#line = line.split(' ')[0]
#print  time.strptime(line,"%d/%b/%Y:%H:%M:%S")

device = '/dev/ttyACM0'
#device = '/dev/cu.usbmodem1411'

with Serial(device, 9600, timeout=8, writeTimeout=8) as serial:
    while True:
        try:
            line = serial.readline().decode().strip()
            if line[0] == "{":
                try:
                    data = json.loads(line)
                except:
                    continue
                    
                data['timestamp'] = datetime.now().isoformat()
                print(json.dumps(data))
        except:
            break
        time.sleep(30)
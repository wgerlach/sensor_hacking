#!/usr/bin/env python3

from serial import Serial

import time
from datetime import datetime, timezone
import json



# apt-get install -y python3-serial

# apt-get install -y influxdb
# apt-get install -y python3-influxdb



from influxdb import InfluxDBClient

#json_body = [
#    {
#        "measurement": "temperature",
#        "time": "2009-11-10T23:00:00Z",
#        "fields": {
#            "value": 0.64
#        }
#    }
#]


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'sensor')

client.create_database('sensor')

#client.write_points(json_body)


#result = client.query('select value from temperature;')

print("Result: {0}".format(result))

#line = '17/Dec/2011:09:48:49 -0600'
#line = line.split(' ')[0]
#print  time.strptime(line,"%d/%b/%Y:%H:%M:%S")

device = '/dev/ttyACM0'
#device = '/dev/cu.usbmodem1411'

with Serial(device, 9600, timeout=8, writeTimeout=8) as serial:
    while True:
        try:
            line = serial.readline().decode().strip()
            if line:
                if line[0] == "{":
                    try:
                        data = json.loads(line)
                    except Exception as e:
                        print(str(e))
                        continue
                    
                    data['timestamp'] = datetime.now().isoformat()
                    print(json.dumps(data))
                    client.write_points([
                        {
                            "measurement": "temperature",
                            "time": data['timestamp'],
                            "fields": {
                                "value": data['value']
                            }
                        }
                    ])
                else:
                    print("error parsing, got: \"%s\"" % (line))
            else:
                print("no data")
        except Exception as e:
            print(str(e))
            break
        time.sleep(5)
        
        
        
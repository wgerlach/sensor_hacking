#!/usr/bin/env python3

from serial import Serial


with Serial("/dev/cu.usbmodem1411", 9600, timeout=8, writeTimeout=8) as serial:
    while True:
        try:
            line = serial.readline().decode().strip()
            print(line)
        except:
            break
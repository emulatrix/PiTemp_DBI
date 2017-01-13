#!/usr/bin/env python

# import python modules required
import suds 
import os
import glob
import time
from time import strftime
from suds.client import Client

# run the modprobe commands to load gpio and therm modules into kernel
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


# define location and id of temperature device in linux
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-0000053e5148')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.00
    return temp_c    
 
# Variables for Web Service Values
temp = (float(read_temp()))
datetime = (time.strftime("%Y-%m-%d") +'T'+ time.strftime("%H:%M:00"))
device_id = 'pi00000001'
 
#send to web Service
client = Client('http://vm-hercules:1121/WcfTempDemo.svc?WSDL')
try:
    result = client.service.SaveTemperature(device_id,datetime,temp)
except suds.WebFault, e:
    print e
print result

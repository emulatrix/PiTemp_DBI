# -*- coding: utf-8 -*-
import os 

# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

CPU_temp = getCPUtemperature()
RAM = getRAMinfo()
print "CPU Temparature = "+ CPU_temp + "°C"
print RAM[0] +" kb Total RAM"
print RAM[1] +" kb used"
print RAM[2] +" kb free"

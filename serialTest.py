#!/usr/bin/python

import serial
import array
import sys

ser = serial.Serial('/dev/ttyACM0', baudrate=9600)  # open serial port
ser.delay_before_tx=0.03,
ser.delay_before_rx=0.03,

ser.baudrate = 9600
print(ser.name)         # check which port was really used
ser.write('ID499\n'.encode('ascii'))     # Start Auto-Send Reading Mode (Remote off)

def getMeasurement():
    temperature = None
    pH = None
    dO = None

    while temperature is None or pH is None or dO is None:
        line = ser.readline()   # read a '\n' terminated line
        bytelist = list(line)
        #bytelist = list(filter(lambda a: a != 0, bytelist))
        #print(bytelist)

        decoded = line.decode('utf-16', 'replace')
        messageArr = decoded.split(',')
        #print(messageArr)

        try:
            if messageArr[5] == 'PHC101':
                temperature = messageArr[11]
                print('temp: ' , temperature)

                pH = messageArr[9]
                print('pH: ' , pH)


            elif messageArr[5] == 'LDO101':
                dOIndex = messageArr.index("mg/L")
                dO = messageArr[9]
                print('dO: ' , dO)
        except:
            pass

        ser.flushInput()
        ser.flushOutput()

    return {
        "temperature": temperature,
        "pH": pH,
        "dO": dO
    }

def logDeamon():
    while True:
        measurement = getMeasurement()
        with open("measurements", "a") as myfile:
            myfile.write(measurement + '\n')

logDeamon()

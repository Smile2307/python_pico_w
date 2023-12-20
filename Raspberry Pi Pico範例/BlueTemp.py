#----------------------------------------------------------
#		SEND TEMPERATURE TO SMART PHONE
#		===============================
#
# In this project a HC-06 type serial Bluetooth module is
# connected to the Raspberry Pi Pico. Internal temperature
# readings are sent to a smart phone every 10 seconds
#
# Author: Dogan Ibrahim
# File  : BlueTemp.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, UART, ADC
import utime

uart = UART(0, baudrate=9600,rx=Pin(1),tx=Pin(0))

Conv = 3.3 / 65535
AnalogIn = ADC(4)

def GetTemperature():
    V = AnalogIn.read_u16()
    V = V * Conv
    Temp = 27 - (V - 0.706) / 0.001721
    return Temp
    
#
# Send the temperature to smart phone
#
while True:
     T = GetTemperature()
     Temp = "T=" + str(T) + "\r\n"
     uart.write(Temp)
     utime.sleep(10)
     

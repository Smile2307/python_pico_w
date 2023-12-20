#----------------------------------------------------------
#		TMP102 TEMPERATURE SENSOR
#		=========================
#
# In this project a TMP102 type I2C compatible temperature
# sensor chip is connected to Raspberry Pi Pico. The temperature
# readings are displayed on the Thonny screen.
#
# Author: Dogan Ibrahim
# File  : TMP102.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=",i2c.scan())

Device_Address = 0x48					# TMP102 I2C address
PointerReg = 0                          # TMP102 register

#
# This function reads the temperature, extracts degrees Celius
# and returns the temperature to the main calling program
#
def Read():
    data = [0, 0]
    LSB = 0.0625
    data = i2c.readfrom_mem(Device_Address, PointerReg, 2)
    temp = (data[0] << 4) | (data[1] >> 4)
    if temp > 0x7FF:
        temp = (~temp) & 0xFF
        temp = temp + 1
        temperature = -temp * LSB
    else:
        temperature = temp * LSB
    return(temperature)

#
# Main program reads and displays the temperature every second
#
while True:
    Temperature = Read()
    print("Temperature = %+5.2f" %Temperature)
    utime.sleep(1)
          
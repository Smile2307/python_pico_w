#----------------------------------------------------------
#		BMP280 TEMPERATURE AND PRESSURE SENSOR
#		======================================
#
# In this project the BMP280 temperature and pressure sensor
# is connected to the Raspberry Pi Pico. The temperature and
# pressure readings are displayed every 5 seconds on the
# Thonny screen
#
# In this version of the program the BMP280 code is imported
# as a module
#
# Author: Dogan Ibrahim
# File  : ReadBMP280-2.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime
import bmp280

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=" ,i2c.scan())

while True:
    T,P = bmp280.BMP280()
    print("Temperature in Celsius : %.2f C" %T)	
    print("Pressure : %.2f hPa \n" %P)
    utime.sleep(5)
   
   
    
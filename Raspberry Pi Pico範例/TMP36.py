#--------------------------------------------------------
#				TEMPERATURE MEASUREMENT
#				=======================
#
# This program measures the temperature using an external
# TMP36 type temperature sensor chip
#
# Author: Dogan Ibrahim
# File  : TMP36.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime
import LCD

AnalogIn = ADC(0)						# ADC channel 0
Conv = 3300 / 65535						# Conversion factor
LCD.lcd_init()

while True:								# Do forever
    V = AnalogIn.read_u16()			    # Read temp
    mV = V * Conv						# Convert to Volts
    Temp = (mV - 500.0) / 10.0          # Convert to temp
    LCD.lcd_clear()                     # Clear screen
    Tempstr = str(Temp)[:5]             # Convert to string
    LCD.lcd_puts(Tempstr)               # Display
    utime.sleep(1)						# Wait 1 second
  

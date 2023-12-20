#--------------------------------------------------------
#				TEMPERATURE MEASUREMENT
#				=======================
#
# This program measures the temperature using the internal
# temperature sensor of the Pico and displyas on LCD
#
# Author: Dogan Ibrahim
# File  : TempInt.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime
import LCD

AnalogIn = ADC(4)						# ADC channel 4
Conv = 3.3 / 65535						# Conversion factor
LCD.lcd_init()

while True:								# Do forever
    V = AnalogIn.read_u16()			    # Read temp
    V = V * Conv						# Convert to Volts
    Temp = 27 - (V - 0.706) / 0.001721  # Convert to temp
    LCD.lcd_clear()                     # Clear screen
    Tempstr = str(Temp)                 # Convert to string
    LCD.lcd_puts(Tempstr)               # Display
    utime.sleep(1)						# Wait 1 second
  


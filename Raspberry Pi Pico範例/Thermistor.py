#------------------------------------------------------------
#		THERMISTOR TEMPERATURE MEASUREMENT
#		==================================
#
# This program measures the ambient temperature using a
# low-cost NTC thermistor module (KY-013). The readings are
# displayed on the LCD
#
# Author: Dogan Ibrahim
# File  : Thermistor.py
# Date  : February 2011
#-------------------------------------------------------------
from machine import ADC
import utime
import math
import LCD

Thermistor = ADC(0)						# ADC channel 0
LCD.lcd_init()							# Initialize LCD

#
# Calculate the temperature using Steinhart-Hart equation
#
def Temperature(RawValue):
    c1 = 0.001129148
    c2 = 0.000234125
    c3 = 0.0000000876741
    R1 = 10000.0
    ADC_Res = 65535.0
    
    R2 = R1 / ((ADC_Res/RawValue - 1))
    T = math.log(R2)
    Tmp = 1.0 / (c1 + (c2 + (c3 * T * T)) * T)
    Temp = Tmp - 273.15
    return Temp

while True:								# Do forever
    Raw = Thermistor.read_u16()			# Read channel 0
    temp = Temperature(Raw)				# Calculate temp
    LCD.lcd_clear()						# Clear LCD
    LCD.lcd_puts("Temperature (C)")		# Display heading
    LCD.lcd_goto(0, 1)					# Move cursor
    tempstr = str(temp)[:5]       		# Convert to string
    LCD.lcd_puts(tempstr)				# Display temperature
    utime.sleep(2)						# Wait 2 seconds
  
#--------------------------------------------------------
#				VOLTMETER
#				=========
#
# This is a voltmeter project. The voltage to me measured
# is applied to GP26 (pin 31) of the Pico
# This version of the program displays the measured voltage
# on the LCD
#
# Author: Dogan Ibrahim
# File  : VoltLCD.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime
import LCD

AnalogIn = ADC(0)						# ADC channel 0
Conv = 3300 / 65535						# Conversion factor
LCD.lcd_init()

while True:								# Do forever
    mV = AnalogIn.read_u16()			# Read input
    mV = mV * Conv						# Input in mV
    LCD.lcd_clear()                     # Clear screen
    mVstr = str(mV)                     # Convert to string
    LCD.lcd_puts(mVstr)                 # Display
    utime.sleep(1)						# Wait 1 second
  



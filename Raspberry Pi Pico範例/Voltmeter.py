#--------------------------------------------------------
#				VOLTMETER
#				=========
#
# This is a voltmeter project. The voltage to me measured
# is applied to GP26 (pin 31) of the Pico
#
# Author: Dogan Ibrahim
# File  : Voltmeter.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime

AnalogIn = ADC(0)						# ADC channel 0
Conv = 3300 / 65535						# Conversion factor

while True:								# Do forever
    mV = AnalogIn.read_u16()			# Read input
    mV = mV * Conv						# Input in mV
    print("Voltage = %5.2f" %mV)		# Display
    utime.sleep(1)						# Wait 1 second
  



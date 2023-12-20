#--------------------------------------------------------
#				MEASURE THE LIGHT INTENSITY
#				===========================
#
# In this project an LCD is connected to the Pico in series
# with a fixed resistor. The program displays the volatge
# across the fixed resisor which is proportional to the
# light level falling on the LCD
#
# Author: Dogan Ibrahim
# File  : LDR.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime

LDRin = ADC(0)							# ADC channel 0

while True:								# Do forever
    r = LDRin.read_u16()			    # Read LDR
    print("ADC=",r)						# Display ADC reading
    utime.sleep(1)						# Wait 1 second
  

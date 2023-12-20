#--------------------------------------------------------------
#				OHMMETER
#				========
#
# In this project the value of an unknown resistor is measured
#
# Author: Dogan Ibrahim
# File  : Ohmmeter.py
# Date  : February 2011
#-------------------------------------------------------------
from machine import ADC
import utime

RF = 10									# RF = 10K
LDRin = ADC(0)							# ADC channel 0

while True:								# Do forever
    sum = 0
    for i in range(5):					# Get 5 readings
        sum = sum + LDRin.read_u16()	# Read voltage
    Vm = sum / 5						# Average
    Rx = 65535*RF / Vm - RF				# Calculate Rx
    RxOhms = 1000 * Rx					# Rx in Ohms
    print("Rx (Ohms)=%8.1f" %RxOhms)	# Display Rx
    utime.sleep(1)						# Wait 1 second
  

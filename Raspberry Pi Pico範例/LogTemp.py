#--------------------------------------------------------
#				LOGGING THE TEMPERATURE DATA
#				============================
#
# This program measures the temperature using an external
# temperature sensor chip and logs the data every second
# for 30 seconds (i.e. 30 records)
#
# Author: Dogan Ibrahim
# File  : LogTemp.py
# Date  : February 2011
#----------------------------------------------------------
from machine import ADC
import utime

AnalogIn = ADC(0)							# ADC channel 0
Conv = 3300 / 65535							# Conversion factor

file = open("Temp.txt", "w")				# Create a new file
file.write("Ambient Temperature\n")			# Write heading

for secs in range(30):						# Do forever
    V = AnalogIn.read_u16()			    	# Read temp
    mV = V * Conv							# Convert to Volts
    Temp = (mV - 500.0) / 10.0          	# Convert to temp
    Tempstr = str(Temp)[:5]             	# Convert to string
    data = str(secs+1) + "   " + Tempstr + "\n"
    file.write(data)						# Write to file
    utime.sleep(1)							# Wait 1 second
    
file.close()								# Close file
print("Data has been written to file...")
  

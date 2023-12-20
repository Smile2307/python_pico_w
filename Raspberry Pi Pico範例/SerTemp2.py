#----------------------------------------------------------
#		SERIAL LINK - SEND TEMPERATURE READING TO ARDUINO
#		=================================================
#
# This project reads the internal temperature and sends it
# to Arduino Uno over a serial link at 9600 Baud.
# This version of the program imports machine
#
# Author: Dogan Ibrahim
# File  : SerTemp2.py
# Date  : February 2011
#------------------------------------------------------------
import machine
import utime

AnalogIn = machine.ADC(4)				# ADC channel 4
Conv = 3.3 / 65535						# Conversion factor
  
uart=machine.UART(id=0,baudrate=9600,bits=8,parity=None,stop=1 )

while True:								# Do forever
    V = AnalogIn.read_u16()			    # Read temp
    V = V * Conv						# Convert to Volts
    Temp = 27 - (V - 0.706) / 0.001721  # Convert to temp
    Tempstr = str(Temp)                 # Convert to string
    uart.write(Tempstr[:5])					# Send to UART
    uart.write(" Degrees C\n")
    utime.sleep(10)						# Wait 10 seconds
  


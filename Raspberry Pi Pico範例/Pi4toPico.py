#---------------------------------------------------------------
#	RASPBERRY PI 4 TO RASPBERRY PI PICO SERIAL COMMS
#	------------------------------------------------
#
# This program receives a message from the Raspberry Pi Pico,
# and sends back another message
#
# Author: Dogan Ibrahim
# File  : Pi4toPico.py
# Date  : February, 2021
#---------------------------------------------------------------
import time				# Import time library
import serial				# Import serial
port = "/dev/serial0"			# Serial port

GPIO.setwarnings(False)

ser = serial.Serial(port,baudrate=9600,timeout=100)

while True:
     data = ser.readline()		# Read the message 
     ser.write(b'Hello back\n')		# Send back message
     print(data)			# Display the message
     time.sleep(5)



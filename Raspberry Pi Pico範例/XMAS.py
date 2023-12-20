#---------------------------------------------------------
#				CHRISTMAS LIGHTS
#				================
#
# In this program 8 LEDs are connected to Pico. The LEDs
# flash randomly
#
# Author: Dogan Ibrahim
# File  : XMAS.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime
import random

PORT = [7, 6, 5, 4, 3,  2,  1,  0]	# port connections
DIR = ["0","0","0","0","0","0","0","0"]	# port directons
L = [0]*8

#
# This function configures the port pins as outputs ("0") or
# as inputs ("I")
#
def Configure_Port():
   for i in range(0, 8):
      if DIR[i] == "0":
         L[i] = Pin(PORT[i], Pin.OUT)
      else:
         L[i] = Pin(PORT[i], Pin.IN)
   return

#
# This function sends 8-bit data (0 to 255) to the PORT
#
def Port_Output(x):
   b = bin(x)					# convert into binary
   b = b.replace("0b", "")		# remove leading "0b"
   diff = 8 - len(b)			# find the length
   for i in range (0, diff):
      b = "0" + b				# insert leading os

   for i in range (0, 8):
      if b[i] == "1":
         L[i].value(1)
      else:
         L[i].value(0)
   return

#
# Configure PORT to all outputs
#
Configure_Port()

#
# Main program loop. Count up in binary every second
#
while True:
  numbr = random.randint(1, 255)	# generate a random number
  Port_Output(numbr)			    # send cnt to port
  utime.sleep(0.25)			        # wait 250ms
 

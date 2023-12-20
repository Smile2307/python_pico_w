#---------------------------------------------------------
#				LUCKY DAY OF THE WEEK
#				=====================
#
# In this program 7 LEDs are connected to Pico where each
# LED represents a day of the week. Pressing a button
# turns ON one of the LEDs randomly and this corresponds to
# your lucky day of the week
#
# Author: Dogan Ibrahim
# File  : LuckyDay.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime
import random

PORT = [7, 6, 5, 4, 3,  2,  1,  0]	# port connections
L = [0]*8
Button = Pin(15, Pin.IN)

#
# This function configures the LED ports as outputs
#
def Configure_Port():
   for i in range(0, 8):
         L[i] = Pin(PORT[i], Pin.OUT)

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
# Main program loop, check if Button is pressed
#
print("Press the Button to display your lucky number...")

random.seed(utime.ticks_ms())

while Button.value() == 1:		  # If Button not pressed
   pass
r = random.randint(1, 7)		  # Generate random number
r = pow(2, r-1)				      # LED to be turned ON
Port_Output(r)			          # Send to LEDs


 

#---------------------------------------------------------
#				DICE PROGRAM
#				============
#
# In this program 7 LEDs are connected to Pico to simlate
# a dice. When a pushbutton is pressed the LEDs display a
# dice number between 1 and 6
#
# Author: Dogan Ibrahim
# File  : DICE.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime
import random

PORT = [7, 6, 5, 4, 3,  2,  1,  0]	# port connections
DICE_NO = [0, 0x08, 0x22, 0x2A, 0x55, 0x5D, 0x77]
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
# The program jumps here after the button is pressed
#
def DICE():
   n = random.randint(1, 6)		# generate a random number
   pattern = DICE_NO[n]			# find the pattern
   Port_Output(pattern)			# turn ON required LEDs
   utime.sleep(3)			    # wait for 3 seconds
   Port_Output(0)			    # turn OFF all LEDs
   return
#
# Configure PORT to all outputs
#
Configure_Port()

#
# Main program loop, check if Button is pressed
#
while True:
  if Button.value() == 0:		  # Button pressed?
     DICE()						  # Call DICE
  pass                            # Do nothing
 

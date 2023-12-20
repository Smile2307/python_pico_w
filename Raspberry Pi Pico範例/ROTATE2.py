#---------------------------------------------------------
#				ROTATING LEDs
#				=============
#
# In this program 4 LEDs are connected to Pico. The LEDs
# display pattern of rotating to the left
#
# Author: Dogan Ibrahim
# File  : Rotate2.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LEDS = [0, 1, 2, 3]					# LED ports
L = [0, 0, 0, 0]

for i in range(4):					# Do for all LEDs
    L[i] = Pin(LEDS[i], Pin.OUT)	# All are outputs

while True:							# Do forever
    for i in range(4):
        L[i].value(1)				# LED ON
        utime.sleep(0.5)			# Wait 0.5 second
        L[i].value(0)				# LED OFF
                
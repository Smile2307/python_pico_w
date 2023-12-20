#---------------------------------------------------------
#			FLASHING AN EXTERNAL LED
#			========================
#
# In this program an external LED is connected to port pin
# GP0 (pin 1). The LED is flashed every second
#
# Author: Dogan Ibrahim
# File  : ExtFlash.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LED = Pin(0, Pin.OUT)		    # LED at GP0

while True:						# DO FOREVER
    LED.value(1)				# LED ON
    utime.sleep(1)				# Wait 1 second
    LED.value(0)				# LED OFF
    utime.sleep(1)				# Wait 1 second
    
    
#---------------------------------------------------------
#			FLASHING THE ON-BOARD LED
#			=========================
#
# In this program the on-board LED (at GP25) is flashed
# every second. In this version only module Pin is imported
#
# Author: Dogan Ibrahim
# File  : LEDINT2.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LED = Pin(25, Pin.OUT)		    # LED at GP25

while True:						# DO FOREVER
    LED.value(1)				# LED ON
    utime.sleep(1)				# Wait 1 second
    LED.value(0)				# LED OFF
    utime.sleep(1)				# Wait 1 second
    
    
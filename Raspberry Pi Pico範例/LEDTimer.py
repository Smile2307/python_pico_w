#---------------------------------------------------------
#				LED FLASHING USING A TIMER
#				==========================
#
# In this program an external LED is connected to port pin
# GP0 (pin 1). The LED flashes every second using a timer
#
# Author: Dogan Ibrahim
# File  : LEDTimer.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LED = Pin(0, Pin.OUT)
LED.ON()
utime.sleep(2)
LED.value(0)


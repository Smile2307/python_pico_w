#---------------------------------------------------------
#				ROTATING LEDs
#				=============
#
# In this program 4 LEDs are connected to Pico. The LEDs
# display pattern of rotating to the left
#
# Author: Dogan Ibrahim
# File  : Rotate.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LEDS = [0, 1, 2, 3]
for i in range(4):
    Pin(LEDS[i], Pin.OUT)


while True:
    LED1.value(1)
    utime.sleep(0.5)
    LED1.value(0)
    LED2.value(1)
    utime.sleep(0.5)
    LED2.value(0)
    LED3.value(1)
    utime.sleep(0.5)
    LED3.value(0)
    LED4.value(1)
    utime.sleep(0.5)
    LED4.value(0)
    
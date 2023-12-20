#---------------------------------------------------------
#				ALTERNATELY FLASHING RGB LED
#				============================
#
# In this program an RGB LED is connected to Pico.The three
# colours of the LED are flashed alternately every 500ms
#
# Author: Dogan Ibrahim
# File  : RGB.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

Red = Pin(0, machine.Pin.OUT)
Green = Pin(1, Pin.OUT)
Blue = Pin(2, Pin.OUT)

Red.value(0)
Green.value(0)
Blue.value(0)

while True:
    Red.value(1)
    utime.sleep(0.5)
    Red.value(0)
    Green.value(1)
    utime.sleep(0.5)
    Green.value(0)
    Blue.value(1)
    utime.sleep(0.5)
    Blue.value(0)

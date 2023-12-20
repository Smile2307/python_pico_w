#---------------------------------------------------------
#				RANDOMLY FLASHING RGB LED
#				=========================
#
# In this program an RGB LED is connected to Pico.The three
# colours of the LED are flashed randomly every 500ms
#
# Author: Dogan Ibrahim
# File  : RGB2.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime
import random

Red = Pin(0, machine.Pin.OUT)
Green = Pin(1, Pin.OUT)
Blue = Pin(2, Pin.OUT)

while True:
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    Red.value(r)
    utime.sleep(0.2)
    Green.value(g)
    utime.sleep(0.2)
    Blue.value(b)
    utime.sleep(0.2)

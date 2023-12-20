#---------------------------------------------------------
#		DOOR ALARM WITH 7-COLOUR FLASHING LED
#		=====================================
#
# In this program a reed switch is connected as an input and
# a 7-colour flashing LED is connected as an output. The LED
# flashes when the door is opened
#
# Author: Dogan Ibrahim
# File  : ReedDoor.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin

ReedSwitch = Pin(0, Pin.IN)
LED = Pin(1, Pin.OUT)

LED.value(0)

while True:
    door = ReedSwitch.value()
    if door == 1:
        LED.value(1)
    else:
        LED.value(0)



 

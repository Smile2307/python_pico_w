#---------------------------------------------------------
#				LED FLASHING SOS
#				================
#
# In this program an external LED is connected to port pin
# GP0 (pin 1). The LED flashes the SOS signal
#
# Author: Dogan Ibrahim
# File  : SOS.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

Dot = 0.25                      # Dot time
Dash = 1.0                      # Dash time
Gap = 0.2                       # Gap time
ON = 1                          # ON
OFF = 0                         # OFF

LED = Pin(0, Pin.OUT)		    # LED at GP0

while True:						# DO FOREVER
    for i in range(0, 3):
        LED.value(ON)           # LED ON
        utime.sleep(Dot)        # Wait Dot time
        LED.value(OFF)          # LED OFF
        utime.sleep(Gap)        # Wait Gap time
        
    utime.sleep(0.5)            # 0.5 second delay
    
    for i in range(0, 3):
        LED.value(ON)           # LED ON
        utime.sleep(Dash)       # Wait Dash time
        LED.value(OFF)          # LED OFF
        utime.sleep(Gap)        # Wait Gap time
    
    utime.sleep(2)              # Wait 2 seconds

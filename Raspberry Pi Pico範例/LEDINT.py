#---------------------------------------------------------
#			FLASHING THE ON-BOARD LED
#			=========================
#
# In this program the on-board LED (at GP25) is flashed
# every second
#
# Author: Dogan Ibrahim
# File  : LEDINT.py
# Date  : February, 2021
#----------------------------------------------------------
import machine
import utime

LED = machine.Pin(25, machine.Pin.OUT)		# LED at GP25

while True:									# DO FOREVER
    LED.value(1)							# LED ON
    utime.sleep(1)							# Wait 1 second
    LED.value(0)							# LED OFF
    utime.sleep(1)							# Wait 1 second
    
    
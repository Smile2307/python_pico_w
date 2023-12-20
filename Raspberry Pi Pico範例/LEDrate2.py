#---------------------------------------------------------
#				CHANGE THE LED FLASHING RATE
#				============================
#
# In this program an external LED and two pushbuttons are
# connected to Pico. Pressing Faster flashes the LED faster,
# and pressing Slower flashes the LED slower
# In this modified version, internal pull-ups are used
#
# Author: Dogan Ibrahim
# File  : LEDrate2.py
# Date  : February, 2021
#----------------------------------------------------------
import machine
import utime

LED = machine.Pin(0, machine.Pin.OUT)

while True:
    LED.on()				# LED ON
    utime.sleep(1)			# Delay dly
    LED.off()				# LED OFF
    utime.sleep(1)			# Delay dly
   


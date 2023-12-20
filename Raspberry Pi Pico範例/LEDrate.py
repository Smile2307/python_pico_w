#---------------------------------------------------------
#				CHANGE THE LED FLASHING RATE
#				============================
#
# In this program an external LED and two pushbuttons are
# connected to Pico. Pressing Faster flashes the LED faster,
# and pressing Slower flashes the LED slower
#
# Author: Dogan Ibrahim
# File  : LEDrate.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin
import utime

LED = Pin(0, Pin.OUT)			# LED at pin GP0
Faster = Pin(1, Pin.IN)			# Faster at pin GP1
Slower = Pin(2, Pin.IN)			# Slower at pin GP2
dly = 1.0						# Default delay

#
# This is the interrupt service routine. Whenever pushbutton
# Faster is pressed, the program jumps here and decrements
# delay to make the flashing faster
#
def Flash_Faster(Faster):
   global dly
   dly = dly - 0.1

#
# This is the interrupt service routine. Whenever pushbutton
# Slower is pressed, the program jumps here and increments
# delay to make the flashing slower
#
def Flash_Slower(Slower):
    global dly
    dly = dly + 0.1
 
#
# Configure the external interrupts
#
Faster.irq(handler=Flash_Faster,trigger=Faster.IRQ_FALLING)
Slower.irq(handler=Flash_Slower,trigger=Slower.IRQ_FALLING)

#
# Main program loop
#
while True:
    LED.value(1)				# LED ON
    utime.sleep(dly)			# Delay dly
    LED.value(0)				# LED OFF
    utime.sleep(dly)			# Delay dly

    


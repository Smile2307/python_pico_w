#--------------------------------------------------------
#				LCD SECONDS COUNTER
#				===================
#
# This program counts up every secon and displays on LCD
#
# Author: Dogan Ibrahim
# File  : LCDCount2.py
# Date  : February 2011
#----------------------------------------------------------
import LCD
import utime

LCD.lcd_init()
count = 0
while True:
    LCD.lcd_goto(0, 0)
    cntstr = str(count)
    LCD.lcd_puts(cntstr)
    count = count + 1
    utime.sleep(1)


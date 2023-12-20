#------------------------------------------------------------
#		EXTERNAL AND INTERNAL TEMPERATURE MEASUREMENT
#		=============================================
#
# This program measures the external and internal temperatures
# using two TMP36 type temperature sensor chips. Both external
# and internal temperatures are displayed on the LCD
#
# Author: Dogan Ibrahim
# File  : MultiTmp.py
# Date  : February 2011
#-------------------------------------------------------------
from machine import ADC
import utime
import LCD

ExtTemp = ADC(0)						# ADC channel 0
IntTemp = ADC(1)						# ADC channel 1
Conv = 3300 / 65535						# Conversion factor
LCD.lcd_init()

while True:								# Do forever
    Vext = ExtTemp.read_u16()			# Read channel 0
    mV = Vext * Conv					# Convert to mV
    Tempext = (mV - 500.0) / 10.0       # External temp
    Vint = IntTemp.read_u16()			# Read channel 1
    mV = Vint * Conv					# Convert to mV
    Tempint = (mV - 500.0) / 10.0		# Internal temp
    LCD.lcd_clear()                     # Clear screen
    Tempextstr = str(Tempext)[:5]       # Convert to string
    Tempintstr = str(Tempint)[:5]		# Convert to string
    LCD.lcd_puts("Ext: ")				# Heading
    LCD.lcd_puts(Tempextstr)			# Display external
    LCD.lcd_goto(0, 1)					# Cursor at row 1
    LCD.lcd_puts("Int: ")				# Heading
    LCD.lcd_puts(Tempintstr)			# Display internal
    utime.sleep(2)						# Wait 2 seconds
  
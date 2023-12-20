#----------------------------------------------------------
#				ON-OFF TEMPERATURE CONTROLLER
#				=============================
#
# This is an ON-OFF temperature controller program. The
# project consists of a temperature sensor, an LED and a
# heater. The heater and the LED are turned ON if the room
# temperature (RoomTemp) is below the desired value (SetTemp)
#
# An LCD is used to display the desired temperature at the top
# row, and room temperature at bottom row
#
# Author: Dogan Ibrahim
# File  : ONOFFLCD.py
# Date  : February 2011
#------------------------------------------------------------
from machine import ADC, Pin
import utime
import LCD

LCD.lcd_init()                          # Initialize LCD
AnalogIn = ADC(0)						# ADC channel 0
Conv = 3300 / 65535						# Conversion factor

SetTemp = 24.0                          # Desired temperature
LED = Pin(16, Pin.OUT)                  # LED at GP16
Relay = Pin(17, Pin.OUT)                # Relay at GP17
LED.value(0)                            # Turn OFF LED
Relay.value(0)                          # Turn OFF Relay

LCD.lcd_clear()							# Clear LCD
LCD.lcd_puts("Set : ")					# Display Set :
LCD.lcd_puts(str(SetTemp)[:5])			# Display SetTemp

while True:								# Do forever
    V = AnalogIn.read_u16()			    # Read temp
    mV = V * Conv						# Convert to Volts
    RoomTemp = (mV - 500.0) / 10.0      # Measured temperature
    LCD.lcd_goto(0, 1)					# Cursor at 0,1
    LCD.lcd_puts("Meas: ")				# Display Meas:
    LCD.lcd_puts(str(RoomTemp)[:5])		# Display RoomTemp
    if RoomTemp < SetTemp:              # If Room temp < desired
        Relay.value(1)                  # Turn Relay ON
        LED.value(1)                    # Turn LED ON
    else:
        Relay.value(0)                  # Turn Relay OFF
        LED.value(0)                    # Tuen LED OFF
    utime.sleep(3)                      # Wait 3 seconds

#----------------------------------------------------------
#				ON-OFF TEMPERATURE CONTROLLER
#				=============================
#
# This is an ON-OFF temperature controller program. The
# project consists of a temperature sensor, an LED and a
# heater. The heater and the LED are turned ON if the room
# temperature (RoomTemp) is below the desired value (SetTemp)
#
# Author: Dogan Ibrahim
# File  : ONOFF.py
# Date  : February 2011
#------------------------------------------------------------
from machine import ADC, Pin
import utime

AnalogIn = ADC(0)						# ADC channel 0
Conv = 3300 / 65535						# Conversion factor

SetTemp = 24.0                          # Desired temperature
LED = Pin(16, Pin.OUT)                  # LED at GP16
Relay = Pin(17, Pin.OUT)                # Relay at GP17
LED.value(0)                            # Turn OFF LED
Relay.value(0)                          # Turn OFF Relay

while True:								# Do forever
    V = AnalogIn.read_u16()			    # Read temp
    mV = V * Conv						# Convert to Volts
    RoomTemp = (mV - 500.0) / 10.0      # Measured temperature
    if RoomTemp < SetTemp:              # If Room temp < desired
        Relay.value(1)                  # Turn Relay ON
        LED.value(1)                    # Turn LED ON
    else:
        Relay.value(0)                  # Turn Relay OFF
        LED.value(0)                    # Tuen LED OFF
    utime.sleep(3)                      # Wait 3 seconds

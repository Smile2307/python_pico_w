#----------------------------------------------------------
#		BLUETOOTH COMMUNICATION
#		=======================
#
# In this project a HC-06 type serial Bluetooth module and
# and LED are connected to the Raspberry Pi Pico. The LED
# is controlled by sending commands from a Bluetooth
# compatible smart phone.
#
# Author: Dogan Ibrahim
# File  : BlueLED.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, UART
import utime

uart = UART(0, baudrate=9600,rx=Pin(1),tx=Pin(0))

LED = Pin(16, Pin.OUT)
LED.value(0)

#
# Main program loop. Receive a command and control the LED
#
while True:
     buf = uart.readline()						# Read data
     dat = buf.decode('UTF-8')					# Decode
     if dat[0] == 'L' and dat[1] == '1':		# L1?
         LED.value(1)                           # LED ON
         uart.write("LED is ON")                # Send confirmation
     elif dat[0] == 'L' and dat[1] == '0':		# L0?
         LED.value(0)							# LED OFF
         uart.write("LED is OFF")               # Send confirmation

         
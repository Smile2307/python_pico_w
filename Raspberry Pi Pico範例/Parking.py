#----------------------------------------------------------
#      RUNNING A PROGRAM AUTOMATICALLY AFTER REBOOT
#      ===========================================
#
# In some applications we may want to run a program
# automatically after reboot.This is done easily by saving
# the program with the name "main.py". This very simple
# program flashes an LED connected to GP16 automatically
# after the Raspberry Pi Pico boots.
#
# Author: Dogan Ibrahim
# File  : main.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin
import utime

LED = Pin(16, Pin.OUT)					# LED at pin 16

while True:                             # Do Forever
    LED.value(1)                        # LED ON
    utime.sleep(1)                      # Wait 1 second
    LED.value(0)                        # LED OFF
    utime.sleep(1)                      # Wait 1 second
    

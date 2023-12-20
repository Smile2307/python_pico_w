#----------------------------------------------------------
#		SERIAL LINK WITH RASPBERRY PI 4
#		===============================
#
# This project sends a message to Raspberry Pi 4 and then
# receives back a message and displays the received message
#
# Author: Dogan Ibrahim
# File  : PicotoPi4.py
# Date  : February 2011
#------------------------------------------------------------
from machine import UART
import utime

uart = UART(0, 9600)

while True:
    uart.write("Hello from Raspberry Pi Pico\n")
    recv = uart.readline()
    enc = recv.decode('utf-8')
    print(enc)
    utime.sleep(5)
    

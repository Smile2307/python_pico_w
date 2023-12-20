#----------------------------------------------------------
#		USING WI-FI
#		===========
#
# In this project a ESP-01 chip is connected to the Raspberry
# Pi Pico. This chip is used to connect the Pico to the Wi-Fi
#
# Author: Dogan Ibrahim
# File  : Picowifi.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, UART
import utime
uart = UART(0, baudrate=115200,rx=Pin(1),tx=Pin(0))

LED = Pin(16, Pin.OUT)
LED.value(0)

#
# Send AT commands to ESP-01 to connect to local WI-Fi
#
def ConnectToWiFi():
      uart.write("AT+RST\r\n")
      utime.sleep(5)
      
      uart.write("AT+CWMODE=1\r\n")
      utime.sleep(1)

      uart.write('''AT+CWJAP="BTHomeSpot-XNH","49345xyzw"\r\n''')
      utime.sleep(5)
   
      uart.write("AT+CPIMUX=0\r\n")
      utime.sleep(3)

      uart.write('''AT+CIPSTART="UDP","0.0.0.0",5000,5000,2\r\n''')
      utime.sleep(3)

ConnectToWiFi()

#
# Main program loop
#
while True:
     buf = uart.readline()					# Read data
     dat = buf.decode('UTF-8')				# Decode
     print(dat)
     n = dat.find("LON")					# Includes LON?
     if n > 0:
        LED.value(1)						# LED ON
     n = dat.find("LOFF")					# Includes OFF?
     if n > 0:
        LED.value(0)						# LED OFF

     




    
    


      
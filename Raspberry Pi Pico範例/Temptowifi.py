#----------------------------------------------------------
#		SEND TEMPERATURE TO SMART PHONE
#		===============================
#
# In this project a ESP-01 chip is connected to the Raspberry
# Pi Pico. Internal temperature of the Raspberry Pi Pico is
# sent to the smart phone
#
# Author: Dogan Ibrahim
# File  : Temptowifi.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, UART, ADC
import utime

uart = UART(0, baudrate=115200,rx=Pin(1),tx=Pin(0))

Conv = 3.3 / 65535
AnalogIn = ADC(4)

def GetTemperature():
    V = AnalogIn.read_u16()
    V = V * Conv
    Temp = 27 - (V - 0.706) / 0.001721
    return Temp

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

      uart.write('''AT+CIPSTART="UDP","192.168.1.199",5000,5000,2\r\n''')
      utime.sleep(3)

ConnectToWiFi()

#
# Main program loop. Send the temperature to smart phone
#
while True:
     buf = uart.readline()					# Read data
     dat = buf.decode('UTF-8')				# Decode
     n = dat.find("T?")						# T? received?
     if n > 0:
         T = GetTemperature()				# Get the temperature
         Tstr = "T=" + str(T)				# Insert T=
         Tlen = str(len(Tstr))				# Length
         Dt = "AT+CIPSEND="+Tlen + "\r\n"	# AT command to send
         uart.write(Dt)						# Send to ESP-01
         utime.sleep(2)						# Wait 2 sec
         uart.write(Tstr)					# Send data
         
         
     
     
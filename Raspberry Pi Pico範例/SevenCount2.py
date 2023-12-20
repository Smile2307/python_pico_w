#---------------------------------------------------------
#				2-DIGIT 7-SEGMENT COUNTER
#				=========================
#
# In this program a 2-digit 7-segment display is connected
# to the Pico. The program counts up every second.
# In this version of the program leading zero is omitted
#
# Author: Dogan Ibrahim
# File  : SevenCount.py
# Date  : February, 2021
#----------------------------------------------------------
from machine import Pin, Timer
import utime

tim = Timer()
LED_Segments = [6, 5 ,4, 3, 2, 1, 0]
LED_Digits = [8, 7]
L = [0]*7
D = [0, 0]

#
# LED bit pattern for all numbers 0-9
#
LED_Bits ={
' ':(0,0,0,0,0,0,0),            # Blank
'0':(1,1,1,1,1,1,0),			# 0
'1':(0,1,1,0,0,0,0),			# 1
'2':(1,1,0,1,1,0,1),			# 2
'3':(1,1,1,1,0,0,1),			# 3
'4':(0,1,1,0,0,1,1),			# 4
'5':(1,0,1,1,0,1,1),			# 5
'6':(1,0,1,1,1,1,1),			# 6
'7':(1,1,1,0,0,0,0),			# 7
'8':(1,1,1,1,1,1,1),			# 8
'9':(1,1,1,1,0,1,1)}			# 9

count = 0				# Initialzie count
#
# This function configures the LED ports as outputs
#
def Configure_Port():
   for i in range(0, 7):
         L[i] = Pin(LED_Segments[i], Pin.OUT)
   
   for i in range(0, 2):
         D[i] = Pin(LED_Digits[i], Pin.OUT)


#
# Refresh the 7-segment display
#
def Refresh(timer):					# Thread Refresh
   global count
   cnt = str(count)					# into string
   if len(cnt) < 2:
      cnt = " " + cnt				# Make sure 2 digits
   for dig in range(2):				# Do for 2 digits
      for loop in range(0,7):
          L[loop].value(LED_Bits[cnt[dig]][loop])
      D[dig].value(1)
      utime.sleep(0.01)
      D[dig].value(0)

#
# Configure PORT to all outputs
#
Configure_Port()

#
# Main program loop. Start the periodic timer and counting
#
tim.init(freq=50, mode=Timer.PERIODIC, callback=Refresh)

while True:					# Do forever
   utime.sleep(1)			# Wait a second
   count = count + 1		# Increment count
   if count == 100:			# If count = 100
       count = 0
 

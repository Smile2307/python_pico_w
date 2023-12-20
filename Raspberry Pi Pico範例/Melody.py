#----------------------------------------------------------
#				MELODY MAKER - PLAY HAPPY BIRTHDAY
#				==================================
#
# In this project a buzzer is connected to port pin GP0
# which is configured as a PWM output. The program plays the
# melody Happy Birthday
#
# Author: Dogan Ibrahim
# File  : Melody.py
# Date  : February 2011
#------------------------------------------------------------
from machine import Pin, PWM    
import utime

ch = PWM(Pin(0))				            # PWM output at GP0
MaxNotes = 25
Durations = [0]*MaxNotes
#
# Melody frequencis
#
frequency = [262,262,294,262,349,330,262,262,294,262,
			   392,349,262,262,524,440,349,330,294,466,
			   466,440,349,392,349]
#
# Frequency durations
#
duration = [1,1,2,2,2,3,1,1,2,2,2,3,1,1,2,2,2,2,
			  2,1,1,2,2,2,3]

for k in range(MaxNotes):
    Durations[k] = 400 * duration[k]
    
while True:								# Do forever
    for k in range(MaxNotes):			# Do for all notes
        ch.duty_u16(32767)				# Duty cycle
        ch.freq(2*frequency[k])			# Play 2nd harmonics
        utime.sleep_ms(Durations[k])	# Durations
        utime.sleep_ms(100)				# Wait
    ch.duty_u16(0)						# Stop playing
    utime.sleep(3)						# Stop 3 seconds

    
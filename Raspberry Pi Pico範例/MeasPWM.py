#----------------------------------------------------------
#				MEASURE THE FREQUENCY AND DUTY CYCLE
#				====================================
#
# In this project a PWM wave is applied to the PIco. The
# frequency and duty cycle of this wave are measured and
# displayed on the Thonny screen.
#
# Author: Dogan Ibrahim
# File  : MeasFreq.py
# Date  : February 2011
#------------------------------------------------------------
from machine import Pin
import utime

PWMin = Pin(17, Pin.IN)				# PWM wave input

while True:							# Do forever
    while True:
        if PWMin.value() == 1:		# Wait while 0
            break
    Tmr1Strt = utime.ticks_cpu()    # Start timer 1
    
    while True:
        if PWMin.value() == 0:		# Wait while 1
            break
    Tmr1End = utime.ticks_cpu()		# End
    
    while True:
        if PWMin.value() == 1:		# Wait while 0
            break
            
    Tmr2End = utime.ticks_cpu()      # End
    
    Mark = utime.ticks_diff(Tmr1End, Tmr1Strt)
    Space = utime.ticks_diff(Tmr2End, Tmr1End)
    duty = 100.0 * Mark / (Mark + Space)
    freqkHz = 1000.0 / (Mark + Space)
    print("Duty Cycle = %5.2f" % duty)
    print("Frequency (kHz) = ", freqkHz, "\n")
    utime.sleep(2)

#----------------------------------------------------------
#				FREQUENCY GENERATOR
#				===================
#
# In this project a potentiometer is connected to channel 0
# of the Pico. Also, an LCD is connected. The program generates
# PWM waveforms of different frequencies as the potentiometer
# arm is moved
#
# Author: Dogan Ibrahim
# File  : FreqGen.py
# Date  : February 2011
#------------------------------------------------------------
from machine import Pin, PWM, ADC
import LCD
import utime

Pot = ADC(0)                    	# Pot at channel 0
LCD.lcd_init()

ch = PWM(Pin(16))					# PWM at GP16
ch.freq(100)						# Default freq
LCD.lcd_clear()
LCD.lcd_puts("Frequency(Hz)")

while True:							# Do forever
    frequency = Pot.read_u16()	    # Read pot data
    LCD.lcd_goto(0, 1)
    LCD.lcd_puts("                ")
    LCD.lcd_goto(0, 1)
    LCD.lcd_puts(str(frequency))
    ch.duty_u16(32767)
    ch.freq(frequency)				# Change the freuency
    utime.sleep(1)

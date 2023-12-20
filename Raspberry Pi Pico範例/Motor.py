#----------------------------------------------------------
#				CHANGING THE MOTOR SPEED
#				========================
#
# In this project a brushed DC motor is connected to the
# Pico.Additionally, a potentiometer is conencted to channel
# 0 of the ADC.Varying the potentiometer changes the motor speed
#
# Author: Dogan Ibrahim
# File  : Motor.py
# Date  : February 2011
#------------------------------------------------------------
from machine import Pin, PWM, ADC

Pot = ADC(0)                    	# Pot at channel 0
Motor = Pin(17, Pin.OUT)        	# Motor at GP17

ch = PWM(Pin(17))					# PWM at GP17
ch.freq(1000)						# Frequency = 1000Hz
  
while True:							# Do forever
    duty = Pot.read_u16()			# Read pot data
    ch.duty_u16(duty)				# Change duty cycle


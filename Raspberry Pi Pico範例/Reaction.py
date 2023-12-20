#--------------------------------------------------------
#				REACTION TIMER
#				==============
#
# This is a reaction timer program which measures the
# reaction of the user and displays on the LCD in ms.
# For a fast reaction time, the user should press the 
# pushbutton as soon as the LED is lit
#
# Author: Dogan Ibrahim
# File  : Reaction.py
# Date  : February 2011
#----------------------------------------------------------
import LCD
from machine import Pin
import utime
import random

Button = Pin(17, Pin.IN, Pin.PULL_UP)
LED = Pin(16, Pin.OUT)
LCD.lcd_init()
flag = 0

#
# This is the interrupt service routine. The progra jumps
# here as soon as the pushbutton is pressed
#
def MyButton(pin):
    global flag
    Button.irq(handler = None)
    LED.value(0)
    TmrEnd = utime.ticks_ms()
    ReactionTime = utime.ticks_diff(TmrEnd, TmrStart)
    ReactionStr = str(ReactionTime)
    flag = 1
    LCD.lcd_puts("Reaction Time:")
    LCD.lcd_goto(0, 1)
    LCD.lcd_puts(ReactionStr)
    utime.sleep(3)

#
# Start of MAIN program
#
LED.value(0)
while True:
    flag = 0
    LCD.lcd_clear()
    rnd = random.randint(3, 10)
    utime.sleep(rnd)
    LED.value(1)
    TmrStart = utime.ticks_ms()
    Button.irq(handler=MyButton, trigger = Pin.IRQ_FALLING)
    while flag == 0:
       pass
       


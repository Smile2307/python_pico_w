#----------------------------------------------------------
#           ULTRASONIC DISTANCE MESUREMENT
#           ==============================
#
# In this project a HC-SR04 type ultrasonic sensor module is
# connected to the Raspberry Pi Pico. The program displays
# distance to an object in-front of the sensor
#
# Author: Dogan Ibrahim
# File  : Ultrasonic.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin
import utime
import LCD

trig = Pin(16, Pin.OUT)					# trig pin
echo = Pin(17, Pin.IN)					# echo pin

LCD.lcd_init()							# Init LCD

while True:
    trig.value(0)
    utime.sleep_us(5)                 	# Wait until settled
    
    trig.value(1)						# Send trig pulse
    utime.sleep_us(10)					# 10 microseconds
    trig.value(0)						# Remove trig pulse
    
    while echo.value() == 0:			# Wait for echo 1
        pass
    Tmrstrt = utime.ticks_us()
    
    while echo.value() == 1:			# Wait for echo 0
        pass
    Tmrend = utime.ticks_us()

    Duration = utime.ticks_diff(Tmrend, Tmrstrt)
    distancecm = Duration * 0.0171
    LCD.lcd_clear()
    D = "Dist = " + str(distancecm)[:6] + " cm"
    LCD.lcd_puts(D)
    utime.sleep(1)
    
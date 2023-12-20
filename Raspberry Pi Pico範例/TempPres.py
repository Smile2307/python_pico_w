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

trig = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)

LCD.lcd_init()

while True:
    trig.value(0)
    utime.sleep_us(5)                 # Wait until sensor settler
    trig.value(1)
    utime.sleep_us(10)
    
    trig.value(0)
#    Tmrstrt = utime.ticks_ms()
    while echo.value() == 0:
        pass
    Tmrstrt = utime.ticks_ms()
    
    while echo.value() == 1:
        pass
    Tmrend = utime.ticks_ms()
    
    Duration = utime_ticks_diff(Tmrend, Tmrstrt)
    distancemetres = (Duration * 340.0) / 2.0
    distancecm = 100.0 * distancemetres
    print(distancecm)
    utime.sleep(1)
    
    
    
    
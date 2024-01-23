from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
status= False

while True:
    if button.value():
        #led.toggle()
        status = not(status)
        led.value(status)
        time.sleep(0.5)
from machine import Pin
from time import sleep
led = Pin("LED", Pin.OUT)
#led = Pin(0, Pin.OUT)
while True:
    led.value(1)
    print("LED on")
#led.value(0)
    sleep(1)
    led.value(0)
    print("LED off")
    sleep(1)

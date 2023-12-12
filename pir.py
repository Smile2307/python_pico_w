from machine import Pin
import utime

pir_sensor = Pin(28, Pin.IN)
led = Pin("LED", Pin.OUT)

while True:
    if pir_sensor.value() == 1:
        print("偵測到動作!")
        led.value(1)
        utime.sleep(5)
        led.value(0)
    else:
        print("無動作")
    utime.sleep(1)

import time, _thread
from machine import Pin

def task(n, delay):
    led = Pin("LED", Pin.OUT)
    for i in range(n):
        led.on()
        time.sleep(delay)
        led.off()
        time.sleep(delay)
    print('done')

_thread.start_new_thread(task, (10, 3))

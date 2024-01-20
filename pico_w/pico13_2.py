from machine import Pin
import time
led=Pin(15,Pin.OUT)
btn_1=Pin(14,Pin.IN,Pin.PULL_DOWN)
is_press = False
led_status=False

def btn_detect(mybtn):
    global is_press
    global led_status

    if mybtn.value():
        #消除debound
        time.sleep(0.05)
        if mybtn.value():
            is_press = True
    elif is_press:
        #消除debound
        time.sleep(0.05)
        if not mybtn.value():
            led_status = not led_status
            led.value(led_status)
            is_press = False

while True:
    btn_detect(btn_1)
    


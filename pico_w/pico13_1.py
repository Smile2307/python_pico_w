from machine import Pin
import time
led=Pin(15,Pin.OUT)
btn=Pin(14,Pin.IN,Pin.PULL_DOWN)
is_press = False
led_status=False

while True:
    #print(btn.value())
    if btn.value():
        #消除debound
        time.sleep(0.05)
        if btn.value():
            #print("按下")
            is_press = True
        #led.value(1)
        #led.on()
    elif is_press:
        #led.value(0)
        #print('release')
        #消除debound
        time.sleep(0.05)
        if not btn.value():
            led_status = not led_status
            led.value(led_status)
            is_press = False
        #led.off()
    #led.value(is_press)
    #time.sleep_ms(300)
        
    #time.sleep(0.2)
    

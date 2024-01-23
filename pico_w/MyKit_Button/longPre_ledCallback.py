config = {'btn':14, 'led':15, 'long':2000}

import time
from machine import Pin
from MyKit_Button import myButton

btn = myButton(config['btn'])  
led = Pin(config['led'], Pin.OUT)    # 內建 LED => ESP8266:D4, ESP32:D2


def led_blink(times=3, ms_on=100, ms_off=100):
    for i in range(times):
        print(f'{i}. LED 亮', end=' ... ')
        led.on()
        time.sleep_ms(ms_on)
        print('LED 滅')
        led.off()
        time.sleep_ms(ms_off)    

def test():
    btn.callback(led_blink)
    print(f'當長按超過 {config["long"]} 毫秒後再放開, 會自動執行一次LED閃爍程式')
    while True:
        btn.longPressed(config['long'], 6, 1000, 500)  # 長按後, LED 閃 3 次, 每次亮 100 毫秒, 滅 200 毫秒
test()
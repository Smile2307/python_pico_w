config = {'btn':14, 'led':15}

import time
from machine import Pin
from MyKit_Button import myButton

led = Pin(config['led'], Pin.OUT)    # 內建 LED => ESP8266:D4, ESP32:D2
btn = myButton(config['btn'])

def led_blink(times=3, ms_on=100, ms_off=100):
    for _ in range(times):
        led.on()
        time.sleep_ms(ms_on)
        led.off()
        time.sleep_ms(ms_off)     

def test():
    btn.callback(led_blink)
    while True:
        btn.atPressed(3, 1000, 500)  # 按下, 閃 3 次, 每次亮 100 毫秒, 滅 200 毫秒

test()
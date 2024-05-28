config = {'btn':14, 'led':0}

import time
from machine import Pin
from MyKit_Button import myButton

led = Pin(config['led'], Pin.OUT)    # 內建 LED => ESP8266:D4, ESP32:D2
btn = myButton(config['btn'])

def test():
    print('\n==> 執行 5 次開關的按下測試 !!')
    while btn.counter < 5:
        if btn.atPressed():  # 瞬間偵測：偵測按鈕開關被 "按下" 的瞬間
            print(f'按下第{btn.counter}次')
            led.value(not led.value())
        time.sleep_ms(100)
test()


    
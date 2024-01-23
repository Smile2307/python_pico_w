config = {'btn':14, 'led':15}

import time
from machine import Pin
from MyKit_Button import myButton

led = Pin(config['led'], Pin.OUT)    # 內建 LED => ESP8266:D4, ESP32:D2
btn = myButton(config['btn'])

def test():
    print('\n==> 執行 5 次開關的按下後放開的測試 !!')
    counter = 0 
    while counter < 5:
        if btn.atReleased():  # 瞬間偵測：偵測按鈕開關被 "放開" 的瞬間
            counter += 1
            print(f'按下後再放開的第{counter}次')

test()
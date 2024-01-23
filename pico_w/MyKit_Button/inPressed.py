config = {'btn':14, 'led':15}

import time
from machine import Pin
from MyKit_Button import myButton

led = Pin(config['led'], Pin.OUT)    # 內建 LED => ESP8266:D4, ESP32:D2
btn = myButton(config['btn'])

def test():
    print('\n==> 執行 5 次開關的按下測試 !!')
    while btn.counter < 5:
        if btn.inPressed():  # 狀態偵測：目前一直處於 "按下" 的狀態 (長時間偵測)
            print(f'按下第{btn.counter}次')
            led.on()
        else:
            led.off()
        time.sleep_ms(100)
test()


    

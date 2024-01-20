from machine import Pin
import time
import urequests as requests
from tools import connect,reconnect

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
led_status = False
#switch button
#解決彈跳

def btn_detect(btn1):
    global is_press,led_status    
    if btn1.value():
        time.sleep_ms(50)
        if btn1.value():
            is_press = True
    elif is_press:
        time.sleep_ms(50)
        if btn1.value() == False:
            print('release')
            led_status = not led_status        
            red_led.value(led_status)        
            is_press = False
            try:
                if led_status == True:
                    get_url = 'https://blynk.cloud/external/api/update?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v0=1'
                else:
                    get_url = 'https://blynk.cloud/external/api/update?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v0=0'
                response = requests.get(get_url)
            except:
                reconnect()
            else:
                if response.status_code == 200:
                    print("傳送成功")
                else:
                    print("server有錯誤訊息")
                    print(f'status_code:{response.status_code}')
                    
                response.close()
    

connect()
while True:
    btn_detect(btn)
    
    
    
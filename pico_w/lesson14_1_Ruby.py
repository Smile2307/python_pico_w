from machine import Timer, Pin, ADC
import time
from tools import connect, reconnect
import urequests as requests

led_status = 0

def fun10(t:Timer | None = None):    
    print('5秒')
    #led.toggle() #turn on/off led

def fun10ms(t:Timer):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')

def updateDV(t:Timer):
    global led_status
    light_value = light.read_u16()
    vr_value = vr.read_u16()
        
    try:
        if led_status == 0:
            led_status = 1
        else:
            led_status = 0
            
        url = f'https://blynk.cloud/external/api/batch/update?token=Mcr1vSCkqhfcoFpDr5aMN92mDNWKD0EC&v1={vr_value}&v2={light_value}&v0={led_status}'
        response = requests.get(url)
    except:
        #連線失敗
        reconnect()
    else:
        #連線成功且get回傳成功
        if response.status_code == 200:
            print('連線成功')
            print(f'light:{light.read_u16()}')
            print(f'vr:{vr.read_u16()}')
            print(f'led:{led_status}')
            led.value(led_status)
        else:
        #連線成功但server有問題
            led_status = 0
            print("server有錯誤訊息")
            print(f'status_code:{response.status_code}')
        response.close()
    
    

connect()
led = Pin(15, Pin.OUT)
light = ADC(Pin(28)) #光敏電阻接Pin28
vr = ADC(Pin(27)) #可變電阻接Pin27
timer10 = Timer(period=5000, mode=Timer.PERIODIC, callback=fun10)
#timer10ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun10ms)
timerUpdate = Timer(period=500, mode=Timer.PERIODIC, callback=updateDV)
fun10() #trigger function first







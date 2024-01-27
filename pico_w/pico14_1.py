from machine import Timer,ADC,Pin
import utime
from tools import connect,reconnect
import urequests as requests

#url='https://blynk.cloud/external/api/batch/update?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v1=65535&v0=1&v2=12345'

led = Pin(15,Pin.OUT)
light = ADC(Pin(28))
vr = ADC(Pin(27))

led_status = 0
vr_value = 0
light_value = 0

def fun10(t:Timer|None=None):
    global led_status
    #print("10秒了")
    #led_status = led.value(not led.value())
    led_status = not led_status
    led.value(led_status)
    
def fun500ms(t:Timer|None=None):
    global vr_value,light_value
    vr_value = vr.read_u16()
    light_value = light.read_u16()
    #print(f"light: {light_value}")
    #print(f"vr: {vr_value}")

def funblynk(t:Timer|None=None):
    global vr_value,light_value,led_status
    led_int = int(led_status)
    print(f"led: {led_int}")
    print(f"light: {light_value}")
    print(f"vr: {vr_value}")
    #url=f'https://blynk.cloud/external/api/batch/update?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v1={vr_value}&v0={led_status}&v2={led_int}'
    url=f'https://blynk.cloud/external/api/batch/update?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v1={vr_value}&v2={light_value}'
    try:
        led.on()
        response = requests.get(url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("server有錯誤訊息")
            print(f'status_code:{response.status_code}')
        response.close()
    led.off()
    
        
    
connect()

#第一次即執行    
fun500ms()	
#fun10()
funblynk()

#每10秒執行一次
#timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
#timer500ms = = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)

timerblynk = Timer(period=10000, mode=Timer.PERIODIC, callback=funblynk)


#while True:
#    pass
    
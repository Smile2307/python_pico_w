from tools import connect,reconnect
from machine import WDT,Timer,ADC,RTC
import time


def alert(t:float):
    print('要爆炸了!')
    rtc = RTC()
    date_tuple = rtc.datetime()
    year = date_tuple[0]
    month = date_tuple[1]
    day = date_tuple[2]
    hour = date_tuple[4]
    minites = date_tuple[5]
    second = date_tuple[6]
    date_str = f'{year}-{month}-{day} {hour}:{minites}:{second}'
    try:
        response = requests.get('https://hook.us1.make.com/lwylhnsajcmk7kfpnog7kmb8l25894u7?name=robert&date=%E4%BB%8A%E5%A4%A9&temperature=56.987')
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("server有錯誤訊息")
            print(f'status_code:{response.status_code}')
        response.close()
    
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert(temperature)
        start = time.ticks_ms()#重新設定計時的時間
        

connect()       

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒    
time1 = Timer()
time1.init(period=1000,callback=callback1)
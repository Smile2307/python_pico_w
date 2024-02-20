import time
from machine import ADC,Timer 

counter = 0

def alert():
    print("要爆炸了!")

def callback1(t):
    global start	#建立外變數
    sensor =ADC(0)	#ADC的第4個channel，pio26(0)、27(1)、28(2)、29(3,參考電壓用)、Temperture sensor(4,無腳位顯示)
    #sensor =ADC(4)	#ADC的第4個channel，pio26(0)、27(1)、28(2)、29(3,參考電壓用)、Temperture sensor(4,無腳位顯示)
    #sensor.read_u16():12進位轉16作位
    vol = sensor.read_u16() *(3.3 / 65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f"溫度:{temperature:.2f}")
    
    delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
    print(delta)
    #溫度>24 且 間隔60秒後才會執行alert()
    if temperature >=27 and delta >= 60 * 1000:
        alert()
        #重新計時
        start = time.ticks_ms()
start = time.ticks_ms() - 60 *1000	#第1次發生時即可執行alter

time1 = Timer()
time1.init(freq=1,callback=callback1) 
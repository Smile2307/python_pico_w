import time
from machine import ADC,Timer 

counter = 0

def alert():
    print("要爆炸了!")

def callback1(t):
    global start	#建立外變數
    sensor =ADC(4)
    vol = sensor.read_u16() *(3.3 / 65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f"溫度:{temperature}")
    
    delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
    print(delta)
    #溫度>24 且 間隔60秒後才會執行alert()
    if temperature >=22 and delta >= 60 * 1000:
        alert()
        #重新計時
        start = time.ticks_ms()
start = time.ticks_ms() - 60 *1000	#第1次發生時即可發alter

time1 = Timer()
time1.init(freq=1,callback=callback1) 
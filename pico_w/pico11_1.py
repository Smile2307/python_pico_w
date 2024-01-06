import network
import time
from machine import WDT
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('Smile_S23', '0939763309b')

max_wait = 10

#處理正在連線
while max_wait > 0:
    max_wait -= 1
    status = nic.status()
    if status < 0 or status >=3:
        break
    print("等待連線")
    time.sleep(1)


    
#沒有wifi的處理
if nic.status() != 3:
    #連線失敗,重新開機(開發完成商品時使用)
    #wdt = WDT(timeout=2000)
    #wdt.feed()
    
    #開發時使用
    raise RuntimeError('連線失敗')
    
else:
    print("成功連線")
    print(nic.ifconfig())
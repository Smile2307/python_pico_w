#ref https://iotstarters.com/custom-android-app-with-ds18b20-sensor-and-raspberry-pi-pico-w/
from machine import Pin
import network
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep
import urequests as requests

ssid = 'Smilewireless' #Your network name
password = '0939763309' #Your WiFi password

led_onboard = Pin("LED", Pin.OUT)
mydata = 0
#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
    led_onboard.value(0)
    print('Connecting...')
    sleep(1)
ip = wlan.ifconfig()[0]
print('Connection successful')
print(f'Connected on {ip} \n')
led_onboard.value(1)

# Initialization GPIO, OneWire and DS18B20
one_wire_bus = Pin(26) #pin 31 in PICO W
sensor_ds = DS18X20(OneWire(one_wire_bus))

# Discover one-wire devices
devices = sensor_ds.scan()

# Create the connection to our Firebase database - don't forget to change the URL!
import ufirebase as firebase
firebase_url="https://pico-test-89fc9-default-rtdb.firebaseio.com/"
firebase.setURL(firebase_url)

def firebase_callback(data):
    #global retrieved_data
    retrieved_data = data
    print("從 Firebase 獲取的數據:", retrieved_data)

while True:
    try:
        '''
    # Measure temperature
        sensor_ds.convert_temp()
    # Query sensors
        for device in devices:
                temp = sensor_ds.read_temp(device)
                temp_C = "{:.1f}".format(temp)
                #print('Temp_C :', temp_C , '°C')
                temp_f = ((sensor_ds.read_temp(device)) * (9/5) + 32)
                temp_F = "{:.1f}".format(temp_f)
                #print('Temp_F:', temp_F, '°F \n')
                
        '''
        temp_C=18.4
        firebase.put("random/data", temp_C, bg=0)
        #目前無法正確抓取資料 get(PATH, DUMP, id, cb, limit)
        sleep(5)
        #mydata=firebase.get("random/data", 1, bg=0)
        # 使用 get 方法從 Firebase 獲取數據
        #firebase.get("random/data", "mydata", bg=0, cb=get_callback)
        #mydata=firebase.get("random/", "data", bg=False,  id=0, limit=False)
        #retrieved_data = {}  # 用來存儲從 Firebase 獲取的數據
        #firebase.get("random/data", "retrieved_data", bg=0)
        #firebase.get("/random/data", "mydata")
        print("fb_data: ",firebase.mydata)
        #response=requests.get(firebase_url+"random/data.json")
        '''
        response=requests.get(firebase_url+"random.json")

        data=response.json()
        response.close()
        print(data)
        '''
        # 打印從 Firebase 獲取的數據
        #print("從 Firebase 獲取的數據:", mydata)
                
    except OSError as e:
        #continue
        print('Connection closed')
        


       
#ref https://github.com/ckoever/micropython-firebase-realtime-database
#firebase project:Esp32_timer
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

ssid = 'Smilewireless' #Your network name
password = '0939763309' #Your WiFi password

# 拆解firebase的資料內容
def myparser(Tdata,sp,star=0,mystep=1):
    #print("Tdata: ",Tdata)
    #print("Tdata type: ",type(Tdata))
    tdata=Tdata.split(sp)
    
    for i in range(star, len(tdata),mystep):
        #print(i, end=" ")
        t_data=tdata[i].strip('[]')
        print(f"datavalue_{i}:{t_data} ")

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect(ssid, password)

firebase_url="https://water-system-d5605-default-rtdb.firebaseio.com/"

while not GLOB_WLAN.isconnected():
  pass

#firebase example
import ufirebase as firebase
firebase.setURL(firebase_url)

#Put Tag1
#firebase.put("testtag", "1234", bg=0)
#temp_C=18.4
firebase.put("Esp32_timer/humi", 78, id=0, bg=0)
MOD_TIME.sleep(.1)
firebase.put("Esp32_timer/temp", 17.6, id=0, bg=0)

#Put Tag2
#firebase.put("lolval/testval", {"somenumbers": [1,2,3], "something": "lol","nothing": ("1","0","1")}, bg=0)
#Get Tag1

MOD_TIME.sleep(.1)
firebase.get("Esp32_timer", "data", bg=0)
mydata = firebase.data
print("mydata: "+str(mydata))
print("Switch: ",mydata['Switch'])
print("Timer: ",mydata['Timer'])
print("Timer_value: ",mydata['Timer_value'])


        
myparser(mydata['Timer_value'],',')

print("Type: ",mydata['Type'])

print("Watering: ",mydata['Watering'])

myparser(mydata['Watering'],',',0)

print("Watering_value: ",mydata['Watering_value'])
myparser(mydata['Watering_value'],',',0)

print("Week: ",mydata['Week'])
myparser(mydata['Week'],',',0)

print("humi: ",mydata['humi'])
print("temp: ",mydata['temp'])
'''
MOD_TIME.sleep(.1)
firebase.get("lolval/testval", "A0", bg=0)
print("testA0: "+str(firebase.A0))

print("something: ",firebase.A0['something'])
print("somenumbers_0: ",firebase.A0['somenumbers'][0])
print("somenumbers_1: ",firebase.A0['somenumbers'][1])
print("somenumbers_2: ",firebase.A0['somenumbers'][2])
print("nothing_0: ",type(firebase.A0['nothing'][0]))
'''     
#print("test0: "+str(firebase.A0[something].value))
#print("test1: "+str(firebase.A0[something].value))
#print("test2: "+str(firebase.A0[somenumbers][2]))

'''
#Get Tag2
def callbackfunc():
  print("\nlolval_1: "+str(firebase.lolwhat["lolval"]["testval"][somenumbers][0])+
  "\nlolval_2: "+str(firebase.lolwhat["lolval"]["testval"][somenumbers][1])+
  "\nlolall: "+str(firebase.lolwhat))

firebase.get("lolval/testval", "lolwhat", bg=1, cb=(callbackfunc, ()))
#firebase.get("lolval/testval/somenumbers", "a1",id=1, bg=1, cb=(callbackfunc, ("lolval/testval/somenumbers","1", "a1")))
#firebase.get("lolval/testval/somenumbers", "a2",id=2, bg=1, cb=(callbackfunc, ("lolval/testval/somenumbers","2", "a2")))
print(end="Im getting lolval now")

#Do something in this time
while 1:
  print(end=".")
  MOD_TIME.sleep(1)
  try: 
    print(firebase.lolwhat)
    break
  except:
    pass
'''
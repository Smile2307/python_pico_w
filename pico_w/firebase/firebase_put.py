import urequests as requests
from tools import connect,reconnect
from machine import WDT,Timer,ADC,RTC
import time
import random

connect()

def generate_data():
    return {
        'data':random.uniform(20,100)
        }

firebase_url='https://pico-test-89fc9-default-rtdb.firebaseio.com/random/data.json'
auth_data={
        "email":"smile.lin309@gmail.col",
        "password":"smile@1234",
        "returnSecureToken":"True"
    }
auth_response= requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCBt4PQcIekM1wdYOCnbv54A0d-1Hw_3XY",json=auth_data)
auth_response_data=auth_response.json()
print(auth_response_data)
auth_response.close()
local_id=auth_response_data.get('localId')
print(local_id)

while True:
    randomData=generate_data()
    print(randomData)
    response=requests.post(firebase_url,json=randomData)
    data=response.json()
    response.close()
    print(data)
    time.sleep(1)

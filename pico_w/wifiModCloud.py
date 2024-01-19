from wifiModCloud import WifiModCloud
import time

wmc = WifiModCloud()
#
wmc.connect_wifi(ssid="Smilewireless",password="0939763309")
wmc.connect_wifi("Smil309","0939763309b")

wmc.setdb_to_firebase(host="https://water-system-d5605-default-rtdb.firebaseio.com/",auth="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkIjp7InVpZCI6IjI3ZDlhM2U5LTlhZDYtNDQ2Mi1hY2U3LTY1ZmI4MjFhMWJhYiIsInByb2plY3QiOiJFc3AzMl93bV9PVEFfRmRiIiwiZGV2ZWxvcGVyIjoic21pbGU6bGluMzA5QGdtYWlsOmNvbSJ9LCJ2IjowLCJleHAiOjE2NzU1MDQzOTEwLCJpYXQiOjE2NzA4MTM1MTB9.7QqsxdAflkEd7yvEyb_57GyAoSZTIRJ0viAT61-4t4M",tree="Esp32_timer")
wmc.set_value(key="temp",value=28.54)
time.sleep(5)
#get_value=wmc.get_value(key="MyNumber")
#print("Retrieved number={}",format(get_value))
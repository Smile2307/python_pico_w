# Import Library
from linenotify import LineNotify
from network import WLAN,STA_IF

# Network Setup
#ssid = '<ssid>'
#password = '<password>'
ssid = 'Smile_S23'
password = '0939763309b'
#ssid = 'Smilewireless'
#password = '0939763309'
wlan = WLAN(STA_IF)
wlan.active(True)
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Set Line Token 
#line = LineNotify('<token>')
line = LineNotify('RRkyUxrZa8jjo0DPRchWdSqsjkOdyOUEY1Di5GSHqRO')
# Notify text message 
line.notify('Hello World!')
# Notify sticker with message
line.notifySticker(3,240,'Nice Sticker')
# Notify image from URL with message
line.notifyImageURL('https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Pochita.PNG','Pochita')

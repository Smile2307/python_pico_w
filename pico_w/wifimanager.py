import network
import socket

# 初始化 WiFi 設備
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# 掃描可用網路
networks = wlan.scan()
network_list = [network[0].decode('utf-8') for network in networks]

# 設定為 AP 模式
ap = network.WLAN(network.AP_IF)
#必須先停止，然後再設定，再啟動，才能設定成功
ap.active(False)
ap.config(essid='Pico-W-AP', password='12345678')
ap.active(True)
# 獲取 Pico W 的 AP 模式 IP 地址WPA/WPA2-PSK
ip_address = ap.ifconfig()[0]
print("ip_address:",ip_address)
print("ssid:",ap.ifconfig())

# 創建一個網頁服務器
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

# 網頁服務器循環
while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    request = str(request)
    
    # HTML 頁面
    response = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Pico W WiFi Setup</title>
    </head>
    <body>
        <h1>Pico W WiFi Setup</h1>
        <p>Pico W IP: {ip_address}</p>
        <form action="/" method="get">
            <label for="ssid">SSID:</label>
            <select id="ssid" name="ssid">"""
    for network in network_list:
        response += f"<option>{network}</option>"
    response += """</select><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Connect">
        </form>
    </body>
    </html>
    """
    
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()

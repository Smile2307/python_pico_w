from machine import UART, Pin
import json
import time

class WifiConnector:
    def __init__(self, uart_port=0, baudrate=57600, tx_pin=16, rx_pin=17):
        self.uart = UART(uart_port, baudrate=baudrate, tx=Pin(tx_pin), rx=Pin(rx_pin))

    def connect_wifi(self, ssid, password):
        wifi_command = {
            "command": "connect_wifi",
            "ssid": ssid,
            "password": password
        }
        self.send_command(wifi_command)
        response = self.wait_for_response()
        return response

    def send_command(self, command):
        command_str = json.dumps(command) + '\n'
        print("發送的命令字串:", command_str)  # 打印发送的命令字符串
        self.uart.write(command_str)

    def wait_for_response(self, timeout=10):
        start_time = time.ticks_ms()
        response = bytearray()
        while time.ticks_diff(time.ticks_ms(), start_time) < timeout * 1000:
            if self.uart.any():
                response += self.uart.read(self.uart.any())
                if response.endswith(b'\n'):
                    break
            time.sleep(0.1)
        
        response_str = response.decode('utf-8').strip()
        print("原始响应字符串:", response_str)  # 打印原始响应字符串

        try:
            return json.loads(response_str)
        except ValueError as e:
            print("JSON 解析錯誤:", e)
            return None

# 使用範例
wifi = WifiConnector()
response = wifi.connect_wifi('Smilewireless', '0939763309')
print("Response:", response)

from machine import Pin, SoftSPI
import ssd1306
from time import sleep

spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

dc = Pin(4)   # data/command
rst = Pin(5)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

oled = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)
 
oled.text('Welcome to', 0, 0)
oled.text('ENGINEERSGARAGE', 0, 16)

oled.show()
sleep(2)
oled.text('Have fun with', 0, 35)
oled.text('MicroPython', 0, 45)        
oled.show()
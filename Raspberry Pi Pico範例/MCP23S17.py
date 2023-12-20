#----------------------------------------------------------
#		SPI BUS PORT EXPANDER
#		=====================
#
# In this project the SPI bus compatible MCP23S17 chip is used
# to add 16 more ports to Raspberry Pi Pico.An LED is connected
# to pin GPA0 of the expander and the LED is flashed every
# second
#
# Author: Dogan Ibrahim
# File  : MCP23S17.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,SPI
import utime

spi_sck = Pin(2)					# SCK pin at GP2
spi_tx = Pin(3)						# TX pin at GP3
spi_rx = Pin(0)						# RX pin at GP0 (not used)

spi = SPI(0,sck=spi_sck,mosi=spi_tx,miso=spi_rx,baudrate=100000)

Device_Address = 0x40				# MCP23S17 SPI address
MCP_GPIOA = 0x12                    # MCP23S17 GPIOA address
MCP_IODIRA = 0                      # MCP IODIRA address
CS = Pin(16, Pin.OUT)				# CS
CS.value(1)							# Disable chip

#
# This function configures PORTA as output
#
def Configure():
    buff = [0, 0, 0]
    buff[0] = Device_Address
    buff[1] = MCP_IODIRA
    buff[2] = 0
    CS.value(0)
    spi.write(bytearray(buff))
    CS.value(1)

#
# This function sends data to register RegAddr
#
def Send(RegAddr, data):
    buff = [0, 0, 0]
    buff[0] = Device_Address
    buff[1] = RegAddr
    buff[2] = data
    CS.value(0)
    spi.write(bytearray(buff))
    CS.value(1)

#
# Main program reads and displays the temperature every second
#
while True:
    Configure()
    
    while True:
        Send(MCP_GPIOA, 1)				# LED ON
        utime.sleep(1)					# 1 second delay
        Send(MCP_GPIOA, 0)				# LED OFF
        utime.sleep(1)					# 1 second delay

#----------------------------------------------------------
#		GENERATE SINE WAVEFORM
#		======================
#
# In this project a MCP4921 type DAC chip is connected to the
# Raspberry Pi Pico.The program generates a sine waveform with
# the specifications given in the text
# 
# Author: Dogan Ibrahim
# File  : Sine.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, SPI
import utime
import math

spi_sck = Pin(2)					# SCK pin at GP2
spi_tx = Pin(3)						# TX pin at GP3
spi_rx = Pin(0)						# RX pin at GP0 (not used)

spi = SPI(0,sck=spi_sck,mosi=spi_tx,miso=spi_rx,baudrate=100000)

CS = Pin(16, Pin.OUT)					# CS
CS.value(1)								# Disable chip

R = 0.0628
T = 100
Conv = 4095.0 / 3.3
PeaktoPeak = 1.4 * Conv					# 1.4V
ReqDCoffset = 1.0 * Conv				# 1.6V

def DAC(data):
    buff = [0, 0]
    buff[0] = (data >> 8) & 0x0F		# HIGH byte
    buff[0] = buff[0] + 0x30
    buff[1] = data & 0xFF				# LOW byte
    CS.value(0)							# Enable MCP4921
    spi.write(bytearray(buff))			# Send to SPI bus
    CS.value(1)							# DIsable MCP4921

#
# Main program
#
sins=[0]*101

for i in range (101):
    sins[i] = ReqDCoffset+PeaktoPeak/2 + PeaktoPeak/2 * math.sin(R*i)
    
while True:
    for k in range(101):
        value = sins[k]
        DAC(int(value))
        utime.sleep_us(200)
        
    
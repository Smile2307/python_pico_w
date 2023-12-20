#----------------------------------------------------------
#		GENERATE ARBITRARY WAVEFORM
#		===========================
#
# In this project a MCP4921 type DAC chip is connected to the
# Raspberry Pi Pico.The program generates an arbitarry waveform
# whose characteristics are defined in the text
# 
# Author: Dogan Ibrahim
# File  : Arbitrary.py
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

Waveform = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.6,1.6,1.6,1.6,
                    1.4,1.2,1.0,0.8,0.6,0.4,0.2,0.0]

def Voltage(V):
    Amplitude = int(V * 4095 / 3.3)
    return Amplitude
    
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
while True:
    for k in range(21):
        DAC(int(4095*Waveform[k]/3.3))
        utime.sleep_ms(1)
        
    
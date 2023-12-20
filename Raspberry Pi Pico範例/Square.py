#----------------------------------------------------------
#		GENERATE SQUARE WAVE SIGNAL WITH AMPLITUDE +2V
#		==============================================
#
# In this project a MCP4921 type DAC chip is connected to the
# Raspberry Pi Pico.The program generates a square wave signal
# with frequency f=500Hz, 50% duty cycle (ON and OFF tiems equal
# and each 1ms), and 2V amplitude
#
# Author: Dogan Ibrahim
# File  : Square.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, SPI, Timer
import utime

spi_sck = Pin(2)					# SCK pin at GP2
spi_tx = Pin(3)						# TX pin at GP3
spi_rx = Pin(0)						# RX pin at GP0 (not used)

spi = SPI(0,sck=spi_sck,mosi=spi_tx,miso=spi_rx,baudrate=100000)

CS = Pin(16, Pin.OUT)				# CS
CS.value(1)							# Disable chip

ONvalue = int(2000 * 4095 / 3300)	# For +2V amplitude
OFFvalue = 0

tim = Timer()
flag = 0

def DAC(timer):
    global flag, Onvalue, OFFvalue
    buff = [0, 0]
    if flag == 0:
        data = ONvalue
        flag = 1
    else:
        data = OFFvalue
        flag = 0
        
    buff[0] = (data >> 8) & 0x0F	# HIGH byte
    buff[0] = buff[0] + 0x30
    buff[1] = data & 0xFF			# LOW byte
    CS.value(0)						# Enable MCP4921
    spi.write(bytearray(buff))		# Send to SPI bus
    CS.value(1)						# DIsable MCP4921

#
# Main program
#
tim.init(freq = 250, mode = Timer.PERIODIC, callback =DAC)
while True:
    pass


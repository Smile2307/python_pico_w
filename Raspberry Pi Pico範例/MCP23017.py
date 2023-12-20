#----------------------------------------------------------
#		I2C PORT EXPANDER
#		=================
#
# In this project the MCP23017 port expander chip is used.
# An LED is connected to port pin GPA0 of the port expander
# and this LED is flashed every second
#
# Author: Dogan Ibrahim
# File  : MCP23017.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=",i2c.scan())

Device_Address = 0x20					# MCP23017 I2C address
MCP_GPIOA_REG = 0x12					# MCP23017 GPIOA address
MCP_IODIRA_REG = 0						# MCP23017 IODIRA Address

conf = [MCP_IODIRA_REG, 0]				# Configure as output
buff1 = (MCP_GPIOA_REG, 0)				# Set GPIOA to 0
buff0 = [MCP_GPIOA_REG, 1]				# Set GPIOA to 1

i2c.writeto(Device_Address, bytearray(conf))

while True:
    i2c.writeto(Device_Address, bytearray(buff1))
    utime.sleep(1)
    i2c.writeto(Device_Address, bytearray(buff0))
    utime.sleep(1)
 
    
#----------------------------------------------------------
#		I2C PORT EXPANDER
#		=================
#
# In this project the MCP23017 port expander chip is used.
# An LED is connected to port pin GPA0 of the port expander
# and this LED is flashed every second
#
# This version of the program uses the i2c memory functions
#
# Author: Dogan Ibrahim
# File  : MCP23017-2.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=",i2c.scan())

Device_Address = 0x20					# MCP23017 I2C address
MCP_GPIOA_REG = 0x12					# MCP23017 GPIOA address
MCP_IODIRA_REG = 0						# MCP23017 IODIRA Address

i2c.writeto_mem(Device_Address, MCP_IODIRA_REG, b'0')

while True:
    i2c.writeto_mem(Device_Address, MCP_GPIOA_REG, b'1')
    utime.sleep(1)
    i2c.writeto_mem(Device_Address, MCP_GPIOA_REG, b'0')
    utime.sleep(1)
 
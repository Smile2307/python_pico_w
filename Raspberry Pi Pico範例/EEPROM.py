#----------------------------------------------------------
#		I2C EEPROM READ/WRITE
#		=====================
#
# In this project a 24LC256 type I2C EEPROM memory chip is
# connected to the Raspberry Pi Pico. The program writes and
# then reads from the memory
#
# Author: Dogan Ibrahim
# File  : EEPROM.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=",i2c.scan())

len = 4
Device_Address = 0x50					# EEPROM I2C address

#
# This function reads len bytes starting from specified memory
# address memloc (16 bits)
#
def Read(memloc, len):
    data = [0]*4
    data = i2c.readfrom_mem(Device_Address, memloc, 4,addrsize=16)
    return(data)

#
# This function writes the data to starting from the specified
# memory address memloc (16 bits)
#
def Write(memloc, data,len):
    i2c.writeto_mem(Device_Address, memloc, data, addrsize = 16)
    utime.sleep_ms(10)
        
wmsg = '1357'					# Data to be written
rmsg = [0]*len					# List for return data
Write(0x1000, wmsg, len)		# Write the data
rmsg = Read(0x1000, len)		# Read the data

#
# Display the data read starting from address 0x1000
#
print("Data read is: %c%c%c%c\n" %(rmsg[0],rmsg[1],rmsg[2],rmsg[3]))

          
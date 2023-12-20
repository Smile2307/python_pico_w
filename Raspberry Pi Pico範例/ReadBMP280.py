#----------------------------------------------------------
#		BMP280 TEMPERATURE AND PRESSURE SENSOR
#		======================================
#
# In this project the BMP280 temperature and pressure sensor
# chip is used and the readings are displayed on the screen
# every 5 seconds
#
# Author: Dogan Ibrahim
# File  : ReadBMP280.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin,I2C
import utime
#import machine
import utime

i2c = machine.I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
print("i2c address=" ,i2c.scan())

#
# THis function returns the temperature and pressure readings
# Adapted for the RAspberry Pi Pico from:
#
# https://github.com/ControlEverythingCommunity/
#       BMP280/blob/master/Python/BMP280.py
#
def BMP280():
    # BMP280 address, 0x76(118)
    # Read data back from 0x88(136), 24 bytes
    b1 = i2c.readfrom_mem(0x76, 0x88, 24)

    # Convert the data
    # Temp coefficents
    dig_T1 = b1[1] * 256 + b1[0]
    dig_T2 = b1[3] * 256 + b1[2]
    if dig_T2 > 32767 :
        dig_T2 -= 65536
    dig_T3 = b1[5] * 256 + b1[4]
    if dig_T3 > 32767 :
        dig_T3 -= 65536

# Pressure coefficents
    dig_P1 = b1[7] * 256 + b1[6]
    dig_P2 = b1[9] * 256 + b1[8]
    if dig_P2 > 32767 :
        dig_P2 -= 65536
    dig_P3 = b1[11] * 256 + b1[10]
    if dig_P3 > 32767 :
        dig_P3 -= 65536
    dig_P4 = b1[13] * 256 + b1[12]
    if dig_P4 > 32767 :
        dig_P4 -= 65536
    dig_P5 = b1[15] * 256 + b1[14]
    if dig_P5 > 32767 :
        dig_P5 -= 65536
    dig_P6 = b1[17] * 256 + b1[16]
    if dig_P6 > 32767 :
        dig_P6 -= 65536
    dig_P7 = b1[19] * 256 + b1[18]
    if dig_P7 > 32767 :
        dig_P7 -= 65536
    dig_P8 = b1[21] * 256 + b1[20]
    if dig_P8 > 32767 :
        dig_P8 -= 65536
    dig_P9 = b1[23] * 256 + b1[22]
    if dig_P9 > 32767 :
        dig_P9 -= 65536

# BMP280 address, 0x76(118)
# Select Control measurement register, 0xF4(244)
#		0x27(39)	Pressure and Temperature Oversampling rate = 1
#					Normal mode
    i2c.writeto_mem(0x76, 0xF4, b'\x27')
# BMP280 address, 0x76(118)
# Select Configuration register, 0xF5(245)
#		0xA0(00)	Stand_by time = 1000 ms
    i2c.writeto_mem(0x76, 0xF5, b'\xA0')

    utime.sleep(0.5)

# BMP280 address, 0x76(118)
# Read data back from 0xF7(247), 8 bytes
# Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
# Temperature xLSB, Humidity MSB, Humidity LSB
    data = i2c.readfrom_mem(0x76, 0xF7, 8)

# Convert pressure and temperature data to 19-bits
    adc_p = ((data[0] * 65536) + (data[1] * 256) + (data[2] & 0xF0)) / 16
    adc_t = ((data[3] * 65536) + (data[4] * 256) + (data[5] & 0xF0)) / 16

# Temperature offset calculations
    var1 = ((adc_t) / 16384.0 - (dig_T1) / 1024.0) * (dig_T2)
    var2 = (((adc_t) / 131072.0 - (dig_T1) / 8192.0) * ((adc_t)/131072.0 - (dig_T1)/8192.0)) * (dig_T3)
    t_fine = (var1 + var2)
    cTemp = (var1 + var2) / 5120.0


# Pressure offset calculations
    var1 = (t_fine / 2.0) - 64000.0
    var2 = var1 * var1 * (dig_P6) / 32768.0
    var2 = var2 + var1 * (dig_P5) * 2.0
    var2 = (var2 / 4.0) + ((dig_P4) * 65536.0)
    var1 = ((dig_P3) * var1 * var1 / 524288.0 + ( dig_P2) * var1) / 524288.0
    var1 = (1.0 + var1 / 32768.0) * (dig_P1)
    p = 1048576.0 - adc_p
    p = (p - (var2 / 4096.0)) * 6250.0 / var1
    var1 = (dig_P9) * p * p / 2147483648.0
    var2 = p * (dig_P8) / 32768.0
    pressure = (p + (var1 + var2 + (dig_P7)) / 16.0) / 100
    return(cTemp, pressure)

#
# Main program, read and siaplay the temperature and pressure
#
while True:
    T,P = BMP280()
    print("Temperature in Celsius : %.2f C" %T)	
    print("Pressure : %.2f hPa \n" %P)
    utime.sleep(5)
   
   
    
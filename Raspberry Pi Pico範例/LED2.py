import time
import machine
import utime
# 設定IO2腳位為輸入腳
input_pin = machine.Pin(2, machine.Pin.IN)

# 設定IO26腳位為類比輸入腳
adc_pin = machine.ADC(machine.Pin(26))
# 設定ADC為3.3V範圍
adc_pin.atten(machine.ADC.ATTN_11DB)
# 設定ADC為12BIT精度
adc_pin.width(machine.ADC.WIDTH_12BIT)

mode = None
no = None
press = None
i = None

def init():
    global mode, no, press, i
    wb.cls(0)
    wb.colors(999,999)
    wb.str(str('Frequence mode'),0,0,1,2)
    mode = 'X'
    no = 0
    press = False
    SERVO()
    freq()

def SERVO():
    global mode, no, press, i
    pass

def freq():
    global mode, no, press, i
	# 初始化各種變數初始值
	last_time = utime.ticks_us()	
	current_time = 0
	
	# 訊號週期計數變數
	high_time = 0

	# 顯示或是ADC轉換切換變數
	count_show = 0

	# IO2正負緣偵測變數
	input_value = 0
	last_input_value = 0

	# 計算ADC的最大值和參考電壓設定
	last_time_adc = utime.ticks_us()
	max_adc = 2 ** 12 - 1  # 12位元的ADC最大值
	ref_voltage = 3.3      # 參考電壓3.3V

	# 計算頻率用變數
	frequency = 0
	
	# 清除螢幕
	wb.cls()
    # 讀取輸入IO2狀態
    last_input_value = input_value    
    input_value = input_pin.value()

    # 如果檢測到IO2從高電位變為低電立時，開始記錄時間，並將count_show設為1
    current_time = utime.ticks_us()
    if input_value == 0 and last_input_value == 1 and count_show == 0:
        last_time = utime.ticks_us()
        count_show = 1
    else:
        # 如果檢測到IO2從高電位變為低電立時，並count_show為1時，計算週期長度，並計算頻率
        if input_value == 0 and last_input_value == 1 and count_show == 1:
            high_time = utime.ticks_diff(current_time, last_time)
            count_show = 0
            frequency = 1/(float(high_time)/1000000.0)
            
    # 每一秒讀取ADC並顯示電壓值，如一直沒有IO2輸入則每二秒讀取一次
    if (utime.ticks_diff(current_time, last_time_adc) > 1000000 and count_show == 1) or utime.ticks_diff(current_time, last_time_adc) > 2000000:
        # 讀取ADC並轉換為電壓
        last_time_adc = utime.ticks_us()
        adc_value = adc_pin.read_uv()
        voltage = adc_value/1000000.0
        # 顯示頻率和電壓值
        wb.cls()
        wb.str('Frequency: %.2f Hz' % frequency, 8, 0, 3, 1)
        wb.str('Voltage: %.2f V' % voltage, 8, 16, 3, 1)

def Umode():
    global mode, no, press, i
    wb.cls(0)
    wb.colors(999,999)
    wb.str(str('Star mode'),20,20,1,3)
    no = 0

def Rmode():
    global mode, no, press, i
    wb.cls(0)
    wb.colors(999,999)
    wb.str(str('Dice1 mode'),20,20,1,3)

def display():
    global mode, no, press, i
    if no >= 1:
        wb.cls(0)
        wb.colors(999,999)
        wb.str(str('*'),0,0,1,2)
    if no >= 2:
        wb.colors(999,999)
        wb.str(str('**'),0,20,1,2)
    if no >= 3:
        wb.colors(999,999)
        wb.str(str('***'),0,40,1,2)
    if no >= 4:
        wb.colors(999,999)
        wb.str(str('****'),0,60,1,2)
    if no >= 5:
        wb.colors(999,999)
        wb.str(str('*****'),0,80,1,2)
    if no >= 6:
        wb.colors(999,999)
        wb.str(str('******'),0,100,1,2)

def Lmode():
    global mode, no, press, i
    wb.cls(0)
    wb.colors(999,999)
    wb.str(str('Dice2 mode'),20,20,1,3)
    if machine.Pin(5,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('1'),20,60,1,4)
    elif machine.Pin(21,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('2'),20,60,1,4)
    elif machine.Pin(19,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('3'),20,60,1,4)
    elif machine.Pin(18,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('4'),20,60,1,4)
    elif machine.Pin(22,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('5'),20,60,1,4)
    elif machine.Pin(23,1).value() == 1:
        wb.colors(999,999)
        wb.str(str('6'),20,60,1,4)


init()
while True:
    if(wb.getkey()==32):
        if mode != 'L' and mode != 'R':
            mode = 'U'
            Umode()
    if(wb.getkey()==8):
        if mode != 'U' and mode != 'R':
            mode = 'L'
            Lmode()
    if(wb.getkey()==4):
        if mode != 'U' and mode != 'L':
            mode = 'R'
            Rmode()
    if(wb.getkey()==16):
        init()
    if wb.getkey() == 1:
        if mode == 'U':
            no = no + 1
            if no > 6:
                no = 6
            display()
            time.sleep(0.1)
        elif mode == 'R':
            press = True
            wb.cls(0)
            wb.colors(999,999)
            wb.str(str((wb.rand(1,6+1))),20,20,1,6)
            time.sleep(0.1)
    if wb.getkey() == 0:
        if press == True:
            for i in range(1, 21):
                wb.cls(0)
                wb.colors(999,999)
                wb.str(str((wb.rand(1,6+1))),20,20,1,6)
                time.sleep(0.1)
            press = False
    if(wb.getkey()==2):
        if mode == 'U':
            no = no - 1
            if no < 1:
                no = 1
            display()
            time.sleep(0.1)

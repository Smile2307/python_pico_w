from machine import Timer

def callback1(t:Timer):
    print(1)
    
def callback2(t:Timer):
    print(2)
    
def callback3(t:Timer):
    print(3)
    #t.deinit()

#1秒執行1次
time1 = Timer()
time1.init(freq=1,callback=callback1)

#每2秒執行1次
time2 = Timer()
time2.init(period=2000,callback=callback2)

#每3秒執行1次
time3 = Timer()
time3.init(period=3000,callback=callback3)
'''
while True:
    a = input("是否停止y/n:")
    print(a)
    if a == "y" :
        time3.deinit() #指定time3停止計時
'''        



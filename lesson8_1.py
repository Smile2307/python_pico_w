import random
import pyinputplus as pyip
while(True):
    min = 1
    max = 100
    count = 0
    randomNum = random.randint(min,max)
    print(randomNum)
    print("===========猜數字遊戲=============")
    while True:
        keyin = pyip.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
        print(keyin)
        count += 1
        if(keyin == randomNum):
            print(f"賓果!猜對了, 答案是:{randomNum}")
            print(f"您共猜了:{count}次")
            break
        elif keyin > randomNum:
            print("再小一點")
            max = keyin - 1
        elif keyin < randomNum:
            print("再大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")
    is_play = pyip.inputYesNo("您還要繼續玩嗎?(y,n):")
    if is_play=="no":
        break
    
print("Game Over!")
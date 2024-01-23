config = {'button':14, 'long':2000} # 長按時間設須超過2000毫秒 

from MyKit_Button import myButton
btn = myButton(config['button'])  

def test():
    print(f"已設長按時間須為 {config['long']} 毫秒, 請按下一段時間再放開試試")
    while True:
        ms_hold = btn.longPressed(config['long'])
        if ms_hold > 0:
            print(f'時間為 {ms_hold} 毫秒：', end='')
            if ms_hold >= config['long']:
                print(f'第{btn.counter}次長按')
            else:
                print(f'短按')
test()
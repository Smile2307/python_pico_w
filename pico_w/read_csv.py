# 确保此路径与您的 CSV 文件的实际位置相匹配
file_path = 'wifi_config.csv'
   
try:
    # 嘗試打開檔案
    with open(file_path, 'r') as file:
        # 逐行讀取檔案
        for index, line in enumerate(file):
            # 跳過第一行標題列
            if index == 0:
                continue
            # 移除每行末尾的換行符並分割數據
            row = line.strip().split(',')
            # 打印每行的數據
            print(f'ssid:{row[0]},password:{row[1]}')
except OSError as e:
    print('無法打開檔案:', e)

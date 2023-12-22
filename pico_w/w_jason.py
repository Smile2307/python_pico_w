#建立50位學生,每位學生有5個分數
#list內放dictionary
import random
students = []
for i in range(1,51):
    stdDict = {'姓名':'stu' + str(i),
               '國文':random.randint(50,100),
               '英文':random.randint(50,100),
               '數學':random.randint(50,100),
               '自然':random.randint(50,100),
               '社會':random.randint(50,100),
              }
    students.append(stdDict)

#儲存為json的檔案格式
#使用json.dump()
#json可以儲存複雜的python的資料結構

import json
with open('students.json','w',encoding='utf-8') as file:
    #json.dump(students, file, ensure_ascii=False)
    json.dump(students, file)
print("json存檔成功")
file.close()

# 操作範例 2:請動手操作，並留意輸出結果
#使用load()將json檔轉成Dictionary

#import json

#data = json.load('score.json')  #會出錯

with open('students.json') as json_file:
    data = json.load(json_file)
    #for p in data['姓名']:
    for p in data:
        print('姓名:' + p['姓名'])
        print('數學:' + str(p['數學']))
        print('英文:' + str(p['英文']))
        print('自然:' + str(p['自然']))
        print('國文:' + str(p['國文']))
        print('社會:' + str(p['社會']))
        print()
json_file.close()
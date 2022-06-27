#程序文件ex2_10.py
Dict={'age':18, 'score':[98,97], 'name':'Zhang', 'sex':'male'}
for item in Dict:            #遍历输出字典的“键”
    print(item)
print("----------" )          
for item in Dict.items():     #遍历输出字典的元素
    print(item)
print("----------")
for value in Dict.values():  #遍历输出字典的值
    print(value)

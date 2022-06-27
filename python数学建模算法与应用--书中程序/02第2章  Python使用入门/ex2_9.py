#程序文件ex2_9.py
Dict={'age':18,'score':[98,97],'name':'Zhang','sex':'male'}
print(Dict['age'])          #输出18
print(Dict.get('age'))      #输出18
print(Dict.get('address','Not Exists.'))   #输出No Exists 
print(Dict['address'])      #出错

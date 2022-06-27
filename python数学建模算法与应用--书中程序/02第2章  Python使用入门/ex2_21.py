#程序文件ex2_21.py
import random
x=random.randint(1e5,1e8)  #生成一个随机整数
y=list(map(int,str(x)))    #提出每位上的数字
z=list(map(lambda x,y: x%2==1 and y%2==0, [1,3,2,4,1],[3,2,1,2]))
print(x); print(y); print(z)

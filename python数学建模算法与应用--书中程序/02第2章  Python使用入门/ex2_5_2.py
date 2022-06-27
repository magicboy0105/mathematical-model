#程序文件ex2_5_2.py
from numpy.random import randint
import numpy as np
a=randint(10,20,16)  #生成16个[10,20)上的随机整数
ma=max(a)
ind1=[index for index,value in enumerate(a) if value==ma]
ind2=np.where(a==ma)  #第二种方法求最大值的地址
print(ind1); print(ind2[0])

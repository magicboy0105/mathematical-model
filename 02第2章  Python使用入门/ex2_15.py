#程序文件ex2_15.py
import math                  #导入标准库math
import random                #导入标准库random
import numpy.random as nr    #导入numpy库中的random模块
a=math.gcd(12,21)            #计算最大公约数，a=3
b=random.randint(0,2)        #获得[0,2]区间上的随机整数
c=nr.randint(0,2,(4,3))      #获得[0,2)区间上的4×3随机整数矩阵
print(a); print(b); print(c) #输出a,b,c的值

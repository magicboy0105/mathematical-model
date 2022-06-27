#程序文件ex2_27.py
import numpy as np
a = np.arange(16).reshape(4,4)  #生成4行4列的数组
b = a[1][2]   #输出6
c = a[1, 2]   #同b
d = a[1:2, 2:3]  #输出[[6]]
x = np.array([0, 1, 2, 1])
print(a[x==1])  #输出a的第2、4行元素

#程序文件ex2_43.py
import numpy as np
a=np.random.rand(6,8)  #生成6×8的[0,1)上均匀分布的随机数矩阵
np.savetxt("data2_43_1.txt", a)  #存成以制表符分隔的文本文件
np.savetxt("data2_43_2.csv", a, delimiter=',')  #存成以逗号分隔的CSV文件
b=np.loadtxt("data2_43_1.txt")   #加载空格分隔的文本文件
c=np.loadtxt("data2_43_2.csv", delimiter=',')  #加载CSV文件

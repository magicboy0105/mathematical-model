#程序文件ex2_26.py
import numpy as np
a = np.ones(4, dtype=int)     #输出[1, 1, 1, 1]
b = np.ones((4,), dtype=int)  #同a
c= np.ones((4,1))             #输出4行1列的数组
d = np.zeros(4)               #输出[0, 0, 0, 0]
e = np.empty(3)               #生成3个元素的空数组行向量
f = np.eye(3)                 #生成3阶单位阵
g = np.eye(3, k=1)  #生成第k对角线的元素为1，其他元素为0的3阶方阵
h = np.zeros_like(a)          #生成与a同维数的全0数组


#程序文件ti14_3.py
import numpy as np
import pandas as pd

a = np.loadtxt('ti14_3_1.txt'); n = a.shape[0]
s = a.sum(axis=0)  #逐列求和
P = a / s          #求特征比重矩阵
e = -(P*np.log(P)).sum(axis=0)/np.log(n)  #计算熵值
g = 1 - e; w = g / sum(g)  #计算差异系数和权重系数
f = P @ w  #计算评价值
ind = np.argsort(-f)  #从大到小排序的地址
y = np.arange(1984, 2001)
sy = y[ind]  #评价值从大到小排列的年代
sf = sorted(f, reverse=True)
d = np.vstack([sy, sf])
pd.DataFrame(d).to_excel('ti14_3_2.xlsx', index=None)
print('评价值从高到低的年代：', sy)
print('对应的评价值：', np.round(sf,4))

                  

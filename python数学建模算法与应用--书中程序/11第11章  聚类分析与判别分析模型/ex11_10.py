#程序文件ex11_10.py
import numpy as np
import pandas as pd
from numpy.linalg import inv
a=pd.read_excel('data11_10.xlsx',header=None)
b=a.values; x0=b[:-2,:-1].astype(float)
y0=b[:-2,-1].astype(float)
x=b[-2:,:-1].astype(float)  #提取待判样本点的观察值
A1 = x0[:10, :]; A2 = x0[10:, :]
mu1 = A1.mean(axis=0); mu2 = A2.mean(axis=0)
s1 = np.cov(A1.T, ddof=1); s2 = np.cov(A2.T, ddof=1)
D = []  #存放待判样本点的马氏距离
for i in x:
    d1 = np.sqrt((i-mu1)@inv(s1)@(i-mu1))
    d2 = np.sqrt((i-mu2)@inv(s2)@(i-mu2))
    D.append([d1, d2])
ind = np.argmin(D, axis=1)+1
check =[]  #存放已知样本点的马氏距离
for i in x0:
    d1 = np.sqrt((i-mu1)@inv(s1)@(i-mu1))
    d2 = np.sqrt((i-mu2)@inv(s2)@(i-mu2))
    check.append([d1, d2])
ind2 = np.argmin(check, axis=1)+1
rate = sum(y0-ind2)/len(y0) #计算误判率
print('待判样本的分类：', ind)   #输出待判类别
print('已知样本的检验：', ind2)

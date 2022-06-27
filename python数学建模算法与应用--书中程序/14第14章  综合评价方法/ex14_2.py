#程序文件ex14_2.py
import numpy as np
from scipy.stats import rankdata

a = np.loadtxt('data14_1_2.txt')
bp = a.max(axis=0)  #求正理想解
bm = a.min(axis=0)  #求负理想解
d1 = np.linalg.norm(a-bp,axis=1)  #求到正理想解的距离
d2 = np.linalg.norm(a-bm,axis=1)  #求到负理想解的距离
f1 = d2 / (d1+d2); print('TOPSIS评价值：', f1)

c = bp - a      #计算参考序列与每个序列的差
m1 = c.max(); m2 = c.min()  #计算最大差和最小差
r = 0.5  #分辨系数
xs = (m2+r*m1)/(c+r*m1)  #计算灰色关联系数
f2 = xs.mean(axis=1)     #求灰色关联度
print('灰色关联度：', np.round(f2,4))

n = a.shape[0]; s = a.sum(axis=0)  #逐列求和
P = a / s  #求特征比重矩阵
e = -(P*np.log(P)).sum(axis=0)/np.log(n)  #计算熵值
g = 1- e; w = g / sum(g)  #计算差异系数和权重系数
f3 = P @ w  #计算各对象的评价值
print('评价值：', np.round(f3,4))

R = rankdata(a, axis=0)  #逐列编秩
RSR = R.mean(axis=1) / n  #计算秩和比
print('秩和比：', np.round(RSR,4))

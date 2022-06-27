#程序文件ex11_11.py
import numpy as np
from numpy.linalg import inv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

a = np.loadtxt('data11_11.txt')
a1 = a[:5, :]; a2 = a[5:10, :]; x = a[10:, :]
V = np.cov(a[:10, :].T, ddof=1)  #计算协方差阵
VI = inv(V)  #计算协方差阵的逆阵
mu1 = a1.mean(axis=0); mu2 = a2.mean(axis=0)
k = VI @ (mu1-mu2)  #判别函数系数向量
b = -(mu1+mu2) @ VI @ (mu1-mu2)/2  #判别函数常数项
val = x @ k + b  #计算判别函数的值
print('判别函数的值：', val)
d = {0:'B', 1:'A'}
print('直接计算结果：',[d[e>0] for e in val])  #输出判别结果
y0 = np.hstack([np.ones(5), np.zeros(5)])
md = LDA().fit(a[:10, :], y0)  #直接使用库函数
k2 = md.coef_; b2 = md.intercept_ 
c = b2/b; check = k * c  #验证直接计算和库函数调用等价
val2 = md.predict(x)
print('库函数结果：  ',[d[e] for e in val2])
print('k=',k, ',b=',b);
print('k2=',k2, ',b2=',b2); print('比例c=', c)
print('已知样本误判率为：', 1-md.score(a[:10, :], y0))

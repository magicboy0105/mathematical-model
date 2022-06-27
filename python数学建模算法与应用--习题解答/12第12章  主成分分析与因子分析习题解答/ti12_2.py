#程序文件ti12_2.py
import numpy as np
from factor_analyzer import FactorAnalyzer as FA
from scipy.stats import zscore

c=np.loadtxt('ti12_2.txt'); n=c.shape[0]
d=zscore(c,ddof=1)          #数据标准化
r=np.corrcoef(d.T)          #求相关系数矩阵
val,vec=np.linalg.eig(r)
cs=np.cumsum(val)      #求特征值的累加和
rate=val/cs[-1]        #求贡献率
Trate=np.cumsum(rate)  #求累积贡献率
print('特征值为：',val); print('贡献率为：',rate)
print('累积贡献率为：',np.round(Trate,4))
fa = FA(3,rotation='varimax')  #构建模型
fa.fit(d)         #求解方差最大的模型
A=fa.loadings_    #提取载荷矩阵
gx=np.sum(A**2, axis=0)    #计算信息贡献
s2=np.sum(A**2, axis=1)    #计算共同度
ss=np.linalg.inv(np.diag(1-s2))
f=ss@A@np.linalg.inv(A.T@ss@A)  #计算因子得分函数系数
print('载荷矩阵为：\n',np.round(A,4))
print('共同度为：',np.round(s2,4))
print('各因子的方差贡献：',np.round(gx,4))





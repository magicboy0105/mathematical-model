#程序文件ex12_5.py
import numpy as np
from sklearn.decomposition import FactorAnalysis as FA
from scipy.stats import zscore
import pandas as pd

c=np.loadtxt('data12_5_1.txt')
d=zscore(c,ddof=1)          #数据标准化
r=np.corrcoef(d.T)          #求相关系数矩阵
val,vec=np.linalg.eig(r)
cs=np.cumsum(val)  #求特征值的累加和
rate=val/cs[-1]    #求贡献率
print("特征值为：",val,"\n贡献率为：",rate)
fa = FA(3,rotation='varimax')  #构建模型
fa.fit(d)         #求解方差最大的模型
A=fa.components_.T  #提取载荷矩阵
gx=np.sum(A**2, axis=0)    #计算信息贡献
s2=1-np.sum(A**2, axis=1)  #计算特殊方差
ss=np.linalg.inv(np.diag(s2))
df = d @ ss @ A @ np.linalg.inv(A.T @ ss @ A)
print("载荷矩阵为：\n",A)
print("特殊方差为：\n",s2)
pj=df@gx/sum(gx)  #计算综合得分

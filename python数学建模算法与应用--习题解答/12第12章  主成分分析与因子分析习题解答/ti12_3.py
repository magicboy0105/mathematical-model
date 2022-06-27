#程序文件ti12_3.py
import numpy as np
from scipy.stats import zscore
import pandas as pd

a = np.loadtxt('ti12_3_1.txt')
b = zscore(a, ddof=1)          #数据标准化
r = np.corrcoef(b.T)   #求相关系数矩阵
c, d = np.linalg.eig(r)  #求特征值和特征向量
ind = np.argsort(-c)  #特征值从大到小排序的地址
cc = c[ind]; dd = d[ind,:]  #重排特征值和特征向量的顺序
print('特征值为：', cc)
print('特征向量为：\n', dd)
rt = cc/sum(cc)  #计算各主成分的贡献率
cr = np.cumsum(rt)  #求累积贡献率
print('各主成分的贡献率为：', rt)
da1 = np.vstack([cc, rt, cr]).T
da1 = pd.DataFrame(da1); da2 = pd.DataFrame(dd)
f = pd.ExcelWriter('ti12_3_2.xlsx')
da1.to_excel(f, 'Sheet1', index=None)
da2.to_excel(f, 'Sheet2', index=None)
f.save()



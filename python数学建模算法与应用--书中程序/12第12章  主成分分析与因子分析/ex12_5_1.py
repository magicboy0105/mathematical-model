#程序文件ex12_5_1.py
import numpy as np
from factor_analyzer import FactorAnalyzer as FA
from scipy.stats import zscore
import pandas as pd

c=np.loadtxt('data12_5_1.txt')
d=zscore(c,ddof=1)          #数据标准化
r=np.corrcoef(d.T)          #求相关系数矩阵
val,vec=np.linalg.eig(r)
cs=np.cumsum(val)  #求特征值的累加和
rate=val/cs[-1]    #求贡献率
srate=sorted(rate,reverse=True)
print('特征值为：',val,'\n贡献率为：',srate)
fa = FA(3,rotation='varimax')  #构建模型
fa.fit(d)         #求解方差最大的模型
A=fa.loadings_    #提取载荷矩阵
gx=np.sum(A**2, axis=0)    #计算信息贡献
s2=1-np.sum(A**2, axis=1)  #计算特殊方差
ss=np.linalg.inv(np.diag(s2))
f=ss@A@np.linalg.inv(A.T@ss@A)  #计算因子得分函数系数
df=d@f            #计算因子得分
pj=df@gx/sum(gx)  #计算评价值
print('载荷矩阵为：\n',np.round(A,4))
print('特殊方差为：',np.round(s2,4))
print('各因子的方差贡献：',np.round(gx,4))
print('评价值为：\n',pj)
ind0=np.argsort(-pj)  #从大到小的排名地址
ind=np.zeros(17); ind[ind0]=np.arange(1,18)
print('排名次序为：', ind)
F=pd.ExcelWriter('data12_5_2.xlsx')
pd.DataFrame(r).to_excel(F)
pd.DataFrame(df).to_excel(F,'Sheet2',index=False)
pd.DataFrame(pj).to_excel(F,'Sheet3',index=False)
F.save()




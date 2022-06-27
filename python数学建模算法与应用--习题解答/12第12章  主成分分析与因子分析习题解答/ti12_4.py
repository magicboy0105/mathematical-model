#程序文件ti12_4.py
import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer as FA
from scipy.stats import zscore
import pylab as plt

c=pd.read_excel('ti12_4_1.xlsx',usecols=np.arange(1,7))
N=c.shape[0]  #评价对象的个数
c=c.values; d=zscore(c,ddof=1)  #数据标准化
r=np.corrcoef(d.T)   #求相关系数矩阵
val,vec=np.linalg.eig(r)
cs=np.cumsum(val)  #求特征值的累加和
print('特征值为：',val)
print('累积贡献率：',cs/cs[-1])
n=2  #选择因子的个数
fa= FA(2, rotation='varimax')  #构建模型
fa.fit(d)   #求解最大方差的模型
A=fa.loadings_  #提取载荷矩阵
s2=1-np.sum(A**2, axis=1)  #计算特殊方差
print('载荷矩阵为：\n',A)
print('特殊方差为：\n',s2)
ss=np.linalg.inv(np.diag(s2))
f = ss @ A @ np.linalg.inv(A.T @ ss @ A)  #计算因子得分函数系数
dd = d @ f              #计算因子得分
Ac=np.sum(A**2,axis=0)  #计算方差贡献
w=Ac/sum(Ac)            #计算因子权重
df1=dd@w                 #计算每个评价对象的因子总分
df2=np.sum(c,axis=1)     #计算每个评价对象的求和总分
ind1=np.argsort(-df1)+1    #因子总分从高到低的序号
ind2=np.argsort(-df2)+1    #求和总分从高到低的序号
ind11=np.zeros(N); ind11[ind1-1]=np.arange(1,N+1)
ind22=np.zeros(N); ind22[ind2-1]=np.arange(1,N+1)
xz=np.stack([df1,ind11,ind22],axis=1)
zh=np.hstack([dd,xz])
pd.DataFrame(zh).to_excel('ti12_4_2.xlsx', index=None)
rr=sum(abs(ind11-ind22)>5)/N  #计算两种评价差异率
s=['A'+str(i) for i in range(1,N+1)]
plt.rc('font',family='SimHei'); plt.rc('axes',unicode_minus=False)
plt.rc('font',size=14); plt.plot(dd[:,0],dd[:,1],'.')
for i in range(N): plt.text(dd[i,0],dd[i,1]+0.03,s[i])
plt.xlabel('基础课因子得分'); plt.ylabel('开闭卷因子得分')
plt.show()



#程序文件ti12_1.py
import numpy as np
from sklearn.decomposition import PCA
from scipy.stats import zscore

a=np.loadtxt('ti12_1.txt'); n=a.shape[0]
b=zscore(a, ddof=1)   #数据标准化
md=PCA().fit(b)  #构造并拟合模型
print('特征值为：', md.explained_variance_)
rate=md.explained_variance_ratio_  #提出各主成分的贡献率
print('各主成分贡献率：', rate)
print('累积贡献率：', np.cumsum(rate))
xs1=md.components_  #提出各主成分系数，每行是一个主成分
print('各主成分系数:\n',xs1)
check=xs1.sum(axis=1,keepdims=True)  #计算各个主成分系数的和
xs2=xs1*np.sign(check)  #调整主成分系数，和为负时乘以-1
print('调整后的主成分系数：\n', xs2)
num=3  #选取的主成分的个数
df = b @ (xs2[:num,:].T)   #计算主成分的得分
tf = df @ rate[:num]       #计算综合得分
ind = np.argsort(-tf)     #计算综合得分从大到小排列的地址
y=np.arange(1984,2001); print('排名次序：\n', y[ind])
print('对应的综合评价值：\n',np.round(tf[ind],4))


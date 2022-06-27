#程序文件ex12_1.py
import numpy as np
from sklearn.decomposition import PCA
from scipy.stats import zscore

a=np.loadtxt('data12_1.txt')
b=zscore(a, ddof=1)   #数据标准化
md=PCA().fit(b)  #构造并拟合模型
print('特征值为：', md.explained_variance_)
print('各主成分贡献率：', md.explained_variance_ratio_)
xs1=md.components_  #提出各主成分系数，每行是一个主成分
print('各主成分系数:\n',xs1)
check=xs1.sum(axis=1,keepdims=True)  #计算各个主成分系数的和
xs2=xs1*np.sign(check)  #调整主成分系数，和为负时乘以-1
print('调整后的主成分系数：', xs2)


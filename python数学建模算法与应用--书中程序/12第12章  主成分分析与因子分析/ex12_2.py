#程序文件ex12_2.py
import numpy as np
from sklearn.decomposition import PCA
import statsmodels.api as sm

a=np.loadtxt('data12_2.txt')
mu=a.mean(axis=0)  #逐列求均值
s=a.std(axis=0,ddof=1)  #逐列求标准差
b=(a-mu)/s  #数据标准化
r=np.corrcoef(b[:,:-1].T)  #计算相关系数矩阵
md1=PCA().fit(b[:,:-1])  #构造并拟合模型
print('特征值为：', md1.explained_variance_)
print('各主成分贡献率：', md1.explained_variance_ratio_)
xs=md1.components_  #提出各主成分系数，每行是一个主成分
print('主成分系数：\n', np.round(xs,4))
print('累积贡献率：', np.cumsum(md1.explained_variance_ratio_))

n=3  #选定主成分的个数
f=b[:,:-1]@(xs[:n,:].T)  #主成分的得分
d2={'y':a[:,-1],'x': a[:,:-1]}
md2=sm.formula.ols('y~x',d2).fit()  #原始数据线性回归
d3={'y':a[:,-1], 'z':f}
md3=sm.formula.ols('y~z',d3).fit()  #对主成分的回归方程
xs3=md3.params  #提取主成分回归方程的系数
xs40=xs3[0]-sum(xs3[1:]@xs[:n,:]*mu[:-1]/s[:-1]) #常数项
xs4=xs3[1:]@xs[:n,:]/s[:-1]  #原始变量回归方程的其他系数
print('回归方程的常数项：',round(xs40,4))
print('回归方程的其他系数：',np.round(xs4,4))
print('直接回归的残差方差：',md2.mse_resid)
print('主成分回归的残差方差：',md3.mse_resid)


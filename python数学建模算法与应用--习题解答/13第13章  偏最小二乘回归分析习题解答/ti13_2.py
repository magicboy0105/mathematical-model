#程序文件ti13_2.py
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from scipy.stats import zscore
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error

d0 = np.loadtxt('ti13_2.txt')
mu = d0.mean(axis=0)       #求均值
s =d0.std(axis=0, ddof=1)  #求标准差
r = np.corrcoef(d0.T)  #求相关系数矩阵
d = zscore(d0, ddof=1)  #数据标准化
a = d[:, :7]; b = d[:, 7:]
n = a.shape[1]; m = b.shape[1]  #自变量和因变量个数
mse = []  #均方误差初始化
for i in range(1, n+1):  #以下确定成分的个数
    pls = PLSRegression(i)
    y_cv = cross_val_predict(pls, a, b)
    mse.append(mean_squared_error(b, y_cv))
nmin = np.argmin(mse); print('均方误差：\n', mse)
print('建议的成分个数: ', nmin+1)

md = PLSRegression(5).fit(a, b)
b = md.coef_   #每一列是y对x的回归系数
print('标准化数据的回归系数(列)：\n', b)
b0 = np.zeros((n+1, m))
b0[0, :] = mu[n:] - mu[:n]/s[:n] @ b * s[n:]
for i in range(m):
    b0[1:, i] = s[n+i]/s[:n] * b[:,i]
print('(原始数据)y关于x回归系数(列):\n', b0)

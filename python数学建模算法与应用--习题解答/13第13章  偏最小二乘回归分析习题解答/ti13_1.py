#程序文件ti13_1.py
import numpy as np
import pylab as plt
from sklearn.cross_decomposition import PLSRegression
from scipy.stats import zscore
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error

d0 = np.loadtxt('ti13_1.txt'); N = d0.shape[0]
mu = d0.mean(axis=0)       #求均值
s = d0.std(axis=0, ddof=1)  #求标准差
r = np.corrcoef(d0.T)  #求相关系数矩阵
d = zscore(d0, ddof=1)  #数据标准化
a = d[:, :7]; b = d[:, -1]
n = a.shape[1]; m = 1  #自变量和因变量个数
rmse = []  #均方误差初始化
for i in range(1, n+1):  #以下确定成分的个数
    pls = PLSRegression(i)
    y_cv = cross_val_predict(pls, a, b)
    rmse.append(mean_squared_error(b, y_cv))
nmin = np.argmin(rmse); print('均方误差：\n', rmse)
print('建议的成分个数: ', nmin+1)

md = PLSRegression(3).fit(a, b)
xd = md.x_scores_; yd = md.y_scores_    #成分得分
zx = np.linalg.pinv(a) @ xd  #计算自变量的成分系数   
print('自变量的成分系数(列）：\n', zx)  #每列为一成分
xzh = md.x_loadings_  #x主成分回归系数
yzh = md.y_loadings_  #y主成分回归系数
print('x主成分回归(行)：\n', xzh); print('\n------')
print('y主成分回归：\n', yzh); print('\n------')
beta2 = md.coef_   #每一列是y对x的回归系数
print('（标准化）y关于x回归系数：\n', np.round(beta2,4))
beta3 = np.zeros((n+1, m))
beta3[0, :] = mu[n:] - mu[:n]/s[:n] @ beta2 * s[n:]
for i in range(m):
    beta3[1:, i] = s[n+i]/s[:n] * beta2[:,i]
print('(原始数据)y关于x回归系数:\n', beta3)
aa = np.hstack([np.ones((N,1)), d0[:,:n]])
yh = aa @ beta3   #求预测值

plt.rc('font', family='SimHei'); plt.rc('font', size=15)
plt.rc('axes', unicode_minus=False)
plt.bar(np.arange(1,n+1),beta2.flatten(),width=0.4)
plt.plot([0, 10], [0, 0]); plt.figure()
plt.plot(yh, d0[:,-1],'*',label='原辛烷值预测图')
plt.plot([80, 100], [80, 100])  #画参照直线
plt.xlabel('预测数据'); plt.ylabel('观测数据'); plt.show()

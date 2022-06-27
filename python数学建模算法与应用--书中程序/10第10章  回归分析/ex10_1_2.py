#程序文件ex10_1_2.py
import numpy as np
import statsmodels.api as sm
import pylab as plt

d = np.loadtxt('data10_1.txt')
x0 = d[0]; y0 = d[1]; d ={'x':x0, 'y':y0}
re = sm.formula.ols('y~x', d).fit() #拟合线性回归模型
print(re.summary())
print(re.outlier_test())  #输出已知数据的野值检验
print('残差的方差', re.mse_resid)
pre=re.get_prediction(d)
df = pre.summary_frame(alpha=0.05)
dfv = df.values; low, upp = dfv[:,4:].T #置信下限上限
r = (upp-low)/2  #置信半径
num = np.arange(1, len(x0)+1)
plt.errorbar(num, re.resid, r, fmt='o')
plt.show()



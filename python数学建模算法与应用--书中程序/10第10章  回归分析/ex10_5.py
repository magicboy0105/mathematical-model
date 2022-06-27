#程序文件ex10_5.py
import numpy as np
import pandas as pd
from scipy.stats import t, f
import statsmodels.api as sm

a = pd.read_excel('data10_5.xlsx', header=None)
b = a.values; Y=np.hstack([b[:,1],b[:-1,6]])
X = np.vstack([b[:,2:5],b[:-1,7:]])
XX = np.hstack([np.ones((25,1)),X])
cs = np.linalg.pinv(XX) @ Y   #最小二乘法拟合参数
print('拟合的参数为：', np.round(cs,4))
yb = Y.mean()  #计算y的观测值的平均值
yh = XX @ cs    #计算y的估计值
q = sum((yh-Y)**2)   #计算残差平方和
u = sum((yh-yb)**2)  #计算回归平方和
m =3; n = len(Y)  #变量个数和样本容量
F = u/m/(q/(n-m-1))  #计算F统计量的值
print('F=', round(F,4))
fw = f.ppf(0.95, m, n-m-1)   #计算上alpha分位数
print('F分布的上alpha分位数：', round(fw,4))
c = np.diag(np.linalg.inv(XX.T @ XX))  
ts = cs/np.sqrt(c)/np.sqrt(q/(n-m-1))  #计算t统计量的值
tw = t.ppf(0.975, n-m-1)  #计算上alpha/2分位数
print('t统计量值为：', np.round(ts,4))
print('t分布的上alpha/2分位数：', round(tw,4))
XD = np.delete(XX,1,axis=1)  #删除x1的观测值
cs2 = np.linalg.pinv(XD) @ Y  #重新拟合参数
print('x2,x3模型的参数值：',np.round(cs2,4))
d = {'y':Y,'x1':X[:,0],'x2':X[:,1],'x3':X[:,2]}
md = sm.formula.ols('y~x1*x2+x1*x3+x2*x3+I(x1**2)+\
                    I(x2**2)+I(x3**2)',d).fit()
print('完全二次式的系数为：', md.params)


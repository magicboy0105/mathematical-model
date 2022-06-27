#程序文件ti10_6.py
import numpy as np
import statsmodels.api as sm
import pylab as plt

a = np.loadtxt('ti10_6.txt'); x = a[0]; p = a[1]
plt.rc('font', size=16); plt.rc('text', usetex=True)
plt.plot(x, p, 'p'); plt.xlabel('$x$')
plt.ylabel('$p$', rotation=0); plt.show()
X = sm.add_constant(x)
md = sm.OLS(p, X).fit()  #构建并拟合模型
print(md.summary())   #输出计算结果

y = np.log(p/(1-p))
cs = np.linalg.pinv(X) @ y  #线性最小二乘拟合
x0 = -cs[0] / cs[1]   #求剂量
print(cs,'\n','剂量为：',x0)

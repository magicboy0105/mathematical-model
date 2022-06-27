#程序文件ex10_4.py
import numpy as np
import statsmodels.formula.api as smf
import pylab as plt

a = np.loadtxt('data10_4.txt'); x1 = a[0]; x2 = a[1]; y = a[2]
plt.rc('text', usetex=True); plt.rc('font', size=16)
plt.plot(x1, y, '*', label='$x_1$'); plt.plot(x2, y, 'o', label='$x_2$')
d = {'y': y, 'x1': x1, 'x2': x2}
re1 = smf.ols('y~x1+x2', d).fit()
print('线性回归的残差方差：', re1.mse_resid)
re2 = smf.ols('y~x1+x2+I(x1**2)+I(x2**2)', d).fit()
print('纯二次的残差方差：', re2.mse_resid)
re3 = smf.ols('y~x1*x2', d).fit()
print('交叉二次的残差方差：', re3.mse_resid)
re4 = smf.ols('y~x1*x2+I(x1**2)+I(x2**2)', d).fit()
print('完全二次的残差方差：', re4.mse_resid)
print('预测值：', re2.predict({'x1': 170, 'x2': 160}))
print(re2.summary()); plt.legend(); plt.show()



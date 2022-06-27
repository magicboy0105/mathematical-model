#程序文件ex10_2_1.py
import numpy as np
import statsmodels.api as sm
import pylab as plt

a = np.loadtxt('data10_2.txt')
plt.rc('text', usetex=True); plt.rc('font', size=16)
plt.plot(a[0], a[2], '*', label='$x_1$')
plt.plot(a[1], a[2], 'o', label='$x_2$')
plt.legend(loc='upper left')
d = {'x1': a[0], 'x2': a[1], 'y': a[2]}
re = sm.formula.ols('y~x1+x2', d).fit()
print(re.summary())
yh = re.predict({'x1': [9, 10], 'x2': [10, 9]})
print('残差的方差:', re.mse_resid)
print('预测值：', yh); plt.show()



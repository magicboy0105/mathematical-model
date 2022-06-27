#程序文件ex10_3.py
import numpy as np
import statsmodels.formula.api as smf
import pylab as plt

x = np.arange(17, 30, 2); a = np.loadtxt('data10_3.txt')
plt.rc('text', usetex=True); plt.rc('font', size=16)
plt.plot(x, a[0], '*', label='$y_1$')
plt.plot(x, a[1], 'o', label='$y_2$')
x = np.hstack([x, x]); d = {'y': a.flatten(), 'x': x}
re = smf.ols('y~x+I(x**2)', d).fit()
print(re.summary()); print('残差的方差：', re.mse_resid)
plt.legend(); plt.show()



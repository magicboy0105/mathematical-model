#程序文件ex10_2_2.py
import numpy as np
import statsmodels.api as sm
import pylab as plt

a = np.loadtxt('data10_2.txt')
plt.rc('text', usetex=True); plt.rc('font', size=16)
plt.plot(a[0], a[2], '*', label='$x_1$')
plt.plot(a[1], a[2], 'o', label='$x_2$')
plt.legend(loc='upper left')
X = sm.add_constant(a[:2].T)
re = sm.OLS(a[2], X).fit()
print(re.summary())
yh = re.predict(np.array([[1,9,10],[1,10,9]]))
print('残差的方差:', re.mse_resid)
print('预测值：', yh); plt.show()



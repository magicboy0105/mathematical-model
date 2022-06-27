#程序文件ex7_14.py
import numpy as np
from scipy.optimize import curve_fit

a = np.loadtxt('data7_13.txt')
t0 = a[0]; y0 = a[1]
y = lambda t, k, m: k*np.exp(m*t)
p, pcov = curve_fit(y, t0, y0)
print('拟合的参数为：', np.round(p,4))
yh = y(np.array([5, 8]), *p)
print('预测值为：', np.round(yh,4))

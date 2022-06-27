#程序文件ti7_8.py
import numpy as np
from scipy.optimize import curve_fit

a=np.loadtxt('ti7_8.txt')
t0=np.arange(0, 2.1, 0.1)
y0=a[1::2,:].flatten()  #按时间顺序提出y的观测值
y=lambda t,b1,L1,b2,L2: b1*np.exp(-L1*t)+b2*np.exp(-L2*t)
bd=(0, [np.inf]*4)  #构造拟合参数的下界和上界
p,pcov=curve_fit(y, t0, y0, bounds=bd)
print('拟合的参数值为：', np.round(p,4))

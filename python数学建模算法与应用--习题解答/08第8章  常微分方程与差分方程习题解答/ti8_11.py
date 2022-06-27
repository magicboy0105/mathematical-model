#程序文件ti8_11.py
import numpy as np
from scipy.integrate import odeint

d=np.loadtxt('ti8_11.txt'); a=d[0]; s=d[1]
mat=np.vstack([a[:-1],-a[:-1]*s[:-1],-s[:-1]]).T
cs=np.linalg.pinv(mat)@np.diff(s)
print('拟合参数值：', cs)
eq=lambda s,t: -cs[-1]*s
ss=odeint(eq,s[-1],range(7))
print('预测值：', np.round(ss))


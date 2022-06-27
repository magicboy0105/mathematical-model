#程序文件ti10_8.py
import numpy as np
from scipy.optimize import curve_fit

a=np.loadtxt('ti10_8.txt')
mat=np.stack([np.ones(13),1/a[0]]).T
cs1=np.linalg.pinv(mat)@(1/a[1])  #拟合参数
print('线性拟合参数值：',np.round(cs1,4))

y=lambda x,b0,b1: x/(b0*x+b1)
cs2=curve_fit(y, a[0], a[1])[0]
print('非线性拟合参数值：',np.round(cs2,4))
bd=[(-0.5,1),(0, 5)]  #约束两个参数的下界和上界
cs3=curve_fit(y, a[0], a[1],p0=[-0.2,2.5],bounds=bd)[0]
print('非线性拟合参数值：',np.round(cs3,4))

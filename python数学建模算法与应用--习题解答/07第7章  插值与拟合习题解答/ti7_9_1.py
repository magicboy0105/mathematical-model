#程序文件ti7_9_1.py
import numpy as np
from scipy.optimize import curve_fit

x0=np.linspace(-6,6,30)
y0=np.linspace(-8,8,30)
xy0=np.vstack([x0,y0])
f=lambda xy,a,b: a*xy[0]*xy[1]/(1+b*np.sin(xy[0]))
z0=f(xy0,2,3)  #计算对应的函数值
bd=(0, [np.inf]*2)  #拟合参数的下界和上界
c0=np.random.uniform(0,10,2) #拟合参数初值  
p,pcov=curve_fit(f,xy0,z0,bounds=bd,p0=c0)
print('拟合的参数值为：', p)

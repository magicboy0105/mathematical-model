#程序文件ti7_9_2.py
import numpy as np
from scipy.optimize import curve_fit

x0=np.linspace(-6,6,30)
y0=np.linspace(-8,8,30)
xy0=np.vstack([x0,y0])
g=lambda xy,a,b: a*xy[0]*xy[1]+b*xy[0]
z0=g(xy0,2,3)  #计算对应的函数值
p,pcov=curve_fit(g,xy0,z0)
print('拟合的参数值为：', p)

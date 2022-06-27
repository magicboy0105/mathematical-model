#程序文件ex7_17.py
import numpy as np
from scipy.optimize import curve_fit
import pylab as plt

x0 = np.array([0.81,0.91,0.13,0.91,0.63,0.098,0.28,0.55,0.96,0.96,0.16,0.97,0.96])
y0 = np.array([0.17,0.12,0.16,0.0035,0.37,0.082,0.34,0.56,0.15,-0.046,0.17,-0.091,-0.071])
y = lambda x,a,b,c,d,k: (a+b*x)*(x<k)+(c+d*x)*(x>=k)
LB=[-np.inf]*4; LB.append(min(x0))
UB=[np.inf]*4; UB.append(max(x0))
p= curve_fit(y,x0,y0,bounds=(LB,UB))[0]
print('拟合参数为:', p)
x = np.linspace(min(x0), max(x0), 100)
plt.rc('font', family='SimHei')     #用来正常显示中文标签
plt.rc('axes', unicode_minus=False) #用来正常显示负号
plt.plot(x0,y0,'*',label='数据')    #画已知数据的散点图
plt.plot(x,y(x,*p),label='拟合')    #画拟合函数的图形
plt.legend(); plt.show()

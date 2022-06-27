#程序文件ti7_1.py
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import pylab as plt

g=lambda x: (3*x**2+4*x+6)*np.sin(x)/(x**2+8*x+6)
x0=np.linspace(0,10,1000); y0=g(x0)
gh=interp1d(x0,y0,'cubic')  #计算三次样条插值函数
xn=np.linspace(0,10,10000); yn=gh(xn)
I1=quad(g,0,10)     #求原来函数的积分
I2=np.trapz(yn,xn)  #求插值函数的积分
print('I1=',I1); print('I2=',I2)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)
plt.plot(x0,y0,'*-',label='原来函数')
plt.plot(xn,yn,'.-',label='插值函数')
plt.legend(); plt.show()

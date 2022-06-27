#程序文件ti8_10.py
import numpy as np
import sympy as sp
import pylab as plt
from scipy.optimize import fsolve, fmin

La = np.log(2)/5; mu = np.log(2)/6  #求两个系数
yc = 1100*La/(La-mu)  #计算y(t)前面系数
xt = lambda t: 1100*np.exp(-La*t)
yt = lambda t: yc*(np.exp(-mu*t)-np.exp(-La*t))
t0 = np.linspace(0, 25, 50)
plt.rc('font',size=16); plt.rc('text', usetex=True)
plt.plot(t0, xt(t0),'--', label='$x(t)$')
plt.plot(t0, yt(t0),label='$y(t)$')
plt.legend(); plt.grid(); plt.xlabel('$t$/h')
plt.ylabel('$x,y$/mg', rotation=90)
y2 = yt(2)  #2h时血液中的药量
print('2h时血液中的药量：', y2)
eq = lambda t: yt(t)-400  #定义代数方程
t1 = fsolve(eq, 2)  #求血液中药量达到400mg的时间
print('药量达到400mg的时间：', t1)
ytm = lambda t: -yt(t)  #定义yt相反数的匿名函数
t2 = fmin(ytm, 2)  #求2附近y(t)的极大点
print('{}时达到最大药量{}'.format(t2,yt(t2)))
mu2 = 2*mu; print('mu2=', mu2)
c1 = 1100*La/(mu2-La)
c2 = (y2-c1*np.exp(-La*2))/np.exp(-mu2*2)
zt = lambda t: c1*np.exp(-La*t)+c2*np.exp(-mu2*t)
t2 = np.linspace(2, 25, 50)
plt.figure(); plt.plot(t2, zt(t2), label='$z(t)$')
plt.plot(t0, xt(t0), '--', label='$x(t)$')
plt.legend(); plt.grid(); plt.xlabel('$t$/h')
plt.ylabel('$x,z$/mg', rotation=90)
ztm = lambda t: -zt(t)  #定义zt相反数的匿名函数
t3 = fmin(ztm, 2)  #求2附近z(t)的极大点
print('{}时达到最大药量{}'.format(t3,zt(t3)))
x2 = xt(2); mu3 = x2*La/y2; n = mu3/mu
print('药量不增加时mu=', mu3); print('倍数：',n)
plt.show()


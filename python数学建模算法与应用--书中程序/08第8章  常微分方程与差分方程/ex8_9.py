#程序文件ex8_9.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

np.random.seed(2)  #为了进行一致性比较，每次运行取相同随机数
sigma=10; rho=28; beta=8/3;
g=lambda f,t: [sigma*(f[1]-f[0]), rho*f[0]-f[1]-f[0]*f[2],
               f[0]*f[1]-beta*f[2]]   #定义微分方程组的右端项
s01=np.random.rand(3)   #初始值
t0=np.linspace(0,50,5000)
s1=odeint(g,s01,t0)   #求数值解
plt.rc('text',usetex=True); plt.rc('font',size=16)
plt.subplots_adjust(wspace=0.6)
ax=plt.subplot(121, projection='3d')
plt.plot(s1[:,0],s1[:,1],s1[:,2],'r')  #画轨线
ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
s02=s01+0.000001
s2 = odeint(g,s02,t0)  #初值变化后，再求数值解
plt.subplot(122)
plt.plot(t0,s1[:,0]-s2[:,0],'.-') #画x(t)的差
plt.xlabel('$t$'); plt.ylabel('$x_1(t)-x_2(t)$',rotation=90)
plt.show()


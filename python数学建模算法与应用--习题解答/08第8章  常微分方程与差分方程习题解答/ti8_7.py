#程序文件ti8_7.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

dy1=lambda y,t: [y[1],-9.8*np.sin(y[0])]
dy2=lambda y,t: [y[1],-9.8*np.sin(y[0])-0.1*y[1]]               
t0=np.linspace(0,30,201); y0=[15/np.pi,0]  #初值
s1=odeint(dy1,y0,t0)
plt.subplot(121); plt.plot(t0,s1[:,0])
s2=odeint(dy2,y0,t0)
plt.subplot(122); plt.plot(t0,s2[:,0]); plt.show()

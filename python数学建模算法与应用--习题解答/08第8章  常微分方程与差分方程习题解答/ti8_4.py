#程序文件ti8_4.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

plt.rc('font',size=15); plt.rc('text',usetex=True)
dz=lambda z,t: [-z[0]**3-z[1],z[0]-z[1]**3]
t0=np.linspace(0,30,201)
s=odeint(dz,[1,0.5],t0)
plt.subplot(121)
plt.plot(t0,s[:,0],'--',label='$x(t)$')
plt.plot(t0,s[:,1],label='$y(t)$')
plt.legend(); plt.subplot(122)
plt.plot(s[:,0],s[:,1]); plt.show()





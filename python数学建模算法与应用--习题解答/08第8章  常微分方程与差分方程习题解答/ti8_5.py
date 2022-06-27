#程序文件ti8_5.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

plt.rc('font',size=15); plt.rc('text',usetex=True)
dy=lambda y,t: [y[1],y[2],-3*y[0]*y[2]+2*y[1]**2-y[3],y[4],-2.1*y[0]*y[4]]
t0=np.linspace(0,10,51); y0=[0,0,0.68,1,-0.5]
s=odeint(dy,y0,t0)
plt.plot(t0,s[:,0],'--*',label='$f(\eta)$')
plt.plot(t0,s[:,3],'p-',label='$T(\eta)$')
plt.xlabel('$\eta$'); plt.legend(); plt.show()

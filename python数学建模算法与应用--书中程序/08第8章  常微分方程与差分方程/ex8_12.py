#程序文件ex8_12.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

mu = 1/82.45; lamda= 1-mu
dz = lambda z, t: [z[1], 2*z[3]+z[0]-lamda*(z[0]+mu)/
    ((z[0]+mu)**2+z[2]**2)**(3/2)-mu*(z[0]-lamda)/
    ((z[0]+lamda)**2+z[2]**2)**(3/2), z[3],
    -2*z[1]+z[2]-lamda*z[2]/((z[0]+mu)**2+z[2]**2)**(3/2)-
    mu*z[2]/((z[0]+lamda)**2+z[2]**2)**(3/2)]
t = np.linspace(0, 100, 1001);
s = odeint(dz, [1.2, 0, 0, -1.0494], t)
plt.rc('text',usetex=True)
plt.plot(s[:,0], s[:,2]); plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0); plt.show()



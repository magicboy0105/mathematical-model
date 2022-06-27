#程序文件zex8_1.py
import numpy as np
import pylab as plt

i0 = 0.1; r = 0.01
it = lambda t: 1/(1+(1/i0-1)*np.exp(-r*t))
dit = lambda t: r*it(t)*(1-it(t))
t = np.linspace(0, 800, 801)
plt.rc('text', usetex=True)
plt.rc('font', size=18)
plt.subplot(121); plt.plot(t, dit(t))
plt.xlabel('$t$')
plt.ylabel('$\\frac{di}{dt}$', rotation=0)
plt.subplot(122); plt.plot(t, it(t))
plt.xlabel('$t$'); plt.ylabel('$i(t)$', rotation=0)
plt.show()

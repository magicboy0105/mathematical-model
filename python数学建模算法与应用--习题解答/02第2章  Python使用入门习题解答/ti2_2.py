#程序文件ti2_2.py
from scipy.special import gamma
import pylab as plt
import numpy as np

plt.rc('text',usetex=True)
x = np.linspace(-5, 5, 1000)
plt.plot(x, gamma(x), c='k')
plt.xlabel('$x$')
plt.ylabel('$\Gamma(x)$'); plt.show()

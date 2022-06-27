#程序文件ti8_2_1.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

dy = lambda y,x: [y[1], (1/(4*x**2)-1)*y[0]-y[1]/x]
y0 = [2, -2/np.pi]  #初值
x = np.linspace(np.pi/2, 6, 100)
s = odeint(dy, y0, x)  #求数值解
plt.plot(x, s[:,0], '*-'); plt.show()

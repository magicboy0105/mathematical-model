#程序文件ti8_2_2.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

dy = lambda y,x: [y[1], -y[0]*np.cos(x)]
y0 = [1, 0]  #初值
x = np.linspace(0, 8, 100)
s = odeint(dy, y0, x)  #求数值解
plt.plot(x, s[:,0], '*-'); plt.show()

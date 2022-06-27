#程序文件ex7_3.py
import numpy as np
import pylab as plt
from scipy.interpolate import lagrange

yx = lambda x: 1/(1+x**2)

def fun(n):
    x = np.linspace(-5, 5, n+1)
    p = lagrange(x, yx(x))  # n次插值多项式
    return p

x0 = np.linspace(-5, 5, 100)
plt.rc('text', usetex=True)    #使用LaTeX字体
plt.rc('font', size=15); N = [6, 8, 10]
s = ['--*b', '-.', '-p']
for k in range(len(N)):
    p = fun(N[k]); plt.plot(x0, np.polyval(p,x0),s[k])
plt.plot(x0, yx(x0));
plt.legend(['$n=6$', '$n=8$', '$n=10$', '$1/(1+x^2)$'])
plt.show()



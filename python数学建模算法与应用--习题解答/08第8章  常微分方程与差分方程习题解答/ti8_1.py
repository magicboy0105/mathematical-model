#程序文件ti8_1.py
import sympy as sp
import numpy as np
import pylab as plt

sp.var('x'); sp.var('y',cls=sp.Function)
eq=y(x).diff(x)-y(x)-sp.sin(x)
x0=np.linspace(-2,4,100)
s=['-', '--', ':', '-.']
plt.rc('text',usetex=True); plt.rc('font',size=15)
for k in range(1,5):
    yk1=sp.dsolve(eq,ics={y(0):k})  #求常微分方程符号解
    yk2=sp.simplify(yk1.args[1]); print(yk2)
    yk3=sp.lambdify(x,yk2,'numpy')  #转换为匿名函数
    plt.plot(x0, yk3(x0), s[k-1], label='$y(0)={}$'.format(k))
plt.legend(); plt.show()



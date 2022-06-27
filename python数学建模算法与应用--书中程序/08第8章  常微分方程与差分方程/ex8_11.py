#程序文件ex8_11.py
from scipy.integrate import odeint
import numpy as np
import sympy as sp
import pylab as plt

df = lambda f, x: [f[1], 2*f[1]-f[0]+np.exp(x)]
x1 = np.linspace(0,1,51); s1 = odeint(df,[1,-1],x1)
x2 = np.linspace(0,-1,51); s2 = odeint(df,[1,-1],x2)
plt.rc('font', family='SimHei')
plt.rc('axes', unicode_minus=False)
plt.rc('font', size=16)
plt.plot(x2,s2[:,0],'P-',x1,s1[:,0],'^-')
sp.var('x'); y = sp.Function('y')
eq = y(x).diff(x,2)-2*y(x).diff(x)+y(x)-sp.exp(x)
con = {y(0):1,y(x).diff(x).subs(x,0):-1}
s = sp.dsolve(eq, ics=con)
sx = sp.lambdify(x, s.args[1], 'numpy')  #转换成匿名函数
x3 = np.linspace(-1,1,101); plt.plot(x3, sx(x3), 'k-')
plt.legend(['[-1,0]上数值解','[0,1]上数值解','符号解'])
plt.show()


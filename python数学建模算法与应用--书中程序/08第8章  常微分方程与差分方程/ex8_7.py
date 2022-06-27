#程序文件ex8_7.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt
import sympy as sp

dy = lambda y, x: -2*y+2*x**2+2*x  #自变量参数在函数参数最后
xx = np.linspace(0,3,31)
s = odeint(dy, 1, xx)
print('x={}\n对应的数值解y={}'.format(xx, s.flatten()))
plt.plot(xx, s,'*')
sp.var('x'); y=sp.Function('y')
eq=y(x).diff(x)+2*y(x)-2*x**2-2*x
s2=sp.dsolve(eq,ics={y(0):1})
sx = sp.lambdify(x,s2.args[1],'numpy')  #符号函数转匿名函数
plt.plot(xx, sx(xx))
plt.show()

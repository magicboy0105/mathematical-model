#程序文件ti8_3.py
import sympy as sp
import numpy as np
import pylab as plt

sp.var('t'); sp.var('x,y',cls=sp.Function)
eq = [x(t).diff(t)-x(t)+2*y(t), y(t).diff(t)-x(t)-2*y(t)]
con = {x(0): 1,y(0): 0}
s = sp.dsolve(eq, ics=con)
xt = s[0].args[1]; print(xt)
yt = s[1].args[1]; yt = sp.simplify(yt); print(yt)
xt = sp.lambdify(t,xt,'numpy')  #转换为匿名函数
yt = sp.lambdify(t,yt,'numpy')
t0 = np.linspace(0,1,20)
plt.rc('font', size=15); plt.rc('text', usetex=True)
plt.plot(t0, xt(t0), label='$x(t)$')
plt.plot(t0, yt(t0), '--', label='$y(t)$')
plt.xlabel('$t$'); plt.legend(); plt.show()




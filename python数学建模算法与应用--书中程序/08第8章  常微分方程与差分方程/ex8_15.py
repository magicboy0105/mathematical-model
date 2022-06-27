#程序文件ex8_15.py
import numpy as np
import sympy as sp
import pylab as plt
from scipy.integrate import odeint

plt.rc('text',usetex=True)
plt.rc('font',size=15); sp.var('x,y')
eq=[0.2*x-0.005*x*y,-0.5*y+0.01*x*y]
s1=sp.solve(eq,[x,y]); print(s1)
x=np.linspace(0,100,10)
x,y=np.meshgrid(x,x)
u=0.2*x-0.005*x*y; v=-0.5*y+0.01*x*y
plt.quiver(x,y,u,v)
plt.xlabel('$x$'); plt.ylabel('$y$',rotation=0)
def func(f,t):
    x, y=f
    return [0.2*x-0.005*x*y,-0.5*y+0.01*x*y]
t=np.linspace(0,100,1000)
s=odeint(func, [70,40], t)
x1=max(s[:,0]); x2=min(s[:,0])
print("x最大值：", x1); print("x最小值为：", x2)
y1=max(s[:,1]); y2=min(s[:,1])
print("y最大值：", y1); print("y最小值：", y2)
plt.plot(s[:,0], s[:,1]); plt.figure()
plt.plot(t, s[:,0], '.-', label='$x(t)$')
plt.plot(t, s[:,1], 'P-', label='$y(t)$')
plt.legend(); plt.xlabel('$t$')
print("请点击x(t)或y(t)解曲线上相邻两个极小点!")
x=plt.ginput(2); print('点击的点',x)
T=x[1][0]-x[0][0]; print("周期T为：",T)
plt.show()

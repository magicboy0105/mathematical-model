#程序文件ex8_18.py
import numpy as np
import pylab as plt

v = 1; u = 5 * v; dt = 0.00004  #设置t的变化步长
x = 0; y = 0; t = 0  #设置初始位置和时间
plt.rc('text', usetex=True)
plt.rc('font', size=15)
plt.plot(x, y, '.')
while x <= 0.99999:
    pq = [1-x, v*t-y]
    x = x + u * pq[0]/np.linalg.norm(pq) * dt
    y = y + u * pq[1]/np.linalg.norm(pq) * dt
    t = t + dt
    plt.plot(x, y, '.')
print('x=', round(x,4)); print('y=', round(y,4))
print('t=', round(t,4)); plt.xlabel('$x$')
plt.ylabel('$y$', rotation=0); plt.show()
    







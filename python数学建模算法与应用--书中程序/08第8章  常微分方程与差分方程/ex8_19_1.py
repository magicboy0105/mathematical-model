#程序文件ex8_19_1.py
import numpy as np
import pylab as plt

a = 1 - 0.2**(1/12); m = 1.109 * 10 ** 5
w3 = 17.86; w4 = 22.99
X=[]; Z=[]; N=[]
for k in np.arange(0, 0.875, 0.001):
    x1 = 1.22*10**11*(1-1/(m*(1-a-0.42*k)**8*(1-a)**24*
         (1/2+(1-a-k)**8*(1-a)**4)))
    x2 = (1-a)**12*x1; x3 = (1-a)**12*x2
    x4 = (1-a-0.42*k)**8*(1-a)**4*x3
    X.append([x1, x2, x3, x4])
    n = m*(1-a-0.42*k)**8*(1-a)**24*(1/2+(1-a-k)**8*(1-a)**4)*x1
    N.append(n)
    z = (0.42*k*w3*(1-(1-a-0.42*k)**8)/(a+0.42*k)*x3+
         k*w4*(1-(1-a-k)**8)/(a+k)*x4)
    Z.append(z)
mz = max(np.array(Z)); ind = np.argmax(Z)
k4 = 0.001 * ind; k3 = 0.42 * k4
print('最大生产量：', mz)
print('各年龄组鱼群数：', X[ind])
print('k4=',k4); print('k3=',k3)
plt.rc('text', usetex=True); plt.rc('font', size=16)
plt.plot(np.arange(0, 0.875, 0.001), Z)
plt.ylabel('$z$', rotation=0)
plt.xlabel('$k$'); plt.show()

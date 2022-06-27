#程序文件ti5_7.py
import cvxpy as cp
import numpy as np
import pylab as plt

x=cp.Variable(3, pos=True)
con=[x[0]>=0, sum(x[:2])>=100, sum(x)==180]
obj0=cp.Minimize(0.2*sum(x**2)+50*sum(x)+4*(2*x[0]+x[1]-140))
prob0=cp.Problem(obj0, con)
prob0.solve(); print('最优值为：', prob0.value)
print('最优解为：\n', x.value)

plt.subplots_adjust(wspace = 0.5); V1=[]
for a in np.arange(40, 61, 2):
    obj1=cp.Minimize(0.2*sum(x**2)+a*sum(x)+4*(2*x[0]+x[1]-140))
    prob1=cp.Problem(obj1, con)
    prob1.solve(); V1.append(prob1.value)
plt.subplot(131); plt.plot(np.arange(40, 61, 2), V1)

V2=[]
for b in np.arange(0.15, 0.26, 0.01):
    obj2=cp.Minimize(b*sum(x**2)+50*sum(x)+4*(2*x[0]+x[1]-140))
    prob2=cp.Problem(obj2, con)
    prob2.solve(); V2.append(prob2.value)
plt.subplot(132); plt.plot(np.arange(0.15, 0.26, 0.01), V2)

V3=[]
for c in np.arange(3, 5.1, 0.1):
    obj3=cp.Minimize(0.2*sum(x**2)+50*sum(x)+c*(2*x[0]+x[1]-140))
    prob3=cp.Problem(obj3, con)
    prob3.solve(); V3.append(prob3.value)
plt.subplot(133); plt.plot(np.arange(3, 5.1, 0.1), V3)
plt.show()
    


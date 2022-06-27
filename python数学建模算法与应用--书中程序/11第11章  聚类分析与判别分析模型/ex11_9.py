#程序文件ex11_9.py
import numpy as np
import sympy as sp
from numpy.linalg import inv
f = open('data11_9.txt'); d = f.readlines()
a = []; b = []
for i in range(2): a.extend(d[i].split())
a = np.array([eval(e) for e in a]).reshape(2,-1)
mu1 = a.mean(axis=1, keepdims=True); s1 = np.cov(a, ddof=1)
for i in range(2,4): b.extend(d[i].split())
b = np.array([eval(e) for e in b]).reshape(2,-1)
mu2 = b.mean(axis=1, keepdims=True); s2 = np.cov(b, ddof=1)
sp.var('x1,x2'); X = sp.Matrix([x1, x2]) #X为列向量
d1 = (X-mu1).T@inv(s1)@(X-mu1)
d1 = sp.expand(d1)
d2 = (X-mu2).T@inv(s2)@(X-mu2)
d2 = sp.expand(d2)
W = sp.lambdify('x1,x2', d1-d2, 'numpy')
sol = W(np.array([1.24,1.28,1.40]), np.array([1.80,1.84,2.04]))
check1 = W(a[0], a[1]); check2 = W (b[0], b[1])
print(np.round(sol,4))  #输出3个判别函数值

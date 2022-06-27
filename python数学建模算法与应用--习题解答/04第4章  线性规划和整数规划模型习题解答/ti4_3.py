#程序文件ti4_3.py
import pylab as plt
import numpy as np
import cvxpy as cp
plt.rc('text',usetex=True); plt.rc('font',size=16)
x=cp.Variable(6,pos=True)
obj=cp.Minimize(x[5])
a1=np.array([0.025, 0.015, 0.055, 0.026])
a2=np.array([0.05, 0.27, 0.19, 0.185, 0.185])
a3=np.array([1, 1.01, 1.02, 1.045, 1.065])
k=0.05; kk=[]; ss=[]; X=[]
while k<0.27:
    con=[cp.multiply(a1,x[1:5])<=x[5],
         a2@x[:-1]>=10000*k, a3@x[:-1]==10000]
    prob=cp.Problem(obj,con)
    prob.solve(solver='GLPK_MI')
    kk.append(k); ss.append(prob.value)
    X.append(x.value); k=k+0.005
plt.plot(kk,ss,'r*'); plt.xlabel('$k$')
plt.ylabel('$R$',rotation=0); plt.show()
print(round(ss[32],2)); print(np.round(X[32],2))

#程序文件ex7_12.py
import numpy as np
import cvxpy as cp

a = np.loadtxt('data7_12.txt'); x0 = a[0]; y0 = a[1]
t=cp.Variable(2,pos=True)  #拟合的参数：t[0]=a,t[1]=b
c=np.vstack([np.exp(x0),np.log(x0)]).T
obj=cp.Minimize(cp.sum_squares(c@t - y0))
con=[sum(t)<=1]; prob=cp.Problem(obj,con)
prob.solve(solver='CVXOPT')
print("最优解为：\n", t.value)

#程序文件ti4_5.py
import cvxpy as cp
import numpy as np

c=np.loadtxt('ti4_5.txt',delimiter=',')
c=np.reshape(c,(6,6))
x=cp.Variable((6,6),integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
con= [cp.sum(x, axis=0)==1, cp.sum(x, axis=1)==1, x>=0, x<=1]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value); print("最优解为：\n",x.value)

#程序文件ti4_8.py
import numpy as np
import cvxpy as cp

a=np.array([18,15,23,12])
b=np.array([480,650,580,390])
c=np.array([3100,3800,3500,2850])
w=np.array([10,16,8])
v=np.array([6800,8700,5300])
x=cp.Variable((4,3),pos=True)
obj=cp.Maximize(c@cp.sum(x,axis=1))
con=[cp.sum(x,axis=1)<=a, cp.sum(x,axis=0)<=w,
     x.T@b<=v, sum(x[:,0])/10==sum(x[:,1])/16,
     sum(x[:,1])/16==sum(x[:,2])/8]
prob=cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print('最优值为：', prob.value)
print('最优解为：\n', x.value)
print('三种货物的运量为：', np.sum(x.value, axis=1))

#程序文件ex6_11.py
import numpy as np
import cvxpy as cp

L=[(1,2,18),(1,5,15),(2,3,20),(2,4,60),(2,5,12),
   (3,4,30),(3,5,18),(4,6,10),(5,6,15)]
a=np.ones((6,6))*100000  #邻接矩阵初始化
for i in range(len(L)):
    a[L[i][0]-1,L[i][1]-1]=L[i][2]
    a[L[i][1]-1,L[i][0]-1]=L[i][2]
x=cp.Variable((6,6), integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(a, x)))
con=[sum(x[1,:])==1, sum(x[:,1])==0,
     sum(x[:,3])==1, x>=0, x<=1]
for i in set(range(6))-{1,3}:
    con.append(sum(x[i,:])==sum(x[:,i]))
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", x.value)
i,j=np.nonzero(x.value)
print("最短路径的起点：", i+1)
print("最短路径的终点：", j+1)

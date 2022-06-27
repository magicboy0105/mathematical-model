#程序文件ex6_13.py
import cvxpy as cp
import numpy as np

L=[(0,1,2),(0,2,1),(0,3,3),(0,4,4),(0,5,4),(0,6,2),(0,7,5),(0,8,4),
   (1,2,4),(1,8,1),(2,3,1),(3,4,1),(4,5,5),(5,6,2),(6,7,3),(7,8,5)]
a=np.ones((9,9))*10000
for i in range(len(L)):
    a[L[i][0], L[i][1]]=L[i][2]
    a[L[i][1], L[i][0]]=L[i][2]
x=cp.Variable((9,9), integer=True)
u=cp.Variable(9, pos=True)
obj=cp.Minimize(cp.sum(cp.multiply(a,x)))
con=[cp.sum(x[0,:])>=1, u[0]==0,
     u[1:]>=1, u[1:]<=8, x>=0, x<=1]
for i in range(1,9):
    con.append(sum(x[:,i])==1)
for i in range(9):
    for j in range(1,9):
        con.append(u[i]-u[j]+9*x[i,j]<=8)
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
i, j = np.nonzero(x.value)
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
print('i=', i); print('j=', j)

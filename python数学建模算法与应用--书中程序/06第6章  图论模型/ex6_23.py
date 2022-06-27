#程序文件ex6_23.py
import numpy as np
import cvxpy as cp

L = [(1,2,5,5,0), (1,3,10,8,700), (1,4,11,8,400), (2,5,4,3,450), (3,4,4,4,0),
     (3,5,0,0,0), (4,6,15,15,0), (5,6,21,16,600), (5,7,25,22,300),
     (5,8,35,30,500), (6,7,0,0,0), (6,8,20,16,500), (7,8,15,12,400)]
x = cp.Variable(8, pos=True)
y = cp.Variable((8,8), integer=True); fun = 0
for i in range(len(L)):
    fun = fun + y[L[i][0]-1,L[i][1]-1] * L[i][4]
obj = cp.Minimize(fun); con =[x[7]-x[0]<=49, y>=0]
for i in range(len(L)):
    con.append(x[L[i][1]-1]-x[L[i][0]-1]+y[L[i][0]-1,L[i][1]-1]>=L[i][2])
    con.append(y[L[i][0]-1,L[i][1]-1]<=L[i][2]-L[i][3])
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值为', prob.value); print('x的取值为：\n', x.value)
print('y的取值为：\n', y.value); ni, nj = np.nonzero(y.value)
print('压缩工期的作业为:'); print(ni+1); print(nj+1)


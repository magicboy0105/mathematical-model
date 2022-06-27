#程序文件ex6_20.py
import numpy as np
import cvxpy as cp

x = cp.Variable(8, pos=True)
L = [(1,2,5), (1,3,10), (1,4,11), (2,5,4), (3,4,4), (3,5,0), (4,6,15),
     (5,6,21), (5,7,25), (5,8,35), (6,7,0), (6,8,20), (7,8,15)]
obj = cp.Minimize(sum(x)); con = []
for k in range(len(L)):
    con.append(x[L[k][1]-1] >= x[L[k][0]-1] + L[k][2])
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值为', prob.value); print('最优解为：', x.value)

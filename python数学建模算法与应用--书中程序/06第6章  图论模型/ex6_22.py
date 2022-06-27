#程序文件ex6_22.py
import numpy as np
import cvxpy as cp

L = [(1,2,5), (1,3,10), (1,4,11), (2,5,4), (3,4,4), (3,5,0), (4,6,15),
     (5,6,21), (5,7,25), (5,8,35), (6,7,0), (6,8,20), (7,8,15)]
x = cp.Variable((8,8), integer=True); fun = 0
for i in range(len(L)):
    fun = fun + x[L[i][0]-1,L[i][1]-1] * L[i][2]
obj = cp.Maximize(fun); con =[ x>=0, x<=1]
out = [a[1]-1 for a in L if a[0]==1]  #起点相邻顶点的编号
con.append(sum(x[0,out])==1)   #起点发出弧的约束
ind = [a[0]-1 for a in L if a[1]==8]  #终点相邻顶点的编号
con.append(sum(x[ind,7])==1)   #终点进入弧的约束
for k in range(2,8):
    out = [a[1]-1 for a in L if a[0]==k]  #k的出弧的相邻顶点
    ind = [a[0]-1 for a in L if a[1]==k]  #k的入弧的相邻顶点
    con.append(sum(x[k-1,out])==sum(x[ind,k-1]))
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值为', prob.value); print('最优解为：\n', x.value)
ni, nj = np.nonzero(x.value)
print('关键路径的端点为:'); print(ni+1); print(nj+1)


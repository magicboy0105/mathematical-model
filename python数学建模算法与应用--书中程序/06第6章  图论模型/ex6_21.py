#程序文件ex6_21.py
import numpy as np
import cvxpy as cp

n =8; x = cp.Variable(n, pos=True); z = np.zeros(n)
L = [(1,2,5), (1,3,10), (1,4,11), (2,5,4), (3,4,4), (3,5,0), (4,6,15),
     (5,6,21), (5,7,25), (5,8,35), (6,7,0), (6,8,20), (7,8,15)]
obj = cp.Minimize(sum(x)); con = []
for k in range(len(L)):
    con.append(x[L[k][1]-1] >= x[L[k][0]-1] + L[k][2])
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值为', prob.value); print('最优解为：', x.value)
xx = x.value; z[-1] = xx[-1]
for k in range(n-1, 0, -1):
    z[k-1]=min([z[a[1]-1]-a[2] for a in L if a[0]==k])
print('z:', z); es=[]; lf=[]; ls=[]; ef=[]
for i in range(len(L)):
    es.append([L[i][0], L[i][1], xx[L[i][0]-1]])
    lf.append([L[i][0], L[i][1], z[L[i][1]-1]])
    ls.append([L[i][0], L[i][1], z[L[i][1]-1]-L[i][2]])
    ef.append([L[i][0], L[i][1], xx[L[i][0]-1]+L[i][2]])
print('作业最早开工时间如下：'); print(es)
print('作业最晚开工时间如下：'); print(ls)


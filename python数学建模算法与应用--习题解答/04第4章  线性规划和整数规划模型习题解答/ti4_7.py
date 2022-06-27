#程序文件ti4_7.py
import numpy as np
import cvxpy as cp

t=np.loadtxt('ti4_7.txt')
x=cp.Variable((4,3),pos=True)
y=cp.Variable((4,4),integer=True)
T=cp.Variable(pos=True)
obj=cp.Minimize(T)
cons=[]
for i in range(4):
    cons.append(T>=x[i,2]+t[i,2])
for i in range(4):
    for j in range(2):
        cons.append(x[i,j]+t[i,j]<=x[i,j+1])
for i in range(3):
    for k in range(i+1,4):
        for j in range(3):
            cons.append(x[i,j]+t[i,j]<=x[k,j]+10000*y[i,k])
            cons.append(x[k,j]+t[k,j]<=x[i,j]+10000*(1-y[i,k]))
cons.append(y>=0); cons.append(y<=1)
prob=cp.Problem(obj,cons)
prob.solve(solver="GLPK_MI")
print("最优值为：", prob.value)
print("最优解为：\n x={}\n y={}".format(x.value, y.value))

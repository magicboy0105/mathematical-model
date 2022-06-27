#程序文件ex4_11.py
import cvxpy as cp
import numpy as np
a=np.loadtxt("data4_11.txt")
d=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        d[i,j]=np.linalg.norm(a[:,i]-a[:,j])
x=cp.Variable(10, integer=True)
y=cp.Variable((10, 10),integer=True)
obj=cp.Minimize(sum(x))
con=[sum(y)>=1, cp.sum(y,axis=1)<=5,
     x>=0, x<=1, y>=0, y<=1]  
for i in range(10):
    con.append(x[i]==y[i,i])
    for j in range(10):
        con.append(d[i,j]*y[i,j]<=10*x[i])
        con.append(x[i]>=y[i,j])
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", x.value)
print('----------\n', y.value)



#程序文件ex4_9_2.py
import cvxpy as cp
import numpy as np

a=np.array([35,40,50,45,55,30])
x=cp.Variable(6, integer=True)
obj=cp.Minimize(sum(x)); cons=[x>=0]
for i in range(6):
    cons.append(x[(i-1)%6]+x[i]>=a[i])
prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print("最优值为：",prob.value)
print("最优解为：",x.value)

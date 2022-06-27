#程序文件ti5_2.py
import numpy as np
import cvxpy as cp
a=np.array([1, 0, 1, 4, 3, 4, 1, 0])  #8个余数的值
x=cp.Variable(integer=True)
y=cp.Variable(8, integer=True)
obj=cp.Minimize(x)
con=[x>=0, y>=0]
for i in range(8):
    con.append((i+2)*y[i]+a[i]==x)
prob=cp.Problem(obj, con)
prob.solve(solver="GLPK_MI")
print("最优值为：", prob.value)

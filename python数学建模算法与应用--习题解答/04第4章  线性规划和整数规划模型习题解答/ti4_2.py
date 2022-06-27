#程序文件ti4_2.py
import cvxpy as cp
import numpy as np
x=cp.Variable(5,integer=True)
c=np.array([20,90,80,70,30])
a=np.array([[-1,-1,0,0,-1], [0,0,-1,-1,0], [3,0,2,0,0], [0,3,0,2,1]])
b=np.array([-30,-30,120,48])
prob=cp.Problem(cp.Minimize(c@x), [a@x<=b, x>=0])
prob.solve(solver="GLPK_MI")
print("最优值为：", prob.value); print("最优解为：\n", x.value)

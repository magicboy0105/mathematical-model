#程序文件ti4_4.py
import cvxpy as cp
import numpy as np
x=cp.Variable(2, integer=True)
c=np.array([2,1]); a=np.array([[0,5],[6,2],[1,1]])
b=np.array([15,24,5])
prob=cp.Problem(cp.Maximize(c@x), [a@x<=b, x>=0])
prob.solve(solver="GLPK_MI")
print("最优值为：",prob.value); print("最优解为：\n", x.value)

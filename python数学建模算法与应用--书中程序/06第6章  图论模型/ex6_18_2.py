#程序文件ex6_18_2.py
import numpy as np
import cvxpy as cp
a=np.array([4, 3, 3, 2, 4])
x=cp.Variable((4,5), integer=True)
obj = cp.Maximize(cp.sum(x))
con= [cp.sum(x, axis=0) <= a, x[1,0]+x[1,1]+x[1,4] <= 2,
      x[2,0]+x[2,3] <= 1, sum(x[3,:-1]) <= 2, x>=0, x<=1]
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value)
print("最优解为：\n",x.value)

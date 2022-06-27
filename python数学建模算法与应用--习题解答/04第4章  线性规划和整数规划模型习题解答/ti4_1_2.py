#程序文件ti4_1_2.py
import cvxpy as cp
import numpy as np
x=cp.Variable(2,pos=True)
c=np.array([72,64])
a=np.array([[1,1],[12,8],[3,0]])
b=np.array([50,480,100])
obj=cp.Maximize(c@x); con=[a@x<=b]
prob=cp.Problem(obj,con)
prob.solve(solver="GLPK_MI")
print("最优值为：",prob.value); print("最优解为：",x.value)

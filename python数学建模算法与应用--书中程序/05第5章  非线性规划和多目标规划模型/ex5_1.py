#程序文件ex5_1.py
import numpy as np
import cvxpy as cp

x=cp.Variable(2,pos=True)
obj=cp.Minimize(sum(x**2)-4*x[0]+4)
con=[-x[0]+x[1]-2<=0,
     x[0]**2-x[1]+1<=0]
prob = cp.Problem(obj, con)
prob.solve(solver='CVXOPT')
print("最优值为:",round(prob.value,4))
print("最优解为：\n", np.round(x.value,4))


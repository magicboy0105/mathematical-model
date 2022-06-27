#程序文件ex5_3.py
import cvxpy as cp
import numpy as np

c2 = np.array([[-1, -0.15],[-0.15, -2]])
c1 = np.array([98, 277])
a = np.array([[1, 1], [1, -2]])
b = np.array([100, 0])
x = cp.Variable(2, pos=True)
obj =cp.Maximize(cp.quad_form(x,c2) + c1 @ x)
con = [ a @ x <= b]
prob = cp.Problem(obj, con)
prob.solve(solver='CVXOPT')
print('最优解为：', np.round(x.value,4))
print('最优值为：', round(prob.value,4))


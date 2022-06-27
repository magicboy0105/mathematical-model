#程序文件ex5_7_1.py
import cvxpy as cp
import numpy as np

c = np.arange(1, 5)
a = np.array([[1,-1,-1,1], [1,-1,1,-3], [1,-1,-2,3]])
b = np.array([0, 1, -1/2])
x = cp.Variable(4)
obj = cp.Minimize(c @ cp.abs(x))
con = [a @ x == b]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", x.value)

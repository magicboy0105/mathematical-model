#程序文件ex5_7_2.py
import cvxpy as cp
import numpy as np

c = np.arange(1,5)
a = np.array([[1,-1,-1,1],[1,-1,1,-3],[1,-1,-2,3]])
b = np.array([0,1,-1/2])
u = cp.Variable(4, pos=True)
v = cp.Variable(4, pos=True)
obj = cp.Minimize(c@(u+v))
con = [a@(u-v)==b]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", u.value, '\n', v.value)
print("原问题的最优解为：", u.value-v.value)


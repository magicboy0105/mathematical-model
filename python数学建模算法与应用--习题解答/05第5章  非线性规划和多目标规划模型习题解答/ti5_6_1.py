#程序文件ti5_6_1.py
import cvxpy as cp
import numpy as np

R = np.array([[4,2.5,-10], [2.5,36,-15],[-10,-15,100]])
a = np.array([[-5,-8,-10], [20,25,30]])
b = np.array([-1000, 5000])
x = cp.Variable(3, integer=True)
obj = cp.Minimize(cp.quad_form(x, R))
con = [a @ x <= b, x >= 0]
prob = cp.Problem(obj, con)
prob.solve(solver='CPLEX')  #需要pip install cplex
print('最优值：', prob.value)
print('最优解：', x.value)

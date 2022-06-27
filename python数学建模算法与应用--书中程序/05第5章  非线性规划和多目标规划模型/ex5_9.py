#程序文件ex5_9.py
import numpy as np
import cvxpy as cp

c1 = np.array([-2, -3])
c2 = np.array([1, 2])
a = np.array([[0.5, 0.25], [0.2, 0.2], [1, 5], [-1, -1]])
b = np.array([8, 4, 72, -10])
x = cp.Variable(2, pos=True)
obj = cp.Minimize(0.5 * (c1 + c2) @ x)
con = [a @ x <= b]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print('最优解为：', x.value)
print('最优值为：', prob.value)

obj1 = cp.Minimize(c1 @ x)
prob1 = cp.Problem(obj1, con)
prob1.solve(solver='GLPK_MI')
v1 = prob1.value  #第一个目标函数的最优值
obj2 = cp.Minimize(c2 @ x)
prob2 = cp.Problem(obj2, con)
prob2.solve(solver='GLPK_MI')
v2 = prob2.value  #第二个目标函数的最优值
print('两个目标函数的最优值分别为：', v1, v2)
obj3 = cp.Minimize((c1@x-v1)**2+(c2@x-v2)**2)
prob3 = cp.Problem(obj3, con)
prob3.solve(solver='CVXOPT')
print('解法二的最优解：', x.value)

con.append( c1 @ x == v1)
prob4 = cp.Problem(obj2, con)
prob4.solve(solver='GLPK_MI')
x3 = x.value   #提出最优解的值
print('解法三的最优解：', x3)
print('利润：', -c1@x3); print('排放污染物：', c2@x3)


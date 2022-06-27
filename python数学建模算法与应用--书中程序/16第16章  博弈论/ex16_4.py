#程序文件ex16_4.py
import numpy as np
import cvxpy as cp

A = np.loadtxt('data16_3.txt')
x = cp.Variable(6, pos=True); y = cp.Variable(6, pos=True)
u = cp.Variable(); v = cp.Variable()
ob1 = cp.Maximize(u); con1 = [A.T @ x >=u, sum(x)==1]
prob1 = cp.Problem(ob1, con1)  #构造第1个线性规划问题
prob1.solve(solver='GLPK_MI'); print('最优值u:', prob1.value)
print('最优解x:\n', x.value)
ob2 = cp.Minimize(v); con2 = [A@y<=v, sum(y)==1]
prob2 = cp.Problem(ob2, con2)  #构造第2个线性规划问题
prob2.solve(solver='GLPK_MI'); print('最优值v:', prob2.value)
print('最优解y:\n', y.value)

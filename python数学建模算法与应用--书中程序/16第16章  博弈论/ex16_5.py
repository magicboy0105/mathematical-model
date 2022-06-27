#程序文件ex16_5.py
import numpy as np
import cvxpy as cp

A = np.array([[1/3,1/2,-1/3],[-2/5,1/5,-1/2],[1/2,-3/5,1/3]])
x = cp.Variable(3, pos=True); y = cp.Variable(3, pos=True)
u = cp.Variable(); v = cp.Variable()
ob1 = cp.Maximize(u); con1 = [A.T @ x >=u, sum(x)==1]
prob1 = cp.Problem(ob1, con1)  #构造第1个线性规划问题
prob1.solve(solver='GLPK_MI'); print('最优值u:', prob1.value)
print('最优解x:\n', np.round(x.value,4))
ob2 = cp.Minimize(v); con2 = [A@y<=v, sum(y)==1]
prob2 = cp.Problem(ob2, con2)  #构造第2个线性规划问题
prob2.solve(solver='GLPK_MI'); print('最优值v:', prob2.value)
print('最优解y:\n', np.round(y.value,4))

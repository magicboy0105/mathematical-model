#程序文件ex5_4.py
import cvxpy as cp
import numpy as np

a = np.loadtxt('data5_4.txt')
mu = a.mean(axis=0)   #计算年平均收益
F = np.cov(a.T)       #计算协方差矩阵
x = cp.Variable(3, pos=True)
ob1 = cp.Minimize(cp.quad_form(x,F))
con1 = [ mu @ x >= 0.15,
        sum(x) == 1 ]
prob1 = cp.Problem(ob1, con1)
prob1.solve(solver='CVXOPT')
print('最优值为：', round(prob1.value,4))
print('最优解为：', np.round(x.value,4))

ob2 = cp.Maximize(mu @ x)
con2 = [sum(x) == 1,
        cp.quad_form(x, F) <= 0.09]
prob2 = cp.Problem(ob2, con2)
prob2.solve(solver='CVXOPT')
print('最优值为：', round(prob2.value,4))
print('最优解为：', np.round(x.value,4))


#程序文件ti5_6_2.py
import cvxpy as cp
import numpy as np
import pylab as plt

R = np.array([[4,2.5,-10], [2.5,36,-15],[-10,-15,100]])
a = np.array([[-5,-8,-10], [20,25,30]])
x = cp.Variable(3, integer=True)
obj = cp.Minimize(cp.quad_form(x, R))
T_risk=[]; T_rate=[];
for rate in np.arange(0.05,0.25,0.01):
    b = np.array([-5000*rate, 5000])
    con = [a @ x <= b, x >= 0]
    prob = cp.Problem(obj, con)
    prob.solve()     #需要pip install -U gurobipy
    T_risk.append(prob.value); T_rate.append(rate)
print('对应的风险分别为：\n', T_risk)
plt.plot(T_rate, T_risk, '.-'); plt.show()


#程序文件ex4_12_2.py
import numpy as np
import cvxpy as cp
import pylab as plt

plt.rc('font', family='SimHei')
plt.rc('font', size=15)
x = cp.Variable(6, pos = True)
r = np.array([0.05, 0.28, 0.21, 0.23, 0.25])
p = np.array([0, 0.01, 0.02, 0.045, 0.065])
q = np.array([0, 0.025, 0.015, 0.055, 0.026])

def LP(w):
    V = []  #风险初始化
    Q = []  #收益初始化
    X = []  #最优解的初始化
    con = [(1+p) @ x[: -1] == 10000, cp.multiply(q[1:],x[1:5])<=x[5]]
    for i in range(len(w)):
        obj = cp.Minimize(w[i] * x[5] - (1-w[i]) *((r-p) @ x[: -1]))
        prob = cp.Problem(obj, con)
        prob.solve(solver='GLPK_MI')
        xx = x.value   #提出所有决策变量的取值
        V.append(max(q*xx[:-1]))
        Q.append((r-p)@xx[:-1]); X.append(xx)
    print('w=', w);     print('V=', np.round(V,2))
    print('Q=', np.round(Q,2))
    plt.figure(); plt.plot(V, Q, '*-'); plt.grid('on')
    plt.xlabel('风险（元）'); plt.ylabel('收益（元）')
    return X

w1 = np.arange(0, 1.1, 0.1)
LP(w1); print('--------------')
w2 = np.array([0.766, 0.767, 0.810, 0.811, 0.824, 0.825, 0.962, 0.963, 1.0])
X=LP(w2); print(X[-3]); plt.show()

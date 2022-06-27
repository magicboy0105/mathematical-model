#程序文件ex4_10.py
import cvxpy as cp
import numpy as np
c = np.loadtxt('data4_10.txt')
x = cp.Variable((4,5), integer=True)           #定义决策变量
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))    #构造目标函数
cons = [0<=x, x<=1, cp.sum(x, axis=0)==1,
        cp.sum(x, axis=1)<=2]                  #构造约束条件
prob = cp.Problem(obj, cons)
prob.solve(solver='GLPK_MI')                   #求解问题
print('最优解为：\n', x.value)
print('最优值为：', prob.value)

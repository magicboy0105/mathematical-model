#程序文件ex4_2.py
import cvxpy as cp
from numpy import array

c = array([70, 50, 60])  #定义目标向量
a = array([[2, 4, 3], [3, 1, 5], [7, 3, 5]])  #定义约束矩阵
b = array([150, 160, 200])  #定义约束条件的右边向量
x = cp.Variable(3, pos=True)  #定义3个决策变量
obj = cp.Maximize(c@x)    #构造目标函数
cons = [a@x <=b]     #构造约束条件
prob = cp.Problem(obj, cons)
prob.solve(solver='GLPK_MI')   #求解问题
print('最优解为：', x.value)
print('最优值为：', prob.value)

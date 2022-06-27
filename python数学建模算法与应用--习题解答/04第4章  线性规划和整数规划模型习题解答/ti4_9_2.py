#程序文件ti4_9_2.py
import cvxpy as cp
import numpy as np

a=np.loadtxt('data4_9_1.txt', dtype=int)
r=np.loadtxt('data4_9_2.txt')
x=cp.Variable(7, integer=True)
y=cp.Variable(7, integer=True)
obj=cp.Minimize(sum(x))
con=[a@x>=100, x<=1000*y, sum(y)<=3, y>=0, y<=1, x>=0]
prob=cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print('最优值为：', prob.value)
print('最优解为：\n', x.value)
print('余料长度为：\n', r@x.value)
print('三种短钢管的数量为：', a@x.value)



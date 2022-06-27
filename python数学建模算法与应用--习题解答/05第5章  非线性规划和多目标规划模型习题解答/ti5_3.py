#程序文件ti5_3.py
import cvxpy as cp
import numpy as np
x=cp.Variable(5, integer=True)
c1=np.array([1,1,3,4,2])
c2=np.array([-8,-2,-3,-1,-2])
obj=cp.Minimize(c1@x**2+c2@x)
a=np.array([[1,1,1,1,1],[1,2,2,1,6],
            [2,1,6,0,0],[0,0,1,1,5]])
b=np.array([400,800,200,200])
con=[x>=0, x<=99, a@x<=b]
prob=cp.Problem(obj, con)
prob.solve(solver='CPLEX')
print("最优值为：", prob.value)
print("最优解为：", x.value)


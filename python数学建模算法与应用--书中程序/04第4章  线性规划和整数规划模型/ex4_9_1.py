#程序文件ex4_9_1.py
import cvxpy as cp

x=cp.Variable(6, integer=True)
obj=cp.Minimize(sum(x))
cons=[x[0]+x[5]>=35, x[0]+x[1]>=40,
      x[1]+x[2]>=50, x[2]+x[3]>=45,
      x[3]+x[4]>=55, x[4]+x[5]>=30,
      x>=0]
prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print("最优值为：",prob.value)
print("最优解为：",x.value)

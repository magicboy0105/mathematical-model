#程序文件ex4_3.py
import cvxpy as cp
x=cp.Variable((5,4),pos=True)
obj=cp.Maximize(1.15*x[3,0]+1.40*x[1,2]+1.25*x[2,1]+1.06*x[4,3])
cons=[x[0,0]+x[0,3]==100000,
      x[1,0]+x[1,2]+x[1,3]==1.06*x[0,3],
      x[2,0]+x[2,1]+x[2,3]==1.15*x[0,0]+1.06*x[1,3],
      x[3,0]+x[3,3]==1.15*x[1,0]+1.06*x[2,3],
      x[4,3]==1.15*x[2,0]+1.06*x[3,3],
      x[2,1]<=40000,x[1,2]<=30000]
prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print("最优值为：",prob.value)
print("最优解为：",x.value)

#程序文件ti4_1_1.py
import cvxpy as cp
x=cp.Variable(2,pos=True)
obj=cp.Maximize(72*x[0]+64*x[1])
con=[x[0]+x[1]<=50, 12*x[0]+8*x[1]<=480, 3*x[0]<=100]
prob=cp.Problem(obj,con)
prob.solve(solver="GLPK_MI")
print("最优值为：",prob.value); print("最优解为：\n",x.value)

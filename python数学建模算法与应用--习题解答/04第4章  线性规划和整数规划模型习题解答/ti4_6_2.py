#程序文件ti4_6_2.py
import numpy as np
import cvxpy as cp
import pandas as pd

d = np.loadtxt('ti4_6_3.txt')
c = d[:-1, :-1]; a = d[:-1, -1]; b = d[-1, :-1]
x=cp.Variable((15,8), pos=True)
y=cp.Variable((15,8), integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
con= [cp.sum(x, axis=0)<=b, cp.sum(x, axis=1)==a,
      1000*y<=x, x<=2000*y, y>=0, y<=1]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value); print("最优解为：\n", x.value)
xd=pd.DataFrame(x.value)
xd.to_excel("ti4_6_4.xlsx")  #写到数据写到Excel文件，便于做表使用

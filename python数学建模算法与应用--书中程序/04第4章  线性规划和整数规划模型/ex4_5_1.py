#程序文件ex4_5_1.py
import numpy as np
import cvxpy as cp
import pandas as pd
c=np.genfromtxt("data4_5_1.txt", dtype=float, max_rows=6, usecols=range(8)) #读前6行前8列数据
e=np.genfromtxt("data4_5_1.txt", dtype=float, max_rows=6, usecols=8) #读最后一列数据
d=np.genfromtxt("data4_5_1.txt", dtype=float, skip_header=6) #读最后一行数据
x=cp.Variable((6,8), pos=True)
obj=cp.Minimize(cp.sum(cp.multiply(c, x)))
con= [cp.sum(x, axis=0)==d,
      cp.sum(x, axis=1)<=e]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", x.value)
xd=pd.DataFrame(x.value)
xd.to_excel("data4_5_2.xlsx")  #数据写到Excel文件，便于做表使用


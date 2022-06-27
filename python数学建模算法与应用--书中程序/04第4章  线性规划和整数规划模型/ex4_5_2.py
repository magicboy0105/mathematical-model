#程序文件data4_5_2.py
import cvxpy as cp
import pandas as pd

data=pd.read_excel("data4_5_3.xlsx", header=None)
data=data.values; c=data[:-1,:-1]
d=data[-1,:-1]; e=data[:-1,-1]

x=cp.Variable((6,8), pos=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
con= [cp.sum(x, axis=0)==d,
      cp.sum(x, axis=1)<=e]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
xd=pd.DataFrame(x.value)
xd.to_excel("data4_5_4.xlsx")  #数据写到Excel文件，便于做表使用

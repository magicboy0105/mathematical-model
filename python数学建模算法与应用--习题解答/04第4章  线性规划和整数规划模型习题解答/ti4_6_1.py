#程序文件ti4_6_1.py
import numpy as np
import cvxpy as cp
import pandas as pd

c=np.genfromtxt("ti4_6_1.txt", dtype=float, max_rows=15, usecols=range(8)) #读前15行前8列数据
a=np.genfromtxt("ti4_6_1.txt", dtype=float, max_rows=15, usecols=8) #读最后一列数据
b=np.genfromtxt("ti4_6_1.txt", dtype=float, skip_header=15) #读最后一行数据
x=cp.Variable((15,8),pos=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
con= [cp.sum(x, axis=0)<=b, cp.sum(x, axis=1)==a]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value); print("最优解为：\n", x.value)
xd=pd.DataFrame(x.value)
xd.to_excel("ti4_6_2.xlsx")  #写到数据写到Excel文件，便于做表使用

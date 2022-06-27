#程序文件ex4_13.py
import numpy as np
import pandas as pd
import cvxpy as cp

a=pd.read_excel('data4_13_1.xlsx',header=None)
a=a.values; a[np.isnan(a)]=0  #把空格对应的不确定值替换为0
m,n=a.shape
w=np.ones((n+1,n+1))*10000000  #邻接矩阵初始化
for i in range(n):
    for j in range(n):
        if i!=j: w[i,j]=sum(a[:,i]*a[:,j])
for i in range(n):
    w[i, n] = 0; w[n, i] =0
wd = pd.DataFrame(w)
wd.to_excel('data4_13_2.xlsx')  #把邻接矩阵保存到Excel文件
x=cp.Variable((n+1,n+1),integer=True)
u=cp.Variable(n+1,integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(w,x)))
con=[cp.sum(x,axis=0)==1, cp.sum(x,axis=1)==1,
     x>=0, x<=1, u[0]==0, u[1:]>=1, u[1:]<=n]
for i in range(n+1):
    for j in range(1,n+1):
        con.append(u[i]-u[j]+(n+1)*x[i,j]<=n)
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
i,j=np.nonzero(x.value)
print("xij=1对应的行列位置如下：")
print(i+1); print(j+1)

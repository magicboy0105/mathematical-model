#程序文件ti6_9.py
import numpy as np
import cvxpy as cp

a=np.loadtxt('ti6_9.txt').T.astype(int)
m=a.shape[0]; n=5
w=np.zeros((n,n),dtype=int)  #邻接矩阵初始化
for k in range(m):
    w[a[k][0]-1,a[k][1]-1]=1
w=w+w.T  #构造完整的邻接矩阵
K=max(sum(w))  #计算顶点的最大度数
x=cp.Variable((n,K+1),integer=True)
y=cp.Variable()  #定义一个变量
obj=cp.Minimize(y)
con=[cp.sum(x,axis=1)==1, x>=0, x<=1]
for i in range(n):
    con.append(y>=range(1,K+2)@x[i,:])
for k in range(K+1):
    for j in range(m):
        con.append(x[a[j][0]-1,k]+x[a[j][1]-1,k]<=1)
prob=cp.Problem(obj,con); prob.solve(solver='GLPK_MI')
print('最优值为：', prob.value)
print('最优解为:\n',x.value)
i,k=np.nonzero(x.value)
print('顶点和颜色的对应关系如下：')
print('顶点i=',i+1); print('颜色k=',k+1)








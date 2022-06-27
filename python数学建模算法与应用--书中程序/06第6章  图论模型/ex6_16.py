#程序文件ex6_16.py
import cvxpy as cp
import networkx as nx
import numpy as np

L = [{'张','李','王'},{'李','赵','刘'},{'张','刘','王'},
     {'赵','刘','孙'},{'张','王','孙'},{'李','刘','王'}]
w = np.zeros((6,6))
for i in range(5):
    for j in range(i+1,6):
        if len(L[i] & L[j])>=1:
            w[i,j] = 1  #构造邻接矩阵的上三角元素
ni, nj = np.nonzero(w)  #边的端点编号
w = w + w.T   #构造完整的邻接矩阵
deg = w.sum(axis=1)  #求各个顶点的度
K = int(max(deg))  #顶点的最大度
n = len(w)  #顶点的个数
x = cp.Variable((n, K+1), integer=True)
y = cp.Variable()  #定义一个变量
obj = cp.Minimize(y)
con = [cp.sum(x, axis=1)==1, x>=0, x<=1]
for i in range(n):
    con.append(y>=range(1,K+2)@x[i,:])
for k in range(K+1):
    for i in range(len(ni)):
        con.append(x[ni[i],k]+x[nj[i],k]<=1)
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
i, k = np.nonzero(x.value)
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
print('顶点和颜色的对应关系如下：')
print('i=', i+1); print('k=', k+1)



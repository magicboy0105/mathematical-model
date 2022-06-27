#程序文件ex6_25.py
import numpy as np
import cvxpy as cp
from scipy.stats import norm

L = np.array([(1,2,3,5,7),(1,3,8,9,16),(1,4,8,11,14),(2,5,3,4,5),
    (3,4,2,4,6),(3,5,0,0,0),(4,6,8,16,18),(5,6,18,20,28),(5,7,18,25,32),
    (5,8,26,33,52),(6,7,0,0,0),(6,8,11,21,25),(7,8,12,15,18)])
et = (L[:,2]+4*L[:,3]+L[:,4])/6  #计算均值
dt = (L[:,4]-L[:,2])**2/36       #计算方差
n=8; x = cp.Variable((n,n), integer=True)
m=len(L); fun=0
for i in range(m):
    fun=fun+x[L[i][0]-1,L[i][1]-1]*et[i]
obj=cp.Maximize(fun); con=[x>=0, x<=1]
out=np.where(L[:,0]==1)[0]  #起点的相邻顶点
con.append(cp.sum(x[0,L[out,1]-1])==1)
for k in range(2,n):
    out=np.where(L[:,0]==k)[0]  #顶点k发出弧的顶点
    ind=np.where(L[:,1]==k)[0]  #顶点k进入弧的顶点
    con.append(cp.sum(x[L[ind,0]-1,k-1])==cp.sum(x[k-1,L[out,1]-1]))
ind=np.where(L[:,1]==n)  #终点的相邻顶点
con.append(cp.sum(x[L[ind,0]-1,n-1])==1)
prob=cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值为：', prob.value); print('最优解为:\n', x.value)
f=prob.value; xx = x.value; s2=0  #方差的初值
for i in range(m):
    s2=s2+xx[L[i][0]-1,L[i][1]-1]*dt[i]
s=np.sqrt(s2); p=norm.cdf(52, f, s)  #计算标准差和概率
N = norm.ppf(0.95)*s+f; print('标准差s:', s)
print('概率p:', p); print('需要天数N：', N)






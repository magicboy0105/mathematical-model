#程序文件ti6_11.py
import numpy as np
import cvxpy as cp
from scipy.stats import norm

L=np.array([(1,2,6,4,800,2,6,10),(1,3,5,3,600,4,5,6),
(2,4,3,1,300,2,3,4),(3,7,2,1,300,3,4,5),(4,5,2,1,600,1,2,3),
(5,6,3,1,400,1,3,5),(6,7,4,2,200,2,4,6),(7,8,2,2,200,1,2,4)])
n=8; x=cp.Variable(n, pos=True)
y=cp.Variable((n,n), integer=True)
z=cp.Variable((n,n), integer=True)

m=L.shape[0]; ob1=cp.Minimize(sum(x)); con1=[]
for i in range(m):
    con1.append(x[L[i][1]-1]>=x[L[i][0]-1]+L[i][2])
p1=cp.Problem(ob1, con1); p1.solve(solver='GLPK_MI')
print('最优值为', p1.value)
print('各事件的最早时间：', x.value)
xx1=x.value; z=np.zeros(n); z[-1]=xx1[-1]
for k in range(n-1,0,-1):
    z[k-1]=min([z[a[1]-1]-a[2] for a in L if a[0]==k])
print('各事件的最迟时间：', z)
es=[]; ls=[]  #各作业最早、最迟开工时间初始化
for i in range(m):
    es.append([L[i][0],L[i][1],xx1[L[i][0]-1]])
    ls.append([L[i][0],L[i][1],z[L[i][1]-1]-L[i][2]])
print('作业最早开工时间：\n',es)
print('作业最迟开工时间：\n',ls); print('----------')
    
f2=0
for i in range(m):
    f2=f2+y[L[i][0]-1,L[i][1]-1]*L[i][4]
ob2=cp.Minimize(f2); con2=[x[7]-x[0]<=17, y>=0]
for i in range(m):
    con2.append(x[L[i][1]-1]-x[L[i][0]-1]+y[L[i][0]-1,L[i][1]-1]>=L[i][2])
    con2.append(y[L[i][0]-1,L[i][1]-1]<=L[i][2]-L[i][3])
p2=cp.Problem(ob2, con2); p2.solve(solver='GLPK_MI')
print('最优值为：', p2.value); print('x的取值为：\n',x.value)
print('y的取值为：\n', y.value); ni,nj=np.nonzero(y.value)
print('压缩工期的作业为：'); print(ni+1); print(nj+1)
print('---------------------------')

et = (L[:,5]+4*L[:,6]+L[:,7])/6  #计算均值
dt = (L[:,7]-L[:,5])**2/36       #计算方差
f3=0
for i in range(m):
    f3=f3+y[L[i][0]-1,L[i][1]-1]*et[i]
ob3=cp.Maximize(f3); con3=[y>=0, y<=1]
out=np.where(L[:,0]==1)[0]  #起点的相邻顶点
con3.append(cp.sum(y[0,L[out,1]-1])==1)
for k in range(2,n):
    out=np.where(L[:,0]==k)[0]  #顶点k发出弧的顶点
    ind=np.where(L[:,1]==k)[0]  #顶点k进入弧的顶点
    con3.append(cp.sum(y[L[ind,0]-1,k-1])==cp.sum(y[k-1,L[out,1]-1]))
ind=np.where(L[:,1]==n)  #终点的相邻顶点
con3.append(cp.sum(y[L[ind,0]-1,n-1])==1)
p3=cp.Problem(ob3, con3); p3.solve(solver='GLPK_MI')
print('最优值为：', p3.value); print('最优解为:\n', y.value)
f=p3.value; yy = y.value; s2=0  #方差的初值
for i in range(m):
    s2=s2+yy[L[i][0]-1,L[i][1]-1]*dt[i]
s=np.sqrt(s2); p=norm.cdf(21, f, s)  #计算标准差和概率
N = norm.ppf(0.95)*s+f; print('标准差s:', s)
print('概率p:', p); print('需要天数N：', N)








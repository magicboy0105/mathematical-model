#程序文件ti16_4.py
import numpy as np
import cvxpy as cp
import pandas as pd
from scipy.optimize import minimize

d1 = pd.read_excel('ti16_4.xlsx',header=None).values
d0 = pd.read_excel('ti16_4.xlsx','Sheet2',header=None).values
a1 = d1[:,:5]; c1 = d1[:,5]; b1 = d1[:,6:]
a0 = d0[:,:5]; c0 = d0[:,5]; b0 = d0[:,6:]
sk0 = np.zeros((20,20,5)); sk1 = np.zeros((20,20,5))  #初始化
f = lambda x,y: ((x>y)*(0.9+0.1/(9-y*(y<9))*(x-y))+0.9*(x==y)+
                  0.9*x/y*((y-x>0)&(y-x<3)))
for i in range(20):
    for j in range(20):
        for k in range(5):
            sk0[i,j,k] = f(a1[i,k],b0[j,k])
            sk1[i,j,k] = f(a0[j,k],b1[i,k])
s0 = sk0.mean(axis=2)  #求女青年对男青年的综合满意度
s1 = sk1.mean(axis=2)  #求男青年对女青年的综合满意度
ss = np.sqrt(s0*s1)    #求相互满意度

x = cp.Variable((20,20),integer=True)
ob1 = cp.Maximize(cp.sum(cp.multiply(ss,x)))
con = [cp.sum(x,axis=0)==1, cp.sum(x,axis=1)==1, x>=0, x<=1]
for i in range(20):
    for j in range(20):
        con.append((c1[i]-c0[j])*x[i,j]<=5)
        con.append((c0[j]-c1[i])*x[i,j]<=2)
        con.append(x[i,j]*sum(np.sign(a1[i,:]-b0[j,:]))>=-3)
        con.append(x[i,j]*sum(np.sign(a0[j,:]-b1[i,:]))>=-3)
prob1 = cp.Problem(ob1, con); prob1.solve(solver='GLPK_MI')
print('最优值：', round(prob1.value,4)); xx1 = x.value
i, j = np.nonzero(xx1); solu1 = []
for k in range(len(i)):
    solu1.append([i[k]+1, j[k]+1, ss[i[k],j[k]]])

ob2 = cp.Maximize(cp.sum(cp.multiply(np.log(ss),x)))
prob2 = cp.Problem(ob2, con); prob2.solve(solver='GLPK_MI')
print('最优值：', round(np.exp(prob2.value),4))
xx2 = x.value; solu2 = []
i, j = np.nonzero(xx2)
for k in range(len(i)):
    solu2.append([i[k]+1, j[k]+1, ss[i[k],j[k]]])

#以下纯策略枚举
for i in range(20):
    for j in range(20):
        if (s1[:,j]<=s1[i,j]).all() & (s0[i,:]<=s0[i,j]).all():
            print(i+1,'配对',j+1)

#以下是求解混合策略，实际上是没有必要的
ob4 = lambda z: sum(z)  #定义虚拟的目标函数
con1 = {'type':'ineq','fun':lambda z:z[:20]@s1@z[20:]-s1@z[20:]}
con2 = {'type':'ineq','fun':lambda z:z[:20]@s0@z[20:]-s0.T@z[:20]}
con3 = {'type':'eq', 'fun':lambda z:sum(z[:20])-1}
con4 = {'type':'eq', 'fun':lambda z:sum(z[20:])-1}
con = [con1, con2, con3, con4]
bd = [(0, 1) for i in range(40)]
s = minimize(ob4, 0.5*np.ones(40), constraints=con, bounds=bd)
print('解的详细信息如下：\n', s)
x4 = s.x[:20]; y4 = s.x[20:]
print('x的解为:\n',x4); print('y的解为:\n',y4)


#程序文件anli14_1_2
import numpy as np
from scipy.optimize import fsolve
import cvxpy as cp
import pandas as pd

f1 = lambda t: [1/(1+t[0]/(1-t[1])**2)-0.01,
                1/(1+t[0]/(4-t[1])**2)-0.8]
c1 = fsolve(f1, [0.5,0.5])    #待定参数alpha,beta
f2 = lambda t: [t[0]*np.log(4)+t[1]-0.8, t[0]*np.log(7)+t[1]-1]
c2 = fsolve(f2, [0.5, 0.5])   #待定参数a,b
f = lambda x: (1/(1+c1[0]/(x-c1[1])**2) * ((x>=1)&(x<=4))+
               (c2[0]*np.log(x)+c2[1]) * ((x>4) & (x<=7)))
f17 = f(np.arange(1,8))  #计算对应的函数值
d1 = np.loadtxt('anli14_1_1.txt'); d2 = np.loadtxt('anli14_1_3.txt')
a = d1[:, 3:]; b = d2[:, 6:]
g = lambda x: (4*(x==0)+5*(x==-1)+6*(x==-2)+7*(x==-3)+
               3*(x==1)+2*(x==2)+(x>=3))
m = b.shape[0]; n = a.shape[0]; s = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        t1 = g(b[j,:]-a[i,:]); t2 = f(t1)
        s[i,j] = t2.mean()  #计算用人部门对应聘者的评分
d = np.loadtxt('anli14_1_2.txt')

x = cp.Variable((n, m), integer=True)
obj = cp.Maximize(cp.sum(cp.multiply(d, cp.sum(x,axis=1)))
                   + cp.sum(cp.multiply(s, x)))
con = [cp.sum(x)==8, cp.sum(x,axis=1)<=1, cp.sum(x,axis=0)>=1,
       cp.sum(x,axis=0)<=2, x>=0, x<=1]
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值：', prob.value); print('最优解：\n', x.value)
i, j = np.nonzero(x.value)
pf0 = s * x.value; pf = pf0[np.nonzero(pf0)]  #提取非零评分
out = np.vstack([j+1, i+1, d[i], pf])
ind = np.argsort(j); out = out[:,ind]  #按部门序号排序
fid = pd.ExcelWriter('anli14_1_4.xlsx')
pd.DataFrame(s).to_excel(fid, index=None)
pd.DataFrame(out).to_excel(fid, 'Sheet2', index=None)
fid.save()








                

#程序文件anli14_1_3
import numpy as np
import cvxpy as cp
import pandas as pd

fx = lambda x: np.log(4-x)/np.log(3)
w = fx(np.arange(1,4))  #计算权重向量
d1 = np.loadtxt('anli14_1_1.txt'); d2 = np.loadtxt('anli14_1_3.txt')
a = d1[:,[1,2]]  #志愿类别数据
#下面匿名函数把工作类别映射到部门
g = lambda x: (0*(x==1)+np.array([1,2])*(x==2)+
               np.array([3,4])*(x==3)+np.array([5,6])*(x==4))
wij = np.zeros((16,7))  #权重矩阵初始化
for i in range(16):
    wij[i,g(a[i,0])]=1; wij[i,g(a[i,1])]=w[1]
tj = d2[:,1:6]  #提出部门客观评分
t = wij * (tj.mean(axis=1))  #计算对部门的满意度
s = pd.read_excel('anli14_1_4.xlsx').values
r = np.sqrt(s*t)  #计算相互满意度

x = cp.Variable((16, 7), integer=True)
obj = cp.Maximize(cp.sum(cp.multiply(r, x)))
con = [cp.sum(x)==8, cp.sum(x,axis=1)<=1, cp.sum(x,axis=0)>=1,
       cp.sum(x,axis=0)<=2, x>=0, x<=1]
prob = cp.Problem(obj, con); prob.solve(solver='GLPK_MI')
print('最优值：', prob.value); xx = x.value
print('最优解：\n', xx)
i, j = np.nonzero(xx)
fc0 = r * xx; fc = fc0[np.nonzero(fc0)]  #提取满意度数据
out = np.vstack([j+1, i+1, fc])
ind = np.argsort(j); out = out[:,ind]  #部门序号从小到大排序
pd.DataFrame(out).to_excel('anli14_1_5.xlsx', index=None)              

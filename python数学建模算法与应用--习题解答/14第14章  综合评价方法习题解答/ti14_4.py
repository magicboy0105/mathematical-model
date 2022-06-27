#程序文件ti14_4.py
import numpy as np
import scipy.cluster.hierarchy as sch
import pylab as plt

a = np.loadtxt('ti14_4.txt')
m1 = a.max(axis=1,keepdims=True)  #求各门课最高成绩
m2 = a.min(axis=1,keepdims=True)  #求各门课最低成绩
b = (a-m2)/(m1-m2)  #数据标准化
r = np.zeros((7,7)) #相似关系矩阵初始化
for j in range(7):
    for k in range(7):
        r[j,k] = sum(b[:,[j,k]].min(axis=1))/sum(b[:,[j,k]].max(axis=1))

def sym(r):   #定义矩阵合成的函数
    sr = np.zeros_like(r); k = len(r)
    for i in range(k):
        for j in range(k):
            sr[i,j] = max(np.vstack([r[:,i],r[:,j]]).min(axis=0))
    return sr

r1 = sym(r)    #进行第1次合成运算
r2 = sym(r1)   #进行第2次合成运算
r3 = sym(r2)   #进行第3次合成运算
sr = set(np.triu(r3,1).flatten())-{0}  #求聚类的阈值
sr = sorted(sr, reverse=True)
print('聚类的阈值为：', np.round(sr,4))
d = 1 - r3     #计算距离矩阵
dd = np.triu(d,1)  #提取主对角线上方元素
dd = dd[dd!=0]  #提取linkage函数需要的距离
plt.rc('font', family='SimHei')
s = ['经管','汽车','信息','材化','计算机','土建','机械']
z = sch.linkage(dd); sch.dendrogram(z,labels=s)  
plt.yticks([]);  plt.show()  #设置y轴刻度不可见


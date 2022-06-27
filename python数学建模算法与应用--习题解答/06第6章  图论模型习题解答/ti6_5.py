#程序文件ti6_5.py
import numpy as np
import networkx as nx
import pandas as pd
import pylab as plt

n=6; node=['v'+str(i) for i in range(1,n+1)]
A=np.zeros((n,n)); A[0,[1,2]]=[2,7]
A[1,2:5]=[4,6,8]; A[2,[3,4]]=[1,3]
A[3,[4,5]]=[1,6]; A[4,5]=3
G=nx.Graph(A)  #构造赋权无向图 
d=nx.floyd_warshall_numpy(G)  #求所有顶点对之间的最短距离
dm1=np.max(d,axis=0); print('d=\n',d)
print('逐列最大值为:', dm1)
f=pd.ExcelWriter('ti6_5.xlsx');
dd=pd.DataFrame(d)  #为保存到Excel文件转换为DataFrame结构
dd.to_excel(f, 'Sheet1', index=False)
num=np.array([[50,40,60,20,70,90]]).T  #列向量
D=num*d              #广播后对应元素相乘
DD=pd.DataFrame(D); DD.to_excel(f,'Sheet2',index=False)
sd=np.sum(D,axis=0)  #逐列求和
sdm=min(sd)          #求最小值
ind=np.argmin(sd)    #求最小值的地址
f.save(); print('最小值为:',sdm);
print('达到最小值的地点为：',node[ind])

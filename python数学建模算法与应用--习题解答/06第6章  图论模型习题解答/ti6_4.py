#程序文件ti6_4.py
import numpy as np
import networkx as nx
import pylab as plt

a=np.zeros((5,5))  #邻接矩阵初始化
a[0,1:]=[0.8, 2, 3.8, 6]
a[1,2:]=[0.9, 2.1, 3.9]
a[2,3:]=[1.1, 2.3]; a[3,4]=1.4
G=nx.DiGraph(a)  #构造赋权有向图
p=nx.shortest_path(G,0,4,weight='weight')         #求最短路径
d=nx.shortest_path_length(G,0,4,weight='weight')  #求最短距离
print('最短路径为：', np.array(p)+1)
print('最小费用为：', d)

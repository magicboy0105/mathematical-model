#程序文件ti6_2.py
import networkx as nx
import numpy as np
import pandas as pd
import pylab as plt

a=pd.read_excel('ti6_2.xlsx',header=None)
b=a.values; b[np.isnan(b)]=0
G=nx.Graph(b)   #利用邻接矩阵构造赋权无向图
T=nx.minimum_spanning_tree(G)  #构造最小生成树
w=nx.get_edge_attributes(T,'weight') #提出权重字典数据
TL=sum(w.values())  #计算最小生成树的长度
print('最小生成树的边权为：', w)
print('最小生成树的长度为：', TL)
pos=nx.shell_layout(T)  #提出布局坐标字典数据
s=dict(zip(range(6),['L','M','N','Pa','Pe','T']))
nx.draw(T, pos,labels=s)
nx.draw_networkx_edge_labels(T, pos, edge_labels=w)
plt.show()


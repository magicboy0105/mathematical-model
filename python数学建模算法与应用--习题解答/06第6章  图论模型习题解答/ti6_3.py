#程序文件ti6_3.py
import numpy as np
import networkx as nx
import pylab as plt

L=[(1,2,20),(1,5,15),(2,3,20),(2,4,60),(2,5,25),
   (3,4,30),(3,5,18),(4,5,35),(4,6,10),(5,6,15)]
G=nx.Graph(); G.add_nodes_from(range(1,7))
G.add_weighted_edges_from(L)
T=nx.minimum_spanning_tree(G)  #构造最小生成树
w=nx.get_edge_attributes(T,'weight')  #提取权重字典数据
TL=sum(w.values())  #计算最小生成树的长度
print('最小生成树的长度为：',TL)
pos=nx.shell_layout(G)  #提出布局坐标字典数据
s=['v'+str(i) for i in range(1,7)]
s=dict(zip(range(1,7), s)); nx.draw(T,pos,labels=s)
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.show()


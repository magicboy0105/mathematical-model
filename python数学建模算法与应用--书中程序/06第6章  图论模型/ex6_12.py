#程序文件ex6_12.py
import numpy as np
import networkx as nx
import pylab as plt

L=[(0,1,2),(0,2,1),(0,3,3),(0,4,4),(0,5,4),(0,6,2),(0,7,5),(0,8,4),
   (1,2,4),(1,8,1),(2,3,1),(3,4,1),(4,5,5),(5,6,2),(6,7,3),(7,8,5)]
G=nx.Graph()
G.add_weighted_edges_from(L)
T=nx.minimum_spanning_tree(G)  #返回可迭代对象
c=nx.to_numpy_matrix(T)  #返回最小生成树的邻接矩阵
print("邻接矩阵c=\n",c)
w=c.sum()/2  #求最小生成树的权重
print("最小生成树的权重W=",w)
pos=nx.circular_layout(G)
plt.subplot(121)  #下面画连通图
nx.draw(G,pos,with_labels=True, font_size=13)
w1=nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=w1)
plt.subplot(122)  #下面画最小生成树
nx.draw(T, pos, with_labels=True, font_weight='bold')
w2=nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=w2)
plt.show()


#程序文件ex6_9.py
import numpy as np
import networkx as nx
import pylab as plt

a=np.zeros((6,6))
a[0,1:]=[15,20,27,37,54]
a[1,2:]=[15,20,27,37]; a[2,3:]=[16,21,28];
a[3,4:]=[16,21]; a[4,5]=17
G=nx.DiGraph(a)  #构造赋权有向图,顶点编号为0,1,…,5
p=nx.shortest_path(G,0,5,weight='weight')
d=nx.shortest_path_length(G,0,5,weight='weight')
print('path=',p); print('d=',d)
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'weight')
key=range(6); s=['v'+str(i+1) for i in key]
s=dict(zip(key,s)) #构造用于顶点标注的字符字典
nx.draw(G, pos, font_weight='bold', labels=s, node_color='r')
nx.draw_networkx_edge_labels(G, pos, edge_labels=w)
path_edges=list(zip(p, p[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges,
            edge_color='r', width=3)
plt.savefig('fig6_9.png', dpi=500); plt.show()

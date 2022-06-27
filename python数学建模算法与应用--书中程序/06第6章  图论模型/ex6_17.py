#程序文件ex6_17.py
import numpy as np
import networkx as nx
import pylab as plt
L=[(1,2,6),(1,3,4),(1,4,5),(2,3,3),(2,5,9),(2,6,9),
   (3,4,5),(3,5,6),(3,6,7),(3,7,3),(4,3,2),(4,7,5),
   (5,8,12),(6,5,8),(6,8,10),(7,6,4),(7,8,15)]
G=nx.DiGraph()
G.add_nodes_from(range(1,9))
G.add_weighted_edges_from(L,weight='capacity')
value, flow_dict= nx.maximum_flow(G, 1, 8)
print("最大流的流量为：",value)
print("最大流为：", flow_dict)
n = len(flow_dict)
adj_mat = np.zeros((n, n), dtype=int)
for i, adj in flow_dict.items():
    for j, weight in adj.items():
        adj_mat[i-1,j-1] = weight
print("最大流的邻接矩阵为：\n",adj_mat)
ni,nj=np.nonzero(adj_mat)  #非零弧的两端点编号
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'capacity')
nx.draw(G,pos,font_weight='bold',with_labels=True,node_color='y')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(ni+1,nj+1))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=3)
plt.show()

#程序文件ex6_5.py
import networkx as nx
import pylab as plt

G=nx.DiGraph()
List=[(1,2),(1,3),(2,3),(3,2),(3,5),(4,2),(4,6),
      (5,2),(5,4),(6,5)]
G.add_nodes_from(range(1,7))  #必须显式地对顶点赋值
G.add_edges_from(List)
plt.rc('font',size=16)
pos=nx.shell_layout(G) 
nx.draw(G,pos,with_labels=True, font_weight='bold', node_color='y')
W = nx.to_numpy_matrix(G)   #从图G导出邻接矩阵
print(W); plt.show()

#程序文件ex6_6.py
import networkx as nx
import pylab as plt
import numpy as np

G=nx.Graph()
List=[(1, 3, 10), (1, 4, 60), (2, 3, 5),
      (2, 4, 20), (3, 4, 1)]
G.add_nodes_from(range(1,5))
G.add_weighted_edges_from(List)
W1 = nx.to_numpy_matrix(G)   #从图G导出权重邻接矩阵
W2 = nx.get_edge_attributes(G, 'weight')  #导出赋权边的字典数据
pos=nx.spring_layout(G) 
nx.draw(G,pos,with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(G,pos, font_size=13, edge_labels=W2)
print('邻接矩阵为：\n', W1); print('邻接表字典为：\n', G.adj)
print('邻接表列表为：\n', list(G.adjacency()))
print('列表字典为：\n', nx.to_dict_of_lists(G))
np.savetxt('data6_6.txt', W1, fmt='%d')  #邻接矩阵保存到文本文件
plt.show()

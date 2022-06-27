#程序文件ex6_8.py
import networkx as nx
import numpy as np

G = nx.Graph()
List = [(1, 3, 10), (1, 4, 60), (2, 3, 5), (2, 4, 20), (3, 4, 1)]
G.add_nodes_from(range(1,5))
G.add_weighted_edges_from(List)
d = nx.floyd_warshall_numpy(G)
print('最短距离矩阵为：\n', d)
path = nx.shortest_path(G, weight='weight', method='bellman-ford')
for i in range(1,len(d)):
    for j in range(i+1, len(d)+1):
        print('顶点{}到顶点{}的最短路径为：'.format(i,j), path[i][j])

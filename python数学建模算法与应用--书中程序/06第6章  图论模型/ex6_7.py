#程序文件ex6_7.py
import networkx as nx

G = nx.DiGraph()
List = [(1,2,6), (1,3,3), (1,4,1), (2,5,1), (3,2,2), (3,4,2), (4,6,10), (5,4,6),
        (5,6,4), (5,7,3), (5,8,6), (6,5,10), (6,7,2), (7,8,4), (9,5,2), (9,8,3)]
G.add_nodes_from(range(1,10))
G.add_weighted_edges_from(List)
path = nx.dijkstra_path(G, 1, 8, weight='weight')  #求最短路径
d = nx.dijkstra_path_length(G, 1, 8, weight='weight')
print('最短路径为：', path)
print('最小费用为：', d)


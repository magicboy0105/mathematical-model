#程序文件ex6_4.py
import networkx as nx
import pylab as plt

G = nx.Graph()
G.add_node(1)    #添加编号为1的一个顶点
G.add_nodes_from(['A', 'B'])  #从列表中添加多个顶点
G.add_edge('A', 'B')   #添加顶点A和B之间的一条边
G.add_edge(1, 2, weight=0.5)   #添加顶点1和2之间权重为0.4的一条边
e = [('A','B',0.3),('B','C',0.9),('A','C',0.5),('C','D',1.2)]
G.add_weighted_edges_from(e)  #从列表中添加多条赋权边
print(G.adj)      #显示图的邻接表的字典数据
print(list(G.adjacency()))  #显示图的邻接表的列表数据


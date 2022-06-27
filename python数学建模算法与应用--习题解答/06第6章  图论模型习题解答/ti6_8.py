#程序文件ti6_8.py
import numpy as np
import numpy.random as nr
import networkx as nx
import pylab as plt

nr.seed(2)  #进行一致性比较，每次运行结果一样
a=nr.rand(10,10)  #生成10×10的随机数矩阵
a=np.tril(a,-1)   #截取下三角元素
w=nr.randint(1,11,(10,10))  #生成[1,10]上的随机整数矩阵
wx = (a>=0.6)*w  #生成赋权图邻接矩阵的下三角部分
G=nx.Graph(wx)   #构造赋权无向图
s=dict(zip(range(10),range(1,11)))
G=nx.relabel_nodes(G, s)

T=nx.minimum_spanning_tree(G)  #利用Kruskal算法构造最小生成树
w1=nx.get_edge_attributes(T,'weight')  #提取边权的字典数据
LT=sum(w1.values())  #求最小生成树的长度
print('最小生成树的长度为：', round(LT,4))
pos=nx.shell_layout(G)  #生成顶点坐标字典数据
nx.draw(T,pos,with_labels=True)
nx.draw_networkx_edge_labels(T,pos,edge_labels=w1)
                       
p=nx.shortest_path(G,1,10,weight='weight')  #求最短路径
d=nx.shortest_path_length(G,1,10,weight='weight')
print('最短路径为：',p); print('最短距离为：',round(d,4))
plt.figure(); w2=nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,with_labels=True)
path_edges=list(zip(p,p[1:]))
nx.draw_networkx_edge_labels(G,pos,edge_labels=w2)
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            style='dashed',width=3)
D=nx.floyd_warshall_numpy(G)
print('所有顶点对之间的距离：\n',D); plt.show()


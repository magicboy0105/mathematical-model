#程序文件ti6_10.py
import numpy as np
import networkx as nx

L=[('vs','v1',4,10),('vs','v2',1,8),('v1','v3',6,2),('v1','vt',1,7),
   ('v2','v1',2,5),('v2','v3',3,10),('v3','vt',2,4)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0], L[k][1], weight=L[k][2], capacity=L[k][3])
maxFlow=nx.max_flow_min_cost(G,'vs','vt')
print('所求最大流为：',maxFlow)
mincost=nx.cost_of_flow(G, maxFlow)
print('最小费用为：', mincost)
node = list(G.nodes())  #导出顶点列表
n=len(node); flow_mat=np.zeros((n,n))
for i,adj in maxFlow.items():
    for j,f in adj.items():
        flow_mat[node.index(i),node.index(j)]=f
print('最大流的流量为：', sum(flow_mat[:,-1]))
print('最小费用最大流的邻接矩阵为：\n',flow_mat)







#程序文件ex6_19.py
import numpy as np
import networkx as nx
L=[('vs','v2',5,3),('vs','v3',3,6),('v2','v4',2,8),('v3','v2',1,2),('v3','v5',4,2),
   ('v4','v3',1,1),('v4','v5',3,4),('v4','vt',2,10),('v5','vt',5,2)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0], L[k][1], capacity=L[k][2], weight=L[k][3])
maxFlow=nx.max_flow_min_cost(G,'vs','vt')
print("所求最大流为：",maxFlow)
mincost=nx.cost_of_flow(G, maxFlow)
print("最小费用为：", mincost)
node = list(G.nodes())  #导出顶点列表
n=len(node); flow_mat=np.zeros((n,n))
for i,adj in maxFlow.items():
    for j,f in adj.items():
        flow_mat[node.index(i),node.index(j)]=f
print("最大流的流量为：", sum(flow_mat[:,-1]))
print("最小费用最大流的邻接矩阵为：\n",flow_mat)

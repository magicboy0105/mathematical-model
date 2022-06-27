#程序文件ex6_18_1.py
import numpy as np
import networkx as nx
node=['s','A','B','C','D','E','2b','3b','4b','1','2','3','4','t']
n=len(node); G=nx.DiGraph(); G.add_nodes_from(node)
L=[('s','A',4),('s','B',3),('s','C',3),('s','D',2),('s','E',4),('A','2b',1),
   ('A','1',1),('A','3b',1),('A','4b',1),('B','2b',1),('B','1',1),('B','3',1),
   ('B','4b',1),('C','1',1),('C','2',1),('C','3',1),('C','4b',1),('D','1',1),
   ('D','2',1),('D','3b',1),('D','4b',1),('E','2b',1),('E','1',1),('E','3',1),
   ('E','4',1),('2b','2',2),('3b','3',1),('4b','4',2),('1','t',5),('2','t',4),
   ('3','t',4),('4','t',3)]
for k in range(len(L)):
    G.add_edge(L[k][0],L[k][1],capacity=L[k][2])
value, flow_dict= nx.maximum_flow(G, 's', 't')
print(value); print(flow_dict)
A=np.zeros((n,n),dtype=int)
for i,adj in flow_dict.items():
    for j,f in adj.items():
        A[node.index(i), node.index(j)]=f
print(A)

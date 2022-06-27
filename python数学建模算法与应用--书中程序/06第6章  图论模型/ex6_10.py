#程序文件ex6_10.py
import numpy as np
import networkx as nx

L=[(1,2,20), (1,5,15), (2,3,20), (2,4,60), (2,5,25), (3,4,30), (3,5,18), (5,6,15)]
G = nx.Graph(); G.add_nodes_from(np.arange(1,7))
G.add_weighted_edges_from(L)
d = nx.floyd_warshall_numpy(G)
d = np.array(d)  #转换为array数组
md = np.max(d, axis=1)   #逐行求最大值
mmd = min(md)          #求最小值
ind = np.argmin(md)+1     #求最小值的地址
print(d); print("最小值为：", mmd)
print("最小值的地址为：", ind)

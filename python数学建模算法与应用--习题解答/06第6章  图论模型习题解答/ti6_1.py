#程序文件ti6_1.py
import networkx as nx
import pylab as plt

L1=[(1,2),(1,3),(1,4),(2,3),(2,6),(3,4),(4,5),(5,6)]
G1=nx.Graph(); G1.add_nodes_from(range(1,7))
G1.add_edges_from(L1); pos1=nx.shell_layout(G1)
plt.subplot(131)
nx.draw(G1,pos1,with_labels=True,font_weight='bold')

L2=[(1,2,7),(1,3,3),(1,4,12),(2,3,1),(2,6,1),(3,4,8),(4,5,9),(5,6,3)]
G2=nx.Graph(); G2.add_nodes_from(range(1,7))
G2.add_weighted_edges_from(L2); pos2=nx.shell_layout(G2)
plt.subplot(132)
nx.draw(G2,pos2,with_labels=True,font_weight='bold')
w2=nx.get_edge_attributes(G2,'weight')
nx.draw_networkx_edge_labels(G2,pos2,edge_labels=w2)

L3=[(1,3,3),(2,1,7),(2,3,1),(3,4,8),(4,1,12),(5,4,9),(5,6,3),(6,2,1)]
G3=nx.DiGraph(); G3.add_nodes_from(range(1,7))
G3.add_weighted_edges_from(L3); pos3=nx.shell_layout(G3)
plt.subplot(133)
nx.draw(G3,pos3,with_labels=True,font_weight='bold')
w3=nx.get_edge_attributes(G3,'weight')
nx.draw_networkx_edge_labels(G3,pos3,edge_labels=w3)
plt.show()

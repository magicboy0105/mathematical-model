#程序文件ex6_3.py
import networkx as nx
import pylab as plt

G = nx.cubical_graph() # 生成一个3正则图
plt.subplot(121)       # 激活1号子窗口
nx.draw(G, with_labels=True)
plt.subplot(122)
s = ['v'+str(i) for i in range(1,9)]
s = dict(zip(range(8), s))  #构造顶点标注的字符字典
nx.draw(G,pos=nx.circular_layout(G), labels=s,
        node_color='y', node_shape='s', edge_color='b')
plt.show()

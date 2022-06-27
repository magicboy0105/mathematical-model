import numpy as np
import pandas as pd
import networkx as nx
import pylab as plt

a=pd.read_excel('ti6_7.xlsx'); b=a.values
s=list(b[:,0])      #提取顶点字符串
x=b[:,1]; y=b[:,2]  #提取x,y坐标
num=b[:,3].astype(float)  #提取顶点类别
ad=b[:,4:].astype(str)    #提取邻接顶点
in1=np.where(num==1)[0]  #提取第1类点的编号
in2=np.where(num==2)[0]  #提取第2类点的编号
in3=np.where(np.isnan(num))[0]

plt.plot(x[in1],y[in1],'Pk')
for i in range(len(in1)):
    plt.text(x[in1[i]]+10,y[in1[i]],s[in1[i]])
plt.plot(x[in2],y[in2],'*k')
for i in range(len(in2)):
    plt.text(x[in2[i]]+10,y[in2[i]],s[in2[i]])
plt.plot(x[in3],y[in3],'.k')
for i in range(len(in3)):
    plt.text(x[in3[i]]+10,y[in3[i]],s[in3[i]])
c=np.zeros((95,95))
for i in range(95):
    tt=list(ad[i])  #转换为列表
    tt=[t for t in tt if t!='nan']  #删除nan
    if len(tt)==0: continue
    for k in range(len(tt)):
        j=s.index(tt[k])
        c[i,j]=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
i,j=np.nonzero(c)  #提取所有边的端点编号
for k in range(len(i)):
    plt.plot([x[i[k]],x[j[k]]],[y[i[k]],y[j[k]]])

G=nx.Graph()         #构造无向图
G.add_nodes_from(s)  #加入顶点集
eds=[]               #边集初始化
for k in range(len(i)):
    eds.append([s[i[k]],s[j[k]],c[i[k],j[k]]])
G.add_weighted_edges_from(eds)  #加入赋权边集
T=nx.minimum_spanning_tree(G)  #利用Kruskal算法构造最小生成树
w=nx.get_edge_attributes(T,'weight')  #提取边权的字典数据
LT=sum(w.values())  #求最小生成树的长度
print('最小生成树的长度为：', round(LT,4))
pos=dict(zip(s,b[:,[1,2]]))  #顶点坐标的字典数据
plt.figure()
nx.draw_networkx(T,pos,node_size=180,font_weight='bold',
                 with_labels=True,node_color='w')

p=nx.shortest_path(G,'L','R3',weight='weight')  #求最短路径
d=nx.shortest_path_length(G,'L','R3',weight='weight')
print('最短路径为：',p); print('最短距离为：',round(d,4))
plt.figure()
nx.draw_networkx(G,pos,node_size=180,font_weight='bold',
                 with_labels=True,node_color='w')
path_edges=list(zip(p,p[1:]))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',style='dashed',width=4)
plt.show()

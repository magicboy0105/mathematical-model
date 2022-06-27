#程序文件anli6_1.py
import cvxpy as cp
import numpy as np
import networkx as nx
import pandas as pd

s1 = ['S'+str(i) for i in range(1,8)]
s2 = ['A'+str(i) for i in range(1,16)]
s3 = ['B'+str(i) for i in range(1,18)]
L = s1 + s2 + s3   #构造顶点字符列表
G1 = nx.Graph(); G1.add_nodes_from(L)
L1 = [('B1','B3',450),('B2','B3',80),('B3','B5',1150),('B5','B8',1100),
      ('B4','B6',306),('B6','B7',195),('S1','B7',20),('S1','B8',202),
      ('S2','B8',1200),('B8','B9',720),('S3','B9',690),('B9','B10',520),
      ('B10','B12',170),('S4','B12',690),('S5','B11',462),('B11','B12',88),
      ('B12','B14',160),('B13','B14',70),('B14','B15',320),('B15','B16',160),
      ('S6','B16',70),('B16','B17',290),('S7','B17',30)]
G1.add_weighted_edges_from(L1)  #构造铁路赋权图
d1 = nx.floyd_warshall_numpy(G1) #求最短距离矩阵
d1 = np.array(d1)  #转换为array数组
c1 = np.ones(d1.shape)*np.inf
c1[d1==0]=0; c1[(d1>0) & (d1<=300)]=20
c1[(d1>300) & (d1<=350)]=23; c1[(d1>350) & (d1<=400)]=26
c1[(d1>400) & (d1<=450)]=29; c1[(d1>450) & (d1<=500)]=32
c1[(d1>500) & (d1<=600)]=37; c1[(d1>600) & (d1<=700)]=44
c1[(d1>700) & (d1<=800)]=50; c1[(d1>800) & (d1<=900)]=55
c1[(d1>900) & (d1<=1000)]=60; ind=(d1>1000) & (d1<np.inf)
c1[ind]=60+5*np.ceil(d1[ind]/100-10)

G2 = nx.Graph()
G2.add_nodes_from(L)
L2 = [('A1','A2',104),('A2','B1',3),('A2','A3',301),('A3','B2',2),
      ('A3','A4',750),('A4','B5',600),('A4','A5',606),('A5','B4',10),
      ('A5','A6',194),('A6','B6',5),('A6','A7',205),('A7','B7',10),
      ('S1','A7',31),('A7','A8',201),('A8','B8',12),('A8','A9',680),
      ('A9','B9',42),('A9','A10',480),('A10','B10',70),('A10','A11',300),
      ('A11','B11',10),('A11','A12',220),('A12','B13',10),('A12','A13',210),
      ('A13','B15',62),('A13','A14',420),('S6','A14',110),('A14','B16',30),
      ('A14','A15',500),('A15','B17',20),('S7','A15',20)]
G2.add_weighted_edges_from(L2)  #构造公路赋权图
c2 = nx.to_numpy_matrix(G2)  #导出图G2的邻接矩阵
c2 = np.array(c2)   #转换为array数组
c2[c2==0] = np.inf
c3 = np.minimum(c1, 0.1*c2)

G3 = nx.Graph(c3)
c4 = nx.floyd_warshall_numpy(G3) #求最短距离矩阵
c5 = c4[:7,7:22]   #提出7行15列的运费数据
f = pd.ExcelWriter('anli6_1.xlsx')
pd.DataFrame(c5).to_excel(f, index=False)

s = np.array([800, 800, 1000, 2000, 2000, 2000, 3000])
p = np.array([160, 155, 155, 160, 155, 150, 160])
b = np.array([104, 301, 750, 606, 194, 205, 201,
              680, 480, 300, 220, 210, 420, 500])
c = np.tile(p,(15,1)).T + c5  #购运费用
x = cp.Variable((7,15), integer=True)  #调整为整型
y = cp.Variable(15, pos=True); z = cp.Variable(15, pos=True)
t = cp.Variable(7, integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c, x))+0.05*cp.sum(y**2+y+z**2+z))
con = [500*t<=cp.sum(x,axis=1), cp.sum(x,axis=1)<=cp.multiply(s,t),
       cp.sum(x,axis=0)==y+z, y[1:]+z[:-1]==b,
       y[0]==0, z[14]==0,t>=0, t<=1, x>=0]
prob = cp.Problem(obj, con); prob.solve(solver='CPLEX')
print('最优值为：', prob.value); print('最优解为：\n', x.value)
sx = np.sum(x.value, axis=1)  
pd.DataFrame(c).to_excel(f, 'Sheet2', index=False)
pd.DataFrame(x.value).to_excel(f, 'Sheet3', index=False)
f.close()

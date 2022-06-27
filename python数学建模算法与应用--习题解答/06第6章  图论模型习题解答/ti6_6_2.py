#程序文件ti6_6_2.py
import numpy as np
from scipy.sparse.linalg import eigs
import pylab as plt

a = np.array([[0,1,0,1,1,1],
              [0,0,0,1,1,1],
              [1,1,0,1,0,0],
              [0,0,0,0,1,1],
              [0,0,1,0,0,1],
              [0,0,1,0,0,0]])
w = a
r = np.sum(w,axis=1,keepdims=True)#图中每只球队赢球有向图发出的链接数目
print(r)
n = w.shape[0]#总的球队数目
d=0.85
P=(1-d)/n+d*w/r#利用pageRank公式
print(P)
#pagerank值是转移概率矩阵A的转置矩阵的最大特征值所对应的归一化特征向量
w,v=eigs(P.T,1)  #求最大特征值及对应的特征向量
v=v/sum(v)
v=v.real.flatten()
print('最大特征值为：', w.real)
print('归一化特征向量为：\n', np.round(v,4))
plt.bar(range(1,n+1),v, width=0.6); plt.show()#可以看到3号球队最好

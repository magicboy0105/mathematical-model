#程序文件ti6_6_1.py
import numpy as np
from scipy.sparse.linalg import eigs

a = np.array([[0,1,0,1,1,1],
              [0,0,0,1,1,1],
              [1,1,0,1,0,0],
              [0,0,0,0,1,1],
              [0,0,1,0,0,1],
              [0,0,1,0,0,0]])
e=np.ones(6); sn=np.zeros((6,6))  #初始化
sn[0]=a@e  #计算第1行数据
for i in range(1,6):
    sn[i]=a@sn[i-1]  #计算第i行数据
print(sn)
w,v=eigs(a,1)  #求最大特征值及对应的特征向量
v=v/sum(v)     #特征向量归一化
print('最大特征值为：', w.real)
print('归一化特征向量为：\n', v.real)


#程序文件ti2_12_1.py
import numpy as np

A=np.array([[-1,1,0],[-4,3,0],[1,0,2]])
p=np.poly(A)  #计算特征多项式
w1=np.roots(p)  #计算特征值
w2,v=np.linalg.eig(A)  #直接求特征值和特征向量
w3=np.linalg.eigvals(A)  #计算特征值
print("特征值为：",w2)
print("特征向量为：\n",v)

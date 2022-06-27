#程序文件ti2_12_2.py
import sympy as sp

A=sp.Matrix([[-1,1,0],[-4,3,0],[1,0,2]])
sp.var('lamda')
p=A.charpoly(lamda)  #计算特征多项式
w1=sp.roots(p)  #计算特征值
w2=A.eigenvals()  #直接计算特征值
v=A.eigenvects()  #直接计算特征向量
print("特征值为：",w2)
print("特征向量为：\n",v)

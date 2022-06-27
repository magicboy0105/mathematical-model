#程序文件ex3_2.py
import numpy as np
import sympy as sp

X0 = np.array([500, 1000, 500])
L = np.array([[0, 4, 3], [0.5, 0, 0], [0, 0.25, 0]])
X1 = L @ X0; X2 = L @ X1  #@表示矩阵乘法
X3 = L @ X2

Ls = sp.Matrix([[0, 4, 3], [sp.Rational(1,2), 0, 0],
                [0, sp.Rational(1,4), 0]])  #符号矩阵
sp.var('lamda')  #定义符号变量
p = Ls.charpoly(lamda)  #计算特征多项式
w1 = sp.roots(p)     #计算特征值
w2 = Ls.eigenvals()  #直接计算特征值
v = Ls.eigenvects()  #直接计算特征向量
print("特征值为：",w2)
print("特征向量为：\n",v)
P, D = Ls.diagonalize()  #相似对角化
Pinv = P.inv()  #求逆阵
Pinv = sp.simplify(Pinv)
cc = Pinv @ X0
print('P=\n', P)
print('c=', cc[0])

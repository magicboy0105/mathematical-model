#程序文件ex2_51.py
import numpy as np
import sympy as sp
a = np.identity(4)  #单位矩阵的另一种写法
b = np.rot90(a)
c = sp.Matrix(b)
print('特征值为：', c.eigenvals())
print('特征向量为：\n', c.eigenvects())
